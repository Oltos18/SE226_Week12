import tkinter as tk
from tkinter import *
import mysql.connector

dropdownlist_options_list=[]
database=mysql.connector.connect(
    host='localhost',
    user='root',
    ##passwd
    database='python_project'
)

cursor = database.cursor()
create_table_query = '''
CREATE TABLE IF NOT EXISTS movies (
    ID INT,
    MOVIE VARCHAR(255),
    DATE VARCHAR(255),
    MCU_PHASE VARCHAR(255)
)
'''
cursor.execute(create_table_query)

mySql_insert_query = """INSERT INTO movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"""

with open('Marvel.txt', encoding='utf-8') as f:
    list_1=f.readlines()
    f.close()
for str in list_1:
    str=str.split()
    row_number=str[0]
    movie_name=str[1]
    year=str[2]
    phase_number=str[3]
    dropdownlist_options_list.append(str[0])
    try:
        record=(row_number,movie_name,year,phase_number)
        cursor.execute(mySql_insert_query,record)
        database.commit()
        print("Record inserted successfully into table")
    except mysql.connector.Error as error:
        print("Failed to inserted into table")

def take_input_inAddDatabaseMethod():
    input=add_textBox.get('1.0','end')
    list_input=input.split()
    """database ekle bunlari"""
    try:
        record=(list_input[0],list_input[1],list_input[2],list_input[3])
        cursor.execute(mySql_insert_query,record)
        database.commit()
        dropdownlist_options_list.append(record[0])
        print()
        print("Record inserted successfully into table")
    except mysql.connector.Error as error:
        print()
        print("Failed to inserted into table")

def addToDatabaseWindow_method():
    global pop
    global add_textBox
    pop = Toplevel(main_screen)
    pop.title('Add window')
    pop.geometry('300x300')
    pop.config(bg='blue')

    pop_label=tk.Label(pop,text="Please enter your information \n one by one and by using space in between")
    pop_label.pack(pady=5)
    add_textBox=tk.Text(pop,height=10,width=30)
    add_textBox.pack(pady=5)

    add_button_popWindow=tk.Button(pop, text='Add to database (Ok)', width=25, command=take_input_inAddDatabaseMethod, font=('Helvetica',10),pady=5)
    add_button_popWindow.pack()
    close_button_popWindow=tk.Button(pop, text='Cancel', width=25, command=pop.destroy, font=('Helvetica',10),pady=5)
    """bu close icin direkt icindeki kodu yazdim ama ayri method gerekebilir"""
    close_button_popWindow.pack()
    """add_entry=tk.Entry(pop)"""

"""Also answer for Question 8, section a, my answer"""
def listAll_method():
    main_screen_textBox.delete('1.0', 'end')
    sql_select_query = "select * from movies"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    print()
    for row in records:
        id = row["ID"]
        movie = row["MOVIE"]
        date = row["DATE"]
        phase = row["MCU_PHASE"]
        str_temp_final=f"{id} {movie} {date} {phase}"
        main_screen_textBox.insert(tk.END, str_temp_final + "\n")

        print(f"{id} {movie} {date} {phase} ")

def dropdown_clicked(input_in):
    main_screen_textBox.delete('1.0', 'end')
    sql_select_query = "select * from movies"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    for row in records:
        variable_1=row["ID"]
        variable_2=f"{variable_1}"
        if(variable_2==input_in):
            id = row["ID"]
            movie = row["MOVIE"]
            date = row["DATE"]
            phase = row["MCU_PHASE"]
            str_temp_final = f"{id} {movie} {date} {phase}"
            main_screen_textBox.insert(tk.END, str_temp_final + "\n")



main_screen = tk.Tk()
main_screen.title('Window')
main_screen.geometry('800x600')

button_add=tk.Button(main_screen, text='Add', width=10, command=addToDatabaseWindow_method, font=('Helvetica',20))
button_add.place(x=600,y=10)

button_listAll=tk.Button(main_screen, text='List All', width=10, command=listAll_method, font=('Helvetica',20))
button_listAll.place(x=600, y=75)

clicked=StringVar()
clicked.set('IDs')
dropdownlist_inMain_forId=tk.OptionMenu(main_screen,clicked,*dropdownlist_options_list,command=dropdown_clicked)
dropdownlist_inMain_forId.place(x=10, y=10)

main_screen_textBox=tk.Text(main_screen,height=30,width=60)
main_screen_textBox.place(x=90,y=10)



"""Question 8, section b, my answer"""
sql_update_query="delete from movies where MOVIE='TheIncredibleHulk'"
cursor.execute(sql_update_query)
database.commit()


print()
"""Question 8, section c, my answer"""
sql_select_query = "select * from movies where MCU_PHASE='Phase2'"
cursor = database.cursor(dictionary=True)
cursor.execute(sql_select_query)
records = cursor. fetchall()
for row in records:
    id = row["ID"]
    movie = row[ "MOVIE"]
    date = row["DATE"]
    phase = row["MCU_PHASE"]
    print(f"{id} {movie} {date} {phase} ")


"""Question 8, section d, my answer"""
sql_update_query_2="update movies set Date= '2017' where MOVIE='Thor:Ragnarok'"
cursor.execute(sql_update_query_2)
database.commit()


"""Database'e eklenen datayı dropdownlist'e eklemeyi çözemedim 
ondan öyle bir şey yapamıyor sadece databasenin ilk halindeki ID'leri alıyor"""

main_screen.mainloop()
