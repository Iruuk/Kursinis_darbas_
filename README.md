 Kursinis_darbas_

## Introduction

### Goal of the coursework

The goal of his course work is to write a program using Phyton programing language, during this process learn how to write working code using Phyton programing language basics and how to apply SOLID principles.

### Topic

Topic of my course work is *Dungeons and Dragons (DnD) Helper*. This program should make creating DnD game characters easier, especially for beginners.

### How to run the program

The program working is based on entering your choices and data. While running program you can start by entering one of the choices *Make* or *Exit*:

+ By entering *Make* user will start creating character
+ By entering *Exit* user will close program

### How to use the program

If user have chosen *Make*, then he enters his data this way:

+ Name of user
+ Name of character
+ Level which he wants to play (from 1 to 3)
+ Race of his character (described in *Player's Handbook*)
+ Class he wants to play (all classes available in *Player's Handbook*, plus additional artificial and bloodhunter classes)

After collecting this info program gives two options to create stats for character (1. **Four dice method**, 2. **Default number method**). By entering *1* He will use **Four dice method**, by entering *2* - **Default number method**.

Last but not least program will ask to enter armor and weapon to choose (armors and objects available are only from *Player's Handbook*). 

After that user would have option to add items to his inventory:

+ By entering *1* he then can enter any item he wants to inventory (action is repeated until exit)
+ By entering *2* he will exit inventory

According to data entered and choices made program will print in output file:

+ Player's name
+ Character's name
+ Level
+ Race
+ Class
+ Stats and modifiers
+ Hit points
+ Inventory

## The analysis of the code

### Reading from CSV file

Reading from fail is runed by class **ReadInputFile**. This class reads information using *pandas* library from CSV file *Input*.

<img src="images/input file screenshot.PNG" width="400" height="auto">

1. Race
2. class
3. Abilities
4. Armor
5. Weapon

Then creates valid object lists for

+ Race
+ Class
+ Stats names
+ Armor
+ Weapon

<img src="images/Reading from file screenshot.PNG" width="400" height="auto">

### class **GetInfo**

In class **GetInfo** program is returning valid lists of Races, Classes and Level from class **ReadInputFile**. Then through method *player_name* it gets name of the user and cheks is it a word in method *_is_valid_name*.
Method *character_name* does not check answer for being word, because some of fictional names may contain letters of symbols, for example *C3PO*.
All other methods (*level*,*race* and *class_choice*), are checking the information entered by user for being valid in higher mentioned lists.

<img src="images/GetInfo screenshot.PNG" width="400" height="auto">

### class **FourDiceMethod**

If user decided to make this stats using *Four dice method*, the class **FourDiceMethod** is runed. First this class creates a list *self._abilities* in which later stats will be written. Then in method *method* program creates 4 random numbers from 1 to 6, append them to temporary list *stats* and sorts them from smaller to bigger. After finishing this process program deletes smallest number and sums ones that left.
Last but not least module *add_stats* appends created stats to list *self._abilities* and also creates modifier using formula ((stat - 10)/2) and also adding this number to list *self._modifiers*

<img src="images/FourDiceMethod screenshot.PNG" width="400" height="auto">

### class **DefaultStatsMethod**

If user have chosen *Default stats method*, class **DefaultStatsMethod** is runed. In this situation program will use values (15, 14, 13, 12, 10, 8).
In method *insert stats* I used while loop, where player can choose which number he wants to choose for each ability (abilities are read from CSV file and returned as *valid_stats*). Then the chosen number is deleted from list *self._stats* and loop repeats until list *self._stats* is empty.
Later similar as in **FourDiceMethod**  class, values are added to the list and modifiers are counted.

<img src="images/DefaultStatsMethod screenshot.PNG" width="400" height="auto">

### class **Health**

In this class program counts how many hit points your character have depending on your class and level.

First program finds amount of health for first level character in method *hit_dices* by using the character class that user have chosen.

Depending on which level user is playing the random values from 1 to hit dice number will be added to characters hit points.

<img src="images/Health screenshot.PNG" width="400" height="auto">

### class **Inventory**

Class **Inventory** contains 3 main parts:

1. Method *armour* saves users chosen armor and writes it down to list *self._inventory_items*.

2. Method *weapon* makes everything the same way as method *armour*, except it saves the choice of weapon.

3. Method *inventory* opens a while loop in which user can choose to enter item or exit. If entered *1* user can write down any item he wants and it will be added to inventory (program also checks if the entered item is a word or not, if it is not a word, it prints *Invalid item. Please enter a word.*). If entered *2* while loop is closed, same appeals the inventory.

<img src="images/Inventory screenshot.PNG" width="400" height="auto">

### class **Write_into_file**

This class writes data counted or collected from the classes and appends it down into output file.

### class **Runner**

It opens a while loop, where if user enters *Make*, it will activate all the classes. Beginning from **GetInfo** and immediately writing them down to output file. Then it gives a choice for user what stat method he wants to use. Chosen method describes a class **FourDiceMethod** or **DefaultStatsMethod** using *if*. Later class is runed and data is written into output file. Last but not least classes **Health** and **Inventory** are runed. Program also opens one *for* to describe how many times should program write items to inventory (cycle *for* loop number depends on number of entered items in class **Inventory** method *inventory*). final touch is writing few *\n* signs to create a space between two characters.
If user enters *Exit* - code is closed.

<img src="images/runner screenshot.PNG" width="400" height="auto">

## OOP pillars

### *Abstraction*

**CharacterStats** is an abstract base class. It contains method *calculate_stats*, that allows for different stats counting ways to enforce a common interface.

<img src="images/Abstract.PNG" width="400" height="auto">

### *Polymorphism*

Both classes **CaracterStats** and **FourDiceMethod** uses the same method *calcuate_stats*, but the itself in each of this classes executes different tasks.

<img src="images/Abstract.PNG" width="400" height="auto">

<img src="images/polymorphism.PNG" width="400" height="auto">


### *Inheritance*

Both classes **FourDiceMethod** and **DefaultStatsMethod** are inheriting from class. **CharacterStats**

<img src="images/Inheritance1.PNG" width="400" height="auto">

### *Encapsulation*

In this example objects are encapsulated.

<img src="images/Encapsulation.PNG" width="400" height="auto">

## Results and conclusions

+ I learned how to create CSV files and use them in programing language Python
+ I was able to create working program using Python programing language, implied all OOP pillars, and have not break SOLID principles
+ It was hard to run program which reads form CSV file for the first time
+ Writing a part of code which gives ability for user to choose which stats creating method he wants to use was an issue

All in all I successed in writing working code. During this course work I have used knowledge got on lectures in practice.

This program can be developed in the future by improving stats calculator adding racial traits. Also it would be helpful for new players to get their all skills, attacks and subclasses (based on their race, class and level) written on the output text.
