import pandas as pd
import requests

class BEAClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://apps.bea.gov/api/data"
    
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
             
# from data_loading import BEAClient
# # Initialize the BEA client
# bea_client = BEAClient(api_key=BEA_API_KEY)
# # Fetch GDP data for the year 2020 (or any other year of interest)
# gdp_data = bea_client.get_gdp_data(year="2020")
# # Print the head of the GDP data DataFrame to verify the data
# print(gdp_data.head())
