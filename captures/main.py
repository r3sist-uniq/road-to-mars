import requests
import json, time

url = "https://sublime.app/collection/later-dump?index&sortBy=-first_connection_at&type=all&page=3&_data=routes%2F_app.collection.%24collectionSlug._index"


headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",

    "cookie": "_user_uuid_=eyJ1c2VyVXVpZCI6IjNiOWU4MGM1LWJlOWMtNGUzMi04N2I0LTVmYzMxNWUzMjZlMSJ9.HRH9GA7xVtgoWIdgWIu8TSDxJu9cavmOHle5lDmoTek; _notification_=e30%3D.QKUqdAtlR0l7jySQ7n3s5S7MMuQMYzSpUZlZeR36XZI; _access_token_=eyJhY2Nlc3NUb2tlbiI6ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJbUUwWVRFd1pHVmpaVGs0TXpZMlpEWm1Oak5sTVRZM01qZzJZV1U1WWpZeE1XUXlZbUZoTWpjaUxDSjBlWEFpT2lKS1YxUWlmUS5leUp1WVcxbElqb2lRVzFoYmlJc0luQnBZM1IxY21VaU9pSm9kSFJ3Y3pvdkwyeG9NeTVuYjI5bmJHVjFjMlZ5WTI5dWRHVnVkQzVqYjIwdllTOUJRMmM0YjJOTFpXMW5OV3RvWTBGcGEzSlJXa3BZVjJKRlgyaHdZMjl1VkZjdFRUUmZNWFpUVlVGNVMwWnRjbEYyV21kWGFFSm9MVDF6T1RZdFl5SXNJbWx6Y3lJNkltaDBkSEJ6T2k4dmMyVmpkWEpsZEc5clpXNHVaMjl2WjJ4bExtTnZiUzl6ZFdKc2FXMWxMWEJ5YjJSMVkzUnBiMjRpTENKaGRXUWlPaUp6ZFdKc2FXMWxMWEJ5YjJSMVkzUnBiMjRpTENKaGRYUm9YM1JwYldVaU9qRTNNemM1T1RVd056QXNJblZ6WlhKZmFXUWlPaUowVGtwS2QwNHpXazlEWW5Gck5uVldXblJOUjJobU9FWkJhRkV5SWl3aWMzVmlJam9pZEU1S1NuZE9NMXBQUTJKeGF6WjFWbHAwVFVkb1pqaEdRV2hSTWlJc0ltbGhkQ0k2TVRjME9UUTNNVGMzTlN3aVpYaHdJam94TnpRNU5EYzFNemMxTENKbGJXRnBiQ0k2SW1GdFlXNXRZWFJ5WldwaFFHZHRZV2xzTG1OdmJTSXNJbVZ0WVdsc1gzWmxjbWxtYVdWa0lqcDBjblZsTENKbWFYSmxZbUZ6WlNJNmV5SnBaR1Z1ZEdsMGFXVnpJanA3SW1kdmIyZHNaUzVqYjIwaU9sc2lNVEUwTWpjeU56VTFOVFk0TXpFeE16Y3pNams1SWwwc0ltVnRZV2xzSWpwYkltRnRZVzV0WVhSeVpXcGhRR2R0WVdsc0xtTnZiU0pkZlN3aWMybG5ibDlwYmw5d2NtOTJhV1JsY2lJNkltZHZiMmRzWlM1amIyMGlmWDAuRjNGTXZCck1kUlZneXl3ajh0V09TS05ySV9PcERoVnVySkJwSGI4ZGJvcS10ZTN5U2N1UTJBVE9rU3J1VHpwamdvZHl2a3RWSFpJM1l1LUVOQkFZbHRZanMzZFkxUnNIMHE3WE5IQk1oc3lrSFJ5TG9zdzdCNExSNFNTOHV0aWtzVlhnUGg1QklHRThNaXlhYzhjUnVIRVV2ZlZ1R3ByTWIwRmlnelBNSUMtd25OMkhCZ3JHVmdGLWgwaGJFcXN0MGRxZ2Q3bDZCbnF3emRMR09FVXg0TTlvSEl6bHRiWTUwVnJOcGdadkF4SnVNMVQxUzJFcTN0bHlwWGNtUlNHNGpaOF83V1dQNmVRaENVRDZkbmM2XzVTQVNJQVRoME11ZkNCR1FKN1kydzlmdG1YYnA2SldTeEt0aWswNDJWX3psVFlLYXNyVkZnQ3BTRVdIbUR6T0JnIn0%3D.hutQ1LXXZNHdOr9DIP62DRn4e50ki3jlfAY0Se1MZrE; _expiration_date_=eyJleHBpcmF0aW9uRGF0ZSI6Ik1vbiwgMDkgSnVuIDIwMjUgMTM6MjI6NTUgR01UIn0%3D.nT0gEWad36EBgrstQgVGyp86KtfJ%2B%2B3OlQC3Og6GeLE; _refresh_token_=eyJyZWZyZXNoVG9rZW4iOiJBTWYtdkJ5VXZMdVNwaURyVXd3OUZWUElQdkR5RDRVX0xFRWhudW1tMjZsYXkzUjgzS2c5bjNmeWo1clY2d1BYem5NcFVYTmRYdXFmZG1jUE9LeUxCQmwxeUZUbVFCMTVHVDhXTXVtWHZ6b09ybmdTTGo3VHExcjJtMGJPNFh3WEVPM3NURU0wTmQ5Xy1hd1EzcFY2MU1DX1ZCUUNDcFZRRzVLV0g5R3h4bklqRl8xdUZBcDZ0dzRQUUw4WWVlUmVucnFkdzRsU3JtTFBxaGhzOU5nSFVBLXJxT2M2YUlzeklVLXpBTXdFZXFOSmpNeXg0bGdnWU43QVhfRmU2SmxvVlowWkJsZ0ttSC1aNWQ0LTJmTVZxN0xjU3kxMGJjdThlOUZWNGVnS044bmdNczlyaVVaMF9MRmZyNUJmV2t5X2hmV0R3RERkdTRydHhzdUtpbzBleVIzYVJDQnBmZjFUTFJKWVhkd0UtbXFnM0VvTEN1RTcyMUZ4SmVMS25DaEtGYllFZ0JtTnR1bG5VRmdLX0pjaGF5UkdaWG15ZjJzN2puOW9yd3pfZTJvdVlnUUhwRDRPNE9DWUxDdXJoWlMzaDNRbkFEZU9zdEpaIn0%3D.F7ECfaLInsZ35StP4Ryd2tuckiR9EV3JPz%2FHieiArK0",

    "dnt": "1",
    "priority": "u=1, i",
    "referer": "https://sublime.app/collection/later-dump",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"99\", \"Chromium\";v=\"136\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36"
}

