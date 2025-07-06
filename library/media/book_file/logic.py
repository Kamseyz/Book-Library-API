def logic():
    y = input('What is your name?: ')
    while True:
        x = input("Say something: ").strip()
        if x == 'Hi' or x == "Hello":
            return f'Hello there {y}'
        elif x == 'bye':
            return f'Goodbye {y}'
        elif x == '':
            return f'You said nothing {y}'
        else:
            return "i dont't understand"
    
print(logic())
    
    
    
