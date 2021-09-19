#Assignment: Practice the seaborn on iris dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.corr())
sns.heatmap(df.corr())
sns.jointplot(x='sepal_length', y='petal_length', data=df, kind='hex')
sns.pairplot(df)
sns.pairplot(df, hue='species')
print(df['species'].value_counts())
sns.distplot(df['sepal_width'])             
plt.show()

