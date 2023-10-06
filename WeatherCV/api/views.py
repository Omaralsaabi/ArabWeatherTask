from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import render
from .utils import predict_image
# Create your views here.


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        image = request.FILES['image']
        weather = predict_image(image)
        result = {'class': weather }
        print("result: ", result)
        return render(request, 'api.html', {'result': result})
    return render(request, 'api.html')

