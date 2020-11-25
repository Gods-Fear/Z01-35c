from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from configparser import ConfigParser
import requests
import datetime


url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'
url_one_call_day = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'


config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']
count = 1


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['city']['name']
        country = json['city']['country']
        temperature_kelvin = json['list'][0]['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9 / 5 + 32
        weather = json['list'][0]['weather'][0]['main']
        icon = json['list'][0]['weather'][0]['icon']
        data = json['list'][0]['dt_txt']
        lat = json['city']['coord']['lat']
        lon = json['city']['coord']['lon']
        final = (city, country, temperature_celsius, temperature_fahrenheit, icon, weather, data, lat, lon)
        return final
    else:
        return None


def get_weather_h(city, h):
    result_h = requests.get(url.format(city, api_key))
    if result_h:
        json = result_h.json()
        temperature_kelvin = json['list'][h]['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9 / 5 + 32
        weather = json['list'][h]['weather'][0]['main']
        icon = json['list'][h]['weather'][0]['icon']
        data = json['list'][h]['dt_txt']
        final = (temperature_celsius, temperature_fahrenheit, icon, weather, data)
        return final
    else:
        return None


def print_weather_h():
    city = city_text.get()
    weather = get_weather_h(city, 1)
    if weather:
        temp_lbl_2['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_2['text'] = '{}'.format(weather[3])
        image_2['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_2.photo = image_2['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_2['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


def print_weather_h_2():
    city = city_text.get()
    weather = get_weather_h(city, 2)
    if weather:
        temp_lbl_3['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_3['text'] = '{}'.format(weather[3])
        image_3['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_3.photo = image_3['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_3['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


def print_weather_h_3():
    city = city_text.get()
    weather = get_weather_h(city, 3)
    if weather:
        temp_lbl_4['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_4['text'] = '{}'.format(weather[3])
        image_4['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_4.photo = image_4['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_4['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


def print_weather_h_4():
    city = city_text.get()
    weather = get_weather_h(city, 4)
    if weather:
        temp_lbl_5['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_5['text'] = '{}'.format(weather[3])
        image_5['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_5.photo = image_5['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_5['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


def print_weather_h_5():
    city = city_text.get()
    weather = get_weather_h(city, 5)
    if weather:
        temp_lbl_6['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_6['text'] = '{}'.format(weather[3])
        image_6['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_6.photo = image_6['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_6['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


def print_weather_h_6():
    city = city_text.get()
    weather = get_weather_h(city, 6)
    if weather:
        temp_lbl_7['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_7['text'] = '{}'.format(weather[3])
        image_7['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_7.photo = image_7['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_7['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


def print_weather_h_7():
    city = city_text.get()
    weather = get_weather_h(city, 7)
    if weather:
        temp_lbl_8['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[0], weather[1])
        weather_lbl_8['text'] = '{}'.format(weather[3])
        image_8['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        image_8.photo = image_8['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[2])))
        data_lbl_8['text'] = '{}'.format(weather[4])
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))




def clicked_next():
    global count
    if count < 7:
        count += 1
    else:
        messagebox.showerror('Error', 'You can see forecast only for 7 days')


def clicked_last():
    global count
    count -= 1


def next_day_weather(lat, lon, click):
    result = requests.get(url_one_call_day.format(lat, lon, api_key))
    if result:
        json = result.json()
        print(json)
        temperature_kelvin = json['daily'][click]['temp']['day']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9 / 5 + 32
        weather = json['daily'][click]['weather'][0]['main']
        icon = json['daily'][click]['weather'][0]['icon']
        data = json['daily'][click]['dt']
        timestamp = datetime.datetime.fromtimestamp(data)
        data = timestamp.strftime('%Y-%m-%d %H:%M:%S')

        # hourly
        data_h_c = json['hourly'][0]['dt']
        timestamp = datetime.datetime.fromtimestamp(data_h_c)
        data_h_c = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        icon_h_c = json['hourly'][0]['weather'][0]['icon']
        tem_c = json

        final = (temperature_celsius, temperature_fahrenheit, weather, icon, data)
        return final
    else:
        return None


def print_next_day_weather():
    city = city_text.get()
    weather = get_weather(city)
    weather_daily = next_day_weather(weather[7], weather[8], count)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        image['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather_daily[3])))
        image.photo = image['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather_daily[3])))
        temp_lbl['text'] = '{:.2f}℃, {:.2f}℉'.format(weather_daily[0], weather_daily[1])
        weather_lbl['text'] = '{}'.format(weather_daily[2])
        data_lbl['text'] = '{}'.format(weather_daily[4])
        clicked_next()
        print(count)
    else:
        messagebox.showerror('Error', 'Cannot find tem in  {}'.format(city))


def print_last_day_weather():
    city = city_text.get()
    weather = get_weather(city)
    weather_daily = next_day_weather(weather[7], weather[8], count)
    print(count)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        image['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather_daily[3])))
        image.photo = image['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather_daily[3])))
        temp_lbl['text'] = '{:.2f}℃, {:.2f}℉'.format(weather_daily[0], weather_daily[1])
        weather_lbl['text'] = '{}'.format(weather_daily[2])
        data_lbl['text'] = '{}'.format(weather_daily[4])
        clicked_last()
        print(count)
    else:
        messagebox.showerror('Error', 'Cannot find tem in  {}'.format(city))


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}℃, {:.2f}℉'.format(weather[2], weather[3])
        weather_lbl['text'] = '{}'.format(weather[5])
        image['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[4])))
        image.photo = image['image'] = ImageTk.PhotoImage(Image.open('weather_icons/{}.png'.format(weather[4])))
        data_lbl['text'] = '{}'.format(weather[6])
        print_weather_h()
        print_weather_h_2()
        print_weather_h_3()
        print_weather_h_4()
        print_weather_h_5()
        print_weather_h_6()
        print_weather_h_7()
        next_btn.grid(row=7)
        last_btn.grid(row=8)
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


root = Tk()
root.geometry("800x550")
root.title("Weather")
root.config(bg='#E5E7E7')
root.iconbitmap('weather_icons/icon.ico')

city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.grid(row=0, padx=350)

search_btn = Button(root, text='Search weather', width=12, command=search)
search_btn.grid(row=1, padx=350)

location_lbl = Label(root, text='', font=('bold', 20), bg='#E5E7E7')
location_lbl.grid(row=2, pady=20)

image = Label(root, image='', bg='#E5E7E7')
image.grid(row=3)

temp_lbl = Label(root, text='', bg='#E5E7E7')
temp_lbl.grid(row=4)

weather_lbl = Label(root, text='', bg='#E5E7E7')
weather_lbl.grid(row=5)

data_lbl = Label(root, text='', bg='#E5E7E7')
data_lbl.grid(row=6)

next_btn = Button(root, text='Next', width=12, command=print_next_day_weather)
last_btn = Button(root, text='Last', width=12, command=print_last_day_weather)


# ROW and COLUMN _ h
row5 = Frame(root, bg="#E5E7E7")
row5.grid(row=9, column=0, pady=30)

image_2 = Label(row5, image='', bg='#E5E7E7')
image_2.grid(row=0, column=0)

temp_lbl_2 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_2.grid(row=1, column=0)

weather_lbl_2 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_2.grid(row=2, column=0)

data_lbl_2 = Label(row5, text='', bg='#E5E7E7')
data_lbl_2.grid(row=3, column=0)

# -------------------------------------------------

image_3 = Label(row5, image='', bg='#E5E7E7')
image_3.grid(row=0, column=1)

temp_lbl_3 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_3.grid(row=1, column=1)

weather_lbl_3 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_3.grid(row=2, column=1)

data_lbl_3 = Label(row5, text='', bg='#E5E7E7')
data_lbl_3.grid(row=3, column=1)

# -------------------------------------------------

image_4 = Label(row5, image='', bg='#E5E7E7')
image_4.grid(row=0, column=2)

temp_lbl_4 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_4.grid(row=1, column=2)

weather_lbl_4 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_4.grid(row=2, column=2)

data_lbl_4 = Label(row5, text='', bg='#E5E7E7')
data_lbl_4.grid(row=3, column=2)

# -------------------------------------------------

image_5 = Label(row5, image='', bg='#E5E7E7')
image_5.grid(row=0, column=3)

temp_lbl_5 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_5.grid(row=1, column=3)

weather_lbl_5 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_5.grid(row=2, column=3)

data_lbl_5 = Label(row5, text='', bg='#E5E7E7')
data_lbl_5.grid(row=3, column=3)

# -------------------------------------------------

image_6 = Label(row5, image='', bg='#E5E7E7')
image_6.grid(row=0, column=4)

temp_lbl_6 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_6.grid(row=1, column=4)

weather_lbl_6 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_6.grid(row=2, column=4)

data_lbl_6 = Label(row5, text='', bg='#E5E7E7')
data_lbl_6.grid(row=3, column=4)

# -------------------------------------------------

image_7 = Label(row5, image='', bg='#E5E7E7')
image_7.grid(row=0, column=5)

temp_lbl_7 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_7.grid(row=1, column=5)

weather_lbl_7 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_7.grid(row=2, column=5)

data_lbl_7 = Label(row5, text='', bg='#E5E7E7')
data_lbl_7.grid(row=3, column=5)

# -------------------------------------------------

image_8 = Label(row5, image='', bg='#E5E7E7')
image_8.grid(row=0, column=6)

temp_lbl_8 = Label(row5, text='', bg='#E5E7E7')
temp_lbl_8.grid(row=1, column=6)

weather_lbl_8 = Label(row5, text='', bg='#E5E7E7')
weather_lbl_8.grid(row=2, column=6)

data_lbl_8 = Label(row5, text='', bg='#E5E7E7')
data_lbl_8.grid(row=3, column=6)

root.mainloop()
