# Liz Chandler
# 2/20/24

# Purpose: take in csv files from hospitals and get rid of all the columns except for 
# Charge Code, Charge Description, Patient Type, Rev Code, Gross Charges, 
# Discounted Cash Price, De-Identified Minimum, and De-Identified Maximum.
import pandas as pd
import os

# Shoutout to Bhavya Gupta on youtube for making a great video.
# The following code is derived from his video
#directory = '/home/ebethc31/personalProjects/PrismaHealthCSVs'
#ext = ('.csv')

import os
from openpyxl import load_workbook

# Directory containing Excel files
directory = '/home/ebethc31/personalProjects/PrismaHealthCSVs'

# Number of rows to delete
rows_to_delete = 4

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        # Load the Excel file
        excel_file = os.path.join(directory, filename)
        wb = load_workbook(excel_file)

        # Select the active worksheet (you can also specify a specific sheet by name)
        ws = wb.active

        # Delete the first couple of rows
        ws.delete_rows(1, rows_to_delete)

        # Save the modified Excel file
        output_excel_file = os.path.join(directory, f'modified_{filename}')
        wb.save(output_excel_file)

#for filename in os.listdir(directory):
 #   f = os.path.join(directory, filename)

    #if f.endswith(ext):
     #   head_tail = os.path.split(f)
      #  head_tail1 = '/home/ebethc31/personalProjects/PrismaHealthCSVs'
       # k = head_tail[1]
        #r = k.split(".")[0]

        #p = head_tail1 + "/" + r + " - Cleaned.csv"

        #myData = pd.read_csv(f)

        #new = myData[["Charge Code/Package"]] #, "Charge Description", "Patient Type", "Rev Code", "Gross Charges", "Discounted Cash Price", "De-Identified Minimum", "De-Identified Maximum"]]
        #new.to_csv(p, index = False)

