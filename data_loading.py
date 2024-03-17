import os
import json
from pprint import pprint
from BEAclient import BureauEconomicAnalysisClient

class BEADataRetriever:
    """Class to retrieve and save data from the BEA API."""

    def __init__(self, api_key_file='config.txt', dump_directory='BEA/responses'):
        """Initialize the BEA Data Retriever with an API key."""
        self.bea_client = self.initialize_client(api_key_file)
        self.dump_directory = dump_directory

    def initialize_client(self, api_key_file):
        """Load the API key and initialize the BEA client."""
        api_keys = self.load_api_keys(api_key_file)
        BEA_API_KEY = api_keys.get('BEA_API_KEY')
        return BureauEconomicAnalysisClient(api_key=BEA_API_KEY)

    def load_api_keys(self, filepath):
        """Load API keys from a configuration file."""
        api_keys = {}
        with open(filepath, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=')
                    api_keys[key] = value
        return api_keys

    def save_response(self, name, data):
        """Save the retrieved data to a JSON file."""
        directory = self.dump_directory
        filename = f"{name}.jsonc"
        filepath = os.path.join(directory, filename)

        os.makedirs(directory, exist_ok=True)

        with open(file=filepath, mode="w+", encoding="utf-8") as sample_file:
            json.dump(obj=data, fp=sample_file, indent=4)

    def get_dataset_list(self):
        """Grab the Dataset List."""
        dataset_list = self.bea_client.get_dataset_list()
        pprint(dataset_list)

    def get_parameters_list(self, dataset_name):
        """Grab the Paramters List."""
        parameters_set_list = self.bea_client.get_parameters_list(dataset_name)
        pprint(parameters_set_list)

    def retrieve_and_save_data(self, function_to_call, save_name, *args, **kwargs):
        """Retrieve data using a BEA client function and save it."""
        data = function_to_call(*args, **kwargs)
        self.save_response(save_name, data)

    # Data retrieval functions:

    def get_gdp_by_industry(self):
        """Retrieve and save GDP by Industry data."""
        self.retrieve_and_save_data(
            self.bea_client.gdp_by_industry,
            "gdp_by_industry",
            year=["2021", "2022"], industry="52", frequency="A"
        )
    
    def get_national_income_and_product_accounts(self):
        """Retrieve and save National Income and Product Accounts data."""
        self.retrieve_and_save_data(
            self.bea_client.national_income_and_product_accounts,
            "national_income_and_product_accounts",
            table_name="T10101", frequency=["A", "Q"], year=["2021", "2022"]
        )

    def get_national_income_and_product_accounts_detail(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.national_income_and_product_accounts_detail,
            "national_income_and_product_accounts_detail",
            table_name="U20305", frequency=["A", "Q"], year=["2021", "2022"]
        )

    def get_fixed_assets(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.fixed_assets,
            "fixed_assets",
            table_name="FAAt201", year=["2021", "2022"]
        )
    
    def get_direct_investments_and_multinational_enterprises(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.direct_investments_and_multinational_enterprises,
            "direct_investments_and_multinational_enterprises",
            direction_of_investment="outward",
            classification="country",
            series_id=["30"],
            year=["2021", "2022"],
            country=["650", "699"]
        )
    
    def get_activities_investments_and_multinational_enterprises(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.activities_investments_and_multinational_enterprises,
            "activities_investments_and_multinational_enterprises",
            direction_of_investment="outward",
            classification="CountryByIndustry",
            series_id=["4", "5"],
            year=["2021", "2022"],
            country=["202"],
            ownership_level=False,
            industry="ALL",
            non_bank_affilates_only=False
        )

    def get_international_transactions(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.international_transactions,
            "international_transactions",
            indicator=["BalGds"],
            area_or_country=["China"],
            year=["2021", "2022"],
            frequency=["A"]
        )

    def get_international_investments_positions(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.international_investments_positions,
            "international_investments_positions",
            type_of_investment=["FinAssetsExclFinDeriv"],
            component=["ChgPosPrice"],
            year="ALL",
            frequency=["A"]
        )

    def get_input_output_statistics(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.input_output_statstics,
            "input_output_statistics",
            table_id=["56"], year=["2021", "2022"]
        )

    def get_underlying_gdp_by_industry(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.underlying_gdp_by_industry,
            "underlying_gdp_by_industry",
            industry="ALL", frequency=["A"], year=["2021", "2022"], table_id="ALL"
        )

    def get_international_trade_services(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.international_trade_services,
            "international_trade_services",
            type_of_service="Telecom",
            trade_direction=["Exports"],
            year="ALL",
            affiliation=["USPARENTS"],
            area_or_country="AllCountries"
        )

    def get_regional_data(self):
        """Retrieve and save ??? data."""
        self.retrieve_and_save_data(
            self.bea_client.regional,
            "regional_data",
            table_name=["CAINC1"], line_code=1, geo_fips=["COUNTY"], year=["2021", "2022"]
        )


# Usage Example:


# def main():
#     data_retriever = BEADataRetriever()

#     # Grab the Dataset List.
#     dataset_list = data_retriever.get_dataset_list()
#     pprint(dataset_list)

#     # Grab the Paramters List.
#     parameters_set_list = data_retriever.get_parameters_list(dataset_name="Regional")
#     pprint(parameters_set_list)

#     # GDP by Industry
#     data_retriever.get_gdp_by_industry()

#     # National Income and Product Accounts
#     data_retriever.get_national_income_and_product_accounts()

#     # National Income and Product Accounts Detail
#     data_retriever.get_national_income_and_product_accounts_detail()

#     # Fixed Assets
#     data_retriever.get_fixed_assets()

#     # Direct Investments and Multinational Enterprises
#     data_retriever.get_direct_investments_and_multinational_enterprises()

#     # Activities Investments and Multinational Enterprises
#     data_retriever.get_activities_investments_and_multinational_enterprises()

#     # International Transactions
#     data_retriever.get_international_transactions()

#     # International Investments Positions
#     data_retriever.get_international_investments_positions()

#     # Input-Output Statistics
#     data_retriever.get_input_output_statistics()

#     # Underlying GDP by Industry
#     data_retriever.get_underlying_gdp_by_industry()

#     # International Trade Services
#     data_retriever.get_international_trade_services()

#     # Regional Data
#     data_retriever.get_regional_data()

# if __name__ == "__main__":
#     main()
