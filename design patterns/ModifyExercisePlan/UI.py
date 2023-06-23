from tkinter import *
from Service import Service

root = Tk()
root.title('운동 계획 관리 프로그램 (농구)')

def open_goalSpac():
    global player

    player = Service().genPlayer(float(heightE.get()), float(weightE.get()), float(muscleMassE.get()), positionE.get(), injury_var.get(), ballControl_var.get())

    goal_label.config(text=f"{player.player.getInfo()}'s Goal Condition")
    position_goal_label.config(text=f"{positionE.get()}'s Goal Condition")
    goalWeight_label.config(text=f"Goal Weight: {player.goal.gapText()}")

    exercise_plan_text.delete('1.0', END)
    exercise_plan_text.insert(END, player.plan.plan.exercisePlan())
    return player

def next_day():
    global player
    player.plan.controlAddPlan(player.player,player.goal)

    exercise_plan_text.delete('1.0', END)
    exercise_plan_text.insert(END, player.plan.plan.exercisePlan())
    return player

left_frame = Frame(root, relief="solid", bd=1)
left_frame.pack(side="left", fill="both")

inner_frame = Frame(left_frame)
inner_frame.pack(expand=True, padx=15, pady=10)

height_label = Label(inner_frame, text='Height')
height_label.grid(column=0, row=0, sticky="e")
heightE = Entry(inner_frame, width=30)
heightE.grid(column=1, row=0)

weight_label = Label(inner_frame, text='Weight')
weight_label.grid(column=0, row=1, sticky="e")
weightE = Entry(inner_frame, width=30)
weightE.grid(column=1, row=1)

muscleMass_label = Label(inner_frame, text='Muscle Mass')
muscleMass_label.grid(column=0, row=2, sticky="e")
muscleMassE = Entry(inner_frame, width=30)
muscleMassE.grid(column=1, row=2)

position_label = Label(inner_frame, text='Position')
position_label.grid(column=0, row=3, sticky="e")
positionE = Entry(inner_frame, width=30)
positionE.grid(column=1, row=3)

injury_label = Label(inner_frame, text='Injury')
injury_label.grid(column=0, row=5, sticky="e")
injury_var = BooleanVar()
injury_checkbutton = Checkbutton(inner_frame, variable=injury_var)
injury_checkbutton.grid(column=1, row=5, sticky="w")

ballControl_label = Label(inner_frame, text='Ball Control')
ballControl_label.grid(column=0, row=4, sticky="e")
ballControl_var = BooleanVar()
ballControl_checkbutton = Checkbutton(inner_frame, variable=ballControl_var)
ballControl_checkbutton.grid(column=1, row=4, sticky="w")

process_button = Button(inner_frame, text='Goal', command=open_goalSpac)
process_button.grid(column=0, row=7, columnspan=2,pady=10)

process_button = Button(inner_frame, text='Next Day(Condition No change)', command=next_day)
process_button.grid(column=0, row=9, columnspan=2,pady=10)

left_frame.grid_propagate(False)  
left_frame.grid_anchor("center")  

right_frame = Frame(root, relief="solid", bd=1)
right_frame.pack(side="right", fill="both", expand=True)

goal_label = Label(right_frame, text="")
goal_label.grid(column=0, row=0)

position_goal_label = Label(right_frame, text="")
position_goal_label.grid(column=0, row=1)

goalWeight_label = Label(right_frame, text="")
goalWeight_label.grid(column=0, row=2)

goalMuscleMass_label = Label(right_frame, text="")
goalMuscleMass_label.grid(column=0, row=3)

gapWeight_label = Label(right_frame, text="")
gapWeight_label.grid(column=0, row=4)

gapMuscleMass_label = Label(right_frame, text="")
gapMuscleMass_label.grid(column=0, row=5)

exercise_plan_label = Label(right_frame, text="Exercise Plan:")
exercise_plan_label.grid(column=1, row=0, sticky="w")

exercise_plan_text = Text(right_frame, width=40, height=30)  # Adjust the height here
exercise_plan_text.grid(column=1, row=1, rowspan=6, padx=10, pady=10)

root.mainloop()
