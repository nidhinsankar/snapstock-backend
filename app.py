from flask import Flask,jsonify,request
import models

app = Flask(__name__)

@app.route('/products',methods=['GET'])
def products():  # GET ALL PRODUCTS
    return jsonify(models.products)

@app.route('/addproduct',methods=['POST'])
def addProduct():
    jsonData = request.json
    # models.products.append(jsonData)
    return jsonify({"result":"added successfully","data":jsonData})

@app.route('/deleteproduct/<int:productid>',methods=['DELETE'])
def deleteProduct(productid):
    for product in models.products:
        if product["id"] == productid:
            selectedProduct = models.products.index(product)
            return jsonify({"selected":models.products[selectedProduct]})
    else:
        return jsonify({"result":"product not found"})
    # del models.products[selectedProduct]

@app.route('/updateproduct/<int:productid>',methods=['PUT'])
def editProduct(productid):
    for product in models.products:
        if product["id"] == productid:
            selectedProduct = models.products.index(product)
            return jsonify({"selected":models.products[selectedProduct]})
    else:
        return jsonify({"result":"product not found"})
    # print(selectedProduct)
    # return jsonify({"resultStatus":"successfully done"})

@app.route('/product/<int:productid>',methods=['GET'])
def singleProduct(productid):
    for product in models.products:
        if product["id"] == productid:
            return jsonify({"product":product})
    else:
        return jsonify({"result":"product not found"})