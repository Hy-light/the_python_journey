# APIs through request library
# Fruityvice API

import requests 
import json 
import pandas as pd

# obtain the fruityvice API data using requests.get("url") function. The data is in a json format.

# data = requests.get("https://fruityvice.com/api/fruit/all") # this page is currentlu unavailable and returning an error

# Make the request
url = "https://fruityvice.com/api/fruit/all"  # Replace with your actual URL
data = requests.get(url)
# Check the status code
if data.status_code == 200:
    print("Request was successful.")
    if 'application/json' in data.headers['Content-Type']:
        try:
            # If JSON is returned, parse it
            results = data.json()  # You can use data.json() instead of json.loads()
            print(results)
            # convert json into pandas data frame
            pd.DataFrame(results)
            df2 = pd.json_normalize(results)
            print(df2)
            cherry = df2.loc[df2["name"] == 'Cherry']
            (cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

        except json.JSONDecodeError:
            print("Error: Failed to parse JSON.")
    else:
        print("Error: Expected JSON, but got:", data.headers['Content-Type'])
        # Optionally, you can print or log the HTML response for debugging
        print(data.text)

else:
    print(f"Error: Received status code {data.status_code}")
    print(f"Response: {data.text}")



'''
The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
'''


