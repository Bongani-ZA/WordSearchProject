from django.shortcuts import render
import requests
import json


def home(request):
    return render(request, 'home.html')


def search(request):
    word = request.GET.get('word')
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

    response = requests.get(url)
    response_text = response.text
    data = json.loads(response_text)
    json.dump(data, open('data.json', 'w'), indent=4)
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    return render(request, 'search.html',
                  {'word': word, 'definition': definition})
