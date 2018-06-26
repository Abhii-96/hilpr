# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import forms
from django.shortcuts import render
from django.http import HttpResponse
import serial
import time
# Create your views here.

def index(request):
    ser = serial.Serial("socket://10.191.4.236/logging=debug")
    if ser.isOpen:
            i=0
            var1=""
            while i<11:
                size=ser.inWaiting()
                if (size):
                data=ser.read(ser.inWaiting())
                if(data):
                    var1+=str(data)
                    i=i+1
            var1=var1.replace('b','')
            var1=var1.replace("'",'')
            var2=var1[var1.find("-")+1:var1.find("-")+7]
            if var2.isalnum():
                intvar = int(var2)
    else:

        print("serial port is not open")
    ser.close()




    my_dict={'insert_me': "intvar" ,}
    return render(request,'w_measure/index.html',context=intvar)
