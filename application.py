from flask import  Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from SOURCE.pipelines.prediction_pipelines import Custom_Data,PredictPipeline

application=Flask(__name__)
web_app=application

# routing for the home page

@web_app.route('/')
def index():
    return render_template('index.html')

@web_app.route('/predictdata',methods=['GET','POST'])
def predict_data_point(): #inside this func i will getting my data & doing the prediction
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=Custom_Data(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))  

        )
        pred_df=data.get_data_as_DataFrame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.model_prediction(pred_df)
        return render_template('home.html',results=results[0])

if __name__=='__main__':
    web_app.run(host="0.0.0.0")
