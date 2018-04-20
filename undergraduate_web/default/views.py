from django.shortcuts import render, render_to_response

# Create your views here.

def indexPage(request):
	return render(request,"hello.html",locals())

def testPage(request):
	return render(request, "test.html",locals())
