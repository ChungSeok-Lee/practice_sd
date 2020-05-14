# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pickle


class xy4():
  def __init__(self):
    pass
  def getPredict4(self, a, b):
    c, aaa = divmod(a,2)
    cc = c/2
    result = b*3 - cc
    return result

def home(request):    
    NUM_X = int(request.GET['xx'])
    NUM_Y = int(request.GET['yy'])

    tem = xy4()
    result = tem.getPredict4(NUM_X,NUM_Y)
    requestDict = {'result_response': result}
    return JsonResponse(requestDict)




