# -*- coding: utf-8 -*-
"""Pandas_usingmapForValueReplacement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XhCAY2nuOjCl54wqoacPYAoZ_jD3sPuE
"""

#Example 17: Pandas -Using map() fro Value Replacement

import pandas as pd
# Creatingg a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Department': ['HR','IT','Finance']}
df=pd.DataFrame(data)
#mapping Departments of codes
departments_map={'Hr': 1, 'IT':2, 'Finance': 3}
df['Dept Code'] =df['Department'].map(departments_map)
print ('DataFrame with Mapped Values:\n', df)

