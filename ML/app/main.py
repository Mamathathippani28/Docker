from fastapi import FastAPI
import pickle
import sklearn

app = FastAPI()

def predict_result():
    pickled_model = pickle.load(open('model.pkl', 'rb'))

    si1 = [[0,0,0,0,0,0,0,0,0,0,0,0,2.0,1.30,103.0,106.0]]
    result = pickled_model.predict(si1)

    res = "Still trying to predict"

    if result[0] == 0:
        res = "Congrats! Thyroid Not Detected."
    else:
        res = "Sorry! It's Thyroid."
    return res
@app.get("/")
async def root():
    result = predict_result()
    return result
