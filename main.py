
import tkinter as tk
from global_variables import *
from functions import *

HEIGHT = 700
WIDTH = 700

taskList = ['Choose A Task', 'Pitcher Rankings', 'Batter Rankings', 'Create Lineup', 'Update']



def do_task():
    print('clicked')
    if menu0_var.get() == 'Pitcher Rankings':
        get_pitcherRanks()
    if menu0_var.get() == 'Batter Rankings':
        get_batterRanks()
    if menu0_var.get() == 'Create Lineup':
        get_createdLineup()
    if menu0_var.get() == 'Choose A Task':
        print('Please Choose a Task')
        get_update()


def check_data():
    compList = []
    startersList = load_obj('startersList')
    pitcherDict = load_obj('pitcherDict')

    for pitcher in pitcherDict:
        compList.append(pitcher)

    if set(compList) == set(startersList):
        ''
    else:
        update_data()


def get_update():
    'p'

def get_pitcherRanks():
    print('pr')
    print_pitchersRanked()

def get_batterRanks():
    set_pitcherSkill()
    print_pitchersRanked()

def get_createdLineup():
    print('button clicked' + menu0_var.get())

def update_data():
    set_sdd()
    set_las()
    get_pitcherIDS()
    set_pitcherIDS()
    get_datascrape(entry_0.get(), entry_1.get(), entry_2.get())
    set_pitcherDict()
    set_zscores()
    set_pitcherSkill()

def test():
    get_datascrape(entry_0.get(), entry_1.get(), entry_2.get())
    update_data()
    print_pitchersRanked()


root = tk.Tk()

get_csv()
menu0_var = tk.StringVar(root)
menu0_var.set(taskList[0])

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='grey')
canvas.pack()

frame_0 = tk.Frame(root, bg='white',bd=5)
frame_0.place(relx=0.5, rely=.05, relwidth=0.75, relheight=.2, anchor='n')

label_0 = tk.Label(frame_0, text='DFS WIZARD', font='Helvetica 35 bold')
label_0.place(relwidth=1, relheight=1)

frame_1 = tk.Frame(root, bg='white',bd=5)
frame_1.place(relx=0.5, rely=.3, relwidth=0.85, relheight=.65, anchor='n')

frame_2 = tk.Frame(root, bg='white',bd=5)
frame_2.place(relx=0.5, rely=.3, relwidth=0.85, relheight=.65, anchor='n')

label_1 = tk.Label(frame_1, text='Enter Date', font='Helvetica 18')
label_1.place(relx=.5, rely=.05, anchor='n')

entry_0 = tk.Entry(frame_1, font = 18)
entry_0.place(relx=.42, rely=.13, anchor='n', relwidth=0.07, relheight=.07)

entry_1 = tk.Entry(frame_1, font = 18)
entry_1.place(relx=.5, rely=.13, anchor='n', relwidth=0.07, relheight=.07)

entry_2 = tk.Entry(frame_1, font = 18)
entry_2.place(relx=.58, rely=.13, anchor='n', relwidth=0.07, relheight=.07)

menu_0 = tk.OptionMenu(frame_2, menu0_var, *taskList)
menu_0.place(relx=.5, rely=.25, anchor='n')

button_0 = tk.Button(frame_1, text='Submit', command=combine_funcs(test, frame_2.lift))
button_0.place(relx=.5, rely=.35, anchor='n')

button_1 = tk.Button(frame_2, text='Submit2', command=lambda: do_task)
button_1.place(relx=.5, rely=.35, anchor='n')

frame_2.lower()
frame_1.lift

root.mainloop()































#root = tk.Tk()

# menu0_var = tk.StringVar(root)
# menu0_var.set(taskList[0])
#
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='grey')
# canvas.pack()
#
# frame_0 = tk.Frame(root, bg='white',bd=5)
# frame_0.place(relx=0.5, rely=.05, relwidth=0.75, relheight=.2, anchor='n')
#
# label_0 = tk.Label(frame_0, text='DFS WIZARD', font='Helvetica 35 bold')
# label_0.place(relwidth=1, relheight=1)
#
# frame_1 = tk.Frame(root, bg='white',bd=5)
# frame_1.place(relx=0.5, rely=.3, relwidth=0.85, relheight=.65, anchor='n')
#
# # frame_2 = tk.Frame(root, bg='white',bd=5)
# # frame_2.place(relx=0.5, rely=.3, relwidth=0.85, relheight=.65, anchor='n')
#
# label_1 = tk.Label(frame_1, text='Enter Date', font='Helvetica 18')
# label_1.place(relx=.5, rely=.05, anchor='n')
#
# entry_0 = tk.Entry(frame_1, font = 18)
# entry_0.place(relx=.42, rely=.13, anchor='n', relwidth=0.07, relheight=.07)
#
# entry_1 = tk.Entry(frame_1, font = 18)
# entry_1.place(relx=.5, rely=.13, anchor='n', relwidth=0.07, relheight=.07)
#
# entry_2 = tk.Entry(frame_1, font = 18)
# entry_2.place(relx=.58, rely=.13, anchor='n', relwidth=0.07, relheight=.07)
#
# menu_0 = tk.OptionMenu(frame_1, menu0_var, *taskList)
# menu_0.place(relx=.5, rely=.25, anchor='n')
#
# button_0 = tk.Button(frame_1, text='Submit', command=lambda: do_task())
# button_0.place(relx=.5, rely=.35, anchor='n')


# button_1 = tk.Button(frame_2, text='Submit', command=lambda: do_task)
# button_1.place(relx=.5, rely=.35, anchor='n')

# frame_2.lower()

#root.mainloop()