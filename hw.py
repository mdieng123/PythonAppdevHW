import requests
import json

class CatFactsAPI:
    def __init__(self):
        self.api_url = 'https://catfact.ninja/breeds'
    
    def get_nth_cat_breed(self, n):
        try:
            # Do get request
            result = requests.get(self.api_url)
            result.raise_for_status()  # Raise an exception for bad responses
            
            # Parse JSON response
            breeds_data = result.json()
            
            # Extract the nth cat breed
            if 'data' in breeds_data and n > 0 and n <= len(breeds_data['data']):
                nth_breed = breeds_data['data'][n - 1]['breed']
                return nth_breed
            else:
                return f"Error: Invalid index. There are {len(breeds_data['data'])} cat breeds available."
        
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

# Example usage:
cat_facts_api = CatFactsAPI()
nth_breed = cat_facts_api.get_nth_cat_breed(3)
print(f"The 3rd cat breed is: {nth_breed}")
