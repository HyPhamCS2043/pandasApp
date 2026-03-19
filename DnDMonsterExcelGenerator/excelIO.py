import pandas as pd;

with pd.ExcelFile("..\MonsterManualExcel\D&D 5e Monster Manual by Ability Scores, Saves, Damage and Condition immunities.xlsx") as manual:
    baseStats = pd.read_excel(manual, sheet_name = 0, header = 0, usecols = "A:G")

    print("First 15 Monsters:\n ")
    print(baseStats.head(15))

    print("\n")

    print(baseStats.tail(5))
    
    print("\n")

    #Indexing with loc, which returns the index with the LABEL 5 (not the 5th index from the top)
    #to_string() removes the name and dtype at the bottom of output
    print(baseStats.loc[5].to_string())

    print("\n")

    #This apply the boolean operation to all element in dataframe, and create a boolean dataFrame that stores the output of
    #"if index i has "Beast" in its entry for column "Type"
    print(baseStats["Type"] == "Beast")

    #Example of applying a boolean list to a dataFrame
    #boolDF = [True, True, False]

    print("\n")
    #print(baseStats.head(3)[boolDF])

    #Returning all rows that has type = Beast
    beastList = pd.DataFrame(baseStats[baseStats["Type"] == "Beast"])
    print(beastList)

    print("\n")

    #NOTES: Certain values in the excel might have the wrong data types. For example, in CR, some 1/4 is actually datetime for 2018/1/4 
