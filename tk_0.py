import tkinter as tk

root = tk.Tk()
root.geometry("500x800+300+300")
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text=whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

hello_label = tk.Label(root, text="Hello Tkinter!")
hello_label.pack()

click_counter = 0

slogan_button_label = tk.StringVar(root, 'Click me')


def write_slogan():
	global click_counter
	global slogan_button_label
	slogan_button_label.set('Click ' + str(click_counter))
	click_counter += 1
	print("Tkinter is easy to use!")


slogan = tk.Button(root,
									 textvariable=slogan_button_label,
									 command=write_slogan
									 )

slogan.pack(side=tk.LEFT)

quit_button = tk.Button(root,
												text="QUIT",
												background="RED",
												command=quit)
quit_button.pack(side=tk.LEFT)

tk.mainloop()
