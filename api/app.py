import os

from flask import Flask, request, flash, redirect, render_template
from fastai.vision.all import *
from fastai.vision.core import PILImage
from fastai.vision.all import load_learner
from werkzeug.utils import secure_filename

from api.utils.constants import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from api.utils.cors import crossdomain

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # specify upload file limit
app.config["SECRET_KEY"] = "secret!"  # for flash messages


def allowed_files(filename):
    """Reurn list of allowed urls"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def ml_inference(filename):
    learn_inf = load_learner("../export.pkl")
    img = PILImage.create(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    pred_class, pred_idx, outputs = learn_inf.predict(img)
    return pred_class


@app.route("/predict/tree", methods=["POST", "GET"])
@crossdomain(origin="*")
def predict_tree():
    """Predict the tree using Flask APIs"""
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        print(file)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            tree_class = ml_inference(filename)
            return tree_class
    return "Not supported"


@app.route("/")
def index():
    return render_template("index.html", **{"greeting": "Hello from Flask!"})
