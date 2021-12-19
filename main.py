import pandas as pd


sheets_dict = pd.read_excel('/home/mehrnoosh/workspace/pluto/myreport.xlsx', sheet_name=None)
headers = sheets_dict['whole_avg-1'].columns

full_table = pd.DataFrame()
for sheet_name, sheet in sheets_dict.items():
    sheet['whole_avg-1'] = sheet_name
    counter = 0
    for i in range(len(sheets_dict[sheet_name])):
        print(sheets_dict[sheet_name][counter:counter+1])
        for j in headers:
            value = sheets_dict[sheet_name][counter:counter+1][j].item()
            print(j)
            print(value)

        counter += 1
