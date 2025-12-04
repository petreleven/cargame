import sqlite3
import json
from typing import Dict, List, Any, Optional
from module_manager import DB_PATH, get_module_manager


def insert_module(cursor, title: str, description: str, status: str = "Draft") -> int:
    """Inserts a module and returns its module_id."""
    cursor.execute(
        """
        INSERT INTO modules (title, description, status)
        VALUES (?, ?, ?)
    """,
        (title, description, status),
    )
    return cursor.lastrowid


def insert_objective(cursor, module_id: int, objective_text: str, order_index: int):
    """Inserts a single learning objective."""
    cursor.execute(
        """
        INSERT INTO objectives (module_id, objective_text, order_index)
        VALUES (?, ?, ?)
    """,
        (module_id, objective_text, order_index),
    )


def insert_content_section(
    cursor,
    module_id: int,
    section_title: str,
    body_text: str,
    content_type: str,
    order_index: int,
    media_link: Optional[str] = None,
):
    """Inserts a content section."""
    cursor.execute(
        """
        INSERT INTO content_sections (module_id, section_title, body_text, content_type, order_index, media_link)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (module_id, section_title, body_text, content_type, order_index, media_link),
    )


def import_module_from_json(json_file_path: str, db_path=DB_PATH):
    """
    Reads a JSON file and populates the database using the helper functions.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        print(f"Reading from {json_file_path}...")

        with open(json_file_path, "r") as f:
            content = f.read()
            dict_content: Dict[str, Any] = json.loads(content)

            # 1. Insert Module
            title = dict_content["title"]
            description = dict_content.get("description", "")

            print(f"Creating module: {title}")
            module_id = insert_module(cursor, title, description)

            # 2. Insert Objectives
            objectives: List[str] = dict_content.get("objectives", [])
            for i, obj_text in enumerate(objectives):
                print(f"  Adding objective: {obj_text}")
                insert_objective(cursor, module_id, obj_text, i)

            # 3. Insert Content Sections
            sections: List[Dict] = dict_content.get("sections", [])
            for i, section in enumerate(sections):
                section_title = section.get("section_title", "Untitled Section")
                body_text = section.get("body_text", "")
                media_link = section.get("media_link", None)
                content_type = section.get("content_type", "Text")

                print(f"  Adding section: {section_title}")
                insert_content_section(
                    cursor,
                    module_id,
                    section_title,
                    body_text,
                    content_type,
                    i,
                    media_link,
                )

        conn.commit()
        print("Import completed successfully.")

    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


# Example usage:
if __name__ == "__main__":
    # To run the import, ensure you have a 'module1.json' file and uncomment below:
    manager = get_module_manager()
    import_module_from_json("GRB Facilitator guidelines.json")
