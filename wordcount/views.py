from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
	return render(request,'home.html')

def about_page(request):
	return render(request,'about_page.html')

def count(request):
	data=request.GET['fulltextarea']
	word_list=data.split()
	list_length=len(word_list)

	return render(request,'count.html', {'words' : list_length, 'fulltext': data})



