''' Task: Create a question paper using tkinter.
Listing of all the question along with options ,
a submit button and pop up window to confirm with OK / Cancel are created.
Blocked at selecting guesses for each question
'''


from tkinter import *
from tkinter import messagebox as mb
import time

questions = {"Who manufactures Lifebuoy?": "A",
             "Who is the founder of apple?": "B",
             "Which is the most valued Indian company?": "C",
             "Who is the richest man in the World?": "D"}

options = [["A. HUL", "B. Dabur", "C. ITC", "D. AWL"], ["A. Jeff B", "B. Steve Jobs", "C. Elon Musk", "D. Larry Page"],
           ["A. Infosys", "B. Adani", "C. RELIANCE", "D. TCS"],
           ["A. Jeff B", "B. Ambani", "C. Jack Ma", "D. Elon Musk"]]

window = Tk()
window.geometry('600x600')


def guess():
    pass
    # print(x.get())


def paper(pair):
    ques = pair[0]
    option = pair[1]
    label = Label(window, text=ques)
    label.pack(anchor=W)

    temp = []
    for i in range(0, len(option)):
        global x
        x = IntVar()
        # x.set(0)
        check_button = Checkbutton(window, text=option[i], variable=x, onvalue=option[i], offvalue=0, command=guess).pack(anchor=W)
        print(x.get())
        temp.append(option[x.get()])

    return temp


submit_answer = []
ques_pair = list(zip(questions, options))
for index in ques_pair:
    res = paper(index)
    # print(res)



# def submit():
#     pop_up_window = Tk()
#     pop_up_window.geometry('400x100')
#     label = Label(pop_up_window, text='Do you wish to submit?').pack()
#     ok_button = Button(pop_up_window, text='OK', command=pop_up_window.destroy).pack(side=RIGHT)
#     close_button = Button(pop_up_window, text='Cancel', command=pop_up_window.destroy).pack(side=RIGHT)
#
#     pop_up_window.mainloop()


#  simple way to confirm submit from the user, but after clicking on OK the submit button should be DISABLED
def submit():
    if mb.askokcancel(message='Do you wish to continue?'):
        print("Successfully completed quiz")
    else:
        pass


button = Button(window,
                text='Submit',
                command=submit
                )
button.pack()

window.mainloop()




