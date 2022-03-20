import numpy as np
import seaborn as sns

data = [1, 2, 3, 2, 1, 100, 1, 2, 3, 2, 1, 50, 3, 4, 5, 10, 7, 2 , 5,  80 ]
sort_data = np.sort(data)
sort_data

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
print('25 percentile - ', Q1)
print('75 percentile - ', Q3)

IQR = Q3 - Q1
# print('Interquartile range is', IQR)

low_lim = Q1 - 1.5 * IQR
up_lim = Q3 + 1.5 * IQR
# print('low_limit is', low_lim)
# print('up_limit is', up_lim)

outlier =[]
for x in data:
    if ((x> up_lim) or (x<low_lim)):
         outlier.append(x)
print('Outliers : ', outlier)
sns.boxplot(data)
