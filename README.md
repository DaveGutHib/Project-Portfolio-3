# Project-Portfolio-3
 
# Ultra Street Fighter 4 damage calculator

![Banner image of game](/assets/images/Ultra_SF4_Banner.jpg)

Street Fighter 4 is a game that released in 2008 in arcades to worldwide positive acclaim and ushered in a new era of growth and interest in the entire genre of fighting games that persists to this day.

It's final version, Ultra Street Fighter 4, released on Arcade machines, the Xbox 360 and the Playstation 3 in 2014, and remains a fan favourite to this day.

The core of the game play revolves around damaging your opponent to deplete their health (sometimes referred to as HP or Health Points).
![Example of an Ultra combo](assets/images/combo_sako_gif.gif)
_The Legendary "Sako Combo"_


There are only two win conditions:
1. Deal enough damage to fully deplete your opponents health
![Example of an Ultra combo](assets/images/combo_guy_ultra_gif.gif)
_This one is surprisingly easy to calculate_
<br>
2. There is a time limit per round. If nobody has had their health fully depleted when the time runs out, whoever has a higher percentage of their total health remaining wins. Most of the time this means whoever deals the most damage wins.
![Example of a time over](assets/images/PLACEHOLDER.gif)






Despite the fact that **damage** is absolutely key to every win condition in the game, there are no calculators online or on the mobile app stores to allow players to work out how much total damage a particular combination of attacks (or "combo") would do. Having such a thing would help players to think about and optimise what they do when they're not playing.

![Research searching for an existing calculator 1](assets/images/research_searching_for_existing_calculator.png)
_On first search, only one calculator app shows up in the search results_

![Research searching for an existing calculator 2](assets/images/research_searching_for_existing_calculator_2.png)
_This leads to a reddit topic, which points to a google play store link_

![Research searching for an existing calculator 3](assets/images/research_searching_for_existing_calculator_3.png)
_This link is dead_

![Research searching for an existing calculator 4](assets/images/research_searching_for_existing_calculator_4.png)
_Last developer comment was 9 years ago (2014 at time of writing). It is safe to assume the project is dead_


A calculator still has value today even when playing the game, because health values are obfuscated behind a graphical _"HP bar"_ which, as it depletes, decreases in length and changes from yellow to red. Excluding when players have 100% health, and 0% health (when they are defeated), players can never actually know exactly how much health they currently have.
![HP Bar Screenshot](assets/images/game_screenshot_hp_bars.png)
_A full length health bar usually represents 1000 health. Ryu probably has 850 health remaining. Abel maybe has 300? Even in game it's not very clear_


## Features
---


## Existing features


## Future features



## Design
---
Code Logic on Paper

![Code logic on paper ](assets/images/paper-planning-document-logic.jpg)

![Additional planning on paper ](assets/images/paper-planning-document-to-do-list.jpg)

### Data Formatting

The damage numbers are displayed as such:

"damage": "60x5*173",

But for convenience it would better if they were displayed as such:

"damage": [60,60,60,60,60,173]

Some damage is represented bafflingly confusingly

"damage": "270*38x4*50x3[270*233]"


## Testing
---



## References

Ultra Street Fighter 4 Frame Data source #1 by [Vertigo] (https://github.com/vertigo65536/frame-data/tree/master/sf4) (used extensively)


Ultra Street Fighter 4 Frame Data source #2 by [jpgnotgif](https://github.com/jpgnotgif/usf4-frame-data) (not used, but checked in the hopes of better formatted data)

FAT frame data app Github page by [D4rkOnion](https://github.com/D4RKONION/FAT) (not used, but checked)

