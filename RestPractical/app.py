from flask import Flask, jsonify, request

# 1. Initialize the App
app = Flask(__name__)

# 2. Sample Data (Acting as a fake database)
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'}
]

# 3. Endpoint: Get All Items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': data})

# 4. Endpoint: Get Specific Item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Search for the item in our list
    item = next((item for item in data if item['id'] == item_id), None)
    
    if item:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# 5. Endpoint: Add a New Item
@app.route('/items', methods=['POST'])
def add_item():
    # Create a new item using data sent by the user
    new_item = {
        'id': len(data) + 1,
        'name': request.json['name']
    }
    data.append(new_item)
    return jsonify({'message': 'Item added successfully', 'item': new_item}), 201

# 6. Run the Server
if __name__ == '__main__':
    app.run(debug=True)