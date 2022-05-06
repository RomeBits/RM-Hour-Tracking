# Written by Benjamin Rome 6-6-22
# See README for more info on how to use
import sys
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Need to give us a CSV as input
    if len(sys.argv) != 2:  
        print("ERROR: Usage: python -3 main.py < my_csv.csv >")
        sys.exit(1)

    # Collect CSV name and read it in as pandas datafram
    CSV  = sys.argv[1]
    data = pd.read_csv(CSV, names=['Timestamp', 'RCSID','Subsystem', 'In_Out'])

    # Main loop
    #   Loop through the data find matching ins and outs for specific RCSID
    for i in range(len(data['Timestamp'])):
        if i == 0: continue
        print(data['Timestamp'][i])
        print(data['RCSID'][i])
        print(data['Subsystem'][i])
        print(data['In_Out'][i])








