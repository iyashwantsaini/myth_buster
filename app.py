
import numpy as np
from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify, render_template
import pickle
from transformers import pipeline
ques_ans = pipeline('question-answering')

app = Flask(__name__)

run_with_ngrok(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    context=request.form['context']
    ques=request.form['ques']
    
    out=ques_ans({'context':context,
                'question': ques  })
    
       
    
 
    output=out['answer']

    


    return render_template('index.html', prediction_text='Answer is :  {}'.format(output))



if __name__ == "__main__":
    app.run()
