import pandas as pd
import os
import numpy as np

topics = ["Global Warming", "Nitrogen Air Pollution", "Carbon Monoxide Air Pollution", 
          "Black Carbon Air Pollution", "Poverty", "World Hunger", "Microplastics", 
          "Clean Water", "HIV", "Tuberculosis", "Malaria", "Life Expectancy"]

regressionMap = {}

def predictCovid(year):
    if year <= 2068:
        return 0
    elif year <= 2100:
        return 2*(year-2068)
    elif year <= 2120:
        return 64+(year-2100)
    else:
        return 84

def predictMarsLanding(year):
    if year <= 2025:
        return 0
    else:
        return min(year - 2025, 100)
    
def predictAGI(year):
    if year <= 2030:
        return 0
    elif year <= 2050:
        return (year - 2030) * 5
    else:
        return 100

def predictQuantumComputers(year):
    if year <= 2035:
        return 0
    elif year <= 2135:
        return (year - 2035)
    else:
        return 100

def predictTeleportation(year):
    if year <= 2050:
        return 0
    return (year - 2050)*0.1
    

def predictTimeTravel(year):
    if year <= 2100:
        return 0
    return (year - 2100) * 0.05

def predictAlienContact(year):
    if year <= 2025:
        return 0
    elif year <= 2100:
        return (year - 2025) * 0.5
    else:
        return 37.5 + (year - 2100) * 0.125

def predictNuclearApocalypse(year):
    if year <= 2025:
        return 0
    return min(100, (year - 2025)^2 * 0.001)
    

def predictZombieApocalypse(year):
    if year <= 2025:
        return 0
    else:
        return (year-2025) * 0.001

def predictMeteorImpact(year):
    if year <= 2025:
        return 0
    else:
        return min(100, (year - 2025) / 100)


def predictAGITakeover(year):
    return predictAGI(year-2) 

def predictCovid(year):
    if (year == 2069):
        return 100
    else:
        return 0

def predictEvanMarriage(year):
    if (year >= 2069):
        return 1
    else:
        return 0

def predictChenkaiJaneStreetOffer(year):
    return 0

def predictEdwinMidlifeCrisis(year):
   if (year >= 2046 & year < 2056):
       return 0 + 10*(year - 2046)
   elif (year >= 2056 & year < 2066):
       return 0 + 10*(2066 - year)
   else:
       return 0 

def predictOCamlDomination(year):
    if year <= 2025:
        return 0
    return 100 #evan uses OCaml, so it will dominate the world

def predictGTAVIRelease(year):
    if year < 2025:
        return 0
    return (1-(0.5)^(year-2024))*100 # GTA VI will be released in 2025, and then every year it will be 50% more likely to be released

def makePrediction(topic, year, min, max):
    if topic == "Covid-69":
        predictCovid(year)
    elif topic == "Mars Landing":
        predictMarsLanding(year)
    elif topic == "AGI":
        predictAGI(year)
    elif topic == "Quantum Computers":
        predictQuantumComputers(year)
    elif topic == "Teleportation":
        predictTeleportation(year)
    elif topic == "Time Travel":
        predictTimeTravel(year)
    elif topic == "Alien Contact":
        predictAlienContact(year)
    elif topic == "Nuclear Apocalypse":
        predictNuclearApocalypse(year)
    elif topic == "Zombie Apocalypse":
        predictZombieApocalypse(year)
    elif topic == "Meteor Impact":
        predictMeteorImpact(year)
    elif topic == "AGI Takeover":
        predictAGITakeover(year)
    elif topic == "Evan marriage":
        predictEvanMarriage(year)
    elif topic == "Chenkai Jane Street Offer":
        predictChenkaiJaneStreetOffer(year)
    elif topic == "Edwin Midlife Crisis":
        predictEdwinMidlifeCrisis(year)
    elif topic == "OCaml Domination":
        predictOCamlDomination(year)
    elif topic == "GTA VI Release":
        predictGTAVIRelease(year)
    
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

    df  = pd.read_csv("data/Marine_Microplastics.csv")
    X = pd.to_datetime(df['Date'], format='mixed').dt.year.values
    y = df['Measurement'].values
    regressionMap.update({"Microplastics": np.polyfit(X, y, 3)})
    # Density of plastic per meter cubed
    
    df  = pd.read_csv("data/proportion-using-safely-managed-drinking-water.csv")
    df = df = df[df['Entity'] == 'World']
    X = df["Year"].values
    y = df["Share of the population using safely managed drinking water services"].values
    regressionMap.update({"Clean Water": np.polyfit(X, y, 3)})
    # Percentage of global population with access to safe drinking water

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