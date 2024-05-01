from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,Category
from add.models import Rating
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import CustomUserCreationForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request):
	movie_list=Movie.objects.all().order_by('name')
	paginator=Paginator(movie_list,6)
	try:
		page=int(request.GET.get('page','1'))
	except:
		page=1
	try:
		movie=paginator.page(page)
	except (EmptyPage,InvalidPage): 
		movie=paginator.page(paginator.num_pages)
	return render(request,'movielist.html',{'movie':movie})

def login(request):
    return render(request, 'login.html')

def moviedetail(request,mov_id):
	movie=Movie.objects.get(id=mov_id)
	user=User.objects.all()
	try:
		rating=Rating.objects.all().filter(movie=mov_id).values()
		return render(request,'moviedetail.html',{'movie':movie,'rating':rating,'user':user})
	except Rating.DoesNotExist:
		return render(request,'moviedetail.html',{'movie':movie,'user':user})

def usermoviedetail(request,user_name,mov_id):
	movie=Movie.objects.get(id=mov_id)
	user=User.objects.get(id=user_name)
	try:
		rating=Rating.objects.all().filter(movie=mov_id).values()
		return render(request,'moviedetail.html',{'movie':movie,'user':user,'rating':rating})
	except Rating.DoesNotExist:
		return render(request,'moviedetail.html',{'movie':movie,'user':user})
def logout_view(request):
	logout(request)
	return redirect('/')

def user_home(request):

	movie=Movie.objects.all()
	return render(request,'movielist.html',{'movie':movie})

def userlogin(request):
 	if request.method == 'POST':
 		name = request.POST.get('name')
 		passw = request.POST.get('pass')
 		try:
 			user = User.objects.get(username=name)
 			movie=Movie.objects.all()
 			if user.check_password(passw):
 				return render(request,'user_movielist.html',{'user':user,'movie':movie})
 			else:
 				return render(request,'login.html')
 		except User.DoesNotExist:  
 			return render(request, 'register.html')
 	return render(request, 'login.html')

def user_reg(request):
	if request.method == 'POST':
		form =CustomUserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			return redirect('/login/')
	else:
		form=CustomUserCreationForm() 
	return render(request,'register.html',{'form':form})

def user_details(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request,'user_details.html', {'user': user})

def category(request, cat_name):
    if cat_name is not None:
        category = get_object_or_404(Category, genre=cat_name)
        movies = Movie.objects.filter(category=category)
    else:
        return redirect('/')
    return render(request, 'category.html', {'movies': movies, 'category': category})