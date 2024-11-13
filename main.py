import tkinter as tk
from tkinter import ttk
import subprocess

game1 = 'sam1.py'

def run_game1():
    subprocess.Popen(['python', 'slot_game.py'])
    
def run_game2():
    subprocess.Popen(['python', 'office_run_game.py'])

def run_game3():
    subprocess.Popen(['python', 'space.py'])

r = tk.Tk()
w, h = r.winfo_screenwidth(), r.winfo_screenheight()
r.title('Games')
r.maxsize(w,h)
r.configure(bg='black')
r.geometry("830x800")
# r.state(max)

# Create a canvas widget
canvas = tk.Canvas(r, bg='black')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(r, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
frame = tk.Frame(canvas, bg='black')
canvas.create_window((0, 0), window=frame, anchor='nw')

top1 = tk.PhotoImage(file='D:\\slot_machine\\new\\images\\top.png')
tp1 = tk.Label(frame, image=top1, bg='black')
tp1.pack(fill='both', side='top')

im1= tk.PhotoImage(file='D:\\slot_machine\\new\\New folder\\slots.png')
im2 = tk.PhotoImage(file='D:\\slot_machine\\new\\New folder\\office_jump.png')
im3 = tk.PhotoImage(file='D:\\slot_machine\\new\\images\\space_shooter.png')

button1 = tk.Button(frame, text='SLOT', command=run_game1, bg='black', fg='white', image=im1, compound='top')
button_game = tk.Button(frame, text="Office Jump", bg='black', fg='white', command=run_game2, image=im2, compound='top')
button_game2 = tk.Button(frame, text="Space Shooter", bg='black', fg='white', command=run_game3, image=im3, compound='top')

button2 = tk.Button(frame, text='EXIT ', command=r.quit, bg='black', fg='white')

button1.pack(fill='both', side='top', padx=10, pady=5)
button_game.pack(fill='both', side='top', padx=10, pady=5)
button_game2.pack(fill='both', padx=10, pady=5, side='top')
button2.pack(fill='both')

# Update the scroll region
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

r.mainloop()
