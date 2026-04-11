## pandas Python Library/Package Overview

# 1. Introduction

**pandas** is a an open-source Python library that comes with a wide array of data anlysis and manipulation functionalities.
Developed by AQR Capital Management in 2008 and becoming open-source in 2009, pandas is "actively supported today by a community of like-minded individuals around the world who contribute their valuable time and energy." [1]

# 2. Key Features

### a. Series and DataFrame
**pandas'** primary purpose is to provide developers with efficient, flexible, fast, powerful, and easy-to-use ways to analyze and manipulate a massive amount of data.   
At the center of **pandas** is the introduction of two key classes for the handling of data: **Series** and **DataFrame** 
    
    Series: a one-dimensional labeled array holding data of any type such as integers, strings,  
    Python objects etc.

    DataFrame: a two-dimensional data structure that holds data like a two-dimension array or  
    a table with rows and columns.
[2]

Almost every single other functionalities that the package provides revolve around storing data into these data structures and manipulating them.

#### Series   
To create a series:
```
  s = pd.Series(data, index=index)
```

<ins>index</ins> refers to the name of the axis or the row, while <ins>data</ins> here can be:
* "a Python dict

* an ndarray

* a scalar value (like 5)" [3]

Example:  
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

 
**Series is dict-like**  
Values can be retrieved and set by label. Accessing a label that doesn't exist raises a `KeyError`.
 
**Label alignment** — when two Series are involved in an operation, pandas automatically aligns them by their labels. If a label is not found in one Series, the result for that label is `NaN` ([pandas.pydata.org/docs/user_guide/dsintro.html](https://pandas.pydata.org/docs/user_guide/dsintro.html)):
 
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
 
---

## References
[1] https://pandas.pydata.org/about/index.html  
[2] https://pandas.pydata.org/docs/user_guide/10min.html  
[3] https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro
