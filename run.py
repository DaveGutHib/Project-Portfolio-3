userCharacter = ""; 
# which character the user is playing as and wishing to check the damage for.
opponentStartingHealth = 0;
# global variable for the starting health of the opponent character. Will be a number between 850 and 1100.
comboCount= 0;
# increments as more attacks are performed in a row. As this variable increases, combo damage decreases.
healthCheck = 1;
# at regular points the opponent health will be checked and then multiplied by this number.
# at full health they will receive full damage (multiplied by 1), but this variable will decrease proportional to their health.

