from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UpdateProfileForm, Youssef,UserCreationForms , UpdateUserForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
# Create your views here.

def doctors_list(request):
    doctors = User.objects.all()
    return render(request, 'user/doctors_list.html',{
        'doctors':doctors,
})

def doctor_detail(request,slug):
    doctor_detail= Profile.objects.get(slug= slug)
    return render(request , 'user/doctor_detail.html', {
        'doctor_detail': doctor_detail,
    })
#######################################LOGIN################################
def user_login(request):
    if request.method == 'POST':
        form = Youssef()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:doctors_list')
    else:
        form = Youssef()
    return render(request , 'user/login.html' , {
    'form': form
    })

    ##########################SIGNUP##############################

def signup(request):
    if request.method == "POST":
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('accounts:doctors_list')
    else:
        form = UserCreationForms(request.POST)
    return render(request , 'user/signup.html', {
        'form':form
    })


#######################################################


def updat_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user)
    if request.method == "POST":
        user_form = UpdateProfileForm(request.POST , instance=request.user)
        profile_form = UpdateUserForm(request.POST ,request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:myprofile')
    return render(request , 'user/update_profile.html', {
        'user_form' : user_form ,
        'profile_form': profile_form,
    })


@login_required()
def myprofile(request):
    return render(request , 'user/myprofile.html', {})