# Load existing data
try:
    with open("results.json", "r", encoding="utf-8") as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = []

# Collect all existing UUIDs from all feeds
existing_uuids = set()
for page in existing_data:
    for item in page.get("feed", []):
        existing_uuids.add(item.get("uuid"))

print(f"Loaded {len(existing_uuids)} existing UUIDs.")

new_pages = []
total_new_items = 0  # <-- Counter for all new items

for page_num in range(1, 17):
    url = f"https://sublime.app/collection/later-dump?index&sortBy=-first_connection_at&type=all&page={page_num}&_data=routes%2F_app.collection.%24collectionSlug._index"
    print(f"Fetching page {page_num}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        new_page = response.json()

        new_feed = [item for item in new_page.get("feed", []) if item.get("uuid") not in existing_uuids]

        if new_feed:
            print(f"Found {len(new_feed)} new items on page {page_num}.")
            total_new_items += len(new_feed)

            new_page["feed"] = new_feed
            new_pages.append(new_page)

            for item in new_feed:
                existing_uuids.add(item.get("uuid"))
        else:
            print(f"No new items on page {page_num}.")
            break

    except Exception as e:
        print(f"Error fetching page {page_num}: {e}")

    time.sleep(4)

combined_data = existing_data + new_pages


#use timestamp in the filename
import datetime
from html import escape


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

with open(f"specific_results_{timestamp}.json", "w", encoding="utf-8") as f:
  json.dump(new_pages, f, ensure_ascii=False, indent=2)

with open("results.json", "w", encoding="utf-8") as f:
  json.dump(combined_data, f, ensure_ascii=False, indent=2)


print(f"✅ Done! Added a total of {total_new_items} new items. Data saved to results.json")

for page in new_pages:
  for item in page.get("feed", []):
    name = item.get("name")
    url = item.get("link", {}).get("url")
    if name and url:
      print(f'<li><a href="{escape(url)}" target="_blank">{escape(name)}</a></li>')




