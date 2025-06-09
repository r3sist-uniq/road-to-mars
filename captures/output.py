import json
from html import escape

# Load JSON file
with open("results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Print only the list item lines
for page in data:
    for item in page.get("feed", []):
        name = item.get("name")
        url = item.get("link", {}).get("url")
        if name and url:
            print(f'        <li><a href="{escape(url)}" target="_blank">{escape(name)}</a></li>')

