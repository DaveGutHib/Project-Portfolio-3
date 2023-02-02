# import json

# a = open('/assets/jsons/RyuCopy.json');

# data = json.load(x)

# for i in data['damage']:
#     print(i)

# a.close()
x=0
total = 0
comboCount = 0
damageScaling = 1.0


while x != "q":
    x = input("Enter a number (press q to quit)")
    comboCount = comboCount + 1
    if comboCount >= 10:
        damageScaling = 0.1
    elif comboCount == 9:
        damageScaling = 0.2
    elif comboCount == 8:
        damageScaling = 0.3
    elif comboCount == 7:
        damageScaling = 0.4
    elif comboCount == 6:
        damageScaling = 0.5
    elif comboCount == 5:
        damageScaling = 0.6
    elif comboCount == 4:
        damageScaling = 0.7
    elif comboCount == 3:
        damageScaling = 0.8
    else:
        pass
    print("Combo Count", comboCount)
    print("X equals", x)
    print("Previous total", total)
    total = total + (damageScaling * int(x))
    print("New total", total)
else: print("Thank you for playing. Final total is ", total)