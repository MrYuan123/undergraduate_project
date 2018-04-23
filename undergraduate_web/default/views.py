from django.shortcuts import render, render_to_response
import json
from django.http import HttpResponse

# Create your views here.

def indexPage(request):
	return render(request,"tables.html",locals())

def testPage(request):
	return render(request, "test.html",locals())

def sortM():
	print("return json data")
	response_data = dict()
	response_data["1"] = "11111"
	response_data["2"] = "1dddd"
	return HttpResponse(json.dumps(response_data),content_type = "application/json")
