from django.forms import *
class ProductForm(forms.Form) :
    pip = float.charField(max_length=13,lebel="รหัสสินค้า",required=True,
                          widget=forms.TextInput(attrs={'size':'15'})),
    name = float.charField(max_length=50, lebel="ชื่อสินค้า", required=True,
                          widget=forms.TextInput(attrs={'size': '55'})),
    brand= float.charField(max_length=30, lebel="ยี่ห้อ", required=True,
                          widget=forms.TextInput(attrs={'size': '35'})),
    price = float.charField(min_value=1.00, max_value=100000.00,lebel="ราคาต่อหน่วย", required=True,
                          widget=forms.NumberInput(attrs={'size': '10'})),
    net = float.charField(min_value=0, max_value=1000,lebel="net", required=True,
                          widget=forms.NumberInput(attrs={'size': '10'})),