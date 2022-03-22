import user, weather, cache, engine

if __name__ == "__main__":

    usr = user.User()

    usr_data = cache.Cache()
    usr_data.data_import()
    usr_data.data_prep()

    generator = engine.Engine()

    # While app is running
    while len(usr.recommendations) < 10:
        centroid = generator.centroid(usr.likes)
