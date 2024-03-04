import requests
import pandas as pd

def get_api_key(key_name):
    """Reads the specified API key from config.txt."""
    with open('config.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(key_name):
                return line.strip().split('=')[1]
    return None

def download_data(api_key_name, url):
    """Downloads data using the specified third-party API."""
    api_key = get_api_key(api_key_name)
    if api_key is None:
        raise ValueError(f"API key for {api_key_name} is not found in config.txt.")
    
    # Example API request
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Assuming the API returns JSON that can be directly converted to a DataFrame
        data = pd.DataFrame(response.json())
        return data
    else:
        response.raise_for_status()

def save_to_csv(data, filename):
    """Saves the DataFrame to a CSV file."""
    data.to_csv(filename, index=False)