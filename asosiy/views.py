from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *


# Create your views here.

class Loginview(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        user = authenticate(username = request.POST.get('l'),
                     password = request.POST.get('p'))
        if user is None:

            return redirect("/")

        login(request, user)
        return redirect('/bolim/')

class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class Bolimlarview(View):
    def get(self, request):
        return render(request, 'bulimlar.html')
class Mahsulotlarview(View):
    def get(self, request):



        data = {
            'mahsulotlar': Mahsulot.objects.filter(ombor=Ombor.objects.get(user=request.user)),


        }
        return render(request, 'products.html', data)


class MahsulotdeleteView(View):
    def get(self, request, pk):
        pr = Mahsulot.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect('mahsulotlar')

class MahsulotupdateView(View):
    def get(self, request, pk):
        pr = Mahsulot.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):

            return render(request, 'product_update.html', {'product' : pr})
    def post(self,request, pk):
        Mahsulot.objects.filter(id=pk).update(
            miqdor = request.POST.get('amount'),
            narx = request.POST.get('price'),
        )
        return redirect('mahsulotlar')
class Clientview(View):
    def get(self,request):
        data = {
            'clientlar': Client.objects.filter(ombor=Ombor.objects.get(user=request.user)),
            'forma':ClientForm
        }
        return render(request, 'clients.html', data)
    def post(self, request):
        if request.user.is_authenticated:
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('/bolim/clientlar/')
            return redirect('/bolim/')
        return redirect('/')









