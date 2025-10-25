"""
Counter Service - A RESTful API for managing counters
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for counters
counters = {}


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})


@app.route('/counters', methods=['GET'])
def get_counters():
    """Get all counters"""
    return jsonify(counters)


@app.route('/counters/<name>', methods=['GET'])
def get_counter(name):
    """Get a specific counter"""
    if name not in counters:
        return jsonify({'error': 'Counter not found'}), 404
    return jsonify({name: counters[name]})


@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a new counter"""
    if name in counters:
        return jsonify({'error': 'Counter already exists'}), 409
    
    counters[name] = 0
    return jsonify({name: counters[name]}), 201


@app.route('/counters/<name>/increment', methods=['PUT'])
def increment_counter(name):
    """Increment a counter"""
    if name not in counters:
        return jsonify({'error': 'Counter not found'}), 404
    
    counters[name] += 1
    return jsonify({name: counters[name]})


@app.route('/counters/<name>/decrement', methods=['PUT'])
def decrement_counter(name):
    """Decrement a counter"""
    if name not in counters:
        return jsonify({'error': 'Counter not found'}), 404
    
    counters[name] -= 1
    return jsonify({name: counters[name]})


@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete a counter"""
    if name not in counters:
        return jsonify({'error': 'Counter not found'}), 404
    
    del counters[name]
    return jsonify({'message': 'Counter deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)