## pandas Python Library/Package Overview

# 1. Introduction

**pandas** is a an open-source Python library that comes with a wide array of data anlysis and manipulation functionalities.
Developed by AQR Capital Management in 2008 and becoming open-source in 2009, pandas is "actively supported today by a community of like-minded individuals around the world who contribute their valuable time and energy." [1]

To use pandas, starts by installing the package with

    pip3 install pandas

Then, import the package as followed at the top of your code:

```
import pandas as pd
```

# 2. Key Features, How-To-Use, and Functionalities

## a. Series and DataFrame
**pandas'** primary purpose is to provide developers with efficient, flexible, fast, powerful, and easy-to-use ways to analyze and manipulate a massive amount of data.   
At the center of **pandas** is the introduction of two key classes for the handling of data: **Series** and **DataFrame** 
    
    Series: a one-dimensional labeled array holding data of any type such as integers, strings,  
    Python objects etc.

    DataFrame: a two-dimensional data structure that holds data like a two-dimension array or  
    a table with rows and columns.
[2]

Almost every single other functionalities that the package provides revolve around storing data into these data structures and manipulating them.

-----------------------------------------------------------------
#### Series   
To create a series:
```
  s = pd.Series(data, index=index)
```

`index`refers to the name of the axis or the row, while `data` here can be:
* "a Python dict

* an ndarray

* a scalar value (like 5)" [3]

Input
```
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
```

Output
```
s
Out[4]: 
a    0.469112
b   -0.282863
c   -1.509059
d   -1.135632
e    1.212112
dtype: float64
```
-------------------
**Series is dict-like**  
Values can be retrieved and set by label. Accessing a label that doesn't exist raises a `KeyError`. [3]

------------------
**Label alignment**  
When two Series are involved in an operation, pandas automatically aligns them by their labels. If a label is not found in one Series, the result for that label is marked as missing `NaN` [3]

 Input:
```python
s.iloc[1:] + s.iloc[:-1]
```
 
Output:
```
a         NaN
b   -0.565727
c   -3.018117
d   -2.271265
e         NaN
dtype: float64
```
-----------------
**Name attribute**
**Series** also has a `name` attribute:
Input:
```
s = pd.Series(np.random.randn(5), name="something")
s
```

Output:
```
0   -0.494929
1    1.071804
2    0.721555
3   -0.706771
4   -1.039575
Name: something, dtype: float64
```

To get just the name of the Series, use:

Input:
```
s.name
```
Output:
```
'something'
```


-------------------------------------------
### DataFrame
**DataFrame** is similar to a 2D array with labeled rows and columns. A DataFrame can be considered a "dict of Series objects" [3]. DataFrame accepts the following as input:

* Dict of 1D ndarrays, lists, dicts, or Series
* 2-D numpy.ndarray
* Structured or record ndarray
* A Series
* Another DataFrame

**Example — Creating a DataFrame from a dict of lists:**
 
```python
df = pd.DataFrame({
    "one": [1.0, 2.0, 3.0, 4.0],
    "two": [4.0, 3.0, 2.0, 1.0]
})
print(df)
```
 
Output:
```
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0
```


---------------------------
DataFrames also has optional arguments to rename the labels of rows and columns:
* `index` (for row labels)
* `columns` (for column labels)

**Example**
Input
```python
pd.DataFrame(data, index=["first", "second"])
```

Output
```
        A    B         C
first   1  2.0  b'Hello'
second  2  3.0  b'World'
```

Input
```python
pd.DataFrame(data, columns=["C", "A", "B"])
```

Output
```
          C  A    B
0  b'Hello'  1  2.0
1  b'World'  2  3.0
```
-------------------------
**Example — Creating a DataFrame from structured or record array:**

Input
```python
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "S10")])

data[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]

pd.DataFrame(data)
```

Output
```
   A    B         C
0  1  2.0  b'Hello'
1  2  3.0  b'World'
```
[3]

--------------------------
**Example — Creating a DataFrame from a Series:**
Input:
```python
ser = pd.Series(range(3), index=list("abc"), name="ser")

pd.DataFrame(ser)
```

