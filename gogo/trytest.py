import xlrd

data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\新建 XLS 工作表.xls')
table = data.sheets()[0]

tables=[]

def intable(excel):
    for rown in range(excel.nrows):
        array={'id':''}
        array['id']=table.cell_value(rown,0)
        tables.append(array)


if __name__ == '__main__':
    intable(table)
    for i in tables:
        print(i)