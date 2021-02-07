import keyboard

def pressed(event):
    return [event.event_type, event.name]

while True:
    a = keyboard.on_press(pressed)
    print(a)