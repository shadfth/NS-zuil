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
                WHERE      station = 'Station Zaandam'
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
    CITY = 'Utrecht'
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
    root.configure(bg='yellow')

def utrecht():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = """ SELECT     naam, bericht, station, tijd,datum
                    FROM       bericht
                    WHERE      station = 'Station Utrecht'
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
    labelimg.configure(image=root.toilet)
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
    root.configure(bg='yellow')




def amsterdam():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # DictCursor, not the default cursor!
    query = """ SELECT     naam, bericht, station, tijd,datum
                    FROM       bericht
                    WHERE      station = 'Station Amsterdam'
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
    labelimg.configure(image=root.ovfiets,pady=10,padx=10)
    root.ovfiets = PhotoImage(file='iloveimg-resized/img_ovfiets.png')
    labelimg2 = Label(master=root, image=root.ovfiets)
    labelimg2.pack()






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
    root.configure(bg='yellow')

root = Tk()
frame1 = tk.Frame(root, width= 500, height=600)
frame1.grid(row=0,column=0)

nsfiets = ImageTk.PhotoImage(file='iloveimg-resized/img_ovfiets.png')
ns_widget = tk.Label(frame1,image=nsfiets)
nsfiets.image = nsfiets
ns_widget.pack()


labeltemp = tk.Label(master=root, text=(f"Temperatuur in : °C") + (
        f"\nDe temperatuur voelt aan als: °C"), height=5, bg='yellow', fg='blue',
                     font='arial 14')
labeltemp.pack(pady=10, padx=17, )

root.configure(background='yellow')

root.geometry('800x500')

label = Label(master=root, text='Welkom bij het Stationszuil!', font=('ariel,18'),background='yellow')
label.pack()

button = Button(master=root, text='Zaandam', command=zaandam,font=('ariel,18'))
button.pack(pady=10)

button = Button(master=root, text='Utrecht', command=utrecht, font=('ariel,18'))
button.pack(pady=10)

button = Button(master=root, text='Amsterdam', command=amsterdam, font=('ariel,18'))
button.pack(pady=10)

img = PhotoImage(file='nederlandse-spoorwegen-ns-logo.png')
root.pr  = PhotoImage(file='nederlandse-spoorwegen-ns-logo.png')

root.toilet = PhotoImage(file='iloveimg-resized/img_toilet.png')
root.lift = PhotoImage(file='iloveimg-resized/img_lift.png')

labelimg = Label(master=root, image=root.pr)


labelimg.pack()


root.mainloop()

