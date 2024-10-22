import plotly.express as pl_ex

plot = pl_ex.pie(
    labels=["1° data", "2° data", "3° data", "4° data", "5° data"],
    values=[1255, 425, 2700, 2341, 855]
)

plot.show()
