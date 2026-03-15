#Author: Hy Pham
import pandas as pd;

#The base dataframe for the base stats of a creature (DnD 5e rulesets).
baseStats = pd.DataFrame(
    {
        "Name": [],
        "Type": [],
        "Alignment": [],
        "Size": [],
        "Challenge Rating (CR)": [],
        "Armor Class (AC)": [],
        "Hit Points (HP)": [],
    })

print("Base Stats Table\n")
print(baseStats)

#List containing the possible values for the "Alignment" column in the baseStats dataframe.
alignment = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

#List containing the possible values for the "size" column in the baseStats dataframe.
size = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]