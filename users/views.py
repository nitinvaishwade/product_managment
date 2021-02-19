from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm, RegisterForm

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            print("username login======", username)
            print("password login======", password)
            user = authenticate(username=username, password=password)
            print("user==========", user)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # add_user = form.save(commit=False)
            # add_user.active=True
            # add_user.save()
            print("register form save=========")
            username = form.cleaned_data.get('username')
            print("register username======", username)
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            print("register user===========",user)
            print("dddddddddddddd")
            print("register password==========",raw_password)
            # login(request, user)
            # return redirect('dashboard')
            if user is not None:
                login(request, user)
                # messages.info(request, "You are now logged in")
                return redirect('dashboard')
            else:
                # messages.error(request, "Invalid username or password.")
                pass
        else:
            # messages.error(request, "Invalid password.")
            form = RegisterForm()

    else:
        form = RegisterForm()
    return render(request = request,
            template_name = "users/register.html",
            context={"form":form})


# from .models import User
# from django.contrib.auth.models import Group
# from rest_framework import viewsets
# from rest_framework import permissions
# from .serializers import UserSerializer, GroupSerializer











# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]