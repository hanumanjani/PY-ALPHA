import pickle
cars = ["audi","bmw","maruti","farari"]
file = "mycar.pkl"
filobj = open(file, 'wb')
pickle.dump(cars, filobj)