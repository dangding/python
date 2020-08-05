import xlwings as xw

#app = xw.App(visible=True, add_book=False)

#wb = app.books.open("hello.xlsx")

wb = xw.Book("E:\github\python\src\hello.xlsx")

# 打开第一个sheet
sht = wb.sheets[0]

# 引用单元格
sht.range("a1").value = "a1"


#wb.close();