import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv



# Set the URL you want to webscrape from
url = 'https://www.cdc.gov/media/dpk/diseases-and-conditions/coronavirus/coronavirus-2020.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

usNames = [item.get_text() for item in soup.find_all("th", {"scope": "row"})]
usNumbers = [item.get_text() for item in soup.find_all("td")]

positive = usNames[0]
negative = usNames[1]
pending = usNames[2]
Total = usNames[3]

positiveNumber = usNumbers[0]
negativeNumber = usNumbers[1]
pendingNumber = usNumbers[2]
totalNumber = usNumbers[3]

print("")
print("United States Corona Virus Infection:")
print("")
print("Positive Cases:", positiveNumber)
print("Negative Cases:", negativeNumber)
print("Pending Cases:", pendingNumber)
print("Total Cases:", totalNumber)
print("")

print("China Corona Virus Infection:")
print(" ")

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

infectionData = [item.get_text() for item in soup.find_all("td")]

countryName = infectionData[0]
infectedTotal = infectionData[1]
deaths = infectionData[2]

with open('cdc_data.csv','w') as f:
   i = 0
   fieldnames = ['Country', 'Infected', 'Deaths']
   thewriter = csv.DictWriter(f, fieldnames=fieldnames)
   print("Country /", end=' ')
   print("Infected /", end=' ')
   print("Deaths /", end=' ')
   print("Location:", end=' ')
   print(" ")
   thewriter.writeheader()
   for x in infectionData:
      while i <= 83:
         print(infectionData[i], end=' ')
         thewriter.writerow({'Country': infectionData[i]})
         i += 1
         print(infectionData[i], end=' ')
         thewriter.writerow({'Infected': infectionData[i]})
         i += 1
         print(infectionData[i], end=' ')
         thewriter.writerow({'Deaths': infectionData[i]})
         i += 1
         print(infectionData[i])
         #thewriter.writerow({'Location': infectionData[i]})
         i += 1
