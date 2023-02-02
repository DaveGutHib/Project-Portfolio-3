from healthAmounts import healthAmount;


userCharacter = ""; 
# which character the user is playing as and wishing to check the damage for.
opponentCharacter = "";
# which character the user is doing damage to and calculating the remaining health for.
opponentStartingHealth = 0;
# global variable for the starting health of the opponent character. Will be a number between 850 and 1100.
comboCount= 0;
# increments as more attacks are performed in a row. As this variable increases, combo damage decreases.
healthCheck = 1;
# at regular points the opponent health will be checked and then multiplied by this number.
# at full health they will receive full damage (multiplied by 1), but this variable will decrease proportional to their health.
settingUp = True;
# condition intended to shut down the while loop
stillCalculating = True;
# condition intended to shut down the while loop
implementedCharacters = {"Ryu", "Chun-Li", "Deejay"};
# Unordered set containing characters currently with valid data for calculating

while settingUp:
        if userCharacter (input("Please enter your character name (Ryu, Deejay or Chun-Li)")) in implementedCharacters:
                #implment code to output list of character names

                if opponentCharacter(input("Please enter your opponent\'s character")) in 

                #implement code to output list of opponent names
        else: 
                print("Please enter a valid character name")



# ryu = {
#         "cl.lp":[30],
#         "cl.mp":[70],
#         "cl.hp":[100],
#         "cl.lk":[30],
#         "cl.mk":[80],
#         "cl.hk":[40,70],
#         "s.lp":[30],
#         "s.mp":[80],
#         "s.hp":[120],
#         "s.lk":[40],
#         "s.mk":[80],
#         "s.hk":[110],
#         "cr.lp":[30],
#         "cr.mp":[60],
#         "cr.hp":[90],
#         "cr.lk":[20],
#         "cr.mk":[60],
#         "cr.hk":[90],
#         "f.mp":[30,50],
#         "f.hp":[40,60],
#         "fa lv1":[60],
#         "fa lv2": [80],
#         "fa lv3":[140],
#         "f.throw": [130],
#         "b.throw":[130],
#         "hado":[70],
#         "hado ex": [50,50],
#         "srk lp":[100],
#         "srk mp":[80,50],
#         "srk hp":[160],
#         "srk ex":[80,60],
#         "tatsu lk": [100],
#         "tatsu mk": [110],
#         "tatsu hk":[120],
#         "tatsu ex":[30,30,30,30,40],
#         "air tatsu lk":[70],
#         "air tatsu mk":[80],
#         "air tatsu hk":[90],
#         "air tatsu ex":[40,40,40,40,40],
#         "super": [50,50,50,50,100],
#         "ultra1":[42,42,42,42,42,42,42,75],
#         "ultra2": [270,233],
#     	 }

user_input= str(input("Please enter an attack name:  "));
print(user_input);
