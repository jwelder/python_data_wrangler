import csv

csvfile = open('code/data-wrangling/data/chp3/data-text.csv', 'rb')
reader = csv.reader(csvfile)
for row in reader:
	print row
