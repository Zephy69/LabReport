import pandas as pd
data={
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
}
df=pd.DataFrame(data)
print("shape:",df.shape)
print("dtype:",df.dtypes)
print("Columns:",df.columns.tolist)
