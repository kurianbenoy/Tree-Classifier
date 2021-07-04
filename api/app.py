from flask import Flask
from fastai.vision.all import *

app = Flask(__name__)

@app.route("/predict/tree")
def predict_tree():
    learn_inf = load_learner("export.pkl")
    # img = PILImage.create(upload_btn.data[-1])
    pred, pred_idx, probs = learn_inf.predict(img)
    return pred
