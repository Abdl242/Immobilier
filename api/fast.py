import pandas as pd
#from trainer.trainer import Trainer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import os
from typing import Union

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# define a root `/` endpoint
@app.get("/")
def index():
    return {"Status": "Up and running"}

#Trainer().train()
app.state.model=joblib.load(os.path.join("model", "model.joblib"))

# Implement a /predict endpoint
#['Nombre de lots','year','Nombre pieces principales','Surface reelle bati','Code postal']
@app.get("/predict")
def predict(nb_lot:int,
            year:int,
            nb_rooms:int,
            surface:float,
            zip:int):


            X_pred = pd.DataFrame(dict(
                nb_lot=[nb_lot],
                year=[year],
                nb_rooms=[nb_rooms],
                surface=[surface],
                zip=[zip]
            ))

            return {
                "prix M2": int(app.state.model.predict(X_pred)[0]),
                "Prix logement": int(app.state.model.predict(X_pred)[0])*surface
                }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
