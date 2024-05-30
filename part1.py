import requests

url = "https://gamora.asgard.pp.ua/data/1"

token = "we87fwR4Tf3287w67"

params = {'token': token}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
  
    january_2024_data = [entry for entry in data if entry['station'] == 'London King Cross' and entry['date'].startswith('2024-01')]
    total_arrivals_january_2024 = sum(entry['arrivals'] for entry in january_2024_data)
    
    print("Кількість людей, які прибули на станцію 'London King Cross' у січні 2024 року:", total_arrivals_january_2024)
else:
    print("Помилка при виконанні запиту.")
