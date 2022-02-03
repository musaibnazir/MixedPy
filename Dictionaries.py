#dictionary

states={'CA':'California','WA':'Washington','CO':'Colorato'}

for key,value in states.items():
    print(key+'-->'+value)

states.update({'IN':'Indiana'})
print(str(states))


del states['CA']
print(str(states))


states.update({'Fl':'Florida'})
print(str(states))
