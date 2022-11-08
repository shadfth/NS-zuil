import tkinter
import tkinter as tk
from tkinter import *
import psycopg2.extras # import changed!
import requests
import json
import random
from PIL import ImageTk


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

def zaandam():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # DictCursor, not the default cursor!
    query = """ SELECT     naam, bericht, station, tijd,datum
                FROM       bericht
                WHERE      station = 'Station Zaandam' and goedgekeurd = 'bericht goedgekeurd'
                ORDER BY       bericht.datum, bericht.tijd ASC
                LIMIT 5;"""
    cursor.execute(query)
    station_zaandam = cursor.fetchall()
    conn.close()

    #m = random.choice(station_zaandams)
    message = ""
    for m in station_zaandam:
        message+= f'{m[0]} zegt: {m[1]} ({m[2]})\n\n'
    label['text']=message
    label2['text'] = 'Aanwezige faciliteiten: Park en Ride, Lift'


    CITY = 'Zaandam'
    try:
        api_request = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?lat=52.4420&lon=4.8292&appid=42bd458b01c0125965b416619a794910')
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Fout...'

    response = api

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahreinheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    labeltemp["text"] = text = (f"Temperatuur in {CITY}: {temp_celsius:.2f}°C") + ( \
        f"\nDe temperatuur voelt aan als: {feels_like_celsius:.2f}°C")
    root.configure(bg='#ffc61e')

def utrecht():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = """ SELECT     naam, bericht, station, tijd,datum
                    FROM       bericht
                    WHERE      station = 'Station Utrecht' and bericht = 'bericht goedgekeurd'
                    ORDER BY       bericht.datum, bericht.tijd ASC
                    LIMIT 5;"""
    cursor.execute(query)
    station_utrecht = cursor.fetchall()
    conn.close()

    #m = random.choice(station_zaandam)
    message = ""
    for m in station_utrecht:
        message+= f'{m[0]} zegt: {m[1]} ({m[2]})\n\n'
    label['text']=message
    label2['text'] = 'Aanwezige faciliteiten: OV Fiets, Toilet'



    CITY = 'Utrecht'
    try:
        api_request = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?lat=52.0907&lon=5.1214&appid=42bd458b01c0125965b416619a794910')
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Fout...'

    response = api

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahreinheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    humidity = response['main']['humidity']
    description = response['weather'][0]['description']


    labeltemp["text"] = text=(f"Temperatuur in {CITY}: {temp_celsius:.2f}°C") + (\
       f"\nDe temperatuur voelt aan als: {feels_like_celsius:.2f}°C")
    root.configure(bg='#ffc61e')




def amsterdam():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # DictCursor, not the default cursor!
    query = """ SELECT     naam, bericht, station, tijd,datum
                    FROM       bericht
                    WHERE      station = 'Station Amsterdam' and bericht = 'goedgekeurd'
                    ORDER BY       bericht.datum, bericht.tijd ASC
                    LIMIT 5;"""
    cursor.execute(query)
    station_amsterdam = cursor.fetchall()
    conn.close()

    #m = random.choice(station_amsterdam)
    message = ""
    for m in station_amsterdam:
        message+= f'{m[0]} zegt: {m[1]} ({m[2]})\n\n'
    label['text']=message
    label2['text']='Aanwezige faciliteiten: Park en Ride, Lift'








    CITY = 'Amsterdam'
    try:
        api_request = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=42bd458b01c0125965b416619a794910')
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Fout...'

    response = api

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahreinheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    labeltemp['text'] = (f"Temperatuur in {CITY}: {temp_celsius:.2f}°C") + (
        f"\nDe temperatuur voelt aan als: {feels_like_celsius:.2f}°C")
    root.configure(bg='#ffc61e')








root = Tk()


# Add image file
bg = PhotoImage(file="Nederlandse_Spoorwegen_logoGROOT.svg.png")

# Create Canvas
canvas1 = Canvas(root, width=400,
                 height=400)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")




faciliteiten=tkinter.Frame(root, bg='#ffc61e')
faciliteiten.pack()

labeltemp = tk.Label(master=root, text=(f"Temperatuur in : °C") + (
        f"\nDe temperatuur voelt aan als: °C"), height=5, bg='#ffc61e', fg='dark blue',font='arial 14')
labeltemp.pack(pady=10, padx=17, )

root.configure(background='#ffc61e')

root.geometry('800x500')

label = Label(master=root, text='Welkom bij het Stationszuil!', font=('hind,18'),
              justify= 'left', fg='dark blue', relief= 'sunken')
labal_canvas = canvas1.create_window(900, 300,window=label)
label2 = Label(master=root, text='', font=('ariel,18'),
              justify= 'left', background='#ffc61e')
label2.pack(side=TOP, anchor='nw')


button1 = Button(master=root, text='Zaandam', command=zaandam,font=('ariel,18'))


button2 = Button(master=root, text='Utrecht', command=utrecht, font=('ariel,18'))


button3 = Button(master=root, text='Amsterdam', command=amsterdam, font=('ariel,18'))

#Display Buttons
button1_canvas = canvas1.create_window(1500, 150,

                                       window=button1)

button2_canvas = canvas1.create_window(200, 150,window=button2)

button3_canvas = canvas1.create_window(900, 150,
                                       window=button3)



root.mainloop()

