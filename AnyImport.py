# //ToDo
# 1. Take in file - Complete
#   1A - Get file headers - Complete
# 2. Get api url
# 3. Get Api Headers
# 4. Map file to API headers 
#   4A - Use SQLalchemy as an in memory staging table. 
#5. Push data to api
#
#
#



###Imports
import pandas as pd
import tkinter as tk
from tkinter import filedialog





### Asks for file

root = tk.Tk()
root.withdraw() ##remove this when mapping portion is ready //Todo

file_path = filedialog.askopenfilename() #gets file path

source = pd.read_excel(file_path) #converts file to dataframe
*source_cols, = source #gets local file headers

print(source_cols)
