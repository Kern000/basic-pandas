import pandas as pd
import plotly.express as px

url = "./sales_by_region.csv"
df = pd.read_csv(url)

# This is targeting a column
# regionCondition = df["Region"] == "Europe"
# countryCondition = df["Country"] == "Greece"
# salesChannelCondition = df["Sales Channel"] == "Offline"
# itemTypeCondition = df["Item Type"] == "Snacks"
# orderPriorityCondition = df["Order Priority"] == "C"

# print(df["Region"])
# print("condition here", regionCondition)
# print("df[regionCondition] here", df[regionCondition])
# print("df[countryCondition] here", df[countryCondition])
# print("2nd method", df[regionCondition & salesChannelCondition])
# print("Filtering 4x conditions here", df[countryCondition & salesChannelCondition & itemTypeCondition & orderPriorityCondition])

regionCondition1 = df["Region"] == "Europe"
regionCondition2 = df["Region"] == "North America"

america_and_europe_df = df[regionCondition1 | regionCondition2]

productTypeCondition1 = df["Item Type"] == "Snacks"
productTypeCondition2 = df["Item Type"] == "Beverages"
snacks_and_beverages_df = df[productTypeCondition1 | productTypeCondition2]

# print(america_and_europe_df.head(15))
# print(snacks_and_beverages_df)

# print(df["Total Revenue"].mean())
# print(snacks_and_beverages_df["Total Revenue"].mean())
print(america_and_europe_df["Total Revenue"].mean())

# Each region becomes a group - and assign ea row to corresponding region
revenue_by_region = df.groupby("Region")["Total Revenue"].mean()
# print(revenue_by_region)

units_sold_by_item_type = df.groupby("Item Type")["Units Sold"].sum()
print(units_sold_by_item_type)

fig = px.bar(
    units_sold_by_item_type
)

fig.show()
