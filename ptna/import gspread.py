from urllib.request import *
import json

def main():
    recs = fetch_spreadsheet()
    print(recs)

def fetch_spreadsheet():
    apikey = "apikey"
    myrange = "mysheet!a1:h1000"

    url = "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}?key={}"
    url = url.format(sheetid, myrange, apikey)

    req = Request(url, headers={}, method='GET')

    with urlopen(req) as res:
    body = res.read().decode()

    return recs

if __name__ == "__main__":
    main()