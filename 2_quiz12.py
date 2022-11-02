#What is the result of the following code?

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())

#Download a csv file from https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip and load it into a pandas dataframe. How many rows and columns are there?
import pandas as pd
df = pd.read_csv('https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip')
print(df.head())
print("number of rows : ", df.shape[0])
print("number of columns : ", df.shape[1])




#What method can be used to get the number of non-NA values in a pandas dataframe?
df.count()

#Create a dataframe with 10 rows and 3 columns, where the values are random numbers between 1 and 10 (inclusive). Then, replace all values greater than 5 with the value 10.
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,10,size=(10, 3)))
print(df)

#create a dataframe from this link https://jsonplaceholder.typicode.com/albums
#import pandas as pd

#Url = 'https://jsonplaceholder.typicode.com/albums'
#data = pd.json_normalize(pd.read_json(Url)['data'])
import requests
link = requests.get("https://jsonplaceholder.typicode.com/albums").json()

df = pd.DataFrame(link)

print(df.head())








