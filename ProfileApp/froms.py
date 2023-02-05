from django import forms
from .models import *
class ProductForm(forms.Form):
    PBrand = [('Zara', 'Zara'), ('Uniqlo', 'Uniqlo'), ('H&M', 'H&M'), ('MUJI', 'MUJI'), ('Lacoste', 'Lacoste'), ]
    PSize = [('Free Size','Free Size'),('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL')]
    PType = [('เสื้อยืด', 'เสื้อยืด'),('เสื้อแขนยาว', "เสื้อแขนยาว")]
    PID = forms.CharField(max_length=10 ,label="รหัสสินค้า",required=True,widget=forms.TextInput)
    PName = forms.CharField(label="ชื่อสินค้า",required=True,widget=forms.TextInput)
    Price = forms.IntegerField(min_value=1, label='ราคาสินค้า',required=True,widget=forms.NumberInput)
    Brand = forms.CharField(widget=forms.Select(choices= PBrand),required=True,label='แบรนด์สินค้า')
    Size = forms.CharField(widget=forms.Select(choices= PSize),required=True,label='ไซร์สินค้า')
    Type = forms.ChoiceField(widget=forms.RadioSelect, choices=PType , label='ประเภทสินค้า')
    Amount = forms.IntegerField(min_value=1 , label='จำนวนสินค้า',required=True)

