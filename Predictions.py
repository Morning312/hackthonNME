import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from a given URL
def scrape_data(url, parser="html.parser"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, parser)
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Example function to scrape data for a specific topic
def scrape_environment_data():
    url = "https://example.com/environment-data"  # Replace with a real URL
    soup = scrape_data(url)
    if soup:
        # Extract data (this will vary based on the website structure)
        data = []
        table = soup.find("table")  # Assuming data is in a table
        if table:
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                data.append([col.text.strip() for col in cols])
        # Convert to DataFrame
        df = pd.DataFrame(data, columns=["Year", "Metric", "Value"])
        return df
    return None

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

# Main function to scrape data for all topics
def main():
    for topic, url in topics.items():
        print(f"Scraping data for {topic}...")
        soup = scrape_data(url)
        if soup:
            # Process and save data (customize based on website structure)
            print(f"Data for {topic} scraped successfully!")
        else:
            print(f"Failed to scrape data for {topic}.")

if __name__ == "__main__":
    main()