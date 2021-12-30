import pandas as pd
from Relay import Check

class Statistics:

    def create(self, dates1, dates2, dates3):
        ck = Check.Checks()
        temp, humid = ck.Check_DHT(stat=True)
        dates1["Temperature"] += [temp]
        dates2["Temperature"] += [temp]
        dates3["Temperature"] += [temp]
        dates1["Humidity"] += [humid]
        dates2["Humidity"] += [humid]
        dates3["Humidity"] += [humid]
        df1 = pd.DataFrame(dates1)
        df2 = pd.DataFrame(dates2)
        df3 = pd.DataFrame(dates3)

        sheets = {"Plant 1": df1, "Plant 2": df2, "Plant 3": df3}
        writer = pd.ExcelWriter('/home/pi/Desktop/Hydro/Statistics/Plants.xlsx', engine='xlsxwriter')

        for sheet_name in sheets.keys():
            sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
        
        writer.save()