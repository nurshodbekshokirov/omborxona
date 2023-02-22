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
    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom = request.POST.get('pr_name'),
                brend = request.POST.get('pr_brand'),
                miqdor = request.POST.get('pr_amount'),
                narx = request.POST.get('pr_price'),
                olchov = request.POST.get('pr_olchov'),
                ombor = Ombor.objects.get(user=request.user)
            )
            return redirect('mahsulotlar')
        return redirect('/')


class MahsulotdeleteView(View):
    def get(self, request, pk):
        pr = Mahsulot.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect('mahsulotlar')

class ClientsdeleteView(View):
    def get(self, request, pk):
        pr = Client.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect('clientlar')



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
class Clientupdateview(View):
    def get(self,request, pk):
        pr = Client.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            return render(request, 'client_update.html', {'client':pr})
    def post(self, request, pk):


        Client.objects.filter(id=pk).update(
            tel = request.POST.get('client_phone')
        )
        return redirect('clientlar')
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
class Client_search(View):
    def get(self, request):
        data = {
            'clientlar': Client.objects.filter(ombor=Ombor.objects.get(user=request.user)),
        }
        return render(request, 'clients.html', data)
    def post(self, request):
        qidiruv_soz = request.POST.get('qidirish')
        client = Client.objects.filter(ism__contains=qidiruv_soz) | Client.objects.filter(nom__contains=qidiruv_soz) | Client.objects.filter(tel__contains=qidiruv_soz) | Client.objects.filter(manzil__contains=qidiruv_soz)
        if Client.objects.filter(ombor=Ombor.objects.get(user=request.user)):
            data = {'clientlar': client}
            return render(request, 'clients.html', data)
        return redirect('clientlar')
class Mahsulotsearch(View):
    def get(self, request):



        data = {
            'mahsulotlar': Mahsulot.objects.filter(ombor=Ombor.objects.get(user=request.user)),



        }
        return render(request, 'products.html', data)
    def post(self,request):
        qidiruv_soz = request.POST.get('qidirish')
        mahsulot = Mahsulot.objects.filter(nom__contains=qidiruv_soz) | Mahsulot.objects.filter(brend__contains=qidiruv_soz) | Mahsulot.objects.filter(kelgan_sana__contains=qidiruv_soz)
        if Mahsulot.objects.filter(ombor=Ombor.objects.get(user=request.user)):
            data = {
                'mahsulotlar': mahsulot

            }
            return render(request, 'products.html', data)
        return redirect('mahsulotlar')











