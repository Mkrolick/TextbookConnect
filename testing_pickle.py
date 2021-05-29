import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }

x = pickle.dump( favorite_color, open( "save.p", "wb" ) )
print(x)
