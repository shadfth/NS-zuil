import tkinter as tk
from tkinter import *
import psycopg2.extras # import changed!

import random

def zaandam():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # DictCursor, not the default cursor!
    query = """SELECT     naam, bericht, station
               FROM       bericht
               WHERE      station = 'Station Zaandam';"""
    cursor.execute(query)
    station_zaandam = cursor.fetchall()
    conn.close()

    #m = random.choice(station_zaandams)
    message = ""
    for m in station_zaandam:
        message+= f'{m[0]} zegt: {m[1]} ({m[2]})\n'
    label['text']=message

def utrecht():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # DictCursor, not the default cursor!
    query = """SELECT     naam, bericht, station
               FROM       bericht
               WHERE      station = 'Station Utrecht';"""
    cursor.execute(query)
    station_utrecht = cursor.fetchall()
    conn.close()

    #m = random.choice(station_zaandams)
    message = ""
    for m in station_utrecht:
        message+= f'{m[0]} zegt: {m[1]} ({m[2]})\n'
    label['text']=message
    labelimg.configure(image=root.toilet)



def amsterdam():
    connection_string = "host='localhost' dbname='ns_zuil' user='postgres' password='Babyborn123'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # DictCursor, not the default cursor!
    query = """SELECT     naam, bericht, station
               FROM       bericht
               WHERE      station = 'Station Amsterdam';"""
    cursor.execute(query)
    station_amsterdam = cursor.fetchall()
    conn.close()

    #m = random.choice(station_zaandams)
    message = ""
    for m in station_amsterdam:
        message+= f'{m[0]} zegt: {m[1]} ({m[2]})\n'
    label['text']=message
    labelimg.configure(image=root.ovfiets)


root = Tk()

root.geometry('800x500')

label = Label(master=root, text='Hello World')
label.pack()

button = Button(master=root, text='zaandam', command=zaandam,font=(ariel))
button.pack(pady=10)

button = Button(master=root, text='Utrecht', command=utrecht, font=('ariel,18'))
button.pack(pady=10)

button = Button(master=root, text='Amsterdam', command=amsterdam, font=('ariel,18'))
button.pack(pady=10)

img = PhotoImage(file='iloveimg-resized/img_pr.png')
root.pr  = PhotoImage(file='iloveimg-resized/img_pr.png')
root.ovfiets = PhotoImage(file='iloveimg-resized/img_ovfiets.png')
root.toilet = PhotoImage(file='iloveimg-resized/img_toilet.png')

labelimg = Label(master=root, image=root.pr)
labelimg.pack()

root.mainloop()

