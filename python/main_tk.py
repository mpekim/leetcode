# Main module being run as a Tkinter program for user friendly GUI.
import tkinter as tk
import num_stud_ute as nsu
import odd_int as oi
import palindrome_number as pn
import two_sum as ts

root = tk.Tk()
root.geometry("350x125")

message = tk.Label(root, text = "Welcome to " \
"the Tkinter Python GUI for Leetcode programs.\n" \
"Click a button to run a program.")
message.pack()

button_num_stud = tk.Button(root, text = "Num Stud UTE",
bg = "#FF0000", fg = "#000000", command = nsu.unable_to_eat)
button_odd_int = tk.Button(root, text = "Odd Int",
bg = "#FFFF00", fg = "#000000", command = oi.run_program)
button_pal_num = tk.Button(root, text = "Palindrome Number", 
bg = "#00AAFF", fg = "#000000", command = pn.run_program)
button_two_sum = tk.Button(root, text = "Two Sum",
bg = "#32CD32", fg = "#000000", command = ts.run_program)

button_num_stud.pack()
button_num_stud.place(x = 20, y = 40)
button_odd_int.pack()
button_odd_int.place(x = 210, y = 40)
button_pal_num.pack()
button_pal_num.place(x = 20, y = 90)
button_two_sum.pack()
button_two_sum.place(x = 210, y = 90)

root.mainloop()