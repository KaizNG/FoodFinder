import PySimpleGUI as sg

sg.theme('Black')
priceOptions = ['Cheap', 'Expensive']
priceChoice = ["cheap", "expensive"]

#This is a test for buttons and text box
layout1 = [
    [sg.Text("~Welcome to Food Finder~")],
    [sg.Text("A tool to decide where to eat for you.")],
    [sg.Button("Next")]  ]

layout2 = [
    [sg.Text("Enter desired type of cuisine"), sg.InputText(key='-TYPE-')],
    [sg.Text("Enter postal code"), sg.InputText(key='-POSTAL-')],
    [sg.Text("Select max distance (km)")] + 
    [sg.Slider(range = (1, 50), orientation = 'horizontal')],
    [sg.Text('Choose price range')]] + [
        [sg.Radio(priceOptions[i], 'test', key=priceChoice[i])]
        for i in range(len(priceChoice))] + [[sg.Button('OK')]  ]


#Create window
window = sg.Window("Test App", layout1, margins = (100,50))
window2 = sg.Window("Test2", layout2, margins = (100,50))


while True:
    event, values = window.read()
    #End the program if user closes window or presses the ok button
    if event == "OK" or event == sg.WIN_CLOSED:
        window.close()
        break
    elif event == "Next":
        window.close()
        event, values = window2.read()
        break
