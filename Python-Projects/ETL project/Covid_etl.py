import pandas as pd
import requests

class CovidETL:
    """ETL pipeline for COVID-19 data from disease.sh API."""
    def __init__(self, country: str):
        """ Initialize with the target country. Args: country (str): Country name (e.g., 'slovakia')."""
      
        self.country = country
        self.df = None

    def extract(self):
        """Extract COVID-19 data from the API."""
      
        url = f"https://disease.sh/v3/covid-19/countries/{self.country}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code}")

        data = response.json()

        # Show a summary in the console
        print(f"Country: {data['country']}")
        print(f"Cases: {data['cases']}")
        print(f"Today Cases: {data['todayCases']}")
        print(f"Deaths: {data['deaths']}")
        print(f"Recovered: {data['recovered']}")

        # Store as DataFrame
        self.df = pd.DataFrame([data])

    def transform(self):
        """Add 'Active' cases column to DataFrame."""
      
        if self.df is None:
            raise ValueError("No data to transform. Run extract() first.")
        self.df["Active"] = (self.df["cases"] - self.df["deaths"] - self.df["recovered"])

    def load(self, output_file: str):
        """ Save the DataFrame to a CSV file. Args: output_file (str): Path to the output CSV file. """
      
        if self.df is None:
            raise ValueError("No data to load. Run extract() and transform() first.")
        self.df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")

if __name__ == "__main__":
    etl = CovidETL("slovakia")
    etl.extract()
    etl.transform()
    etl.load("covid_slovakia.csv")
    print(etl.df)



