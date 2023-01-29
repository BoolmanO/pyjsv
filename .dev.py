import requests
from pyjsv import SimpleJson, SimpleXml

url = "https://iss.moex.com/iss/history/engines/stock/markets/index/securities.xml?date=2022.12.12"
my_data = SimpleXml.upload_from_str(requests.get(url).text)
print(my_data.get_dict())