import sys
import re
import requests
from requests.structures import CaseInsensitiveDict
import json

# Replace the following value with your valid access token
access_token = "your_access_token_here"

def search_tracks(query, access_token):
    search_url = "https://api.spotify.com/v1/search"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {access_token}"
    
    params = {
        "q": f'{query} prod',
        "type": "track",
        "limit": 50
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Error: Unable to search tracks. Status code: {response.status_code}")

    results = response.json()
    tracks = results["tracks"]["items"]

    for track in tracks:
        title = track["name"]
        lowercase_title = title.lower()
        prod_by = rf"(\bprod\. by {query}\b(?!\w|\s))"
        produced_by = rf"(\bproduced by {query}\b(?!\w|\s))"

        if re.search(prod_by, lowercase_title, re.IGNORECASE) or re.search(produced_by, lowercase_title, re.IGNORECASE):
            isrc = track["external_ids"]["isrc"]
            url = track["external_urls"]["spotify"]
            print(f"ISRC: {isrc}\nTitle: {title}\nURL: {url}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        producer_name = sys.argv[1]
        search_tracks(producer_name, access_token)
    else:
        print("Usage: python script_name.py [producer_name]")
