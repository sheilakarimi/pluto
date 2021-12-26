import pandas as pd
import mysql.connector


file_path = '/home/workspace/pluto/myreport.xlsx'
excel_file = pd.ExcelFile(file_path)
sheet_names = excel_file.sheet_names
sheets_dict = pd.read_excel(file_path, sheet_name=None)


def database_connector(host, database, user, password):
    mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )


def get_header(sheets_dict):
    headers_list = []
    # import pudb; pudb.set_trace()
    for name in sheet_names:
        headers_list.append(sheets_dict[name].columns)

    return headers_list


def row_seperator(sheet_names):
    xl = pd.ExcelFile(file_path)
    for sheet in sheet_names:
        df = xl.parse(sheet)
        print(sheet)
        for i in range(len(sheets_dict[sheet])):
            # print(df.loc[i])
            values = ','.join([str(elem) for elem in df.loc[i]])
            print("insert into <table name> values(%s)" %values)


def run():
    # import pudb; pudb.set_trace()
    # db = database_connector('localhost', 'zabbix_report', 'worker', 'password')
    row_seperator(sheet_names)


if __name__ == '__main__':
    run()
    # for sheet in sheet_names:
    #     df = xl.parse(sheet)
    #     print(sheet)
    #     for i in range(len(sheets_dict[sheet])):
    #         # print(df.loc[i])
    #         values = ','.join([str(elem) for elem in df.loc[i]])
    #         print("insert into <table name> values(%s)" %values)
