from xlwt import *
import re




def updata_info(updata_mumbers,get_path):
    ini_list = []
    so_list = []
    dll_list = []
    sql_list = []

    book = Workbook(encoding='utf-8')
    tmp = book.add_sheet('升级文件信息', cell_overwrite_ok=True)
    for every_member in updata_mumbers:

        if re.match('.+.sql.+', every_member) != None:
            sql_list.append(every_member)
        elif re.match('.+.ini.+', every_member) != None:
            ini_list.append(every_member)
        elif re.match('.+.dll.+', every_member) != None:
            dll_list.append(every_member)
        elif re.match('.+.so.+', every_member) != None:
            so_list.append(every_member)

    num1 = len(sql_list)
    num2 = len(ini_list)
    num3 = len(dll_list)
    num4 = len(so_list)

    tmp.write(int(num1 / 2), 0, 'sql文件')
    tmp.write(num1 + 1 + int(num2 / 2), 0, 'ini文件')
    tmp.write(num1 + num2 + 2 + int(num3 / 2), 0, 'dll文件')
    tmp.write(num1 + num2 + num3 + 3 + int(num4 / 2), 0, 'so文件')

    i = 0
    for sql in sql_list:
        tmp.write(i, 2, sql)
        i = i + 1

    i = i + 1
    for ini in ini_list:
        tmp.write(i, 2, ini)
        i = i + 1
    i = i + 1
    for dll in dll_list:
        tmp.write(i, 2, dll)
        i = i + 1
    i = i + 1
    for so in so_list:
        tmp.write(i, 2, so)
        i = i + 1
    book.save('{}升级说明.xls'.format(get_path))

