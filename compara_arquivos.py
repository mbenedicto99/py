import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file1 = open('log.txt', 'r')
Lines = file1.readlines()
file2 = open('log_new.txt', 'w')
for line in Lines:
new = line[ :10] + ',' + line[10:19] + ',' + line[19: ]
file2.write(new)
file2.close()

df = pd.read_csv('log_new.txt', sep=',', header=None, names=['Date', 'Time', 'Info'])

df['Hours'] = df['Time'].str[:3]
df = df[df['Info'].str.contains('LCP down')]

#print(df)

#df.info()

plt.figure(figsize = (10,9))
sns.countplot(x ='Hours', data = df.sort_values(by=['Hours']))
plt.show()
