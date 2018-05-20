from django.shortcuts import render, render_to_response
import json
from django.http import HttpResponse,JsonResponse

# Create your views here.

def indexPage(request):
	return render(request,"tables.html",locals())

def testPage(request):
	return render(request, "test.html",locals())

def sortM(request):
	query = request.POST
	if query.get('ID') != '1':
		return JsonResponse({'recommand':[]})
	else:
		print("return json data")
		return_list = list()
		response_data = dict()
		response_data["first"] = "11111"
		response_data["second"] = "1dddd"
		response_data['third'] = 'qqqqss'
		return_list.append(response_data)
		# return HttpResponse(json.dumps(response_data),content_type = "application/json")
		return JsonResponse({'recommand':return_list})
