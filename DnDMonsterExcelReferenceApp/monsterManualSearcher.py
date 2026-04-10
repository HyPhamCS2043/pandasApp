#Author: Hy Pham
import pandas as pd;
from functools import reduce

#pd.options.display.max_columns = None
#pd.options.display.max_rows = None
#pd.set_option('expand_frame_repr', False)
#print(pd.get_option("display.width"))

#Store the path to the excel file
excelFile = "..\MonsterManualExcel\D&D 5e Monster Manual by Ability Scores, Saves, Damage and Condition immunities.xlsx"

with pd.ExcelFile(excelFile) as manual:

    ## Begin Reading the excel file into dataframes ##
    #---------------------------------------------------------------------------------------------
    #Read into a dataframe the 1st few columns of the first sheet of the excel file, which contains all monsters' base stats. 
    baseStats = pd.read_excel(manual, sheet_name = 0, header = 0, usecols = "A:G")
    #Set the name of the index column to "Index"
    baseStats.index.name = "Index" 

    #Read into a dataframe the 1st two columns of the first sheet, along with some of the later columns that indicates the monsters' habitats.
    habitatStats = pd.read_excel(manual, sheet_name = 0, header = 0, usecols = "A, N:X").fillna("Unknown")
    habitatStats.index.name = "Index"

    #Read into a dataframe the 2nd sheet of the excel file, which contains all monsters' ability scores.
    abilityScores = pd.read_excel(manual, sheet_name = 1, header = 0, usecols = "A, H:M")
    abilityScores.index.name = "Index"

    #Read into a dataframe the 3rd sheet of the excel file, which contains all monsters' damage immunities.
    damageImmunities = pd.read_excel(manual, sheet_name = 2, header = 0, usecols = "A, H:T").fillna("None")
    damageImmunities.index.name = "Index"

    #Read into a dataframe the 4th sheet of the excel file, which contains all monsters' saving throw modifiers.
    savingThrows = pd.read_excel(manual, sheet_name = 3, header = 0, usecols = "A, H:M")
    savingThrows.index.name = "Index"

    #Read into a dataframe the 5th sheet of the excel file, which contains all monsters'condition immunities.
    conditionImmunities = pd.read_excel(manual, sheet_name = 4, header = 0, usecols = "A, H:T").fillna("None")
    conditionImmunities.index.name = "Index"

def randomMonster(df):
    #Returns a random row from the baseStats dataframe.
    return df.sample(n = 1)

def mainMenuOptions():
    #print out the main menu
    print("""------------------------------------------------------------\n
Main Menu:
      1. Retrieve the base stats of a random creature
      2. Search for a creature by name
      3. View Full Stats Tables
      4. Exit the program""")

def viewSpecificStatsMenu(name):

    ability = abilityScores[abilityScores["Name"] == name]
    saves = savingThrows[savingThrows["Name"] == name]
    dmgImmune = damageImmunities[damageImmunities["Name"] == name]
    condImmune = conditionImmunities[conditionImmunities["Name"] == name]
    habitat = habitatStats[habitatStats["Name"] == name]

    print("""
      1. View creature's Ability Score 
      2. View creature's Saving Throws 
      3. View creature's Damage Immunities 
      4. View creature's Condition Immunities 
      5. View creature's Habitats
      6. View ALL of the above 
      7. Return to Main Menu
    What would you like to do? (Enter the number corresponding to your choice):""")
    choice = input()
    print("\n------------------------------------------------------------")
    print("\n")
    while choice != 7:
        match choice:
            case "1":
                print("Ability Scores:\n")
                print(ability.to_string(justify = "center"))
            case "2":
                print("Saving Throw Modifiers:\n")
                print(saves.to_string(justify = "center"))
            case "3":
                print("Damage Immunity:\n")
                print(dmgImmune.to_string(justify = "center"))
            case "4":
                print("Condition Immunity:\n")
                print(condImmune.to_string(justify = "center"))
            case "5":
                print("Habitat:\n")
                print(habitat.to_string(justify = "center"))
            case "6":
                
                #merge behaves like SQL join. Joining these tables using the column Name as join key
                mergeddf = pd.merge(ability, saves, on = ['Name'], suffixes = ("", " save"))

                df_list = [mergeddf, dmgImmune, condImmune, habitat]

                allStats = reduce(lambda left, right: pd.merge(left, right, on = ["Name"], how = "outer"), df_list)

                print("Monster Name: " + allStats.iloc[0]["Name"] + "\n")

                print("Base Stats:\n" + baseStats[baseStats["Name"] == name].iloc[0, 2:8].to_string())

                print("\nAbility Scores:\n")
                print(allStats[["STR", "DEX", "CON", "INT", "WIS", "CHA"]].to_string(justify = "center"))

                print("\nSaving Throws:")
                print(allStats.iloc[0, 7:13].to_string())

                print("\nDamage Immunities:")
                print(allStats.iloc[0, 13:26].to_string())

                print("\nCondition Immunities:")
                print(allStats.iloc[0, 26:39].to_string())

                print("\nHabitat:")
                print(allStats.iloc[0, 39:50].to_string())

            case "7":
                break
            case _:
                print("Invalid input. Please enter a number between 1 and 7: ")
                break
        print("\n------------------------------------------------------------")
        print("""
      1. View creature's Ability Score 
      2. View creature's Saving Throws 
      3. View creature's Damage Immunities 
      4. View creature's Condition Immunities 
      5. View creature's habitat 
      6. View ALL of the above 
      7. Return to Main Menu
    What would you like to do? (Enter the number corresponding to your choice):""")
        choice = input()

