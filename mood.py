import requests
import random

def fetch_random_image(mood):
    # Unsplash API endpoint for random images
    mood = mood + " art"
    access_key =   # Replace with your Unsplash API access key
    url = f"https://api.unsplash.com/photos/random?query={mood}&client_id={access_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return data["urls"]["regular"]  # URL for the image
    except Exception as e:
        print("Error fetching image:", e)
        return None

def fetch_random_quote(mood):
    # Using a free quotes API (e.g., ZenQuotes)
    url = "https://zenquotes.io/api/quotes"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        # Filter quotes by mood (randomly select if there's no mood match)
        filtered_quotes = [q for q in data if mood in q['q'].lower()]
        if filtered_quotes:
            quote = random.choice(filtered_quotes)
        else:
            quote = random.choice(data)  # Fallback to any quote if no match
        return f"{quote['q']} – {quote['a']}"
    except Exception as e:
        print("Error fetching quote:", e)
        return "Stay positive and keep going!"

def display_mood_art_and_quote():
    # Prompt user for a mood
    moods = ["happy", "anxious", "sad", "excited", "depressed"]
    print("Choose a mood from the list:", moods)
    selected_mood = input("Enter your mood: ").lower()
    
    if selected_mood in moods:
        print(f"\nFetching data for mood: {selected_mood.capitalize()}...")
        
        # Fetch image and quote
        image_url = fetch_random_image(selected_mood)
        quote = fetch_random_quote(selected_mood)
        
        if image_url:
            print(f"\nHere's a piece of artwork related to your mood: {image_url}")
        else:
            print("\nCould not fetch an image at this time.")
        print(f"Quote: {quote}")
    else:
        print("Invalid mood. Please choose from the given list.")

# Run the function
display_mood_art_and_quote()
