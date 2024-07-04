import pyodbc
from credentials import user, password

## CONNECTION TO THE SERVER AND DATABASE ##
connection = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};SERVER=hospitalpriceapp.database.windows.net;DATABASE=hospitalPriceApp;UID='+user+';PWD='+password+';Encrypt=No')
cursor = connection.cursor()

## EXAMPLE OF HOW TO QUERY SOMETHING
""" 
query = 'SELECT * FROM Anmedcannonstandardcharges WHERE CPT IS NOT NULL'

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

"""

cursor.close()
connection.close()


