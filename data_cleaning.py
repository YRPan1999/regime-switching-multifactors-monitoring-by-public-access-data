import os
import pandas as pd

def read_json_to_df(filepath: str) -> pd.DataFrame:
    """
    Reads a JSON file from the specified filepath and converts it into a pandas DataFrame.

    Parameters:
    - filepath (str): The full path to the JSON file.

    Returns:
    - DataFrame: A pandas DataFrame containing the data from the JSON file.
    """
    return pd.read_json(filepath)


def read_all_jsons_in_directory(directory_path: str) -> dict[str, pd.DataFrame]:
    """
    Reads all JSON files in the specified directory and converts them into pandas DataFrames.

    Parameters:
    - directory_path (str): The path to the directory containing JSON files.

    Returns:
    - dict[str, pd.DataFrame]: A dictionary where keys are filenames and values are DataFrames.
    """
    dataframes = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".jsonc"):  # or ".json", adjust as necessary
            filepath = os.path.join(directory_path, filename)
            df = pd.read_json(filepath)
            dataframes[filename] = df
    
    return dataframes


# filepath = 'BEA/responses/gdp_by_industry.jsonc'
# df = read_json_to_df(filepath)
# # print(df.head())  # Displays the first few rows of the DataFrame
# df

# directory_path = 'BEA/responses'
# dataframes = read_all_jsons_in_directory(directory_path)
# for name, df in dataframes.items():
#     print(f"Data from {name}:")
#     print(df.head())  # Example operation: print the first few rows of each DataFrame