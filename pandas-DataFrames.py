In [1]: import pandas as pd

In [2]: grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
   ...:                'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
   ...:                'Bob': [83, 65, 85]}

In [3]: grades = pd.DataFrames(grades_dict)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-3-1fb73e36e4bc> in <module>
----> 1 grades = pd.DataFrames(grades_dict)

~\anaconda3\lib\site-packages\pandas\__init__.py in __getattr__(name)
    242         return _SparseArray
    243
--> 244     raise AttributeError(f"module 'pandas' has no attribute '{name}'")
    245
    246

AttributeError: module 'pandas' has no attribute 'DataFrames'

In [4]: grades = pd.DataFrame(grades_dict)

In [5]: grades
Out[5]:
   Wally  Eva  Sam  Katie  Bob
0     87  100   94    100   83
1     96   87   77     81   65
2     70   90   90     82   85

In [6]: grades.index = ['Test1', 'Test2', 'Test3']

In [7]: grades
Out[7]:
       Wally  Eva  Sam  Katie  Bob
Test1     87  100   94    100   83
Test2     96   87   77     81   65
Test3     70   90   90     82   85

In [8]: grades['Eva']
Out[8]:
Test1    100
Test2     87
Test3     90
Name: Eva, dtype: int64

In [9]: grades.Sam
Out[9]:
Test1    94
Test2    77
Test3    90
Name: Sam, dtype: int64

In [10]: grades.loc['Test1']
Out[10]:
Wally     87
Eva      100
Sam       94
Katie    100
Bob       83
Name: Test1, dtype: int64

In [11]: grades.iloc[1]
Out[11]:
Wally    96
Eva      87
Sam      77
Katie    81
Bob      65
Name: Test2, dtype: int64

In [12]: grades.loc['Test1':'Test3']
Out[12]:
       Wally  Eva  Sam  Katie  Bob
Test1     87  100   94    100   83
Test2     96   87   77     81   65
Test3     70   90   90     82   85

In [13]: grades.iloc[0:2]
Out[13]:
       Wally  Eva  Sam  Katie  Bob
Test1     87  100   94    100   83
Test2     96   87   77     81   65

In [14]: grades.loc[['Test1', 'Test3']]
Out[14]:
       Wally  Eva  Sam  Katie  Bob
Test1     87  100   94    100   83
Test3     70   90   90     82   85

In [15]: grades.iloc[[0, 2]]
Out[15]:
       Wally  Eva  Sam  Katie  Bob
Test1     87  100   94    100   83
Test3     70   90   90     82   85

In [16]: grades.loc['Test1':'Test2', ['Eva', 'Katie']]
Out[16]:
       Eva  Katie
Test1  100    100
Test2   87     81

In [17]: grades.iloc[[0, 2], 0:3]
Out[17]:
       Wally  Eva  Sam
Test1     87  100   94
Test3     70   90   90

In [18]: grades[grades >= 90]
Out[18]:
       Wally    Eva   Sam  Katie  Bob
Test1    NaN  100.0  94.0  100.0  NaN
Test2   96.0    NaN   NaN    NaN  NaN
Test3    NaN   90.0  90.0    NaN  NaN

In [19]: grades[(grades >= 80) & (grades < 90)]
Out[19]:
       Wally   Eva  Sam  Katie   Bob
Test1   87.0   NaN  NaN    NaN  83.0
Test2    NaN  87.0  NaN   81.0   NaN
Test3    NaN   NaN  NaN   82.0  85.0

In [20]: grades.at['Test2', 'Eva']
Out[20]: 87

In [21]: grades.iat[2, 0]
Out[21]: 70

In [22]: grades.at['Test2', 'Eva'] = 100

In [23]: grades.at["Test2', 'Eva']
  File "<ipython-input-23-633a9bbbdc6a>", line 1
    grades.at["Test2', 'Eva']
                             ^
SyntaxError: EOL while scanning string literal


In [24]: grades.at['Test2', 'Eva']
Out[24]: 100

In [25]: grades.iat[1, 2] = 87

In [26]: grades.iat[1, 2]
Out[26]: 87

In [27]: grades.describe()
Out[27]:
           Wally         Eva        Sam       Katie        Bob
count   3.000000    3.000000   3.000000    3.000000   3.000000
mean   84.333333   96.666667  90.333333   87.666667  77.666667
std    13.203535    5.773503   3.511885   10.692677  11.015141
min    70.000000   90.000000  87.000000   81.000000  65.000000
25%    78.500000   95.000000  88.500000   81.500000  74.000000
50%    87.000000  100.000000  90.000000   82.000000  83.000000
75%    91.500000  100.000000  92.000000   91.000000  84.000000
max    96.000000  100.000000  94.000000  100.000000  85.000000

In [28]: pd.set_option('precision', 2)

In [29]: grades.describe()
Out[29]:
       Wally     Eva    Sam   Katie    Bob
count   3.00    3.00   3.00    3.00   3.00
mean   84.33   96.67  90.33   87.67  77.67
std    13.20    5.77   3.51   10.69  11.02
min    70.00   90.00  87.00   81.00  65.00
25%    78.50   95.00  88.50   81.50  74.00
50%    87.00  100.00  90.00   82.00  83.00
75%    91.50  100.00  92.00   91.00  84.00
max    96.00  100.00  94.00  100.00  85.00

In [30]: grades.mean()
Out[30]:
Wally    84.33
Eva      96.67
Sam      90.33
Katie    87.67
Bob      77.67
dtype: float64

In [31]: grades.T
Out[31]:
       Test1  Test2  Test3
Wally     87     96     70
Eva      100    100     90
Sam       94     87     90
Katie    100     81     82
Bob       83     65     85

In [32]: grades.T.describe()
Out[32]:
        Test1   Test2  Test3
count    5.00    5.00   5.00
mean    92.80   85.80  83.40
std      7.66   13.81   8.23
min     83.00   65.00  70.00
25%     87.00   81.00  82.00
50%     94.00   87.00  85.00
75%    100.00   96.00  90.00
max    100.00  100.00  90.00

In [33]: grades.T.mean()
Out[33]:
Test1    92.8
Test2    85.8
Test3    83.4
dtype: float64

In [34]: grades.sort_index(ascending=False)
Out[34]:
       Wally  Eva  Sam  Katie  Bob
Test3     70   90   90     82   85
Test2     96  100   87     81   65
Test1     87  100   94    100   83

In [35]: grades.sort_index(axis=1)
Out[35]:
       Bob  Eva  Katie  Sam  Wally
Test1   83  100    100   94     87
Test2   65  100     81   87     96
Test3   85   90     82   90     70

In [36]: grades.sort_values(by='Test1', axis=1, ascending=False)
Out[36]:
       Eva  Katie  Sam  Wally  Bob
Test1  100    100   94     87   83
Test2  100     81   87     96   65
Test3   90     82   90     70   85

In [37]: grades.T.sort_values(by='Test1', ascending=False)
Out[37]:
       Test1  Test2  Test3
Eva      100    100     90
Katie    100     81     82
Sam       94     87     90
Wally     87     96     70
Bob       83     65     85

In [38]: grades.loc['Test1'].sort_values(ascending=False)
Out[38]:
Eva      100
Katie    100
Sam       94
Wally     87
Bob       83
Name: Test1, dtype: int64

In [39]:
