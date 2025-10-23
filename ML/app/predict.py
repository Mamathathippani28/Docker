import pickle
pickled_model = pickle.load(open('model.pkl', 'rb'))

si1 = [[0,0,0,0,0,0,0,0,0,0,0,0,2.0,1.30,103.0,106.0]]
result = pickled_model.predict(si1)

if result[0] == 0:
    print("Congrats! Thyroid Not Detected.")
else:
    print("Sorry! It's Thyroid.")


