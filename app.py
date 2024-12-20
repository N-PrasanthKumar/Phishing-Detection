from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

# Load the pre-trained model
file = open("pickle/model.pkl", "rb")
gbc = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)  # Extract features for prediction

        # Predict phishing or non-phishing
        y_pred = gbc.predict(x)[0]
        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

        pred = f"It is {y_pro_phishing*100:.2f}% safe to go"
        return render_template('index.html', xx=round(y_pro_non_phishing, 2), url=url)
    return render_template("index.html", xx=-1)

if __name__ == "__main__":
    app.run(debug=True)
