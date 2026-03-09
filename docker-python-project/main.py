import requests

def fetch_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    print("=== Cat Fact API ===")
    print(f"Status code : {response.status_code}")
    print(f"Content     : {response.json()}")

def fetch_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    print("\n=== Dog Image API ===")
    print(f"Status code : {response.status_code}")
    print(f"Content     : {response.json()}")

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    print("\n=== Random Joke API ===")
    print(f"Status code : {response.status_code}")
    print(f"Content     : {response.json()}")

if __name__ == "__main__":
    fetch_cat_fact()
    fetch_dog_image()
    fetch_joke()
