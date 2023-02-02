# import json

# a = open('/assets/jsons/RyuCopy.json');

# data = json.load(x)

# for i in data['damage']:
#     print(i)

# a.close()
x=0
total = 0
comboCount = 0


while x != "q":
    x = input("Enter a number (press q to quit)")
    comboCount = comboCount + 1
    print("Combo Count", comboCount)
    print("X equals", x)
    print("Previous total", total)
    total = total + int(x)
    print("New total", total)
else: print("Thank you for playing. Final total is ", total)