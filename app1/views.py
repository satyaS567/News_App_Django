from django.shortcuts import render
import requests
API_KEY = '3ca14b998c424d80a3501dd76af683d4'
# Create your views here.
def index(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&language=en&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&language=en&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']


    context = {
        'articles': articles
    }

    return render(request, 'index.html', context)