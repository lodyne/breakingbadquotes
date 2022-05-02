import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    response = requests.get(url) 
    data = response.json()
    return render(request,'core/index.html',{'data':data})
