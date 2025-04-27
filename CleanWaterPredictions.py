import pandas as pd
import os
import numpy as np
 
regressionMap = {}

# Main function to scrape data for all topics
def main():
    df  = pd.read_csv("data/proportion-using-safely-managed-drinking-water.csv")
    df = df = df[df['Entity'] == 'World']
    X = df["Year"].values
    y = df["Share of the population using safely managed drinking water services"].values
    regressionMap.update({"Clean Water": np.polyfit(X, y, 2)})
    # temperature in Celsius average per year
    print(regressionMap)

if __name__ == "__main__":
    main()