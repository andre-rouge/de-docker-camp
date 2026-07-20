import sys
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

month = int(sys.argv[1])

df.to_parquet(f'output_{month}.parquet')

print(df.head())

