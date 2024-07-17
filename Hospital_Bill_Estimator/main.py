import pyodbc
import pandas as pd
import string
from credentials import user, password

availableSections = {'Radiology Procedures': range(70010,79999 + 1),
                     'Pathology and Laboratory Procedures': range(80047,89398+1), 
                     'Fine Needle Aspiration Biopsy Procedures': range(10004,10021+1),
                     'Surgical Procedures on the Heart and Pericardium':range(33016,33999+1)}

## CONNECTION TO THE SERVER AND DATABASE ##
connection = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};SERVER=hospitalpriceapp.database.windows.net;DATABASE=hospitalPriceApp;UID='+user+';PWD='+password+';Encrypt=No')
cursor = connection.cursor()

## Welcome and intro information
print("***WELCOME TO THE HOSPITAL PRICE ESTIMATE TOOL***\n")


query = 'SELECT schema_name(t.schema_id) AS schema_name, t.name AS table_name, t.create_date, t.modify_date FROM sys.tables t ORDER BY schema_name, table_name;'

cursor.execute(query)
hospitals = [] # Holds all of the hospitals that are in the sql database
chosenHospitals = [] # Holds user selected hospitals to be used for comparison later

for row in cursor.fetchall():
    hospitals.append(row[1])
print('List of hospitals with pricing data')
print('************************************************************************************')

for i, name in enumerate(hospitals, 1):  # Start numbering from 1
    print(f"{i}.) {name}")
print('************************************************************************************')

def findHospital(numOfInput):
   switch = {
      1: hospitals[0],
      2: hospitals[1],
      3: hospitals[2],
      4: hospitals[3],
      5: hospitals[4],
      6: hospitals[5],
      7: hospitals[6],
      8: hospitals[7],
      9: hospitals[8],
      10: hospitals[9],
      11: hospitals[10],
      12: hospitals[11],
      13: hospitals[12]
   }
   return switch.get(numOfInput, "Not in hospital list")

## Ask user for hospitals to compare
numOfComparison = int(input("\nHow many hospitals would you like to compare?\n"))

if numOfComparison > 1:
    print("Use the list from above to make a list of hospitals you would like to compare.\nPlease use the number associated with the hospital")
    for i in range(numOfComparison):
     user_input = int(input(f"{i+1}. ")) - 1
     chosenHospitals.append(findHospital(user_input))
else:
   user_input = int(input('Which hospital would you like to get an estimate for?'))
   chosenHospitals.append(findHospital(user_input))

print("Selected Hospitals:")
print('************************************************************************************')
for i, name in enumerate(chosenHospitals, 1):  # Start numbering from 1
    print(f"{i}.) {name}")
print('************************************************************************************')

## MAKE A DATA FRAME WITH ALL OF THE POSSIBLE PROCEDURE QUERIES

## Show most common billing codes for the hospitals selected
## Show all billing codes available based on type (joint, cardiology, GI, etc....)
print('\n')
print('Generally, what do you need to seek care for?\n')

for i, key in enumerate(availableSections):
    print(f"{i + 1}: {key}")

selectedCare = int(input('Please enter a number from the list above:'))- 1
# Get the corresponding key
selectedKey = list(availableSections.keys())[selectedCare]

print(f"\nAvailable procedures for '{selectedKey}' at '{chosenHospitals}:")
avalServices = []
min_value = min(availableSections[selectedKey])
max_value = max(availableSections[selectedKey])
print(min_value)
print(max_value)

#FIXME
result = cursor.execute('SELECT * FROM Anmed_Cannon WHERE CPT IS NOT NULL AND CPT BETWEEN ? AND ?;', {min_value}, {max_value})
rows = result.fetchall()
for row in rows:
   avalServices.append(row[1])

for i, name in enumerate(avalServices, 1):  # Start numbering from 1
    print(f"{i}.) {name}")



cursor.close()
connection.close()


