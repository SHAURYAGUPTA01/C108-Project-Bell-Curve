import pandas as pd
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
x = df["Avg Rating"].tolist()
fig = ff.create_distplot( [x] , ["brand"] )
fig.show()