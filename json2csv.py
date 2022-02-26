import json 
import csv
import argparse

parser = argparse.ArgumentParser(description='Convert JSON to CSV')

parser.add_argument('-i', '--input', help='Input JSON file', type=str, required=True)
parser.add_argument('-o', '--output', help='Output CSV file', type=str, required=True)

args = parser.parse_args()


with open(args.input) as json_file:
    jsondata = json.load(json_file)

csv_file = open(args.output, 'w', newline='')
csv_writer = csv.writer(csv_file)

for index, data in enumerate(jsondata):
    if not index:
        header = data.keys()
        csv_writer.writerow(header)
    else:
        csv_writer.writerow(data.values())

csv_file.close()
