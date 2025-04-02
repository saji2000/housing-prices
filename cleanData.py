import pandas as pd

df = pd.read_csv("housing_data.csv")

print(df["Price"])

for i in range(len(df["Price"])):
    if df["Price"][i] < 0:
        df.loc[i, "Price"] *= -1

df.to_csv("housing_data.csv", index=False)