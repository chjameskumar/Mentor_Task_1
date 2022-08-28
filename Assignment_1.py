import pandas as pd

column_names = ['Class Name','Left-Weight','Left-Distance','Right-Weight','Right-Distance']
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data', names = column_names)

# Check the number of data points and features in the data.

# Find unique values for each column.
print('\n\n')
for i in df:
    print('The unique value of cloumn', i)
    print(df[i].unique())

# Check the data types of values in each column.
print('\n\n')
print('The data types of each column : ')
print(df.dtypes)

# Check basic statistics of data.

print('\n\n')
for i in df:
    print('The sum of columns ',i)
    print(df[i].sum())
print('\n')
for i in df:
    print('The count of column ',i,'is :')
    print(df[i].count())
print('\n')
print('The mean of columns : ')
print(df.mean())
print('\n')
print('The median of columns : ')
print(df.median())

# Add a new column in the data.

print('\n\n')
print('Creating new column which consists values of column Left-Weight multiplied by 2 :')
df['New Column'] = df['Left-Weight']*2
print(df)

# Then drop this column just created.

print('\n\n')
print('Dropping the created new column :')
df = df.drop('New Column', axis =1)
print(df)

# create a new column that has values found as a result of applying some operation on the existing columns.

print('\n\n')
print('creating new column in that adding values of Left-weight & Right-weight :')
df['New Column'] = df['Left-Weight'] + df['Right-Weight']
print(df)

# Access elements using loc and iloc.

print('\n\n')
print('Printing first row in Series format : ')
print(df.iloc[0])
print('\n')
print('Printing first row in DataFrame format : ')
print(df.iloc[[0]])
print('\n')
print('Acceessinfg some values using iloc: ')
print(df.iloc[[1],[1,3]])
print(df.iloc[[324,46],[1,2]])
print(df.iloc[[601,204],[2,3]])
print('\n')
print('Acceessinfg some values using loc: ')
print(df.loc[1,'Class Name'])
print(df.loc[65,'Left-Weight'])
print(df.loc[132,'Right-Weight'])
print(df.loc[335,'Left-Distance'])
print(df.loc[456,'Right-Distance'])

# Check if there are missing values. If yes, which column.

print('\n\n')
print('Checking for any missing value : ')
print(df.isnull().all())