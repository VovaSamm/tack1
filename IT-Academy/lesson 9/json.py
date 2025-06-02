

import json
import csv
from typing import List, Dict, Any


def read_json(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def json_to_csv(json_file: str, csv_file: str):
    data = read_json(json_file)
    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def add_employee_to_json(file_path: str):
    new_employee = {}
    new_employee['name'] = input("Введите имя сотрудника: ")
    new_employee['age'] = int(input("Введите возраст: "))
    new_employee['height'] = int(input("Введите рост: "))
    new_employee['languages'] = input("Введите языки программирования через запятую: ").split(',')
    new_employee['birth\_year'] = int(input("Введите год рождения: "))

    data = read_json(file_path)
    data.append(new_employee)

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def add_employee_to_csv(csv_file: str):
    new_employee = {}
    new_employee['name'] = input("Введите имя сотрудника: ")
    new_employee['age'] = int(input("Введите возраст: "))
    new_employee['height'] = int(input("Введите рост: "))
    new_employee['languages'] = input("Введите языки программирования через запятую: ").split(',')
    new_employee['birth\_year'] = int(input("Введите год рождения: "))

    with open(csv_file, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=new_employee.keys())
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(new_employee)


def find_employee_by_name(file_path: str):
    name = input("Введите имя сотрудника для поиска: ")
    data = read_json(file_path)
    for employee in data:
        if employee['name'].lower() == name.lower():
            print(employee)
            return
    print("Сотрудник не найден\.")


def filter_by_language(file_path: str):
    language = input("Введите язык программирования для фильтрации: ")
    data = read_json(file_path)
    filtered_employees = [emp for emp in data if language in emp['languages']]
    print("Сотрудники, владеющие языком", language)
    for emp in filtered_employees:
        print(emp)


def average_height_by_birth_year(file_path: str):
    year = int(input("Введите год рождения: "))
    data = read_json(file_path)
    heights = [emp['height'] for emp in data if emp['birth\_year'] < year]
    if heights:
        average_height = sum(heights) / len(heights)
        print(f"Средний рост сотрудников, родившихся до {year}: {average_height:.2f}")
    else:
        print("Нет сотрудников, родившихся до указанного года\.")

json_file_path = 'employees\.json'
csv_file_path = 'employees\.csv'


json_to_csv(json_file_path, csv_file_path)


add_employee_to_json(json_file_path)
add_employee_to_csv(csv_file_path)


find_employee_by_name(json_file_path)


filter_by_language(json_file_path)


average_height_by_birth_year(json_file_path)

