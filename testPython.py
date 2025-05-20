import pandas as pd


# def main(n):
#     return n+1
# kk= main(7)
# print(kk)


data = {'Name': ['Kartik', 'Bob', 'Charlie'],
        'Age': [21, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)
# print(df.City)