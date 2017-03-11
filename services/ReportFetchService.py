import requests
import os
def fetch_files(name_arg):
    r = requests.get("https://api.github.com/repos/CSIT-GUIDE/FYP-2016/contents")
    payload_json = r.json()
    name, htmlurl = ("","")
    for each in payload_json:
        temp_name = each.get('name').split('_')
        if name_arg in temp_name:
            name = each.get('name')
            htmlurl = each.get('html_url')
            download_url = each.get('download_url')
        else:
            pass
    return [name, htmlurl, download_url]

if __name__ == "__main__":
    fetch_files()