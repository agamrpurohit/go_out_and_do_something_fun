import pandas as pd

files = ['CONCERT', 'DINING', 'HIKE', 'MOVIES']

df = pd.DataFrame()

for file in files:
    filename  = './recommendation_engine/mock_data/MOCK_' + file + '.csv'
    chunk = pd.read_csv(filename)
    if df.empty:
        df = chunk
    else:
        df = pd.concat([df, chunk], ignore_index=True)

# make sure cost is positive
df['cost'] = abs(df['cost'])

# Export to combined file
df.to_csv('./recommendation_engine/mock_data/MOCK_MERGED.csv')
