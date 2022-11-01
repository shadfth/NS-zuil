from datetime import datetime
import random
import json
import psycopg2
import PySimpleGUI as sg
import os.path




conn = psycopg2.connect(
    host="localhost",
    database="ns_zuil",
    user="postgres",
    password="Babyborn123")

def bericht():
   bericht = str(input('wat wilt u kwijt?: '))
   lengte_bericht = len(bericht)
   if lengte_bericht >= 140:
      print('u mag niet meer dan 140 characters gebruiken (inlusief spaties)!')
   else:
      return bericht



def vraagnaam():
   naam = str(input('wat is uw naam?: '))
   if naam == '':
      return 'annoniem'
   return naam
def tijd():

   # datetime object containing current date and time
   now = datetime.now()

   # dd/mm/YY H:M:S
   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   return dt_string


def random_station():
   random_getal = random.randrange(1,4)
   if random_getal == 1:
      return "Station Zaandam"
   if random_getal == 2:
      return 'Station Amsterdam'
   return 'Station Utrecht'
message = f'{vraagnaam()} zegt {bericht()} op {tijd()}'

with open('bericht.json','r') as file:
   data = json.load(file)
   print(type(data))
   data.append(message)

#print het meest recente bericht
print(message)

with open('bericht.json', 'w') as file:
   json.dump(data,file, indent=True)
def check_bericht():
   goedkeuring = input('type ja of nee: ')
   if goedkeuring == 'ja':
      return 'bericht goedgekeurd'
   if goedkeuring == 'nee':
      return 'bericht afgekeurd'
   else: print('verkeerde input') and check_bericht()
def vraagmail():
  email = str(input('wat is uw email?: '))
  return email


beoordeeld = (f'{check_bericht()} door {vraagnaam()} met email: {vraagmail()} op de dag en tijd {tijd()} het bericht:{message}')

with open('moderator.json','r') as file:
   data = json.load(file)
   print(type(data))
   data.append(beoordeeld)

with open('moderator.json', 'w') as file:
   json.dump(data,file, indent=True)



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    window.close()