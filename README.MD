SpreadSheetImporter.py allows for the uploading of information from a formatted spreadsheet into a MongoDB instance. This script connects to the same
mongoDB instance as the Beacon-in-a-box by default.

test_spreadsheet.xlsx has been provided as an example spreadsheet to ensure this tool works correctly when installed but also acts as a template file which should be adhered to for data imports.

A running mongoDB is required for the script to work.

To use SpreadSheetImporter.py call it from the CLI with an -f argument, the value of which is the absolute path to the spreadsheet file to import.
This script only accepts XLSX files, additional parsers can be added as required.
Only a single file can be passed to this script, to handle a list of files then a wrapper script which calls spreadsheetimporter.py should be used.
test_spreadsheet.xlsx is provided as an example spreadsheet

Details for the DB connection are defined in Shared/conf.py and the connection itself is created in Shared/utils.py which is then imported to the other scripts