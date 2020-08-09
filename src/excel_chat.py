# 引入xlwings包，使用xw作为别名
import xlwings as xw

#visible是否可见。False表示后台运行。 add_book 是否新建一个工作簿
app = xw.App(visible=False, add_book=False)

# 打开Excel文件，参数传入Excel文档的地址
# 建议使用绝对路径
wb = xw.Book("E:\github\python\src\data.xlsx")

# 选择第一个sheet
sht0 = wb.sheets[0]

# 设置图表在Excel中的位置
chart = sht0.charts.add(200, 10)

# 设置数据源
chart.set_source_data(sht0.range("B2").expand())

# 图表类型
chart.chart_type = 'line'

# 设置标题内容
# 使用SetElement方法和参数2一起设置图表上方的标题
chart.api[1].SetElement(2)
chart.api[1].ChartTitle.Text = "2020年1月销售分布"

# 设置横轴标题
chart.api[1].SetElement(302)
chart.api[1].Axes(1).AxisTitle.Text = "日期"

# 设置x轴数据源
chart.api[1].SeriesCollection(1).XValues = sht0.range("A2:A32").value
print(chart.api[1].SeriesCollection(1).XValues)


# 保存修改
wb.save()

# 注释以下内容，可以在前端，看到修改。
# 关闭工作簿
wb.close()

# 关闭Excel，如果注释该语句，Excel程序，将不会自动退出，需要手动关闭
app.quit()
