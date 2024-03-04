import pandas as pd
import requests

class BEAClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://apps.bea.gov/api/data"

    def load_api_key(self, filepath='config.txt'):
        with open(filepath, 'r') as file:
            for line in file:
                if 'BEA_API_KEY=' in line:
                    self.api_key = line.strip().split('=')[1]
    
    def get_gdp_data(self, year="2020"):
        params = {
            "UserID": self.api_key,
            "Method": "GetData",
            "datasetname": "NIPA",
            "TableName": "T10101",
            "Frequency": "Q",
            "Year": year,
            "ResultFormat": "JSON"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            # Transform the data as needed, for example, into a pandas DataFrame
            # The following line is a placeholder and should be adjusted to match the actual data structure
            df = pd.DataFrame(data['BEAAPI']['Results']['Data'])
            return df
        else:
            return pd.DataFrame()  # Return an empty DataFrame if the request fails

###################
## Example usage ##
###################
             
# if __name__ == "__main__":
#     api_key = ???
#     bea_client = BEAClient(api_key=api_key)
#     gdp_data = bea_client.get_gdp_data(year="2020")  # Specify the year or other parameters as needed
#     print(gdp_data.head())