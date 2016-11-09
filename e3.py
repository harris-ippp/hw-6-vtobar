import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

#Creat list of files

years=[] #create empty list of years

# loop to search in lines of the file ELECTION_ID
#create newvar to split each line in python
#to update each year in the lisst
for line in open("ELECTION_ID"):
    newvar=line.strip().split()
    year=newvar[0]
    years.append(year)

#create an empty list for files
files = []

#create a list of the .csv files, naming them with every element in the list of years (years)
for y in years:
    files.append(y + ".csv")

#create an empty list for dataframes
dataframes=[]

#use a loop to search for every element in files
#use a loop to search for every element in years
#pandas

for f in files:
    for y in range(1924, 2013, 4):
        header = pd.read_csv(f, nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()
        df = pd.read_csv(f, index_col = 0, thousands = ",", skiprows = [1])
        df.rename(inplace = True, columns = d) # rename to democrat/republican
        df.dropna(inplace = True, axis = 1)    # drop empty columns
        df["Year"] = y
        dataframes.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

m = pd.concat(dataframes)
print(m)


#To plot
m['Share Republican']=m['Republican']/m['Total Votes Cast']
g=m[m.index == "Accomack County"].plot(x="Year", y="Share Republican", kind="hist")
g.get_figure().savefig('accomack.png')
