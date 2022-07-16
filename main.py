import gspread

gc= gspread.service_account("secrets.json")

spreadsheet= gc.open("weather_doc")

#get a worksheet from file with index (0,1,2,3 sheet number in spreadsheet)
#worksheet1= spreadsheet.get_worksheet(0)

#get a worksheet by name of the sheet from the spreadsheet
worksheet1= spreadsheet.worksheet("2014")

data= worksheet1.get_all_records()
print(data[10])