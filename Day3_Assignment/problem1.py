#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
sns.countplot('species', data = df)
plt.show()
sns.barplot(y = 'sepal_length', x= 'petal_length', data = df)  
plt.show()
sns.boxplot(y = 'sepal_length', x= 'petal_length', data = df)     
plt.show()
sns.boxplot(y = 'sepal_length', x= 'petal_length', data = df, palette = 'rainbow')
plt.show()
sns.boxplot( x='sepal_length', y = 'petal_length', hue = 'species', data = df, orient="h")
plt.show()
sns.violinplot(x='sepal_length', y = 'petal_length', hue = 'species', data = df)
df.iplot(kind = 'scatter', x='sepal_length', y='petal_length', mode = 'markers')
plt.show()
