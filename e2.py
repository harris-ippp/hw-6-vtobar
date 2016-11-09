import requests
import csv
from bs4 import BeautifulSoup

url_template = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for line in open("ELECTION_ID"):
    parts = line.split() # split line into parts
    idl=parts[1]
    year=parts[0]
    url = url_template.format(idl)
    resp = requests.get(url)
    for i in year:
        file_name = year +".csv"
        with open(file_name, "w") as out:
            out.write(resp.text)
