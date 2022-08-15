A running mongoDB is required for these scripts to work, this should be the same DB as what the central beacon index will connect to

To use BeaconImporter.py call it from the CLI using basically any version of python, should be fine with any version 3.6+
The endpoints which are queried are defined in Shared/conf.py.

To use SpreadSheetImporter.py call it from the CLI but add a -f argument, the value of which is the absolute path to the spreadsheet file to import.
This script only accepts XLSX files for now, additional parsers can be added (such as csv) and I am happy to make these if needed.
Only a single file can be passed to this script, to handle a list of files then a wrapper script which calls spreadsheetimporter.py should be used.
test_spreadsheet.xlsx is provided as an example spreadsheet

Details for the DB connection are defined in Shared/conf.py and the connection itself is created in Shared/utils.py which is then imported to the other scripts