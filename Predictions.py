import pandas as pd
import os
import numpy as np

# Topics and their respective URLs (replace with actual URLs)
topics = {
    "Global Warming": "https://example.com/global-warming-data",
    "Nitrogen Oxide Emissions Air Pollution": "https://example.com/air-pollution-data",
    "Carbon Monoxide Emissions Air Pollution": "https://example.com/sea-pollution-data",
    "Black Carbon Emissions Air Pollution": "https://example.com/ozone-layer-data",
    "Poverty": "https://example.com/poverty-data",
    "End World Hunger": "https://example.com/world-hunger-data",
    "Aids": "https://example.com/aids-data",
    "Lung Cancer": "https://example.com/cancer-data",
    "Malaria": "https://example.com/malaria-data",
    "Life Expectancy": "https://example.com/life-expectancy-data",
    "Access to Healthcare": "https://example.com/healthcare-data",
    "Access to Clean Water": "https://example.com/clean-water-data",
    "Microplastics in Human Body": "https://example.com/microplastics-data",
}

regressionMap = {}

# Main function to scrape data for all topics
def main():
    df  = pd.read_csv("data/BetterGlobalTemperatures.csv")
    X = df["Year"].values
    y = df["Temperature"].values
    regressionMap.update({"Global Warming": np.polyfit(X, y, 2)})
    # temperature in Celsius average per year

    df = pd.read_csv("data/AirPollution.csv")
    X = df["Year"].values
    y1 = df["Nitrogen oxides emissions from all sectors"].values
    y2 = df["Carbon monoxide emissions from all sectors"].values
    y3 = df["Black carbon emissions from all sectors"].values
    regressionMap.update({
        "Nitrogen Air Pollution": np.polyfit(X, y1, 2),
        "Carbon Monoxide Air Pollution": np.polyfit(X, y2, 2),
        "Black Carbon Air Pollution": np.polyfit(X, y3, 2)
    })
    #emissions in tons per year

    df = pd.read_csv("data/Poverty.csv")
    X = df.columns.values[1:].astype(int)
    y = df.iloc[0].values[1:].astype(float)
    regressionMap.update({"Poverty": np.polyfit(X, y, 1)})
    #poverty headcount rate in percentage of total population (below $6.85 per day)

    df = pd.read_csv("data/WorldHunger.csv")
    X = df["Year"].values
    y = df["percent_hunger"].values
    regressionMap.update({"World Hunger": np.polyfit(X, y, 1)})
    # percentage of population undernourished

    

if __name__ == "__main__":
    main()








# new_df = pd.DataFrame(columns=["Year", "Temperature"])
    # for index, row in df.iterrows(): 
    #     if index % 12 == 0:
    #         sum = 0
    #         for i in range(12):
    #             sum+=df.iloc[index+i]["LandAverageTemperatureCelsius"]
    #         sum = sum / 12
    #         new_df.loc[int(index/12)] = [df.iloc[index]["dt"][:4], sum]
    # new_df.to_csv("data/BetterGlobalTemperatures.csv")