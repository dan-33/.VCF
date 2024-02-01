# .VCF File /vCard Conversions From 2.1 to any (3.0/3.1/4)
## It resolves all the below issues, without sharing/exposing your data
#### Resolve iCloud icompatbility / contacts(.vcf file /vCard) uploads errors
#### Resolve iCloud unspported contacts issues
#### Resolve iCloud Missing Contact Issues Manually without exposing/sharing your data with any entity
#### Conversion of the Android contacts to iPhone supported contacts
#### Conversion of the Android contacts to iPhone supported contacts

###### With this you can convert the .vcf file/vCard version 2.1 to 3.0/3.1 supported by iPhone/iCloud. You can export you android contacts and use save the on your iPhone

## Two Methods are available
### 1. Manually performing below steps/ If you can't understand code;
1. First Export the contacts from the Android/ old iPhone, which most probably have the 2.1 version .vcf file.
2. Open the vcf file, with any text editor Notepad/ Notepad++ / mousepad or any.
3. First find and replace "VERSION:2.1" with "VERSION:3.0" and save file.
4. Then find "TEL;CELL:" and replace with "TEL;TYPE=CELL:"
5. Then find "N;" if any and replace with "N:"
6. Then find "EMAIL:" if any, replace with "EMAIL;type=INTERNET;type=HOME;type=pref:"
7. Then find any "TEL;X-Fax:" if any, replace with "TEL;TYPE=CELL:"
8. Then find any "TEL;X-Mobile:" if any, replace with "TEL;TYPE=CELL:"
9. Then find any "TEL;X-CUSTOM" if any, replace with "TEL;TYPE=CELL:"
10. Then find any "TEL;X-Other:" if any, replace with "TEL;TYPE=CELL:"
11. Save this file, use it as Version 3.0 file anywhere. (incase of icloud, open icloud.com, sign in and import the vcf file, almost all of your contacts will be found uploaded.

### 2. Auto Convert with Python Script
You need to run the script, provide it your .vcf file path and also mention where you need to save new .vcf file and its name.
Script file is "vcf_File_Conversion.py".
Below is the direct link.
"https://github.com/dan-33/.VCF/blob/main/vcf_File_Conversion.py"
