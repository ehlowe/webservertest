from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

def data(request):
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return JsonResponse(data)