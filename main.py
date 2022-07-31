
import PySimpleGUI as sg
import add_window
import load_window
import sqlite3
import database_interface


# select theme (optional)
sg.theme('DarkTeal9')


conn = sqlite3.connect('clinical_trials.db')
query = (''' CREATE TABLE IF NOT EXISTS CLINICAL_TRIALS
(STUDY_ID INT NOT NULL,
STUDY_PART TEXT NOT NULL,
DATA_1 TEXT,
DATA_2 TEXT,
DATA_3 TEXT,
DATA_4 TEXT,
DATA_5 TEXT,
DATA_6 TEXT);
''')
conn.execute(query)
conn.close()


# create main window layout to add and load trials
main_window_layout = [
    [sg.Text('')],
    [sg.Text('Welcome to CMAX Trial Data Log', justification='central')],
    [sg.Text('')],
    [sg.Text('Study Number', size=(12, 1)), sg.InputText(key='Load_Study_ID', size=(10, 1))],
    [sg.Text('Study Level', size=(11, 1)), sg.Combo(['Part A', 'Part B', 'Part C', 'Part D', 'Part E'], key='Load_Study_Part')],
    [sg.Button('Load Trial Data')],
    [sg.Text('')],
    [sg.Button('Add New Trial Data')],
    [sg.Text('')],
]


# show main layout window
main_window = sg.Window('CMAX Trial Data - Beta v1.0', main_window_layout, size=(420, 320), location=(20, 20), element_justification='c', font=('Arial', 12))

# start while loop to kep main window and function
while True:
    event, values = main_window.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Add New Trial Data':
        add_window.add_trial_data()
    if event == 'Load Trial Data':
        if len(values['Load_Study_ID']) == 0:
            sg.popup('Please enter study number!')
        else:
            study_number = int(values['Load_Study_ID'])
            study_part = values['Load_Study_Part']
            database_interface.load_trial(study_number, study_part)
        # load_window.load_trial_data()

main_window.close()
