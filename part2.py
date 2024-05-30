import csv
import tarfile
import os

# Розпакувати архів tar
with tarfile.open('data.tar', "r") as tar:
    tar.extractall('data')

# Перевірити, чи файли були успішно розпаковані
data_directory = 'data'
if os.path.exists(data_directory):
    csv_files = [file for file in os.listdir(data_directory) if file.endswith('.csv')]
    if csv_files:
        csv_file_path = os.path.join(data_directory, csv_files[0])
        with open(csv_file_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        january_2024_data = [entry for entry in data if entry['Date of Journey'].startswith('2024-01') and entry['Departure Station'] == 'London King Cross']
        total_arrivals_january_2024 = sum(float(entry['Price']) for entry in january_2024_data)

        print("Кількість людей, які прибули на станцію 'London King Cross' у січні 2024 року:", len(january_2024_data))
    else:
        print("Файл CSV не знайдено в папці 'data'.")
else:
    print("Папка 'data' не знайдена.")
