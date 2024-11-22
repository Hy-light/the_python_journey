import requests
import pandas as pd
import json

# the official random jokes api
'https://official-joke-api.appspot.com/jokes/ten'

data = requests.get("https://official-joke-api.appspot.com/jokes/ten")
# print(data.text)
# print(data.status_code)

# parse response as json
results = json.loads(data.text)
# print(results)

# Convert json data into pandas data frame. Drop the type and id columns

df = pd.DataFrame(results)
# print(df)

df.drop(columns=["type","id"],inplace=True)
print(df)


