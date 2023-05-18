import PySimpleGUIQt as sg

form = sg.FlexForm('My first GUI')

layout = [ [sg.Text('Enter your name', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your country', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your phone', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your city', size=(15, 1)), sg.InputText()],
           [sg.OK(), sg.Cancel()] ]

button, values = form.Layout(layout).Read()
name = values[0]
country = values[1]
phone = values[2]
city = values[3]

print(f"name {name}, country {country}, phone {phone}, city {city}")