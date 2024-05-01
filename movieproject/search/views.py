from django.shortcuts import render
from django.http import HttpResponse
from movie.models import Movie
from django.db.models import Q
# Create your views here.
def SearchResult(request):
	movies=None
	query=None
	if 'q' in request.GET:
		query=request.GET.get('q')
		if query:
			movies=Movie.objects.all().filter(Q(name__contains=query)) 
	return render(request,'search.html',{'query':query,'movies':movies})