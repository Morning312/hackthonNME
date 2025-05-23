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
