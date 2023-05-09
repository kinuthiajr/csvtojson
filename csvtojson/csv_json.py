import csv, json

csvfilepath = 'mallcustomer.csv'
jsonfilepath = 'mall_cus.json'

#Read csv the csv then add the data to a dict
data = {}
with open(csvfilepath) as csvfile:
     csvreader = csv.DictReader(csvfile)
     for csvrow in csvreader:
        invoice_no = csvrow['invoice_no']
        data[invoice_no] = csvrow

#write data to a JSON file
with open(jsonfilepath, 'w') as jsonfile:
    jsonfile.write(json.dumps(data,indent=4))



# Putting all of this in a function
def csvConvert(csvfilepath,jsonfilepath):
    data = {}
    with open(csvfilepath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for csvrow in csvreader:
            invoice_no = csvrow['invoice_no']
            data[invoice_no] = csvrow

    #write data to a JSON file
    with open(jsonfilepath, 'w') as jsonfile:
        jsonfile.write(json.dumps(data,indent=4))

csvfilepath = r'mallcustomer.csv'
jsonfilepath = r'mall_cus.json'

# Call the function 
csvConvert(csvfilepath,jsonfilepath)