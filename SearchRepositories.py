import requests
from prettytable import PrettyTable

query = {"q": "language:python stars:>=5000", "sort": "stars", "order": "desc"}
response = requests.get("https://api.github.com/search/repositories", params=query)

data = response.json()

table = PrettyTable()
table.field_names = ["Repository Name", "Created Date","Language", "Stars"]

for repository in data["items"]:
    name = repository["full_name"]
    created_date = repository["created_at"]
    language = repository["language"]
    stars = repository["stargazers_count"]
    table.add_row([name, created_date, language, stars])

print(table)
