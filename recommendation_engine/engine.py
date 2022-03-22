from cache import *

class Engine:
    """
    This class provides recommendations based on the input history stack
    """
    pd = __import__('pandas')
    data = __import__('cache')
    np = __import__('numpy')
    scp = __import__('scipy.spatial')

    def __init__(self):
        self.availables = self.pd.DataFrame()
        self.centroid = self.pd.Series(dtype='int64')


    def load_clean_data(self):
        activities = self.data.ActivitiesCache()
        activities.data_import()
        activities.data_prep()
        self.availables = activities.activities
        pass

    def get_centroid(self, likes):
        # Drop id column, it is irerleveant for the calculation
        likes = likes.drop('id', axis=1)
        n = len(likes)

        # start out with an empty centroid
        centroid = self.pd.Series(index=likes.keys(), dtype='int64')
        centroid = centroid.replace(np.nan, 0)

        # iterate over rows,calculate the centroid
        for idx, row in likes.iterrows():
            centroid += (1/n) * row

        self.centroid = centroid
        pass

    def get_similarity(self, availables, centroid):

        availables = availables.drop('id', axis=1)
        sims = []

        for idx, row in availables.iterrows():
            dist = self.scp.spatial.distance.cosine(row.values, centroid.values)
            sims.append(1-dist)

        # turn sims into a df, concat with availables
        similarity = self.pd.DataFrame(sims, columns=['cosine_similarity'])
        self.availables = self.pd.concat([self.availables, similarity], axis=1)
        pass

    def filter_by_similarity(self, availables):
        self.availables = availables.sort_values(by='cosine_similarity',
                                                 ascending=False)
        pass


if __name__ == "__main__":
    gen = Engine()
    gen.load_clean_data()
    # print(gen.availables)
    gen.get_centroid(gen.availables)
    gen.get_similarity(gen.availables, gen.centroid)
    gen.filter_by_similarity(gen.availables)
    print(gen.availables)
