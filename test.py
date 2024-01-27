from flask import Flask, request, jsonify
from textcortex import TextCortex
import random

app = Flask(__name__)

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key="gAAAAABls7qEekUMnPrxByde9262FiqV42PrOvYy4fx0NKTR1dU14zQKwKYlydo9M7rTN3ILh1GUdRserD7Mh1yV5Nsl7GQpQolB8LhnivDJy9vPQZD7ejY12nVHADQlBTqUwb_yYnle")

# Generate Product Descriptions using Hemingwai
@app.route('/generate_description', methods=['GET'])
def generate_description():
    sentence = request.args.get('text', '')
    temperature = random.randint(0, 1)
    
    if not sentence:
        return jsonify({'error': 'Please provide a sentence in the "text" parameter'}), 400

    product_description = hemingwai.generate(prompt=f"generate text notification for engaging users in {sentence}", token_count=20, temperature=temperature)
    result = product_description[0]['text']

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
