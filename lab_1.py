import pandas as pd
df = pd.read_csv(r"C:\Users\salat\Downloads\archive (3)\marksheet.csv")
print(df)

# print("Head : ")
# print(df.head)

# print("Shape : ")
# print(df.shape)

# print("Columns : ")
# print(df.columns)

# print("Information : ")
# print(df.info())

print("Describe : ")
print(df.describe)