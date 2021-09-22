In [1]: import pandas as pd

In [2]: grades = pd.Series([87, 100, 94])

In [3]: grades
Out[3]:
0     87
1    100
2     94
dtype: int64

In [4]: pd.Series(98.6, range(3))
Out[4]:
0    98.6
1    98.6
2    98.6
dtype: float64

In [5]: grades[0]
Out[5]: 87

In [6]: grades.count()
Out[6]: 3

In [7]: grades.mean()
Out[7]: 93.66666666666667

In [8]: grades.min()
Out[8]: 87

In [9]: grades.std()
Out[9]: 6.506407098647712

In [10]: grades.describe()
Out[10]:
count      3.000000
mean      93.666667
std        6.506407
min       87.000000
25%       90.500000
50%       94.000000
75%       97.000000
max      100.000000
dtype: float64

In [11]: grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])

In [12]: grades
Out[12]:
Wally     87
Eva      100
Sam       94
dtype: int64

In [13]: grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

In [14]: grades
Out[14]:
Wally     87
Eva      100
Sam       94
dtype: int64

In [15]: grades['Eva']
Out[15]: 100

In [16]: grades.Wally
Out[16]: 87

In [17]: grades.dtype
Out[17]: dtype('int64')

In [18]: grades.values
Out[18]: array([ 87, 100,  94], dtype=int64)

In [19]: hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

In [20]: hardware
Out[20]:
0    Hammer
1       Saw
2    Wrench
dtype: object

In [21]: hardware.str.contains('a')
Out[21]:
0     True
1     True
2    False
dtype: bool

In [22]: hardware.str.upper()
Out[22]:
0    HAMMER
1       SAW
2    WRENCH
dtype: object

In [23]:
