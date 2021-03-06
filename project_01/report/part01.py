import pyecharts

print(pyecharts.__version__)

from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家B", [9, 12, 33, 12, 65, 35])
# render 会生成本地 HTML 文件，默认会在当前目录生成  文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()


