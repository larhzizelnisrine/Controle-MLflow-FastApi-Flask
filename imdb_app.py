from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
#import string


app = FastAPI()
class review(BaseModel):
    input: str
import pickle, numpy

import os
import onnxruntime as rt


dir_path = os.path.dirname(os.path.realpath(__file__))
model_name = "model.onnx"
preprocess_name = "preprocessing.pkl"
preprocess = pickle.load(open(f"{dir_path}\\models\\{preprocess_name}", 'rb'))
sess = rt.InferenceSession(f"{dir_path}\\models\\{model_name}")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name


@app.get("/")
def home():
 return {'API for imdb reveiws sentiment analysis'}


@app.post('/make_predictions')
async def make_predictions(features: review):
    return({"prediction":str(sess.run([label_name], {input_name:numpy.array(preprocess.transform([str(review).lower()]))})[0][0])})
if __name__ == "__main__":
 uvicorn.run("imdb_app:app", host="0.0.0.0", port=8080, reload=True)
