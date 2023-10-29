import random
from datetime import datetime
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt
import csv
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs

word_name_list = []
word_translation_name_list = []
word_type_list = []
result_list = []

class Word():
    def __init__(self,number_of_words):
        self.word_name = [0 for i in range(number_of_words)]
        self.word_translation_name = [0 for i in range(number_of_words)]
        self.word_type = [0 for i in range(number_of_words)]
        self.n = number_of_words

    def Input(self):
        self.word_name = [input("Enter a word"+str(i+1)+" : ") for i in range(self.n)]
        self.word_translation_name = [input("Enter the translation of the word"+str(i+1)+" : ") for i in range(self.n)]
        self.word_type = [input("Enter the type of the word"+str(i+1)+" : ") for i in range(self.n)]

    def Print(self):
        for i in range(self.n):
            print("Word name",i+1,"is",self.word_name[i])
            print("Translation of the word", i + 1, "is", self.word_translation_name[i])
            print("Type of the word", i + 1, "is", self.word_type[i])

class Build(Word):
    def __init__(self):
        Word.__init__(self, 3)

    def Result(self):
        for i in range(1):
            word_name_list.append(self.word_name)
            word_translation_name_list.append(self.word_translation_name)
            word_type_list.append((self.word_type))

deneme = Build()
deneme.Input()
deneme.Print()
deneme.Result()

df = pd.concat([df_new1,df_new2,df_new3],axis=1)
print("Result list:",result_list)
df = df.rename({0: '#0', 1: '#1', 2: '#2'}, axis=0)
print(df.index)
#df = df.T
#print(df.head())
df.to_excel("Last.xlsx",index=True,header=False)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
with open('result.csv', 'a') as f:
    f.write(dt_string + "Result Log Sheet" + '\n')
    success = result_list.count("True")/len(result_list)
    f.write(str(success))
    writer = csv.writer(f)
    writer.writerow(result_list)

