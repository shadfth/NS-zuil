from datetime import datetime
import random
import json
from database import insert_to_database


# hier maak ik de functie die het bericht vraagt aan de gebruiker
def bericht():
    bericht = str(input('wat wilt u kwijt?: '))
    lengte_bericht = len(bericht)
    if lengte_bericht >= 140:
        print('u mag niet meer dan 140 characters gebruiken (inlusief spaties)!')
    else:
        return bericht


# hier vraag ik de gebruiker om de naam
def vraagnaam():
    naam = str(input('wat is uw naam?: '))
    if naam == '':
        return 'annoniem'
    return naam


# hier vraag ik de computer om de actuale tijd
def tijd():
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    tijd_string = now.strftime("%H:%M:%S")
    return tijd_string


# hier vraag ik de compute om de actuele datum
def datum():
    # datetime object containing current date and time
    now = datetime.now()

    datum_string = now.strftime("%Y/%m/%d")
    return datum_string


# hier laat ik de computer een random station kiezen
def random_station():
    random_getal = random.randrange(1, 4)
    if random_getal == 1:
        return "Station Zaandam"
    if random_getal == 2:
        return 'Station Amsterdam'
    return 'Station Utrecht'


# hier sla ik de berichten en informatie van gebruiker op
message = {
    'naam': vraagnaam(),
    'bericht': bericht(),
    'datum': datum(),
    'tijd': tijd(),
    'station': random_station()
}

# hier open ik mijn JSON files
with open('bericht.json', 'r') as file:
    data = json.load(file)
    print(type(data))
    data.append(message)

# hier dump ik de informatie naar mijn JSON files
with open('bericht.json', 'w') as file:
    json.dump(data, file, indent=True)
# VANAF HIER BEGINT EEN DEEL VAN MODULE 2
# print het meest recente bericht
print(message)


# hier vraag ik de moderator om zijn of haar ID
def moderator_nummer():
    ID = input('wat is uw ID: ')
    return ID

# hier checked de moderator het bericht
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
    'naam': vraagnaam(),
    'mail': vraagmail(),
    'checked_bericht': check_bericht(),
    'bericht': message,
    'datum': datum(),
    'tijd': tijd()

}
with open('moderator.json', 'r') as file:
    data = json.load(file)
    print(type(data))
    data.append(beoordeeld)

with open('moderator.json', 'w') as file:
    json.dump(data, file, indent=True)

insert_to_database(beoordeeld)
