import pyshorteners #lib to short the url
import webbrowser #control brower
import PySimpleGUI as sg  #simple user interface
import validators #lib the validatade url




    
# Define the window's contents
layout = [[sg.Text("Enter Url :")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]
    

# Create the window
window = sg.Window("Url Shortner", layout)  
    
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    url = pyshorteners.Shortener(api_key = "YOUR API")#bitly api
   
    if validators.url(values["-INPUT-"]) :#check the url if valid
        window['-OUTPUT-'].update("Url Is Opening In The Browser in 2 Seconds .")
        webbrowser.open(url.bitly.short(values['-INPUT-']))#shortning the url
    else:
        window['-OUTPUT-'].update("Invalid Url ! Try Again.")
# Finish up by removing from the screen
window.close()
    
