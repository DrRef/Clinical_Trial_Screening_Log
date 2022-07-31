import PySimpleGUI as sg
import database_interface


def add_trial_data():
    # create add trial layout
    add_layout_1 = [
        [sg.Text('')],
        [sg.Text('Trial Number       CM', size=(15, 1)), sg.InputText(key='Study_ID')],
        [sg.Text('Study Part', size=(15, 1)), sg.Combo(['Part A', 'Part B', 'Part C', 'Part D', 'Part E'], key='Study_Part'),
         sg.Text('     Part Description', size=(15, 1)), sg.InputText(size=(15, 1), key='L01_Part_Desc')],
        [sg.Text('')],
        [sg.Text('PI', size=(15, 1)), sg.InputText(key='L01_PI')],
        [sg.Text("PI's Number", size=(15, 1)), sg.InputText(key='L01_PI_Phone')],
        [sg.Text('DMD', size=(15, 1)), sg.InputText(key='L01_DMD')],
        [sg.Text("DMD's Number", size=(15, 1)), sg.InputText(key='L01_DMD_Phone')],
        [sg.Text('')],
        [sg.Text('On Study Nights (round 1)', size=(25, 1)), sg.Slider(orientation='horizontal', key='L01_Nights1', range=(0, 31))],
        [sg.Text('On Study Nights (round 2)', size=(25, 1)), sg.Slider(orientation='horizontal', key='L01_Nights2', range=(0, 31))],
        [sg.Text('On Study Nights (round 3)', size=(25, 1)), sg.Slider(orientation='horizontal', key='L01_Nights3', range=(0, 31))],
        [sg.Text('On Study Nights (round 4)', size=(25, 1)), sg.Slider(orientation='horizontal', key='L01_Nights4', range=(0, 31))],
        [sg.Text('')],
        [sg.Text('Follow Up Visits', size=(15, 1)), sg.Spin([i for i in range(0, 20)], initial_value='10', key='L01_FU_Visit'),
         sg.Text('                Follow Up Calls', size=(20, 1)), sg.Spin([i for i in range(0, 20)], initial_value='10', key='L01_FU_Phone')],
        [sg.Text('')],
    ]

    add_layout_2 = [
        [sg.Text('')],
        [sg.Text('IP Code', size=(15, 1)), sg.InputText(key='L02_IP_Code')],
        [sg.Text('Class', size=(15, 1)), sg.InputText(key='L02_IP_Class')],
        [sg.Text('')],
        [sg.Text('Administration', size=(15, 1)),
         sg.Combo(['Oral Tab/Cap', 'Oral Liquid', 'Injection IM', 'Injection IV', 'Injection SC', 'Topical', 'Inhalation', 'Spray', 'Drops', 'Rectal', 'Vaginal', 'Others'], key='L02_IP_Administration')],
        [sg.Text('')],
        [sg.Text('Targeted Conditions', size=(15, 1)), sg.Multiline(size=(43, 4), key='L02_Condition')],
        [sg.Text('')],
        [sg.Text('Mode Of Action', size=(15, 1)), sg.Multiline(size=(43, 10), key='L02_MOA')],
        [sg.Text('')],
    ]

    add_layout_3 = [
        [sg.Text('')],
        [sg.Text('Age Min (Inclusive)', size=(18, 1)),
         sg.Slider(orientation='horizontal', key='L03_Age_Min', range=(0, 100), default_value=18)],
        [sg.Text('Age Max (Inclusive)', size=(18, 1)),
         sg.Slider(orientation='horizontal', key='L03_Age_Max', range=(0, 100), default_value=55)],
        [sg.Text('_' * 65)],
        [sg.Text('BMI Min (Inclusive)', size=(18, 1)),
         sg.Slider(orientation='horizontal', key='L03_BMI_Min', resolution=.5, range=(15, 50), default_value=18)],
        [sg.Text('BMI Max (Inclusive)', size=(18, 1)),
         sg.Slider(orientation='horizontal', key='L03_BMI_Max', resolution=.5, range=(15, 50), default_value=32)],
        [sg.Text('Weight Min (Inclusive)', size=(18, 1)),
         sg.Slider(orientation='horizontal', key='L03_Weight_Min', range=(10, 100), default_value=40)],
        [sg.Text('_' * 65)],
        [sg.Text('COVID Vaccination', size=(18, 1)), sg.Checkbox('Required', key='L03_COVID')],
        [sg.Text('Add (1)', size=(18, 1)), sg.InputText(key='L03_Add_1')],
        [sg.Text('Add (2)', size=(18, 1)), sg.InputText(key='L03_Add_2')],
        [sg.Text('Add (3)', size=(18, 1)), sg.InputText(key='L03_Add_3')],
        [sg.Text('Add (4)', size=(18, 1)), sg.InputText(key='L03_Add_4')],
        [sg.Text('Add (5)', size=(18, 1)), sg.InputText(key='L03_Add_5')],
        [sg.Text('Add (6)', size=(18, 1)), sg.InputText(key='L03_Add_6')],
        [sg.Text('Add (7)', size=(18, 1)), sg.InputText(key='L03_Add_7')],
     ]

    add_layout_4 = [
        [sg.Text('')],
        [sg.Text('No participation in other trials within last (days)', size=(35, 1)),
         sg.Slider(orientation='horizontal', key='L04_Ex_Std', range=(30, 180), default_value=30)],
        [sg.Text('No prescribed medication within last (days)', size=(35, 1)),
         sg.Slider(orientation='horizontal', key='L04_Ex_Med', range=(0, 90), default_value=14)],
        [sg.Text('No OTC medication within last (days)', size=(35, 1)),
         sg.Slider(orientation='horizontal', key='L04_Ex_OTC', range=(0, 90), default_value=14)],
        [sg.Text('No herbal/supplements within last (days)', size=(35, 1)),
         sg.Slider(orientation='horizontal', key='L04_Ex_Sup', range=(0, 90), default_value=14)],
        [sg.Text('_' * 65)],
        [sg.Text('Add (1)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_01')],
        [sg.Text('Add (2)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_02')],
        [sg.Text('Add (3)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_03')],
        [sg.Text('Add (4)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_04')],
        [sg.Text('Add (5)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_05')],
        [sg.Text('Add (6)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_06')],
        [sg.Text('Add (7)', size=(10, 1)), sg.Multiline(size=(50, 2), key='L04_Ex_07')],
    ]

    add_layout_5 = [
        [sg.Text('')],
        [sg.Text('AE in Animals', size=(15, 1)), sg.Multiline(size=(45, 10), key='L05_AE_Animal')],
        [sg.Text('AE in Human', size=(15, 1)), sg.Multiline(size=(45, 10), key='L05_AE_Human')],
        [sg.Text('Add (1)', size=(15, 1)), sg.Multiline(size=(45, 3), key='L05_Add_01')],
        [sg.Text('Add (2)', size=(15, 1)), sg.Multiline(size=(45, 3), key='L05_Add_02')],
    ]

    add_layout_6 = [
        [sg.Text('')],
        [sg.Text('Hormonal Contraception', size=(18, 1)), sg.Checkbox('Allowed', key='L06_HCP')],
        [sg.Text('Add (1)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_01')],
        [sg.Text('Add (2)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_02')],
        [sg.Text('Add (3)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_03')],
        [sg.Text('Add (4)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_04')],
        [sg.Text('Add (5)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_05')],
        [sg.Text('Add (6)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_06')],
        [sg.Text('Add (7)', size=(10, 1)), sg.Multiline(size=(50, 3), key='L06_Add_07')],
        [sg.Text('')],
        [sg.Submit(), sg.Text('', size=(37, 1)), sg.Button('Clear'), sg.Exit()],
    ]

    # create tabs
    tab_group = [[
        sg.TabGroup(
            [[
                sg.Tab('General Info', add_layout_1),
                sg.Tab('IP and MOA', add_layout_2),
                sg.Tab('Inclusions', add_layout_3),
                sg.Tab('Exclusions', add_layout_4),
                sg.Tab('Risk', add_layout_5),
                sg.Tab('Specials', add_layout_6),
            ]]
        )
    ]]

    # function to clear input fields after submission or clear clicked
    def clear_input():
        for key in values:
            add_trial_data_window[key]('')
        return None

    # show add trial layout in window
    add_trial_data_window = sg.Window('CMAX Add New Trial Data', tab_group, font=('Arial', 11))

    while True:
        event, values = add_trial_data_window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Clear':
            clear_input()
        if event == 'Submit':
            data_1: str = f"Study: CM {values['Study_ID']} \n" \
                           f"Study: {values['Study_Part']} - {values['L01_Part_Desc']} \n" \
                           f"IP: {values['L01_PI']}, IP's Phone: {values['L01_PI_Phone']} \n" \
                           f"DMD: {values['L01_DMD']}, DMD's Phone: {values['L01_DMD_Phone']} \n\n" \
                           f"On Stay Nights (round 1): {int(values['L01_Nights1'])}\n" \
                           f"On Stay Nights (round 2): {int(values['L01_Nights2'])}\n" \
                           f"On Stay Nights (round 3): {int(values['L01_Nights3'])}\n" \
                           f"On Stay Nights (round 4): {int(values['L01_Nights4'])}\n" \
                           f"Follow up visits: {values['L01_FU_Visit']}\n" \
                           f"Follow up phone calls: {values['L01_FU_Phone']}"
            data_2: str = f"IP Code: {values['L02_IP_Code']}\n" \
                          f"IP Class: {values['L02_IP_Class']}\n" \
                          f"Mode of administration: {values['L02_IP_Administration']}\n\n" \
                          f"Targeted conditions:\n {values['L02_Condition']}\n\n" \
                          f"Mode of Action:\n {values['L02_MOA']}"
            data_3: str = f"Age: {int(values['L03_Age_Min'])} - {int(values['L03_Age_Max'])} (inclusive)\n" \
                          f"BMI: {values['L03_BMI_Min']} - {values['L03_BMI_Max']} (inclusive)\n" \
                          f"Weight min: {int(values['L03_Weight_Min'])}\n" \
                          f"COVID vaccination required: {values['L03_COVID']}\n\n" \
                          f"Inclusion (1): {values['L03_Add_1']}\n" \
                          f"Inclusion (2): {values['L03_Add_2']}\n" \
                          f"Inclusion (3): {values['L03_Add_3']}\n" \
                          f"Inclusion (4): {values['L03_Add_4']}\n" \
                          f"Inclusion (5): {values['L03_Add_5']}\n" \
                          f"Inclusion (6): {values['L03_Add_6']}\n" \
                          f"Inclusion (7): {values['L03_Add_7']}"
            data_4: str = f"No participation in other trials within last: {int(values['L04_Ex_Std'])} (days)\n" \
                          f"No prescribed medication within last: {int(values['L04_Ex_Med'])} (days)\n" \
                          f"No OTC medication within last: {int(values['L04_Ex_OTC'])} (days)\n" \
                          f"No herbal/supplements within last: {int(values['L04_Ex_Sup'])} (days)\n\n" \
                          f"Exclusion (1): {values['L04_Ex_01']}\n" \
                          f"Exclusion (2): {values['L04_Ex_02']}\n" \
                          f"Exclusion (3): {values['L04_Ex_03']}\n" \
                          f"Exclusion (4): {values['L04_Ex_04']}\n" \
                          f"Exclusion (5): {values['L04_Ex_05']}\n" \
                          f"Exclusion (6): {values['L04_Ex_06']}\n" \
                          f"Exclusion (7): {values['L04_Ex_07']}"
            data_5: str = f"Side effects in Animals:\n{values['L05_AE_Animal']}\n\n" \
                          f"Side effects in Human:\n{values['L05_AE_Human']}\n\n" \
                          f"Additional info (1): {values['L05_Add_01']}\n" \
                          f"Additional info (2): {values['L05_Add_02']}"
            data_6: str = f"Hormonal contraception allowed: {values['L06_HCP']}\n\n" \
                          f"Additional info (1): {values['L06_Add_01']}\n" \
                          f"Additional info (2): {values['L06_Add_02']}\n" \
                          f"Additional info (3): {values['L06_Add_03']}\n" \
                          f"Additional info (4): {values['L06_Add_04']}\n" \
                          f"Additional info (5): {values['L06_Add_05']}\n" \
                          f"Additional info (6): {values['L06_Add_06']}\n" \
                          f"Additional info (7): {values['L06_Add_07']}"

            database_interface.insert_new_trial(int(values['Study_ID']), values['Study_Part'], data_1, data_2, data_3, data_4, data_5, data_6)
            sg.popup('New Study Saved')
            clear_input()
    add_trial_data_window.close()