def filterBaseStatsMenu(df):
    print("""\n\t\tFilter the table using the options below:
                1. Types
                2. Alignment
                3. Size
                4. AC
                5. HP
                6. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
    
    choice = input()
    print("\n------------------------------------------------------------")
    while choice != "6":
        match choice:
            case "1":
                print("\nFiltering by Types\n")
                print("Here are all the available creature's Types:\n")
                print("""
                        1. Aberration  5. Dragon      9. Fiend (Demon)    13. Monstrosity
                        2. Beast       6. Elemental   10. Fiend (Devil)   14. Ooze
                        3. Celestial   7. Fey         11. Giant           15. Plant
                        4. Construct   8. Fiend       12. Humanoid        16. Undead
                    (Enter 1 or more number corresponding to the Types, separated by a comma ',')""")
                
                types = input()
                typesToFilter = types.split(",")
                typeDF = pd.DataFrame({
                    "Types": [
                        "Aberration",
                        "Beast",
                        "Celestial",
                        "Construct",
                        "Dragon",
                        "Elemental",
                        "Fey",
                        "Fiend",
                        "Fiend (Demon)",
                        "Fiend (Devil)",
                        "Giant",
                        "Humanoid",
                        "Monstrosity",
                        "Ooze",
                        "Plant",
                        "Undead",],
                }, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
                
                filterList = []
                typeSearched = []

                for i in typesToFilter:
                    typeIndex = int(i.strip())
                    typeName = typeDF.loc[typeIndex]["Types"]

                    typeSearched.append(typeName)

                    filterPhrase = baseStats["Type"] == typeName
                    filterList.append(filterPhrase)
                
                for f in filterList:
                    print("--------------------------------------\n")
                    returnedDF = baseStats[f]
                    print(returnedDF.to_string(justify = "center"))

            case 6:
                break
    
        print("""\nFilter the Base Stats table using the options below:
                1. Types
                2. Alignment
                3. Size
                4. AC
                5. HP
                6. Return to Stats Table Menu
          (Enter the number corresponding to the filter option)\n""")
        choice = input()

print("""Welcome to the DnD Monster Manual Searcher!\n
------------------------------------------------------------\n
This program is designed to assist you with searching through
the DnD 5e Monster Manual excel file, which contains the stats 
of 691 creatures.\n
------------------------------------------------------------\n
Main Menu:
      1. Retrieve the base stats of a random creature
      2. Search for a creature by name
      3. View Full Stats Tables
      4. Exit the program
What would you like to do? (Enter the number corresponding to your choice):""")

#Main Menu I/O loop
inputChoice = input()

while inputChoice != "4":
    if inputChoice == "1":
        print("\nHere's a fun creature for you!\n")
        random = randomMonster(baseStats)
        print(random.to_string(justify = "center"))

        viewSpecificStatsMenu(random.iloc[0]["Name"])

    elif inputChoice == "2":
        monsterName = input("Please enter the name of the creature:\n")

        print("""Would you like to:
                1. Search for a creature with an exact name match
                2. Search for all creatures with a partial name match
              (Enter 1 for exact match, 2 for partial match)\n""")
        choice = input()
        if choice == "1":
            if monsterName in baseStats["Name"].values:
                print("Creature found!\n")
                print("\nHere are the base stats of the creature you are looking for:\n")

                #This line returns a DataFrame containing the row(s) where the "Name" column matches the monsterName variable
                #to_string() is used to print the DataFrame without the name and dtype at the bottom.
                print(baseStats[baseStats["Name"] == monsterName].to_string())
                
                viewSpecificStatsMenu(monsterName)

            else:
                print("Sorry, the creature you are looking for is not in the excel file.")
        elif choice == "2":
            if baseStats["Name"].str.contains(monsterName, case = False).any():
                print("Monster found!\n")
                print("\nHere are the base stats of the creature(s) you are looking for:\n")

                #This line returns a DataFrame containing the row(s) where the string in the "Name" column contains the monsterName variable (case insensitive)
                #to_string() is used to print the DataFrame without the name and dtype at the bottom.
                creatureDF = baseStats[baseStats["Name"].str.contains(monsterName, case = False)]

                print(creatureDF.to_string())
                num_rows = creatureDF.shape[0]

                if num_rows > 1:
                    print("\nType the index of the creature you would like to inspect:\n ")
                    indexChoice = int(input())
                    
                    while indexChoice:
                        if indexChoice in creatureDF.index:
                            #Retrieve creature's name based on the index collected from input.
                            creatureName = creatureDF.loc[indexChoice]["Name"]
                            print("\nCreature Chosen: " + creatureName + "\n")
                            viewSpecificStatsMenu(creatureName)
                            break
                        else: 
                            print("\nPlease input one of the index in the table above: \n")
                            indexChoice = int(input())
                else:
                    creatureName = creatureDF.iloc[0]["Name"]
                    viewSpecificStatsMenu(creatureName)

            else:
                print("Sorry, the creature you are looking for is not in the excel file.")
        else:
            print("Invalid input, please enter 1 or 2.")

    elif inputChoice == "3":
        print("Stat Tables Menu:\n")
        print("""
        1. Monsters by Base Stats
        2. Monsters by Ability Scores
        3. Monsters by Saving Throws
        4. Monsters by Condition Immunities
        5. Monsters by Damage Immunities
        6. Monsters by Habitats
        7. Back to Main Menu
        (Enter the number corresponding to the table you want to view)\n""")
        tableChoice = input()

        while tableChoice != "7":
            if tableChoice == "1":
                print("Monsters by Base Stats:\n")
                print(baseStats.to_string(justify = "center"))

                filterBaseStatsMenu(baseStats)

            elif tableChoice == "2":
                print("Monsters by Ability Scores:\n")
                print(abilityScores.to_string(justify = "center"))
            elif tableChoice == "3":
                print("Monsters by Saving Throws:\n")
                print(savingThrows.to_string(justify = "center"))
            elif tableChoice == "4":
                print("Monsters by Condition Immunities:\n")
                print(conditionImmunities.to_string(justify = "center"))
            elif tableChoice == "5":
                print("Monsters by Damage Immunities:\n")
                print(damageImmunities.to_string(justify = "center"))
            elif tableChoice == "6":
                print("Monsters by Habitats:\n")
                print(habitatStats.to_string(justify = "center"))
            else:
                print("Please enter a number from 1 to 7.")

            print("\n------------------------------------------------------------")
            print("""
        1. Monsters by Base Stats
        2. Monsters by Ability Scores
        3. Monsters by Saving Throws
        4. Monsters by Condition Immunities
        5. Monsters by Damage Immunities
        6. Monsters by Habitats
        7. Back to Main Menu
        (Enter the number corresponding to the table you want to view)\n""")
            tableChoice = input()
        
    else:
        print("Invalid input, please enter a number from 1 to 4.")

    mainMenuOptions()
    print("\nWhat would you like to do? (Enter the number corresponding to your choice):")
    inputChoice = input()

