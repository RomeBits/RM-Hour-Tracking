# Written by Benjamin Rome 5-6-22
# See README for more info on how to use
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


class Person:
    def __init__(self, rcsid):
        self.rcsid = rcsid
        self.total_hours = 0
        self.total_sign_ins = 0
    
    def average_duration(self):
        return self.total_hours / self.total_sign_ins



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
    people_objects  = {}
    people_in_times = {}
    half_found      = set()

    for i in range(len(data['Timestamp'])):
        if i == 0: continue
        # print(data['Timestamp'][i])
        # print(data['RCSID'][i])
        # print(data['Subsystem'][i])
        # print(data['In_Out'][i])

        rcsid = data['RCSID'][i]

        # Case where we have an in time but no out time yet
        if rcsid in half_found:

            if data['In_Out'][i] == "Out":
                # a = int(a.strftime
                final   = int(datetime.strftime(datetime.strptime(data['Timestamp'][i], '%m/%d/%Y %H:%M:%S')))
                init    = datetime.strptime(people_in_times[rcsid], '%m/%d/%Y %H:%M:%S')
                delta   = final - init

                print(delta)
                people_objects[rcsid].total_hours += int(delta)

            else:
                print("{} did not have an \"out\" time marked before signing in again at {}", rcsid, data['Timestamp'][i])


        # Case where this person has not checked in yet
        else:
            # We haven't seen this person yet and we need to create them
            if rcsid not in people_objects:
                person = Person(rcsid)
                people_objects[rcsid]  = person

                
            # Person has not signed in yet and is marked as "in"
            if data['In_Out'][i] == "In":
                half_found.add(rcsid)
                people_in_times[rcsid] = data['Timestamp'][i]


            # Person has not signed in yet and is marked as "out" 
            #  (Missed sign in or marked incorrectly)
            else:
                print("{} did not have an \"in\" time marked before signing out at {}", rcsid, data['Timestamp'][i])


    print(people_objects["romeb"].total_hours)



            









