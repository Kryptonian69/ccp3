from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': data})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    
    if item:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    new_item = {
        'id': len(data) + 1,
        'name': request.json['name']
    }
    data.append(new_item)
    return jsonify({'message': 'Item added successfully', 'item': new_item}), 201

if __name__ == '__main__':
    app.run(debug=True)
