import sys

# INPUT FILE NAME docx
filename = "GRB Facilitator guidelines.docx"
# output file name json
output_filename = "GRB Facilitator guidelines.json"


def check_imports():
    missing_packages = []

    # Check for python-docx
    try:
        import docx
    except ImportError:
        missing_packages.append("python-docx")

    # Check for google-generativeai
    try:
        import google.generativeai
    except ImportError:
        missing_packages.append("google-generativeai")

    if missing_packages:
        print("\n" + "!" * 50)
        print("MISSING LIBRARIES DETECTED")
        print("!" * 50)
        print("\nThis script requires the following packages to run:")
        for pkg in missing_packages:
            print(f" - {pkg}")

        print("\nPlease run this command in your terminal to fix it:")
        print(f"pip install {' '.join(missing_packages)}")
        print("\n" + "!" * 50 + "\n")

        # Stop the script here
        sys.exit(1)


from doc_to_json_helper import extract_text_from_docx, analyze_document_with_gemini
import json


def main():
    print(f"Reading {filename}...")
    doc_text = extract_text_from_docx(filename)

    if doc_text:
        print("Sending content to Gemini for analysis...")
        json_output = analyze_document_with_gemini(doc_text)

        if json_output:
            # Validate and format the JSON
            try:
                parsed_json = json.loads(json_output)

                # Save to file
                with open(output_filename, "w", encoding="utf-8") as f:
                    json.dump(parsed_json, f, indent=2)

                print(f"Success! JSON saved to {output_filename}")

                # Print a preview
                print("\nPreview of output:")
                print(json.dumps(parsed_json, indent=2)[:500] + "...")

            except json.JSONDecodeError:
                print("Gemini returned invalid JSON. Raw output:")
                print(json_output)
    else:
        print("Failed to extract text.")


if __name__ == "__main__":
    main()
