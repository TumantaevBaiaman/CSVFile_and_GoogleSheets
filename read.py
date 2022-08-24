import csv

list_f = []
with open('test_data.csv', 'r', encoding='UTF8') as file:
   reader = csv.DictReader(file, skipinitialspace=True)
   
   for l in reader:
       list_f.append(l)

def test():
    table = list_f
    list = {}
    for i in table:
        list[i['dlg_id']] = []
    for i in table:
        list[i['dlg_id']].append({'line_n': i['line_n'], 'role': i['role'], 'text': i['text']})
    return list

print(test())