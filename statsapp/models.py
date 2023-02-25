from django.db import models

from asosiy.models import *


class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    miqdori = models.PositiveSmallIntegerField()
    summa = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField(default=0)
    qoldi = models.PositiveSmallIntegerField(default=0)
    olchov = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.mahsulot}({self.client})[{self.sana}]"

