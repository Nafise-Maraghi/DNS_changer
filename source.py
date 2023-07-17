from tkinter import *
import tkinter.ttk
import subprocess

# to .exe
# pip intsall pyinstaller
# pyinstaller --onefile -w filename


def set():
    try:
        primary_dns = '''netsh interface ip set dns name="Wi-Fi" source="static" address="178.22.122.10'''
        alternative_dns = '''netsh interface ip add dns name="Wi-Fi" addr="185.51.200.2" index=2'''
        subprocess.run(primary_dns)
        subprocess.run(alternative_dns)
        set_label("SET")
        print("S")

    except Exception as e:
        set_label(e) 


def flush():
    try:
        no_dns = '''netsh interface ip set dns "Wi-Fi" dhcp'''
        subprocess.run(no_dns)
        set_label("FLUSHED")
        print("F")

    except Exception as e:
        set_label(e)


def set_label(message):
    Label(root, text=message, bg='white', width=29).place(x=1, y=20)


root = Tk()
root.title('DNS')
root.configure(bg='white')
root.geometry('220x100')
root.resizable(False, False)

# note: use 'command=lambda: func()' or 'command=func' if func() has no arguments. 'command = func()' is incorrect.
# Set button
tkinter.ttk.Button(root, text='Set', command=set).place(x=20, y=50)
# Flush button
tkinter.ttk.Button(root, text='Flush', command=flush).place(x=120, y=50)

root.mainloop()