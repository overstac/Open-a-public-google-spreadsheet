import gspread

gc= gspread.service_account("secrets.json")

spreadsheet= gc.open("weather_doc")

#get a worksheet from file with index (0,1,2,3 sheet number in spreadsheet)
#worksheet1= spreadsheet.get_worksheet(0)

#get a worksheet by name of the sheet from the spreadsheet
worksheet1= spreadsheet.worksheet("2014")
#get rows by cells
data= worksheet1.get_values("A5:F7")

#get a row by index
rows= worksheet1.row_values(3)

#get column by index
column= worksheet1.col_values(2)[2:]

print(column)