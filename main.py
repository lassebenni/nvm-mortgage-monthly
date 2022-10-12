import requests
import json

url = "https://mijn.makelaarsland.nl/NvmSearch/GetMortgagePayment"

payload = json.dumps({
    "purchasePrice": "500000",
    "yourOwnMoney": 12500,
    "interestDuration": 20,
    "nhg": False,
    "nhgBoundary": "355000"
})
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://mijn.makelaarsland.nl',
    'Connection': 'keep-alive',
    'Cookie': '__RequestVerificationToken=z9VwZWLjyU1Nrsqbqr7s36IGZde9fit0FJj4HuXiNP0-Lmc0C-7L8KRrOXZIIC6sqgiTMyHSbTvuGTfsDi5EFtdwews1; ASP.NET_SessionId=x03ylpqqlz5vdqgy21jb5iub; .MLLOGIN=58539DCB2A3ED19BB6DAA6B93C5419787A98CB17A825C19DF049D6E392040FB28345411E84A5D7044D3F76AA561D30F691B59984AE25F054DD2EA547A43217F3CEC3FD30E2606AA5C34472F6634C25FFA6B241473BA794916D890EB5E98BBA613C5A0534; .MLLOGIN=46D420AF9000124EAFD8A5851299C5013C2318E0B5A1E5E5252407BF3655E24958EEF6548F0548C9E60C7290E46AAC5B113BB7FA3EB244AA494F96908C9BCC645A4DD627764E21C970103536459E02D9B1256D148FE224EF19FC2D76BEEC1CE612940FD0; ASP.NET_SessionId=cbircdx5kkoshcdp42ovz4i0; __RequestVerificationToken=faxVGRGd3bOOXw-0vBNdMf8Wzs2sJl-NGiPyQNO6sp_Re_nPVSrS2_NHjSN92EfPVBNt2O3IOk4OHoOVjZj_ClisO3M1',
    'Sec-Fetch-Site': 'same-origin'
}

response = requests.request("POST", url, headers=headers, data=payload)

res = json.loads(response.text)
with open('mortgage.json', 'w') as f:
    json.dump([res], f, indent=4)
