### Software Requirements: Translate the Business Requirements into Code ###
import csv

def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data, header=None):
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter= csv.writer(csvfile, delimiter=",")
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)