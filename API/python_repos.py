import requests

# Wykonanie żądania API i zapisania odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

# Umieszczenie odpowiedzi w zmiennej
response_dict = r.json()
print(f"Liczba repozytoriów: {response_dict['total_count']}")

# Przetwarzanie informacji o repozytoriach
repo_dicts = response_dict['items']
print(f"Licza zwróconych repozytoriów: {len(repo_dicts)}")

# Pierwsze respozytorium
repo_dict = repo_dicts[0]
print(f"\nKlucze: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

for repo_dict in repo_dicts:
    print(f"\nNazwa: {repo_dict['name']}")
    print(f"Właściciel: {repo_dict['owner']['login']}")
    print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    print(f"Respozytorium: {repo_dict['html_url']}")
    print(f"Utworzone : {repo_dict['created_at']}")
    print(f"Opis: {repo_dict['description']}")

print(response_dict.keys())
