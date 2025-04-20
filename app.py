import pickle
from markupsafe import escape
from flask import Flask, render_template, request
import pandas as pd
from xgboost import *
from pandas import DataFrame

import pickle

app = Flask(__name__)
  
xgboost_model = pickle.load(open('data.pkl', 'rb'))






@app.route("/", methods = ['POST', 'GET'])
def main():
   
            SQUARE_FT = request.form.get("SQUARE_FT")
           
            

            BHK_NO = request.form.get("BHK_NO.")
            
            city_tier = request.form.get("city_tier")

            
            RESALE = request.form.get("RESALE")
            READY_TO_MOVE = request.form.get("READY_TO_MOVE")
            RERA = request.form.get("RERA")
            UNDER_CONSTRUCTION = request.form.get("UNDER_CONSTRUCTION")

            
            
            input_variables = pd.DataFrame([[BHK_NO, READY_TO_MOVE, RERA, RESALE, SQUARE_FT, UNDER_CONSTRUCTION, city_tier]],
           columns=['BHK_NO', 'READY_TO_MOVE', 'RERA', 'RESALE', 'SQUARE_FT', 'UNDER_CONSTRUCTION', 'city_tier'] , dtype=float, index=['input'])
            

            price = xgboost_model.predict(input_variables)[0]

           

            return render_template("index.html", Price = f"{round(price, 1)}")
           
if __name__ == "__main__":
    app.run(debug=True , port=5001)