# Main module being run as a Tkinter program for user friendly GUI.
import tkinter as tk
import num_stud_ute as nsu
import odd_int as oi
import palindrome_number as pn
import two_sum as ts

root = tk.Tk()

message = tk.Label(root, text = "Welcome to " \
"the Tkinter Python GUI for Leetcode programs.\n" \
"Click a button to run a program.")
message.pack()

button_num_stud = tk.Button(root, text = "Num Stud UTE",
                             command = nsu.unable_to_eat)
button_odd_int = tk.Button(root, text = "Odd Int",
                             command = oi.run_program)
button_pal_num = tk.Button(root, text = "Palindrome Number",
                             command = pn.run_program)
button_two_sum = tk.Button(root, text = "Two Sum",
                             command = ts.run_program)

button_num_stud.pack(padx = 30, pady = 30)
button_odd_int.pack(padx = 30, pady = 30)
button_pal_num.pack(padx = 30, ady = 30)
button_two_sum.pack(padx = 30, pady = 30)

root.mainloop()