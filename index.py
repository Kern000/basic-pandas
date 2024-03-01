import pandas as pd
import plotly.express as px
import plotly.io as pio

url = "https://raw.githubusercontent.com/kunxin-chor/data-science-raw-files/main/revenue.csv"
df = pd.read_csv(url)

# df.info is the dataframe = number of entries, their types, name of columns. dataframes is like excel sheet, w rows and columns format

"""
RangeIndex: 5 entries, 0 to 4
 0   date     5 non-null      object
 1   reach    5 non-null      int64
 2   revenue  5 non-null      float64
dtypes: float64(1), int64(1), object(1)

"""
# column is the date, reach, revenue

print(df.info())

df2 = pd.read_csv("./bedroom-type.csv")
df3 = pd.read_csv("./california_housing_test.csv")
print(df3.info())

fig = px.line(
                df, 
                x="date",
                y="reach",
                labels={"reach": "Reach", "date": "Date"},
                title="Reach vs Date"
              )
fig.update_xaxes(dtick="D1", tickformat="%Y-%m-%d")
# big Y is the full year, dtick is each tick https://plotly.com/python/reference/layout/xaxis/

fig.show()

# fig1 = dict({
#     "data": [
#               { 
#                 "type": "bar",
#                 "x": [1, 2, 3],
#                 "y": [1, 3, 2]}
#             ]
#     ,
#     "layout": {
#                 "title": {"text": "A Figure Specified By Python Dictionary"}
#               }
# })
# pio.show(fig1)














