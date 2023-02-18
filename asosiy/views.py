from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View


# Create your views here.

class Loginview(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(user, request)
        return redirect('/bolim/')

class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class Bolimlarview(View):
    def get(self, request):
        return render(request, 'bulimlar.html')




