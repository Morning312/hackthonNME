import pandas as pd
import os
import numpy as np

# Topics and their respective URLs (replace with actual URLs)
topics = {
    "Global Warming": "https://example.com/global-warming-data",
    "Air Pollution": "https://example.com/air-pollution-data",
    "Sea Pollution": "https://example.com/sea-pollution-data",
    "Ozone Layer": "https://example.com/ozone-layer-data",
    "Nuclear Deescalation": "https://example.com/nuclear-deescalation-data",
    "Poverty": "https://example.com/poverty-data",
    "End World Hunger": "https://example.com/world-hunger-data",
    "Diseases": "https://example.com/diseases-data",
    "Aids": "https://example.com/aids-data",
    "Cancer": "https://example.com/cancer-data",
    "Malaria": "https://example.com/malaria-data",
    "Life Expectancy": "https://example.com/life-expectancy-data",
    "Gender Equality": "https://example.com/gender-equality-data",
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
    m, b = np.polyfit(X, y, 1)
    regressionMap.update({"Global Warming": (m, b)})

    


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