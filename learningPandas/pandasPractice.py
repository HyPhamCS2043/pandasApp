import pandas as pd

dataframe = pd.DataFrame(
    {
        "Name": [
            "Austin", 
            "Bob", 
            "Charlie",
            "Joanne",],
        "Age": [
            18,
            29,
            35,
            35,
        ],
    }, index=["a", "b", "c", "d"], 
)


print(dataframe)
print("\n")
print(dataframe.loc["b"]) #prints the row with index "b"
print("\n")
#print(dataframe.head(2)) #prints the first 2 rows of the dataframe
#print("\n")

series1 = pd.Series([1, 2, 3, 4, 5], name = "counts", index=["a", "b", "c", "d", "e"])
print(series1)
print(series1["c"])

print(series1.get("c")) #same as above but it won't throw an error if the key doesn't exist, it will return None instead

print(series1.get("f", "Key not found")) #returns "Key not found" because "f" is not in the series

# multiplies each element in the series by 2. 
#An example of vectorized operations in pandas, which allows you to perform operations on entire arrays of data without the need for explicit loops.
print(series1 * 2) 

