import sqlite3
import load_window


def insert_new_trial(study_ID, study_Part, data_1, data_2, data_3, data_4, data_5, data_6):
    conn = sqlite3.connect('./clinical_trials.db')
    conn.execute("INSERT INTO CLINICAL_TRIALS (STUDY_ID, STUDY_Part, DATA_1, DATA_2, DATA_3, DATA_4, DATA_5, DATA_6) \
     VALUES(?,?,?,?,?,?,?,?)", (study_ID, study_Part, data_1, data_2, data_3, data_4, data_5, data_6))
    conn.commit()
    conn.close()


def load_trial(study_ID, study_part):
    conn = sqlite3.connect('./clinical_trials.db')
    c = conn.cursor()
    c.execute("SELECT * from CLINICAL_TRIALS where STUDY_ID = ? and STUDY_PART = ?", (study_ID, study_part))
    data_tuple = c.fetchone()
    data_list = list(data_tuple)
    load_window.load_trial_data(data_list)
    # print(data_list)
    # print(type(data_list))
    conn.close()
