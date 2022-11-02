from datetime import datetime
import random
import json
import psycopg2
import PySimpleGUI as sg
import os.path
from database import insert_to_database





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
   tijd_string = now.strftime("%H:%M:%S")
   return tijd_string



def datum():

   # datetime object containing current date and time
   now = datetime.now()

   datum_string = now.strftime("%Y/%m/%d")
   return datum_string


def random_station():
   random_getal = random.randrange(1,4)
   if random_getal == 1:
      return "Station Zaandam"
   if random_getal == 2:
      return 'Station Amsterdam'
   return 'Station Utrecht'


message = {
    'naam': vraagnaam(),
    'bericht': bericht(),
    'datum': datum(),
    'tijd': tijd(),
    'station': random_station()
}
scheldwoord = ['kanker','kut','fuck']

#if scheldwoord in message:
 #  print('u mag niet schelden!')
#correct_bericht = message


with open('bericht.json','r') as file:
   data = json.load(file)
   print(type(data))
   data.append(message)

with open('bericht.json', 'w') as file:
   json.dump(data,file, indent=True)
#VANAF HIER
#print het meest recente bericht
print(message)
def moderator_nummer():
    ID = input('wat is uw ID: ')
    return ID

def check_bericht():
   print(message)
   goedkeuring = input('type ja of nee: ')
   if goedkeuring == 'ja':
      return 'bericht goedgekeurd'
   if goedkeuring == 'nee':
      return 'bericht afgekeurd'

def vraagmail():
  email = str(input('wat is uw email?: '))
  return email


beoordeeld = {
    'ID': moderator_nummer(),
    'naam':            vraagnaam(),
    'mail':            vraagmail(),
    'checked_bericht': check_bericht(),
    'bericht':         message,
    'datum':           datum(),
    'tijd':            tijd()

}
with open('moderator.json','r') as file:
   data = json.load(file)
   print(type(data))
   data.append(beoordeeld)

with open('moderator.json', 'w') as file:
   json.dump(data,file, indent=True)



insert_to_database(beoordeeld)