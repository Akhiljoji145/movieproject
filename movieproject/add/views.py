from django.shortcuts import render,redirect,get_object_or_404
from movie.models import Movie,Category
from django.contrib.auth.models import User
from .forms import UpdateMovieForm,ProfileForm
from .models import Rating
# Create your views here.
def addmovie(request, user_id):
    user = get_object_or_404(User, id=user_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('img')
        trailer = request.POST.get('trailer')
        banner = request.FILES.get('banner')
        desc = request.POST.get('desc')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)  # Get the Category instance
        date = request.POST.get('date')

        movie = Movie(name=name, image=image, trailer=trailer, banner=banner, desc=desc, category=category, relea_date=date, user=user.username)
        movie.save()
        return redirect('/')
    return render(request, 'add_movie.html', {'user': user, 'category': categories})
def deletemovie(request,mov_id):
	movie=Movie.objects.get(id=mov_id)
	movie.delete()
	return redirect('/')
def update(request,mov_id):
	movie=Movie.objects.get(id=mov_id)
	form=UpdateMovieForm(request.POST or None,request.FILES,instance=movie)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'update.html',{'movie':movie,'form':form})

def rate(request):
	if request.method=='POST':
		rate=request.POST.get('rate')
		review=request.POST.get('review')
		movie=request.POST.get('movie')
		user=request.POST.get('user')
		rating=Rating(rating=rate,review=review,movie=movie,user=user)
		rating.save()
		return redirect('/')
	return redirect('moviedetail/<str:user_name>/<int:mov_id>/')

def UpdateUser(request,user_id):
	user=User.objects.get(id=user_id)
	form=ProfileForm(request.POST or None,request.FILES,instance=user)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'update.html',{'user':user,'form':form})

