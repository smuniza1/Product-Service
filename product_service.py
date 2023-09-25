# product_service.py

from flask import Flask, request, jsonify

app = Flask(__name__)

#product data with name, price, and quantity in stock of each product in list.
product_data = [
    {"id": 1, "name": "Chips", "price": 1.50, "quantity": 330},
    {"id": 2, "name": "Cereal", "price": 2.00, "quantity": 150},
]

#Endpoint 1: Get list of available products. Including name, price, & quantity in stock.
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(product_data)

#Endpoint 2: Get details about specific product by its ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_details(product_id):
    #print product_data using product's ID
    product = next((p for p in product_data if p["id"] == product_id), None)
    if product is not None:
        return jsonify(product)
    return jsonify({"Product not found"}), 404

#Endpoint 3: Add new grocery products to inventory. Must include name, price, & quantity.
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if 'name' in data and 'price' in data and 'quantity' in data:
        #append product_data's list with new_product
        new_product = {
            "id": len(product_data) + 1,
            "name": data['name'],
            "price": data['price'],
            "quantity": data['quantity']
        }
        product_data.append(new_product)
        return jsonify(new_product), 201
    return jsonify({"The new product's data is incomplete."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
