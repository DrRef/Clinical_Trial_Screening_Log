import PySimpleGUI as sg


# create load trial layout
def load_trial_data(data_list):

    # create load trial layout
    load_layout_1 = [
        [sg.Text('')],
        [sg.Text(data_list[2])],
        ]

    load_layout_2 = [
        [sg.Text('')],
        [sg.Text(data_list[3])],
        ]

    load_layout_3 = [
        [sg.Text('')],
        [sg.Text(data_list[4])],
        ]

    load_layout_4 = [
        [sg.Text('')],
        [sg.Text(data_list[5])],
        ]

    load_layout_5 = [
        [sg.Text('')],
        [sg.Text(data_list[6])],
        ]

    load_layout_6 = [
        [sg.Text('')],
        [sg.Text(data_list[7])],
        [sg.Exit()],
        ]

    # create tabs
    tab_group = [[
        sg.TabGroup(
            [[
                sg.Tab('General Info', load_layout_1),
                sg.Tab('IP and MOA', load_layout_2),
                sg.Tab('Inclusions', load_layout_3),
                sg.Tab('Exclusions', load_layout_4),
                sg.Tab('Risk', load_layout_5),
                sg.Tab('Specials', load_layout_6),
            ]]
                    )
                ]]

    # show add trial layout in window
    load_trial_data_window = sg.Window('CMAX Trial Data', tab_group, font=('Arial', 11))

    while True:
        event, values = load_trial_data_window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    load_trial_data_window.close()
