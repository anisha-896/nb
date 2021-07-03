import csv 
import numpy as np


def getDataSource(data_path):
    Ice-cream Sales( ₹ ) = []
    Cold drink sales( ₹ ) = []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Ice-cream Sales( ₹ ).append(float(row["Ice-creams Sales( ₹ )"]))
            #float means pointing values.
            #append means adding at the last
            Cold drink sales( ₹ ).append(float(row["Cold drink sales( ₹ )"]))

    return{"x" :  Ice-cream Sales( ₹ ), "y" : Cold drink sales( ₹ )}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Ice-cream sale and cold drink sale :- \n--->", correlation[0,1])

def setup():
    data_path = "Temperature.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()