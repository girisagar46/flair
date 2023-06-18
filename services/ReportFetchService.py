import requests


def fetch_files(roll):
    r = requests.get("https://api.github.com/repos/CSIT-GUIDE/FYP-2016/contents")
    payload_json = r.json()
    name, html_url, download_url = None, None, None
    for each in payload_json:
        temp_name = each.get("name").split("_")
        if roll[0] in temp_name:
            name = each.get("name")
            html_url = each.get("html_url")
            download_url = each.get("download_url")
        else:
            pass
    return name, html_url, download_url

