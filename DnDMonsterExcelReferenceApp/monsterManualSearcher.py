#Author: Hy Pham
import pandas as pd;
from functools import reduce

pd.options.display.max_columns = None
pd.options.display.max_rows = None
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
MAIN MENU:
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

def numericFilterMenu(filterName, colName, df):
    print("Select filter option from the list below:\n")
    print("""
                    1. Equals (=) 
                    2. Not Equal (!=)
                    3. Greater Than (>)
                    4. Greater Than or Equal to (>=)
                    5. Less Than(<)
                    6. Less Than or Equal to (<=)
                    7. Between
                    8. Return to Filter Menu
                    (Enter a number between 1 and 7, corresponding to your choice of filter)\n""")
                
    filterChoice = input()
    while filterChoice != "8":
        match filterChoice:
            case "1":
                print("\n-------------------------------------------\n")
                print("Show entries where " + filterName + " is equal to: ")
                numToFind = float(input())

                rowsReturned = df[df[colName] == numToFind]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "2":
                print("\n-------------------------------------------\n")
                print("Show entries where " + filterName + " is NOT equal to: ")
                numToFind = float(input())

                rowsReturned = df[df[colName] != numToFind]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    rowsReturned = rowsReturned.sort_values(by = colName, ascending = True)
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "3":
                print("\n-------------------------------------------\n")
                print("Show entries where " + filterName + " is greater than: ")
                numToFind = float(input())

                rowsReturned = df[df[colName] > numToFind]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    rowsReturned = rowsReturned.sort_values(by = colName, ascending = True)
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "4":
                print("\n-------------------------------------------\n")
                print("Show entries where " + filterName + " is greater than or equal to: ")
                numToFind = float(input())

                rowsReturned = df[df[colName] >= numToFind]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    rowsReturned = rowsReturned.sort_values(by = colName, ascending = True)
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "5":
                print("\n-------------------------------------------\n")
                print("Show entries where " + filterName + " is less than: ")
                numToFind = float(input())

                rowsReturned = df[df[colName] < numToFind]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    rowsReturned = rowsReturned.sort_values(by = colName, ascending = True)
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "6": 
                print("\n-------------------------------------------\n")
                print("Show entries where " + filterName + " is less than or equal to: ")
                numToFind = float(input())

                rowsReturned = df[df[colName] <= numToFind]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    rowsReturned = rowsReturned.sort_values(by = colName, ascending = True)
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "7":
                print("\n-------------------------------------------\n")

                print("Show entries where " + filterName + " is between: ")
                lowerBound = float(input())
                print("AND")
                upperBound = float(input())

                rowsReturned = df[(df[colName] >= lowerBound) & (df[colName] <= upperBound)]

                if rowsReturned.empty:
                    print("Sorry, there is no creature that satisfies your filter.\n")
                else:
                    rowsReturned = rowsReturned.sort_values(by = colName, ascending = True)
                    print("Here are the results (sorted by " + colName + " in ascending order):\n")
                    print(rowsReturned.to_string(justify = "center"))
                print("\n-------------------------------------------\n")

            case "8":
                break
            case _:
                print("Sorry, " + filterChoice + " is not one of the options offered.\n")
                            
        print("Select filter option from the list below:\n")
        print("""
                    1. Equals (=) 
                    2. Not Equal (!=)
                    3. Greater Than (>)
                    4. Greater Than or Equal to (>=)
                    5. Less Than(<)
                    6. Less Than or Equal to (<=)
                    7. Between
                    8. Return to Filter Menu
                    (Enter a number between 1 and 7, corresponding to your choice of filter)\n""")
        filterChoice = input()

