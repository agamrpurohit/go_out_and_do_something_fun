import numpy as np
import pandas as pd

class ActivitiesCache:
    pd = __import__('pandas')

    def __init__(self):
        self.activities = self.pd.DataFrame()

    def data_import(self):
        # Establish connection with database, import data
        # In absence of DB, use MOCK dataset
        dir = 'recommendation_engine/mock_data/'
        self.activities = self.pd.read_csv(dir + 'MOCK_MERGED.csv', index_col=0)

    def data_prep(self):
        if not self.activities.empty:
            # Next line drops time open - time close. Will be removed later
            self.activities = self.activities.drop(['time_open', 'time_close'], axis=1)

            ohe_df = self.pd.DataFrame()

            # Iterate through columns, either OHE or normalize
            for column in self.activities:
                columnSeriesObj = self.activities[column]
                if columnSeriesObj.dtype == 'object':
                    # OneHotEncode
                    ohe = self.pd.get_dummies(columnSeriesObj)
                    ohe_df = self.pd.concat([ohe_df, ohe], axis=1)
                    self.activities = self.activities.drop(column, axis=1)

                if columnSeriesObj.dtype == 'bool':
                    # Single Encoding
                    self.activities[column] = columnSeriesObj.replace([True, False], [1, 0])

                if columnSeriesObj.dtype == 'int64' and column != 'id':
                    # Normalize
                    mn, mx = min(columnSeriesObj.values), max(columnSeriesObj.values)
                    self.activities[column] = (columnSeriesObj.values-mn)/(mx-mn)
            self.activities = self.pd.concat([self.activities, ohe_df], axis=1)
        pass

if __name__ == "__main__":
    a = ActivitiesCache()
    a.data_import().data_prep()
    print(a.activities)