Output:
```
   ser
a    0
b    1
c    2
```
[3]
-------------------------------------------------
## b. Viewing Data

Instead of viewing the entire datasets, print out some of the data at a time.  

To view the top of the dataframes, use `DataFrame.head([number of rows])` 
 
Input:
```python
df.head(5)
```

Output: 
```
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```
[2]

To view the bottom of the dataframes, use `DataFrame.tail([number of rows])` 
  
Input:
```python
df.tail(3)
```

Output:
```
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```
[2]

-------------------------------------------------
## c. Reading and Writing Data  
**pandas** provides a flexible and easy-to-use approach to the reading of data through top level readers and writers function. Regardless of file types, the syntax for the reading of data from external file into a DataFrame is 

    **DataFrame.read_[fileType]** 
    
and the syntax for the writing of data from a DataFrame to an external file is 

    **DataFrame.to_[fileTypes]**

Below is a table showing some common file reading and writing extensions in **pandas**:  
| Format Type   |     Data      |      Read     |      Write    |
| ------------- | ------------- | ------------- | ------------- |
|text|CSV|read_csv |to_csv|
|text|JSON|read_json|to_json|
|text|MS Excel|read_excel|to_excel|
|text|HTML|read_html|to_html|
|text|XML|read_xml|to_xml|  

[4]  
------------------------------------------------------

## d. Indexing and selecting data  

Once you have initialized or loaded data into DataFrames, the next step to manipulating the data lies in **pandas's** indexing and data selection system. 

In the constructor for a Series or a DataFrame, there is an optional arugment `index` that accepts a list of strings to be used as the index label for the rows. 
```
s1 = pd.Series([0, 1, 2], index=["a", "b", "c"])
```
  
The first row of this Series is not labeled as "a", as oppposed to the default 0-indexing.  

----------------------------------------
At the simplest level, `[]` can be used to select a slice out of a Series or a DataFrame.  
Passing a label into `*DataFrame[]` returns a Series or a column.  


Input  
```python
df["A"]
```

Output
```
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.673690
Freq: D, Name: A, dtype: float64
```  
[2]


Passing a list of column into this returns a subset of the DataFrame.  

Input  
```
df[["B", "A"]]
```

Output  
```
                   B         A
2013-01-01 -0.282863  0.469112
2013-01-02 -0.173215  1.212112
2013-01-03 -2.104569 -0.861849
2013-01-04 -0.706771  0.721555
2013-01-05  0.567020 -0.424972
2013-01-06  0.113648 -0.673690
```
[2]

Passing a slice `:` into DataFrame[] returns matching slices of rows. [5]  

**Example**  
Input:
```python
df[0:3]
```

Output: 
```
         A         B         C         D
0     0.469112 -0.282863 -1.509059 -1.135632
1     0.538593 -0.984943 -1.333333 -1.345355
2     1.212112 -0.173215  0.119209 -1.044236
3    -0.861849 -2.104569 -0.494929  1.071804
```



Outside of `[]`, two commonly used methods to select specific row are:

* `DataFrame.loc()`: loc() is a label-based indexer that returns rows with corresponding labels.
* `DataFrame.iloc()`: iloc() on the other hand returns the rows with the corresponding integer position within the DataFrame (0-indexed)

```python

# Grab a row by its label
df.loc["b"]
 
# Grab a row by its position (0-indexed)
df.iloc[2]
 
# Shorthand attribute access — works if the column name is a valid Python variable name
df.A
```

Both these methods can be combined with `[]` to access specific parts of the DataFrame. For example:

```python
df.loc["a"]["Name"]
```

will produce the data on row with index-label "a" and under column "Name".  

When used with slices, `loc()` returns all elements between the lower and upper bound of the slice, inclusive.

Input 
```python
s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])

s.loc[3:5]
```

Output
```
3    b
2    c
5    d
dtype: str
```

With slices in iloc(), "the start bound is included, while the upper bound is excluded" [5]   
Input   
```
df1.iloc[1:5, 2:4]
```

