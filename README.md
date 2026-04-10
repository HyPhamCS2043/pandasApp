# Repo Description
A repo to learn the Python library pandas and to create a program that implements pandas

# DnD Monster Manual Stats Referencer
Have you ever find yourself wondering if a Crab is immune to Lightning damage? Or if a Dracolich (a dragon that is lich)
is immune to Petrification? Ever spent hours going in between different forums page just to find out if a Swarm of Rats can indeed be Restrained? 
    
Well then, the **DnD Monster Manual Stats Referencer (Python Edition)** is the software for you! Utilizing pandas, the program helps any Python enthusiast parses through a DnD Monster Manual Excel that contains a whopping 691 creatures from the DnD 5E Monster Manual. The program provides a textual terminal interface with different filtering options that let you quickly search through the Excel for the information that you want. 


# How to set up

## Installing Packages

The primary package that the DnD Monster Manual Stats Referencer uses is **pandas**.  
Outside of this, the program also uses openpyxl to access the Excel sheet.

To download the packages, go your IDE of choice, and type:

    pip3 install pandas
Once pandas is successfully installed.

    pip3 install openpyxl

Once these are successfully installed, proceed to the next step.

# Running the Program

## 1. Unzip the zip file
Navigate to where you download the zip file.  
Right click on the file, then choose Extract All. Choose a directory of your choice to extract the file.  


## 2. Navigate to the file directory
Navigate to where you extracted the file in your terminal.  
    
    cd path/to/where/you/extracted/the/file

## 3. Run "monsterManualSearcher.py"
In your terminal, run the file "monsterManualSearcher.py" with:

    python3 monsterManualSearcher.py

## 4. Use the Program
The interface below should appear in your terminal:

    Welcome to the DnD Monster Manual Searcher!\n
    ---------------------------------------------------------
    This program is designed to assist you with searching through
    the DnD 5e Monster Manual excel file, which contains the stats 
    of 691 creatures.
    --------------------------------------------------------
    MAIN MENU:
        1. Retrieve the base stats of a random creature
        2. Search for a creature by name
        3. View Full Stats Tables
        4. Exit the program
    What would you like to do? (Enter the number corresponding to your choice):

To navigate between the menu, respond to the command prompt by typing the number that corresponds to the menu option that you would like to select, then pressing **Enter**.  
For example, typing "1" then pressing **Enter** will bring up:

![Random Creature Menu Interface](https://github.com/HyPhamCS2043/pandasApp/blob/main/DnDReferencer1.jpg)

To learn more about the creature's Ability Score, for example, type "1" and press [Enter] again!
The following screen should appears: 

![Ability Score output](https://github.com/HyPhamCS2043/pandasApp/blob/main/DnDReferencer2.jpg)

The entire program can be used with keyboard inputs alone. Have fun exploring the different menu branches! The majority of inputs required are integers, or in some cases, multiple integers separated by a comma.

