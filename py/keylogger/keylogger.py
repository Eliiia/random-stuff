import keyboard
import json

presses = {}
#noregister = ["space", "shift", "right shift"]

def processPress(e):
    char = e.name
    print(char)
    
    if char not in presses.keys(): presses[char] = 1
    else: presses[char] += 1

    pass

def printData(): 
    print("Current key presses: ")
    print(presses)
    with open("out.json", "w") as f:
        json.dump(presses, f, indent=2)
    print("Also available in out.json")


keyboard.on_press(processPress)
keyboard.add_hotkey("shift+esc", printData)
keyboard.wait()