Output
```
          4         6
2  0.301624 -2.179861
4  1.462696 -1.743161
6  1.314232  0.690579
8  0.014871  3.357427
```
[5]

------------------------------------------------------

### Boolean Indexing ###

In pandas, passing a boolean expression into `DataFrame[]` returns a subset of the DataFrame that satisfies the expression.  
The boolean expression or expressions (separated by operators such as `&` or `|`) are processed as boolean vectors, which is then applied to the DataFrame that calls `[]`.


Input  
```
s[s["A"] > 0]
```
  
Output
```
    A    B
4    1   1
5    2   0
6    3   1
dtype: int64
```

Input
```
s[(s < -1) | (s > 0.5)]
```

Output  
```
0   -3
1   -2
4    1
5    2
6    3
dtype: int64
```

---
 
## e. Merging and Combining DataFrames
 
pandas supports SQL-style joins with `pd.merge()`, and stacking tables with `pd.concat()`:

Input
```python
left  = pd.DataFrame({"key": ["a", "b"], "val_left":  [1, 2]})
right = pd.DataFrame({"key": ["b", "c"], "val_right": [3, 4]})
 
pd.merge(left, right, on="key", how="inner")
```
Output
```
  key  val_left  val_right
0   b         2          3
```

pandas also has `DataFrame.join()`, which allows for the merging of multiple DataFrame objects along the columns [6]

Input  
```  
left = pd.DataFrame(
   ....:     {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
   ....: )
   ....: 

right = pd.DataFrame(
   ....:     {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
   ....: )
   ....: 

result = left.join(right)

result
```

Output  
```
Out[86]: 
     A   B    C    D
K0  A0  B0   C0   D0
K1  A1  B1  NaN  NaN
K2  A2  B2   C2   D2
```


---
 
## f. Handling Missing Data
 
pandas uses `NaN` (Not a Number) as its standard placeholder for missing values [3].  

The package provides a host of useful functions that let users work with datasets that come with missing data. 

For example:   
```python
# See where values are missing
pd.isna(df)
 
# Drop any row that has at least one missing value
df.dropna()
 
# Fill in missing values with 0 (or whatever makes sense for your data)
df.fillna(0)
```
Notably, "missing values propagate through arithmetic operations between pandas objects."[6]

---

# 3. Why pandas

I chose pandas as the package for my exploration because of several reasons. First of all, pandas empowers Python, a language that I am well-versed in, with expansive and efficient data analysis and manipulation capabilities. Thus, the package allows me to leverage the ease and flexibility of Python while performing complex operations on massive datasets. For instance, using reduce() alongside pandas.merge() allows me to perform a sequence of SQL-like join operation iteratively and dynamically on data obtained from an Excel documents with over 3000 rows spread across 5 sheets. Secondly, pandas, being open-source since its early years, come with a vibrant and active communities of developers who could assist me with any issues during my learning. There are numerous online resources that come with practical examples to enhance my understanding of the package even further. Last, but not least, pandas expands my data analysis and processing skills, as its easy-to-use functionalities and straight-forward syntaxes (a trait inherited from Python) let me focus on developing efficient and fast data manipulation queries.  

Through learning pandas, I come to appreciate Python's flexibility and high-level language format. I begin to approach problem in more Pythonic way, focusing on creating efficient and reusable code snippets that leverages Python's syntax and resusability.

Overall, I greatly enjoyed exploring and learning more about pandas. The package empowers me with a deeper understanding of how to create good data manipulation queries. The abundance of online resources meant that I encountered little barrier why trying to learn it. I definitely recommend the package to anyone who enjoys Python and wants to increase their data analysis skillset, and will continue to use pandas extensively in the future.
  

## References
[1] https://pandas.pydata.org/about/index.html  
[2] https://pandas.pydata.org/docs/user_guide/10min.html  
[3] https://pandas.pydata.org/docs/user_guide/dsintro.html  
[4] https://pandas.pydata.org/docs/user_guide/io.html  
[5] https://pandas.pydata.org/docs/user_guide/indexing.html  
[6] https://pandas.pydata.org/docs/user_guide/merging.html  
[7] https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html  
