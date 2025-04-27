import pandas as pd
import os
import numpy as np

topics = [
    "AGI",
    "Mars Landing",
    "Quantum Computers",
    "Teleportation",
    "Time Travel",
    "Alien Contact",
    "Nuclear Apocalypse",
    "Zombie Apocalypse",
    "Meteor Impact",
    "AGI Takeover",
    "Covid-69",
    "Evan marriage",
    "Chenkai Jane Street Offer",
    "Edwin Midlife Crisis",
    "OCaml Domination",
    "Brainrot Animals",
    "GTA VI Release"
]

def predictCovid(year):
    if year <= 2068:
        return 0
    elif year <= 2100:
        return 2*(year-2068)
    elif year <= 
    else:
        return 10

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
    pass

def predictTimeTravel(year):
    pass

def predictAlienContact(year):
    pass

def predictNuclearApocalypse(year):
    pass

def predictZombieApocalypse(year):
    pass

def predictMeteorImpact(year):
    if year <= 2031:
        return 0
    else:
        return min(100, (year - 2031) / 10)

def predictAGITakeover(year):
    return predictAGI(year) + 2

def predictCovid(year):
    if (year == 2069):
        return 100
    else:
        return 0

def predictEvanMarriage(year):
    if (year == 2069):
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
    if (year <= 2030):
        return 0
    else:
        return 100

def predictGTAVIRelease(year):
    return 50
    
def predict(topic, year):
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
    else:
        raise ValueError(f"Unknown topic: {topic}")

    

if __name__ == "__main__":
    main()