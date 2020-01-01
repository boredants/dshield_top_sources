import requests
from datetime import datetime

retLimit = input("Enter the number of IP Addresses to retrieve: ")
# Set a default limit
if retLimit == "":
    retLimit = "100"

retDate = input("Enter a date (YYYY-MM-DD): ")
# Set a default date
if retDate == "":
    retDate = datetime.now().strftime('%Y-%m-%d')

url = "https://isc.sans.edu/api/sources/attacks/" + retLimit + "/" + retDate + "?json"


j = requests.get(url).json()

for i in j:
    print('.'.join([str(int(x)) for x in i.get('ip').split('.')]))
