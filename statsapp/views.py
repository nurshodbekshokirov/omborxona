from django.shortcuts import render,redirect
from .models import *

from django.views import View

from asosiy.models import Mahsulot, Client, Ombor
class Statsviewdelete(View):
    def get(self, request, pk):
        pr = Stats.objects.get(id=pk).mahsulot
        if pr.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect('stats')
class Statsviewupdate(View):
    def get(self, request, pk):
        pr = Stats.objects.get(id=pk)
        if pr.mahsulot.ombor == Ombor.objects.get(user=request.user):
            return render(request, 'stats_update.html', {'stats': pr})

    def post(self, request, pk):

        Stats.objects.filter(id=pk).update(

            miqdori= request.POST.get('miqdori'),
            summa = request.POST.get('summa'),
            tolandi = request.POST.get('tolandi')

        )
        return redirect('stats')





class Statsview(View):
    def get(self, request):
        stats = Stats.objects.filter(client__ombor__user=request.user)
        soz = request.GET.get('soz')
        if soz is  not None:

            stats = Stats.objects.filter(client__ombor__user=request.user, mahsulot__nom__contains=soz) | Stats.objects.filter(client__ombor__user=request.user, client__ism__contains=soz)


        data = {
            'stats':stats,
            'mahsulotlar': Mahsulot.objects.filter(ombor__user=request.user),
            'clientlar': Client.objects.filter(ombor__user=request.user)

        }
        return render(request, 'stats.html',data)
    def post(self, request):
        if request.user.is_authenticated:
            farq = int(request.POST.get('summa')) - int(request.POST.get('tolandi'))
            nasiya =  Client.objects.get(id=request.POST.get('client')).qarz + farq
            if farq>0:
                qoldi = farq
            else:
                qoldi = 0


            Stats.objects.create(


                mahsulot= Mahsulot.objects.get(id=request.POST.get('mahsulot')),
                client = Client.objects.get(id=request.POST.get('client')),
                sana = request.POST.get('sana'),
                miqdori = request.POST.get('miqdor'),
                summa = request.POST.get('summa'),
                tolandi = request.POST.get('tolandi'),
                qoldi = qoldi


            )
            # nasiya = Client.objects.get(id=request.POST.get('Client')).qarz + int(request.POST.get('qoldi'))
            Client.objects.filter(id=request.POST.get('client')).update(
                qarz = nasiya
            )

            return redirect('stats')


