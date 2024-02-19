import re
import sys

from titlecase import titlecase


def apply_apa_titlecase(input_file):
    # Define the regular expression pattern to match each entry in the BibTeX file
    entry_pattern = re.compile(r'(\W*)(title|journal|booktitle)\s*=\s*{(.*)},')
    # Currently the fields title, journal, and booktitle are capitalized

    # Read input file and apply APA title case to the specified fields
    with open(input_file, 'r') as f:
        content = f.read()

    # Apply APA title case to matched field values and preserve field names
    def transform(match):
        entry_start = match.group(1)
        field_name = match.group(2)
        field_value = match.group(3)
        return entry_start + field_name + ' = {' + titlecase(field_value) + '},'

    # Apply the transformation to each entry in the BibTeX file
    modified_content = entry_pattern.sub(transform, content)

    # Generate output file name based on input file name
    output_file = input_file.replace('.bib', '-capitalized.bib')

    # Write modified content to output file
    with open(output_file, 'w') as f:
        f.write(modified_content)

    return output_file

# Check if the script is being run as a standalone program
if __name__ == "__main__":
    # Check if the input file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python path/to/bib-titlecase.py path/to/library.bib")
        sys.exit(1)
    
    input_file = sys.argv[1]

    # Apply APA title case to the input file and generate the output file
    output_file = apply_apa_titlecase(input_file)
    print("Output file:", output_file)
