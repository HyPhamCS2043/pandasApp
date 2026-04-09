#Author: Hy Pham
import pandas as pd;

#Store the path to the excel file
excelFile = "..\MonsterManualExcel\D&D 5e Monster Manual by Ability Scores, Saves, Damage and Condition immunities.xlsx"

with pd.ExcelFile(excelFile) as manual:

    ## Begin Reading the excel file into dataframes ##
    #---------------------------------------------------------------------------------------------
    #Read into a dataframe the 1st few columns of the first sheet of the excel file, which contains all monsters' base stats. 
    baseStats = pd.read_excel(manual, sheet_name = 0, header = 0, usecols = "A:G")
    #Set the name of the index column to "Index"
    baseStats.index.name = "Index" 

    #Read into a dataframe the 1st two columns of the first sheet, along with some of the later columns that indicates the monsters' biomes.
    biomeStats = pd.read_excel(manual, sheet_name = 0, header = 0, usecols = "A, N:X")
    biomeStats.index.name = "Index"

    #Read into a dataframe the 2nd sheet of the excel file, which contains all monsters' ability scores.
    abilityScores = pd.read_excel(manual, sheet_name = 1, header = 0, usecols = "A, H:M")
    abilityScores.index.name = "Index"

    #Read into a dataframe the 3rd sheet of the excel file, which contains all monsters' damage immunities.
    damageImmunities = pd.read_excel(manual, sheet_name = 2, header = 0, usecols = "A, H:T")
    damageImmunities.index.name = "Index"

    #Read into a dataframe the 4th sheet of the excel file, which contains all monsters' saving throw modifiers.
    savingThrows = pd.read_excel(manual, sheet_name = 3, header = 0, usecols = "A, H:M")
    savingThrows.index.name = "Index"

    #Read into a dataframe the 5th sheet of the excel file, which contains all monsters'condition immunities.
    conditionImmunities = pd.read_excel(manual, sheet_name = 4, header = 0, usecols = "A, H:T")
    conditionImmunities.index.name = "Index"

def randomMonster(df):
    #Returns a random row from the baseStats dataframe.
    return df.sample(n = 1)

def mainMenuOptions():
    #print out the main menu
    print("""------------------------------------------------------------\n
Main Menu:
      1. Retrieve the base stats of a random monster
      2. Search for a monster by name
      3. View Full Statistic Tables
      4. Exit the program""")

#pd.options.display.max_columns = None
#pd.options.display.max_rows = None
#pd.set_option('expand_frame_repr', False)
#print(pd.get_option("display.width"))
print("""Welcome to the DnD Monster Manual Searcher!\n
------------------------------------------------------------\n
This program is designed to assist you with searching through
the DnD 5e Monster Manual excel file, which contains the stats 
of 691 monsters.\n
------------------------------------------------------------\n
Main Menu:
      1. Retrieve the base stats of a random monster
      2. Search for a monster by name
      3. View Full Statistic Tables
      4. Exit the program
What would you like to do? (Enter the number corresponding to your choice):""")

#Main Menu I/O loop
inputChoice = input()

while inputChoice != "4":
    if inputChoice == "1":
        print("\nHere's a fun creature for you!\n")
        print(randomMonster(baseStats).to_string())

    elif inputChoice == "2":
        monsterName = input("Please enter the name of the monster:\n")

        print("""Would you like to:
                1. Search for a monster with an exact name match
                2. Search for all monsters with a partial name match
              (Enter 1 for exact match, 2 for partial match)\n""")
        choice = input()
        if choice == "1":
            if monsterName in baseStats["Name"].values:
                print("Monster found!\n")
                print("\nHere are the base stats of the monster you are looking for:\n")

                #This line returns a DataFrame containing the row(s) where the "Name" column matches the monsterName variable
                #to_string() is used to print the DataFrame without the name and dtype at the bottom.
                print(baseStats[baseStats["Name"] == monsterName].to_string())

            else:
                print("Sorry, the monster you are looking for is not in the excel file.")
        elif choice == "2":
            if baseStats["Name"].str.contains(monsterName, case = False).any():
                print("Monster found!\n")
                print("\nHere are the base stats of the monster(s) you are looking for:\n")

                #This line returns a DataFrame containing the row(s) where the string in the "Name" column contains the monsterName variable (case insensitive)
                #to_string() is used to print the DataFrame without the name and dtype at the bottom.
                print(baseStats[baseStats["Name"].str.contains(monsterName, case = False)].to_string())
                #print("Testing dataframe:\n")
                #print(baseStats[baseStats["Name"].str.contains(monsterName, case = False)].iloc[0].to_string())
            else:
                print("Sorry, the monster you are looking for is not in the excel file.")
        else:
            print("Invalid input, please enter 1 or 2.")

    elif inputChoice == "3":
        print("Below are all the stats tables:\n")
        print("""
        1. Monsters by Base Stats
        2. Monsters by Ability Scores
        3. Monsters by Saving Throws
        4. Monsters by Condition Immunities
        5. Monsters by Damage Immunities
        6. Monsters by Biomes
        7. Back to Main Menu
        (Enter the number corresponding to the table you want to view)\n""")
        tableChoice = input()

        if tableChoice == "1":
            print("Monsters by Base Stats:\n")
            print(baseStats.to_string(justify = "center"))
        elif tableChoice == "2":
            print("Monsters by Ability Scores:\n")
            print(abilityScores.to_string(justify = "center"))
        elif tableChoice == "3":
            print("Monsters by Saving Throws:\n")
            print(savingThrows.to_string(justify = "center"))
        elif tableChoice == "4":
            print("Monsters by Condition Immunities:\n")
            print(conditionImmunities.to_string(justify = "center"))
            print("""\n
                  ------------------------------------------------------------------------------------
                  NOTE: If the table is too big, zoom out by clicking [CTRL] and [-] at the same time.
                  ------------------------------------------------------------------------------------""")
        elif tableChoice == "5":
            print("Monsters by Damage Immunities:\n")
            print(damageImmunities.to_string(justify = "center"))
        elif tableChoice == "6":
            print("Monsters by Biomes:\n")
            print(biomeStats.to_string(justify = "center"))
        elif tableChoice == "7":
            mainMenuOptions()
        else:
            print("Please enter a number from 1 to 7.")
    else:
        print("Invalid input, please enter a number from 1 to 4.")

    #mainMenuOptions()
    print("\nWhat would you like to do? (Enter the number corresponding to your choice):")
    inputChoice = input()

