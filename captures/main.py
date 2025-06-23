import requests
import json, time

url = "https://sublime.app/collection/later-dump?index&sortBy=-first_connection_at&type=all&page=2&_data=routes%2F_app.collection.%24collectionSlug._index"


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cookie": "_user_uuid_=eyJ1c2VyVXVpZCI6IjNiOWU4MGM1LWJlOWMtNGUzMi04N2I0LTVmYzMxNWUzMjZlMSJ9.HRH9GA7xVtgoWIdgWIu8TSDxJu9cavmOHle5lDmoTek; _notification_=e30%3D.QKUqdAtlR0l7jySQ7n3s5S7MMuQMYzSpUZlZeR36XZI; _refresh_token_=eyJyZWZyZXNoVG9rZW4iOiJBTWYtdkJ5c0pNaVRnUHRhTmZkZ1V5R0doT09jMjlRVnk0bDR6cjQxNE5jcHNQLXdlMkNEYm1JdjB1dEJLTExNcU8zZG9zb2lZblFhRVhpRE9sM1dVcktVbmVBQ293ZHl3N2FuTUMzWHM4VHBWdVIyWXNEZm8yWWUxS0hTMWF3OWZMTFp6X1ByaGNpdjBhSnJhbXRQelY1NmlQQVJMeWw3b19TaFJ2V3QyVkdNb1ZlcGljSUxIQUJoMngzUHEzclhBWHdGa3FMY3RjSEZWZ3hNU1Z5VUhvOUpIRGUtVVlyWE5MaU0tNlBOZUNUZlVHV3RQMXRlUXI4WkljVTRxUVUwR25UcGNmd2FsU0hObjJfRWRNeVhhcmEyY3ZZTkRXTHdkYXlSRExiNGdvQ3U3Q3ZCLWgyUG5HaWNLaXZPd2dfazllbjJkS1NtWDlfMTkxbDZiSElTa3F6dHJ0TXB4TzRrNWRwb1JBdXA2NUZ5c3FPNktab2VqSXZ3MWpHRWZ3alhmTUpMV2ZPM0hQTkxnRjgyYU8xU2VDQ3BEVzdmR2tKa0RpU21jd2pxTVhwc2V1ckRJc09fVFFsR3pTLUdfSXIwWkNXVnBuaHRKUkNwIn0%3D.g4oSAVfJdv9KzkoiIptouk%2FW%2BYKy79jJuki3wkkHYk8; _access_token_=eyJhY2Nlc3NUb2tlbiI6ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJak5pWmpBMU16a3hNemsyT1RFellUYzRaV000TUdZME1qY3dNek00TmpNMk5EQTJNVEJoWkdNaUxDSjBlWEFpT2lKS1YxUWlmUS5leUp1WVcxbElqb2lRVzFoYmlJc0luQnBZM1IxY21VaU9pSm9kSFJ3Y3pvdkwyeG9NeTVuYjI5bmJHVjFjMlZ5WTI5dWRHVnVkQzVqYjIwdllTOUJRMmM0YjJOTFpXMW5OV3RvWTBGcGEzSlJXa3BZVjJKRlgyaHdZMjl1VkZjdFRUUmZNWFpUVlVGNVMwWnRjbEYyV21kWGFFSm9MVDF6T1RZdFl5SXNJbWx6Y3lJNkltaDBkSEJ6T2k4dmMyVmpkWEpsZEc5clpXNHVaMjl2WjJ4bExtTnZiUzl6ZFdKc2FXMWxMWEJ5YjJSMVkzUnBiMjRpTENKaGRXUWlPaUp6ZFdKc2FXMWxMWEJ5YjJSMVkzUnBiMjRpTENKaGRYUm9YM1JwYldVaU9qRTNNemM1T1RVd056QXNJblZ6WlhKZmFXUWlPaUowVGtwS2QwNHpXazlEWW5Gck5uVldXblJOUjJobU9FWkJhRkV5SWl3aWMzVmlJam9pZEU1S1NuZE9NMXBQUTJKeGF6WjFWbHAwVFVkb1pqaEdRV2hSTWlJc0ltbGhkQ0k2TVRjMU1EWTFNVEUxTVN3aVpYaHdJam94TnpVd05qVTBOelV4TENKbGJXRnBiQ0k2SW1GdFlXNXRZWFJ5WldwaFFHZHRZV2xzTG1OdmJTSXNJbVZ0WVdsc1gzWmxjbWxtYVdWa0lqcDBjblZsTENKbWFYSmxZbUZ6WlNJNmV5SnBaR1Z1ZEdsMGFXVnpJanA3SW1kdmIyZHNaUzVqYjIwaU9sc2lNVEUwTWpjeU56VTFOVFk0TXpFeE16Y3pNams1SWwwc0ltVnRZV2xzSWpwYkltRnRZVzV0WVhSeVpXcGhRR2R0WVdsc0xtTnZiU0pkZlN3aWMybG5ibDlwYmw5d2NtOTJhV1JsY2lJNkltZHZiMmRzWlM1amIyMGlmWDAuUjgtUnhaQm5mY3hFOXNOVGQ3dUE0b2hmd1p3YjVaMFdFNW9zbS0yZHdXOUNHRHVHVndSYjBQRkVHVG1xQzdmVVZIeWpteTl0WVMyZlJZYXNHOFZVeDFMS04wQkRyMlZVQlhRV1lERnZjTG1Md3pLR19xQnRqYTV2MGtYV3RxbGxLR20xTDJTTVNybDJJU1RpQkRLVGlIN0FyTVJfSlZtOXRJSmRJUFlzNFRYam5JSGpiSWdvVzZaYXVYXzdnNjk1bWUyY2x5dHFRUFRRdHJBd3Z1dVhHNjhlczJ6Q2xlRHR0Sjc4QnhZTjRqRkl5TldsMjlsOHpuZFhXQnVOT0l1cXBZbmxOekNJN24xR3N5S1hWYk80a1JTMnJhUUh2X0x1d0lKeElOZEljakJqZDdXamRNSkdad2JaOFgyYkdLUy1jOW1ibDYxaktkWmFKVXJCMXZNVWVnIn0%3D.Hb1BKj0kYchrfE4RcC7qO4YHktvhXHEd28BWXAb9Tio; _expiration_date_=eyJleHBpcmF0aW9uRGF0ZSI6Ik1vbiwgMjMgSnVuIDIwMjUgMDQ6NTk6MTEgR01UIn0%3D.vIy%2FVrapgtRhQxpexMHM3iaBTg%2FFgJmqpOgADzqwHEo",
    "DNT": "1",
    "Priority": "u=1, i",
    "Referer": "https://sublime.app/collection/later-dump",
    "Sec-CH-UA": '"Chromium";v="137", "Not/A)Brand";v="24"',
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
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
    # try:
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

    # except Exception as e:
    #     print(f"Error fetching page {page_num}: {e}")

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




