from flask import Flask,jsonify
import models

app = Flask(__name__)

@app.route('/')
def products():  # GET ALL PRODUCTS
    return jsonify(models.products)

