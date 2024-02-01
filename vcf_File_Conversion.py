import re

def convert_version(vcard_content):
    # Replace vCard 2.1 version with 3.0
    return vcard_content.replace("VERSION:2.1", "VERSION:3.0")

def convert_numbers_in_vcard(vcard_content):
    # Split the input content into individual vCard entries
    vcard_entries = re.split(r'(?<=END:VCARD)\n', vcard_content)

    # Process each vCard entry individually
    vcard_updated_entries = []
    for vcard_entry in vcard_entries:
        if 'BEGIN:VCARD' in vcard_entry and 'END:VCARD' in vcard_entry:
            # Find and replace TEL;TYPE=CELL occurrences with specified formats
            tel_lines = re.findall(r'TEL;TYPE=CELL:[^\n]*\n', vcard_entry)

            if tel_lines:
                new_tels = []

                for i, tel_line in enumerate(tel_lines):
                    tel_parts = re.split(r':|\n', tel_line, maxsplit=1)
                    new_tels.append(f'TEL;TYPE={["CELL", "HOME", "WORK", f"OTHER{i + 1}"][i % 3]}:{tel_parts[1]}')

                vcard_entry = vcard_entry.replace(''.join(tel_lines), '\n'.join(new_tels))

            vcard_updated_entries.append(vcard_entry)

    # Join the processed vCard entries
    vcard_updated_content = '\n'.join(vcard_updated_entries)

    return vcard_updated_content

def main():
  # Provide your .vcf file path below; for Windows ('D:/MyDrive/Contacts-Copy.vcf') & LiNUX ('user/yourContactsFolder/Contacts-Copy.vcf')
    input_file_path = 'path/to/your/input.vcf'
  # Provide path and name for your new converted .vcf file; for Windows ('D:/MyDrive/Contacts-NEW.vcf') & LiNUX ('user/yourContactsFolder/Contacts-NEW.vcf')
    output_file_path = 'path/to/your/output.vcf'

    try:
        # Read the vCard file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            vcard_content = file.read()

        # Convert version from 2.1 to 3.0
        vcard_content = convert_version(vcard_content)

        # Perform the number conversion
        vcard_updated_content = convert_numbers_in_vcard(vcard_content)

        # Write the updated vCard content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(vcard_updated_content)

        print("Conversion completed successfully.")

    except Exception as e:
        print(f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    main()
