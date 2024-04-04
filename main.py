import numpy as np
import pandas as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('./Quality Assessment.csv')
print(data.head(5))
print(data.isnull().sum())
data = data.dropna(axis = 0)
print(data.isnull().sum())   #removing the null values from the dataset (6 null values in quantity column)
print(data.columns)
data.loc[(data['Assembly Line']=='A'),'Assembly Line'] = 0
data.loc[(data['Assembly Line']=='B'),'Assembly Line'] = 1
data.loc[(data['Assembly Line']=='b'),'Assembly Line'] = 1
data.loc[(data['Assembly Line']=='a'),'Assembly Line'] = 0
print(data.head(5))
data['Assembly Line'].astype('int')
print(data.info())
plt1 = sns.heatmap(data.corr(),annot=True,annot_kws={'size':20},cmap = 'RdYlGn')
plt.show()
#Heat map of the given datset (it shows how the data columns are being co related with each other)

# Data Analysis
cols = data.columns
print(cols)

x1 = pd.DataFrame(data.groupby(['Assembly Line'])['Quantity (lts.)'].sum())
print(x1)   # Assembly Line B has higher quantity in lts. which is 313.483658 which is higher than A i.e. 271.928042
# plt2 = sns.catplot(kind = 'point',data = x1,x ='Assembly Line',y = 'Quantity (lts.)')
# plt.show()
x2 = data.groupby(['Assembly Line'])['CO2 dissolved'].sum()
print(x2)   # more CO2 dissolved in assembly line B

# plt3 = px.scatter(data,x= 'Assembly Line',y = 'Quantity (lts.)')
# plt3.show()   #the minimum value and the maximum value of the Quantity has the maximum value of 2.109917 and minimum value of 1.891 related to assembly line B

plt4 = px.scatter(data,x = 'Assembly Line',y = 'CO2 dissolved')
plt4.show()
# seeing that the assembly B has high CO2 dissolved but from the graph there are so 3 outliers in assembly A which produced high amount of CO2 dissolution.
#assembly Line B also has minimum value of Co2 dissolved which is 2.25
f, ax = plt.subplots(1,3,figsize =(18,8))
plt5 = sns.barplot(data,y= data['Time limit Crossed'] == 1,x = 'Assembly Line',ax = ax[0])
plt6 = sns.barplot(data,y= data['Time limit Crossed'] == 0,x = 'Assembly Line',ax = ax[1])
plt7 = sns.countplot(data, x = 'Assembly Line',ax = ax[2])
plt.show() #more value for assembly line B .
# assembly B has crossed time limits so many times than A. by doing things in time limits assembly A has done a great job

x3 = data.groupby(['Time limit Crossed','Assembly Line'])['Quantity (lts.)'].sum()
print(x3)  #when the quantity is high then the chance of crossing the limit is very low irrespective of assembly line.


print(data['Assembly Line'].describe())

# Finding variances :-
variances = data[['Time limit Crossed','Quantity (lts.)','Assembly Line']].var(axis = 0)
print(variances)
plt.figure(figsize=(8, 6))
plt.bar(range(len(variances)), variances, color='skyblue')
plt.xlabel('Feature Index')
plt.ylabel('Variance')
plt.title('Variance of Each Feature')
plt.xticks(range(len(variances)), [f'Feature {i}' for i in range(len(variances))])
plt.grid(True)
plt.show()
