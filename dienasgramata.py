import csv
from datetime import datetime
import pandas as pd

def display_menu():
    print("1.Pievieno uzdevumu")
    print("2. Atzīmē uzdevumu kā pabeigtu")
    print("3. Iziet")
    

task_list = []

def pievieno_uzd():
    subject = input("Kāds ir mācību priekšmeta nosaukums?")
    description = input("Kādi ir uzdevuma nosacījumi?")
    due_date = input("Kāds ir uzdevuma nodošanas laiks?")

    task = {
        'Mācību priekšmets': subject,
        'Apraksts': description,
        'Nodošanas termins': due_date,
        'Status': 'Incomplete'
    }

    task_list.append(task)
    print("Uzdevums ir pievienots sarakstam")


def pabeigts_uzd():
    uzd_nr=int(input("Norādiet uzdevuma kārtas numuru, ko vēlaties atzīmēt kā pabeigtu"))
    if 1 <= uzd_nr <= len(task_list):
        task = task_list[uzd_nr - 1]
        task['Status']= 'Complete'
        print("Uzdevums ir atzīmēts kā pabeigts")
    else:
        print("Nepareizi norādīts kārtas numurs")

def read_csv_file():
    with open("data.csv", "r") as f:
        if  f.readline():
            f.seek(0)
            next(f)
            for line in f:
                row = line.rstrip().split(",")
                subject = row[0]
                description = row[1]
                due_date = row[2]
                task = {
                    'Mācību priekšmets':subject,
                    'Apraksts':description,
                    'Nodošanas termins':due_date,
                    'Status':'Incomplete'
}

                task_list.append(task)

def write_csv_file():
    with open("data.csv", "w") as f:
        
        virsraksti = ['Mācību priekšmets', 'Apraksts', 'Nodošanas termins', 'Status']
        writer = csv.DictWriter(f, fieldnames=virsraksti)

        writer.writeheader()
        sorted_tasks = sorted(task_list, key = lambda x:datetime.strptime(x['Nodošanas termins'], "%d.%m.%y"))
        for task in sorted_tasks:
            writer.writerow(task)

def write_sorted_csv_file():
    incomplete_tasks = [task for task in task_list if task['Status']== 'Incomplete']
    sorted_tasks = sorted(incomplete_tasks, key = lambda x:datetime.strptime(x['Nodošanas termins'], "%d.%m.%y"))

    with open("dienasgramata.csv", "w") as f:
        virsraksti = ['Mācību priekšmets', 'Apraksts', 'Nodošanas termins', 'Status']
        writer = csv.DictWriter(f, fieldnames=virsraksti)

        writer.writeheader()
        for task in sorted_tasks:
            writer.writerow(task)


     



read_csv_file()

while True: 
    display_menu()
    izvēle= input("Izvēlies (1-3)")

    if izvēle == "1":
        pievieno_uzd()
        write_csv_file()
    elif izvēle == "2":
        pabeigts_uzd()
        write_csv_file()
    elif izvēle == "3":
        write_sorted_csv_file()
        print("Paldies, ka izmantojāt šo programmu. Uz redzēšanos!")
        break
    else:
        print("Nepareiza ievade. Lūdzu izvēlaties ciparu 1-3") 



