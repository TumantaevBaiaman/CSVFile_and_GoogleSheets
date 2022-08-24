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

list_h = ['здравствуйте', 'меня зовут', 'до свидания']

file_csv = ['name_manager', 'name_client', 'company', 'hello', 'bye']

t = []

for i in range(len(data)):
   name = ''
   hello = ''
   cl = ''
   company = ''
   client = ''
   b = ''

   for n in data[str(i)]:
      text_data = n['text'].lower()
      doc = nlp(text_data)
      
      if text_data.find(list_h[0])!=-1 and n['role'] == "manager":
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
            

   in_file = []
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


   if name:
      in_file.append(str(name.title()))
   else:
      in_file.append('None')
   
   if client:
      in_file.append(str(client.title()))
   else:
      in_file.append('None')
   
   if company:
      in_file.append(str(company.title()))
   else:
      in_file.append('None')

   if hello:
      in_file.append(str(hello))
   else:
      in_file.append('None')
   
   if b:
      in_file.append(str(b))
   else:
      in_file.append('None')
   
   t.append(in_file)

with open('data.csv', 'w', encoding='UTF8') as file:

   writer = csv.writer(file)
   writer.writerow(file_csv)

   for i in t:
      writer.writerow(i)