def filterBaseStatsMenu():
    print("=====================================")
    print("Base Stats Filter Menu")
    print("""\n\t\tFilter the table using the options below:
                1. Types
                2. Alignment
                3. Size
                4. CR (Challenge Rating)
                5. AC (Armor Class)
                6. HP (Health Point)
                7. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
    
    choice = input()
    print("\n------------------------------------------------------------")
    while choice != "7":
        match choice:
            case "1":
                print("\nFiltering by Types\n")
                print("Here are all the available creature's Types:\n")
                print("""
                        1. Aberration  5. Dragon      9. Fiend (Demon)    13. Monstrosity
                        2. Beast       6. Elemental   10. Fiend (Devil)   14. Ooze
                        3. Celestial   7. Fey         11. Giant           15. Plant
                        4. Construct   8. Fiend       12. Humanoid        16. Undead
                    (Enter 1 or more numbers corresponding to the Types, separated by a comma ',')""")
                
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

                    if typeIndex in typeDF.index:
                        typeName = typeDF.loc[typeIndex]["Types"]
                    else:
                        print("Sorry, " + i + " is not part of the choices offered.")
                        break

                    typeSearched.append(typeName)

                    filterPhrase = baseStats["Type"] == typeName
                    filterList.append(filterPhrase)
                
                for f in filterList:
                    print("--------------------------------------\n")
                    returnedDF = baseStats[f]
                    print(returnedDF.to_string(justify = "center"))
            case "2":
                print("\nFiltering by Alignments\n")
                print("Here are all the available creature's Alignments:\n")
                print("""
                        1. ANY                                      10. LG (Lawful Good)
                        2. ANY EVIL                                 11. LN (Lawful Neutral)
                        3. C (Chaotic)                              12. N (Neutral)
                        4. CE (Chaotic Evil)                        13. NE (Neutral Evil)   
                        5. CG (Chaotic Good)                        14. NG (Neutral Good)
                        6. CG (Chaotic Good) OR NE (Neutral Evil)   15. NOT GOOD
                        7. CN (Chaotic Neutral)                     16. NOT LAWFUL
                        8. E (Evil)                                 17. Same as Eidolon
                        9. LE (Lawful Evil)                         18. U (Unaligned)
                    (Enter 1 or more numbers corresponding to the Alignments, separated by a comma ',')""")
                
                align = input()
                alignsToFilter = align.split(",")
                alignDF = pd.DataFrame({
                    "ALIGNMENT": [
                        "ANY",
                        "ANY EVIL",
                        "C",
                        "CE",
                        "CG",
                        "CG OR NE",
                        "CN",
                        "E",
                        "LE",
                        "LG",
                        "LN",
                        "N",
                        "NE",
                        "NG",
                        "NOT GOOD",
                        "NOT LAWFUL",
                        "Same as Eidolon",
                        "U",],
                }, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
                
                filterList = []
                alignSearched = []

                for i in alignsToFilter:
                    alignIndex = int(i.strip())

                    if alignIndex in alignDF.index:
                        alignName = alignDF.loc[alignIndex]["ALIGNMENT"]
                    else:
                        print("Sorry, " + i + " is not part of the choices offered.")
                        break

                    alignSearched.append(alignName)

                    filterPhrase = baseStats["ALIGNMENT"] == alignName
                    filterList.append(filterPhrase)
                
                for f in filterList:
                    print("--------------------------------------\n")
                    returnedDF = baseStats[f]
                    print(returnedDF.to_string(justify = "center"))

            case "3":
                print("\nFiltering by Size\n")
                print("Here are all the available creature's Size:\n")
                print("""
                        1. Tiny
                        2. Small     
                        3. Medium
                        4. Large
                        5. Huge
                        6. Gargantuan
                        7. VARIES
                    (Enter 1 or more numbers corresponding to the Types, separated by a comma ',')""")
                
                size = input()
                sizeToFilter = size.split(",")
                sizeDF = pd.DataFrame({
                    "Size": [
                        "Tiny",
                        "Small",     
                        "Medium", 
                        "Large", 
                        "Huge", 
                        "Gargantuan", 
                        "VARIES",],
                }, index = [1, 2, 3, 4, 5, 6, 7])
                
                filterList = []
                sizeSearched = []

                for i in sizeToFilter:
                    sizeIndex = int(i.strip())

                    if sizeIndex in sizeDF:
                        sizeName = sizeDF.loc[sizeIndex]["Size"]
                    else:
                        print("Sorry, " + i + " is not part of the choices offered.")
                        break

                    sizeSearched.append(sizeName)

                    filterPhrase = baseStats["Size"] == sizeName
                    filterList.append(filterPhrase)
                
                for f in filterList:
                    print("--------------------------------------\n")
                    returnedDF = baseStats[f]
                    print(returnedDF.to_string(justify = "center"))

            case "4":
                print("\nFiltering by CR (Challenge Rating)\n")
                colName = "CR"
                #Converting all string values in the column CR into float
                baseStats[colName] = baseStats[colName].apply(lambda x : 
                                                        0.5   if x == "1/2" or x == "0.5" else
                                                        0.25  if x == "1/4" or x == "0.25" else
                                                        0.125 if x == "1/8" or x == "0.125" else
                                                        0 if x == "-" else
                                                        int(x))

                filterName = "CR (Challenge Rating)"

                numericFilterMenu(filterName, colName, baseStats)

            case "5":
                print("\nFiltering by AC (Armour Class)\n")
                colName = "AC"
                #Converting all string values in the column AC into numeric
                baseStats[colName] = pd.to_numeric(baseStats[colName])
                
                filterName = "AC (Armour Class)"

                numericFilterMenu(filterName, colName, baseStats)
            case "6":
                print("\nFiltering by HP (Health Point)\n")
                colName = "HP"
                #Converting all string values in the column AC into numeric
                baseStats[colName] = pd.to_numeric(baseStats[colName])
                
                filterName = "HP (Health Point)"

                numericFilterMenu(filterName, colName, baseStats)
            case "7":
                break
            case _ :
                print("Please input a number bewtween 1 and 7.")

        print("=====================================")
        print("Base Stats Filter Menu")
        print("""\n\tFilter the Base Stats table using the options below:
                1. Types
                2. Alignment
                3. Size
                4. CR (Challenge Rating)
                5. AC (Armor Class)
                6. HP (Health Point)
                7. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
        choice = input()

def filterAbilityScoresMenu():
    print("=====================================")
    print("Ability Score Filter Menu")
    print("""\n\t\tFilter the table using the options below:
                1. STR (Strength)
                2. DEX (Dexterity)
                3. CON (Constitution)
                4. INT (Intelligent)
                5. WIS (Wisdom)
                6. CHA (Charisma)
                7. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
    
    choice = input()
    print("\n------------------------------------------------------------")
    while choice != "7":
        match choice:
            case "1":
                print("\nFiltering by STR (Strenght)\n")
                colName = "STR"
                #Converting all string values in the column AC into numeric
                abilityScores[colName] = pd.to_numeric(abilityScores[colName])
                
                filterName = "STR (Strenght)"

                numericFilterMenu(filterName, colName, abilityScores)

            case "2":
                print("\nFiltering by DEX (Dexterity)\n")
                colName = "DEX"
                #Converting all string values in the column AC into numeric
                abilityScores[colName] = pd.to_numeric(abilityScores[colName])
                
                filterName = "DEX (Dexterity)"

                numericFilterMenu(filterName, colName, abilityScores)

            case "3":
                print("\nFiltering by CON (Constitution)\n")
                colName = "CON"
                #Converting all string values in the column AC into numeric
                abilityScores[colName] = pd.to_numeric(abilityScores[colName])
                
                filterName = "CON (Constitution)"

                numericFilterMenu(filterName, colName, abilityScores)

            case "4":
                print("\nFiltering by INT (Intelligent)\n")
                colName = "INT"
                #Converting all string values in the column AC into numeric
                abilityScores[colName] = pd.to_numeric(abilityScores[colName])
                
                filterName = "INT (Intelligent)"

                numericFilterMenu(filterName, colName, abilityScores)

            case "5":
                print("\nFiltering by WIS (Wisdom)\n")
                colName = "WIS"
                #Converting all string values in the column AC into numeric
                abilityScores[colName] = pd.to_numeric(abilityScores[colName])
                
                filterName = "WIS (Wisdom)"

                numericFilterMenu(filterName, colName, abilityScores)

            case "6":
                print("\nFiltering by CHA (Charisma)\n")
                colName = "CHA"
                #Converting all string values in the column AC into numeric
                abilityScores[colName] = pd.to_numeric(abilityScores[colName])
                
                filterName = "CHA (Charisma)"

                numericFilterMenu(filterName, colName, abilityScores)

            case "7":
                break
            case _ :
                print("Please input a number bewtween 1 and 7.")

        print("=====================================")
        print("Ability Score Filter Menu")
        print("""\n\t\tFilter the table using the options below:
                1. STR (Strength)
                2. DEX (Dexterity)
                3. CON (Constitution)
                4. INT (Intelligent)
                5. WIS (Wisdom)
                6. CHA (Charisma)
                7. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
    
        choice = input()

def filterSavingThrowMenu():
    print("=====================================")
    print("Saving Throw Modifier Filter Menu")
    print("""\n\t\tFilter the table using the options below:
                1. STR (Strength) 
                2. DEX (Dexterity)
                3. CON (Constitution)
                4. INT (Intelligent)
                5. WIS (Wisdom)
                6. CHA (Charisma)
                7. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
    
    choice = input()
    print("\n------------------------------------------------------------")
    while choice != "7":
        match choice:
            case "1":
                print("\nFiltering by STR (Strenght)\n")
                colName = "STR"
                #Converting all string values in the column AC into numeric
                savingThrows[colName] = pd.to_numeric(savingThrows[colName])
                
                filterName = "STR Saving Throw Modifier"

                numericFilterMenu(filterName, colName, savingThrows)

            case "2":
                print("\nFiltering by DEX (Dexterity)\n")
                colName = "DEX"
                #Converting all string values in the column AC into numeric
                savingThrows[colName] = pd.to_numeric(savingThrows[colName])
                
                filterName = "DEX Saving Throw Modifier"

                numericFilterMenu(filterName, colName, savingThrows)

            case "3":
                print("\nFiltering by CON (Constitution)\n")
                colName = "CON"
                #Converting all string values in the column AC into numeric
                savingThrows[colName] = pd.to_numeric(savingThrows[colName])
                
                filterName = "CON Saving Throw Modifier"

                numericFilterMenu(filterName, colName, savingThrows)

            case "4":
                print("\nFiltering by INT (Intelligent)\n")
                colName = "INT"
                #Converting all string values in the column AC into numeric
                savingThrows[colName] = pd.to_numeric(savingThrows[colName])
                
                filterName = "INT Saving Throw Modifier"

                numericFilterMenu(filterName, colName, savingThrows)

            case "5":
                print("\nFiltering by WIS (Wisdom)\n")
                colName = "WIS"
                #Converting all string values in the column AC into numeric
                savingThrows[colName] = pd.to_numeric(savingThrows[colName])
                
                filterName = "WIS Saving Throw Modifier"

                numericFilterMenu(filterName, colName, savingThrows)

            case "6":
                print("\nFiltering by CHA (Charisma)\n")
                colName = "CHA"
                #Converting all string values in the column AC into numeric
                savingThrows[colName] = pd.to_numeric(savingThrows[colName])
                
                filterName = "CHA Saving Throw Modifier"

                numericFilterMenu(filterName, colName, savingThrows)

            case "7":
                break
            case _ :
                print("Please input a number bewtween 1 and 7.")

        print("=====================================")
        print("Saving Throw Filter Menu")
        print("""\n\t\tFilter the table using the options below:
                1. STR (Strength)
                2. DEX (Dexterity)
                3. CON (Constitution)
                4. INT (Intelligent)
                5. WIS (Wisdom)
                6. CHA (Charisma)
                7. Return to Stats Table Menu
            (Enter the number corresponding to the filter option)\n""")
    
        choice = input()

def filterConditionImmuneMenu():
    print("=====================================")
    print("Condition Immunity Filter Menu")
    print("""\n\t\tHere are all Conditions:
                1. Blinded              8. Petrified                  
                2. Charmed              9. Poisoned        
                3. Deafened             10. Prone       
                4. Exhaustion           11. Restrained
                5. Frightened           12. Stunned
                6. Grappled             13. Unconscious
                7. Paralyzed             
            (Enter one or multiple numbers (between 1 and 13) corresponding to 
            the Conditions that the creature is immune to, separated by a comma ',')\n""")
    
    conditions = input()
    conditionList = conditions.split(",")
    conditionsDF = pd.DataFrame({
        "Conditions" : [
            "Blinded",
            "Charmed",
            "Deafened",
            "Exhaustion",
            "Frightened",
            "Grappled",
            "Paralyzed",
            "Petrified",
            "Poisoned",
            "Prone",
            "Restrained",
            "Stunned",
            "Unconscious",
        ],
    }, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    print("\n------------------------------------------------------------")

    print("Here are all the creatures that are immune to: \n")

    condNameSelected = []
    filterList = []
    for c in conditionList:
        conditionIndex = int(c.strip())

        if conditionIndex in conditionsDF.index:
            conditionName = conditionsDF.loc[conditionIndex]["Conditions"]
            condNameSelected.append(conditionName)
            
        else:
            print("Sorry, " + c + " is not part of the choices offered.")
            break

        filterList.append(conditionImmunities[conditionName] == 1)

    print(", ".join(condNameSelected))
    print("\n")

    initialDF = conditionImmunities
    filteredDFList = []
    finalFilteredDF = None

    #If there is more than 1 condition filter, apply them cumulatively through reduce()
    if len(filterList) > 1:
        
        cond = 0
        for i in filterList:
            #Select only the column that the user inputs along with the name column
            #Applying the filter conditions (stored in filterList) to the intial dataframe iteratively
            filtered = initialDF[i][["Name", condNameSelected[cond]]]
            filteredDFList.append(filtered)
            cond += 1
        
        #Merging all the different dataframes generated from the condition list above
        finalFilteredDF = reduce(lambda left, right: pd.merge(left, right, how = "inner", on = "Name"), filteredDFList)
        
    else:
        finalFilteredDF = initialDF[filterList[0]][["Name", condNameSelected[0]]]
    
    if finalFilteredDF.empty:
        print("Sorry, no creatures satisfy your filter conditions")
    else:
        print(finalFilteredDF.to_string())

def filterDamageImmuneMenu():
    print("=====================================")
    print("Damage Immunity Filter Menu")

    print("\n\tSelect one of the options below: ")
    print("""
                1. Immunity (takes 0 damage)
                2. Resistance (takes 1/2 damage)
                3. Vulnerable (takes 2 times the damage)
                (Enter 1, 2, OR 3 to proceed)""")
    statusType = input()
    while statusType != "1" and statusType != "2" and statusType != "3":
        print("Invalid input, please enter 1, 2, OR 3")
        statusType = input()
    print("--------------------------------------")


    print("""\n\t\tSelect one or more of the Damage Types below:
                1. Bludgeoning      8. Lightning                  
                2. Piercing         9. Necrotic        
                3. Slashing         10. Poison       
                4. Acid             11. Psychic
                5. Cold             12. Radiant
                6. Fire             13. Thunder
                7. Force            
            (Enter one or multiple numbers (between 1 and 13) separated by a comma ',')\n""")

    damageType = input()
    damageTypeList = damageType.split(",")
    damageTypeDF = pd.DataFrame({
        "Damage" : [
            "Bludgeoning",
            "Piercing",
            "Slashing",
            "Acid",
            "Cold",
            "Fire",
            "Force",
            "Lightning",
            "Necrotic",
            "Poison",
            "Psychic",
            "Radiant",
            "Thunder",
        ],
    }, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    print("\n------------------------------------------------------------")

    if statusType == "1":
        statusString = "immune"
    elif statusType == "2":
        statusString = "resistant"
    else:
        statusString = "vulnerable"
    print("Here are all the creatures that are " + statusString + " to: \n")


    damageTypeSelected = []
    filterList = []
    for c in damageTypeList:
        damageTypeIndex = int(c.strip())

        if damageTypeIndex in damageTypeDF.index:
            damageTypeName = damageTypeDF.loc[damageTypeIndex]["Damage"]
            damageTypeSelected.append(damageTypeName)
            
        else:
            print("Sorry, " + c + " is not part of the choices offered.")
            break

        if statusType == "1":
            filterList.append(damageImmunities[damageTypeName] == 2)
        elif statusType == "2":
            filterList.append(damageImmunities[damageTypeName] == 1)
        else:
            filterList.append(damageImmunities[damageTypeName] == -1)

    print(", ".join(damageTypeSelected))
    print("\n")

    initialDF = damageImmunities
    filteredDFList = []
    finalFilteredDF = None
    
    #If there is more than 1 condition filter, apply them cumulatively through reduce()
    if len(filterList) > 1:
        
        k = 0
        for i in filterList:
            #Select only the column that the user inputs along with the name column
            #Applying the filter conditions (stored in filterList) to the intial dataframe iteratively
            filtered = initialDF[i][["Name", damageTypeSelected[k]]]
            filteredDFList.append(filtered)
            k += 1
        
        #Merging all the different dataframes generated from the condition list above
        finalFilteredDF = reduce(lambda left, right: pd.merge(left, right, how = "inner", on = "Name"), filteredDFList)

    else:
        finalFilteredDF = initialDF[filterList[0]][["Name", damageTypeSelected[0]]]
    
    if finalFilteredDF.empty:
        print("Sorry, no creatures satisfy your filter conditions")
    else:
        print(finalFilteredDF.to_string())  

def filterHabitatMenu():
    print("=====================================")
    print("Habitat Filter Menu")
    print("""\n\t\tHere are all Habitats:
                1. Arctic       7. Mountain                   
                2. Coast        8. Swamp       
                3. Desert       9. Underdark          
                4. Forest       10. Underwater       
                5. Grassland    11. Urban         
                6. Hill                        
            (Enter one or multiple numbers (between 1 and 13) corresponding to 
            the Habitats that the creature is in, separated by a comma ',')\n""")
    
    habitats = input()
    habitatsList = habitats.split(",")
    habitatsDF = pd.DataFrame({
        "Habitat" : [
            "Arctic",
            "Coast",
            "Desert",
            "Forest",
            "Grassland",
            "Hill",
            "Mountain",
            "Swamp",
            "Underdark",
            "Underwater",
            "Urban",
        ],
    }, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print("\n------------------------------------------------------------")

    print("Here are all the creatures that can be found in: \n")

    habitatsSelected = []
    filterList = []
    for c in habitatsList:
        habitatsIndex = int(c.strip())

        if habitatsIndex in habitatsDF.index:
            habitatName = habitatsDF.loc[habitatsIndex]["Habitat"]
            habitatsSelected.append(habitatName)
            
        else:
            print("Sorry, " + c + " is not part of the choices offered.")
            break

        filterList.append(habitatStats[habitatName] == "YES")

    print(", ".join(habitatsSelected))
    print("\n")

    initialDF = habitatStats
    filteredDFList = []
    finalFilteredDF = None
    
    #If there is more than 1 condition filter, apply them cumulatively through reduce()
    if len(filterList) > 1:
        
        k = 0
        for i in filterList:
            #Select only the column that the user inputs along with the name column
            #Applying the filter conditions (stored in filterList) to the intial dataframe iteratively
            filtered = initialDF[i][["Name", habitatsSelected[k]]]
            filteredDFList.append(filtered)
            k += 1
        
        #Merging all the different dataframes generated from the condition list above
        finalFilteredDF = reduce(lambda left, right: pd.merge(left, right, how = "inner", on = "Name"), filteredDFList)

    else:
        finalFilteredDF = initialDF[filterList[0]][["Name", habitatsSelected[0]]]
    
    if finalFilteredDF.empty:
        print("Sorry, no creatures satisfy your filter conditions")
    else:
        print(finalFilteredDF.to_string())  

#------------------------------------------------------------------------------------------------------------------------------------------------  
#START PAGE
print("""Welcome to the DnD Monster Manual Searcher!\n
------------------------------------------------------------\n
This program is designed to assist you with searching through
the DnD 5e Monster Manual excel file, which contains the stats 
of 691 creatures.\n
------------------------------------------------------------\n
MAIN MENU:
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
        1. Creatures by Base Stats
        2. Creatures by Ability Scores
        3. Creatures by Saving Throws
        4. Creatures by Condition Immunities
        5. Creatures by Damage Immunities
        6. Creatures by Habitats
        7. Back to Main Menu
        (Enter the number corresponding to the table you want to view)\n""")
        tableChoice = input()

        while tableChoice != "7":
            if tableChoice == "1":
                print("Creatures by Base Stats:\n")
                print(baseStats.to_string(justify = "center"))

                filterBaseStatsMenu()

            elif tableChoice == "2":
                print("Creatures by Ability Scores:\n")
                print(abilityScores.to_string(justify = "center"))

                filterAbilityScoresMenu()

            elif tableChoice == "3":
                print("Creatures by Saving Throws:\n")
                print(savingThrows.to_string(justify = "center"))

                filterSavingThrowMenu()

            elif tableChoice == "4":
                print("Creatures by Condition Immunities:\n")
                print(conditionImmunities.to_string(justify = "center"))

                filterConditionImmuneMenu()

            elif tableChoice == "5":
                print("Creatures by Damage Immunities:\n")
                print(damageImmunities.to_string(justify = "center"))

                filterDamageImmuneMenu()

            elif tableChoice == "6":
                print("Creatures by Habitats:\n")
                print(habitatStats.to_string(justify = "center"))

                filterHabitatMenu()

            else:
                print("Please enter a number from 1 to 7.")

            print("\n------------------------------------------------------------")
            print("Stat Tables Menu:\n")
            print("""
        1. Creatures by Base Stats
        2. Creatures by Ability Scores
        3. Creatures by Saving Throws
        4. Creatures by Condition Immunities
        5. Creatures by Damage Immunities
        6. Creatures by Habitats
        7. Back to Main Menu
        (Enter the number corresponding to the table you want to view)\n""")
            tableChoice = input()
        
    else:
        print("Invalid input, please enter a number from 1 to 4.")

    mainMenuOptions()
    print("\nWhat would you like to do? (Enter the number corresponding to your choice):")
    inputChoice = input()

