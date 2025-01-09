import re
import os
import sys

def clean_string(string: str):
    
    # Remove English characters, dots, and symbols
    cleaned_string = re.sub(r'[a-zA-Z.,()\/\-:;&\']', '', string)
    # Strip extra spaces and add non-empty results
    cleaned_string = cleaned_string.strip()

    # checking digit after removing english character
    checking_only_digit = re.sub(r'[0-9]', '', cleaned_string).strip()
    if checking_only_digit and len(checking_only_digit) >2:
        return cleaned_string

    return None

def clean_text(input_file_path: str):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        # Check if the line contains only digits, only symbols, or only non-character content
        if re.match(r'^\d+$', line.strip()) or re.match(r'^[^\w\s]+$', line.strip()) or re.match(r'^[\W_]+$', line.strip()):
            continue

        clean_str = clean_string(line)

        if clean_str:
            cleaned_lines.append(clean_str+'\n')

        # cleaned_lines.append(line)
        

    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(input_file_path), 'clean_n')
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file_path = os.path.join(output_dir, os.path.basename(input_file_path))

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)

    print(f"Cleaned file written to: {output_file_path}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 clean_text.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    clean_text(input_file_path)