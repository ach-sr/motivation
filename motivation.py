# pyinstaller motivation.py --noconsole --onefile --add-data="motivation.ico;." --icon=motivation.ico --hidden-import sys --hidden-import os --hidden-import winshell --hidden-import pathlib
# pyinstaller --onefile --add-data="myicon.png;." myscript.py
import webbrowser
import keyboard
import os
import ctypes
import sys
import winshell
from winshell import shortcut, desktop, startup
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, filedialog

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    program_name = 'motivation.exe'
    program_path = ''
    downloads_path = str(os.path.join(Path.home(), 'Downloads'))
    desktop_path = winshell.desktop()

    for root, dirs, files in os.walk(desktop_path):
        for file in files:
            if file == program_name:
                found_path = os.path.join(root, file)
                program_path = found_path
                print('found in desktop: ', {program_path})
                break

    for root, dirs, files in os.walk(downloads_path):
        for file in files:
            if file == program_name:
                found_path = os.path.join(root, file)
                print('found in downloads: ', {program_path})
                program_path = found_path
                break

    print('creating shortcut in: ', {winshell.startup()})
    winshell.CreateShortcut(
        Path=os.path.join (winshell.startup (), "motivation.lnk"),
        Target=program_path,
        Arguments="",
        Description="motivation.exe shortcut",
        StartIn=program_path
    )
    print('created shortcut located at: ', {winshell.startup()})

    # SET THE HOTKEY HERE
    hotkey = 'alt+m'
    print(f'Wating for hotkey: {hotkey}')

    hotkey_state = False

    '''
    # Info to the user
    window = tk.Tk()
    window.title("motivation")
    window.geometry("400x300")
    
    top_label = tk.Label(window, text="GENERAL INSTRUCTIONS:")
    top_label.pack(side='top', pady=(0, 0))

    description = tk.Label(window, text="If you have downloaded the motivation.exe file to either your desktop or your downloads directories, a shortcut file has been made in the windows startup file. \nThis means that the program will autorun on windows startup.")
    description.pack(pady=0)

    window.mainloop()
    '''

    def motivation_hotkey():
        global hotkey_state
        if not hotkey_state:
            hotkey_state = True
            print("motivation_hotkey")
            webbrowser.open('https://www.youtube.com/watch?v=tYzMYcUty6s', new=1, autoraise=True)
            hotkey_state = False

    keyboard.add_hotkey(hotkey, motivation_hotkey)

    keyboard.wait()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)