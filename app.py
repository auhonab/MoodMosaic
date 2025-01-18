from flask import Flask, jsonify, request, render_template
import requests
import random

app = Flask(__name__)

def fetch_random_image(mood):
    mood = mood + " art"
    access_key = "egqPJIQnj9aX2_NhFIYDSSbSHj11QB_MvvOFLJbntsE"  # Replace with your Unsplash API access key
    url = f"https://api.unsplash.com/photos/random?query={mood}&client_id={access_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["urls"]["regular"]
    except Exception as e:
        print("Error fetching image:", e)
        return None

def fetch_random_quote(mood):
    url = "https://zenquotes.io/api/quotes"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        filtered_quotes = [q for q in data if mood in q['q'].lower()]
        if filtered_quotes:
            quote = random.choice(filtered_quotes)
        else:
            quote = random.choice(data)
        return f"{quote['q']} – {quote['a']}"
    except Exception as e:
        print("Error fetching quote:", e)
        return "Stay positive and keep going!"
@app.route("/")
def home():
    return render_template("index.html")
@app.route('/get_mood_data')
def get_mood_data():
    mood = request.args.get('mood')
    if mood:
        image_url = fetch_random_image(mood)
        quote = fetch_random_quote(mood)
        return jsonify({'imageUrl': image_url, 'quote': quote})
    return jsonify({'imageUrl': None, 'quote': "Invalid mood."})

if __name__ == '__main__':
    app.run(debug=True)