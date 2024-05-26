#!/usr/bin/python3
'''
The objective of this exercise is to gain experience in
reading data from one format (CSV) and converting
it into another format (JSON) using serialization techniques.
'''

import csv
import json


def convert_csv_to_json(csvFile):
    '''
    Takes the CSV filename as its parameter
    and writes the JSON data to data.json.

    Returns True if the conversion was successful, False otherwise.
    '''

    try:
        with open(csvFile, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)
            data = [row for row in csvReader]

        with open("data.json", "w", encoding="utf-8") as jsonf:
            json.dump(data, jsonf, indent=None, separators=(',', ':'))

        return True

    except FileNotFoundError as e:
        print(f"{e}")
        return False
    except PermissionError as e:
        print(f"{e}")
        return False
    except Exception as e:
        print(f"{e}")
        return False


csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
