import pandas as pd
import os
import numpy as np

topics = ["Global Warming", "Nitrogen Oxide Emissions Air Pollution", "Carbon Monoxide Emissions Air Pollution", 
          "Black Carbon Emissions Air Pollution", "Poverty", "End World Hunger", "Aids", "Tuberculosis", "Malaria", 
          "Life Expectancy", "Access to Healthcare", "Access to Clean Water", "Microplastics in Human Body"]

regressionMap = {}

def makePrediction(topic, year, min, max):
    if topic not in regressionMap:
        raise ValueError(f"No regression data available for topic: {topic}")
    
    coefficients = regressionMap[topic]
    prediction = np.polyval(coefficients, year)

    if prediction < min:
        prediction = min
    elif prediction > max:
        prediction = max
    
    return prediction

# Main function to scrape data for all topics
def main():
    df  = pd.read_csv("data/BetterGlobalTemperatures.csv")
    X = df["Year"].values
    y = df["Temperature"].values
    regressionMap.update({"Global Warming": np.polyfit(X, y, 3)})
    # temperature in Celsius average per year

    df = pd.read_csv("data/AirPollution.csv")
    X = df["Year"].values
    y1 = df["Nitrogen oxides emissions from all sectors"].values
    y2 = df["Carbon monoxide emissions from all sectors"].values
    y3 = df["Black carbon emissions from all sectors"].values
    regressionMap.update({
        "Nitrogen Air Pollution": np.polyfit(X, y1, 3),
        "Carbon Monoxide Air Pollution": np.polyfit(X, y2, 3),
        "Black Carbon Air Pollution": np.polyfit(X, y3, 3)
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

    df  = pd.read_csv("data/incidence-of-tuberculosis-sdgs.csv")
    df = df = df[df['Entity'] == 'World']
    X = df["Year"].values
    y = df["Estimated incidence of all forms of tuberculosis"].values
    regressionMap.update({"Tuberculosis": np.polyfit(X, y, 3)})
    # tuberculosis incidence

    df  = pd.read_csv("data/Marine_Microplastics.csv")
    X = pd.to_datetime(df['Date'], format='mixed').dt.year.values
    y = df['Measurement'].values
    regressionMap.update({"Microplastics": np.polyfit(X, y, 3)})
    # marine microplastics
    
    df  = pd.read_csv("data/proportion-using-safely-managed-drinking-water.csv")
    df = df = df[df['Entity'] == 'World']
    X = df["Year"].values
    y = df["Share of the population using safely managed drinking water services"].values
    regressionMap.update({"Clean Water": np.polyfit(X, y, 3)})
    # clean water access

    print(regressionMap)

    df = pd.read_csv("data/HIV.csv")
    X = df["Year"].values
    y = df["Prevalence"].values
    regressionMap.update({"HIV": np.polyfit(X, y, 1)})  
    #Adults (15-49) prevalence (%)

    df = pd.read_csv("data/incidence-of-tuberculosis-sdgs.csv")
    df = df[df["Entity"] == "World"]
    X = df["Year"].values
    y = df["Estimated incidence of all forms of tuberculosis"].values
    regressionMap.update({"Tuberculosis": np.polyfit(X, y, 1)})
    #New cases of all forms of tuberculosis per 1,000 population at risk

    df = pd.read_csv("data/incidence-of-malaria.csv")
    df = df[df["Entity"] == "World"]
    X = df["Year"].values
    y = df["Incidence of malaria (per 1,000 population at risk)"].values
    regressionMap.update({"Malaria": np.polyfit(X, y, 1)})
    #Incidences of malaria (per 1,000 population at risk)

    df = pd.read_csv("data/life-expectancy.csv")
    df = df[df["Entity"] == "World"]
    X = df["Year"].values
    y = df["Period life expectancy at birth - Sex: total - Age: 0"]
    regressionMap.update({"Life Expectancy": np.polyfit(X, y, 1)})
    #Life Expectancy at birth


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