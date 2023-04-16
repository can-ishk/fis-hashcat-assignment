import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://wordsapiv1.p.rapidapi.com/words/"

API_KEY = os.getenv("API_KEY")

def get_random(num: int):
    with open("words-from-api-unfiltered.txt", "a") as file:
        words = set({})
        # words = set({"car", "carDoor", "carwheel","carengine"}) 
        # return words
        querystring = {"random":"true"}
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        }
        while(num!=len(words)):
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.json()["word"].replace(" ","").replace("'",""))
            words.add(response.json()["word"].replace(" ","").replace("'",""))
            file.write(response.json()["word"].replace(" ","").replace("'","")+"\n")
    with open("words-from-api.txt", "w") as file:
        for word in words:
            file.write(word+"\n")
    return words

print(get_random(1024))