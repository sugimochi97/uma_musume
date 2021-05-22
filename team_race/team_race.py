#%%
import pandas as pd

RACE_RESULT_PATH = 'チーム競技場データver1.0.0.csv'
TEAME_DATA_PATH = 'チーム編成ver1.0.0.csv'

df = pd.read_csv(RACE_RESULT_PATH)
print(df)
# %%
