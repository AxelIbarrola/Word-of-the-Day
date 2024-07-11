import requests

def get_word():
    
    end_point = 'https://random-word-api.vercel.app/api'

    response = requests.get(end_point)
    data = response.json()

    return data[0]
