# //ToDo
# 1. Take in file - Complete
#   1A - Get file headers - Complete
# 2. Get api url
# 3. Get Api Headers
# 4. Map file to API headers 
#   4A - Use SQLalchemy as an in memory staging table. Maybe. 
#5. Push data to api
#
#
#



###Imports
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from requests import request
import json
from pandas.io.json import json_normalize



### Asks for file

root = tk.Tk()
root.withdraw() ##remove this when mapping portion is ready //Todo

file_path = filedialog.askopenfilename() #gets file path

source = pd.read_excel(file_path) #converts file to dataframe
*source_cols, = source #gets local file headers

#init json request variables
instance = input("What instance? ")
base_url =".repfabric.com/yoxel_sync/v1.2/"
companies = "companies"
contacts = "contacts"

#start Json
response=request(url="http://"+instance+base_url+companies, method='get')
metadata = response.json()
metadata_loaded = json.loads(metadata)
results = json_normalize(metadata_loaded)
print(results)


print(source_cols)
