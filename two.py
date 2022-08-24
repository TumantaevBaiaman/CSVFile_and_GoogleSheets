import spacy
from spacy.lang.ru.examples import sentences
import ru_core_news_lg
import csv

from google_sheets import text
from read import test

# read google sheets
# data = text()

# read csv file
data = test()

nlp = ru_core_news_lg.load()

list_h = ['здравствуйте', 'меня зовут', 'до свидания', 'добрый день']

file_csv = ['dlg_id', 'line_n', 'role', 'text', 'insight']

t = []

for i in range(len(data)):
    for n in data[str(i)]:
        list = []
        list.append(i)
        list.append(n['line_n'])
        list.append(n['role'])
        list.append(n['text'])

        text_data = n['text'].lower()
        doc = nlp(text_data)
        
        if (text_data.find(list_h[0])!=-1 and n['role'] == "manager") or text_data.find(list_h[2])!=-1 or (n['role'] == "client" and text_data.find(list_h[1])!=-1) or (text_data.find(list_h[3])!=-1 and n['role'] == "manager"):
            list.append('True')
        else:
            list.append('False')

        t.append(list)
        
        text_data = n['text'].lower()
        doc = nlp(text_data)
        
        if (text_data.find(list_h[0])!=-1 and n['role'] == "manager") or (text_data.find(list_h[3])!=-1 and n['role'] == "manager"):
            hello = text_data
        
        if text_data.find(list_h[2])!=-1:
            b = text_data

        if n['role'] == "client" and text_data.find(list_h[1])!=-1:

            for p in doc.ents:
                if p.label_ == "PER":
                    client = p.text
            
            cl = text_data
            f = text_data.split(' ')
            index = f.index('компания')
            company = f[index+1]

        if n['role'] == "manager":
            for l in doc.ents:
                
                if l.label_ == "PER":
                    name = l.text
            

    print("Менеджер №:", i+1)
    print("Имя: ", name.title())
    if hello:
        print(hello)
    print("Клиент №:", i+1)
    print("Имя: ", client.title())
    if cl:
        print(cl)
    if company:
        print("Компания: ", company.title())
    if b:
        print(b)
    print("-------------------------")
        



with open('test_data.csv', 'w', encoding='UTF8') as file:

   writer = csv.writer(file)
   writer.writerow(file_csv)

   for i in t:
      writer.writerow(i)