from django.shortcuts import render,HttpResponse,redirect
from ProfileApp.froms import *

def idol(request):
    return render(request, 'idol.html')
def interests(request):
    return render(request, 'interests.html')
def product(request):
    return render(request, 'product.html')
def profile(request):
    return render(request, 'profile.html')
def study(request):
    return render(request, 'study.html')
def showmydata(request):
    name =' วชิระ  บุญปก'
    nickname = 'ซี'
    age = '21 ปี'
    weight = '62 KG'
    height = '176 ซม.'
    nationality = 'ไทย'
    sermon = 'พุทธ'
    phone = '098-3239-764'
    birthday = '4 เดือนกรกฎาคม พ.ศ. 2544'
    blood = 'กรุ๊ป A'
    product = [

        ['Cute Press UV Expert','329 บาท','images/1.jpg'],
        ['Za True White ', '300 บาท', 'images/2.jpg'],
        ["L'Oreal Paris UV Perfect Matt & Fresh Long UVA SPF 50+ PA++++ ", '230 บาท', 'images/3.jpg'],
        ['MizuMi UV Water Defense SPF 50+ PA++++ ', '450 บาท', 'images/4.jpg'],
        ['AquaPlus Multi – Protection Sunscreen SPF50+ PA++++ ','320 บาท','images/5.jpg'],
        ['Bioré UV Aqua Rich Watery Essence SPF 50+ PA++++ ', '570 บาท', 'images/6.jpg'],
        ['Anessa Perfect UV Sunscreen Aqua Booster SPF 50+ PA++++ ', '325 บาท', 'images/7.jpg'],
        ['La Roche-Posay Anthelios XL Dry Touch Gel-Cream SPF 50+ ', '630 บาท', 'images/8.jpg'],
        ["Kiehl's Ultra Light Daily UV Defense SPF 50 PA++++ Anti - Pollution ", '640 บาท', 'images/9.jpg'],
        ['Srichand Luminescence Fabulous UV Shield SPF50 PA++++ ', '420 บาท', 'images/10.jpg'],



    ]
    return render(request,'showmydata.html',
                     {'name':name , 'nickname':nickname , 'age':age ,'weight':weight ,'height':height ,'nationality':nationality ,'sermon':sermon
                      ,'phone':phone ,'birthday':birthday ,'blood':blood ,'product':product}
                   )







from ProfileApp.models import *
productList = []
# def show(request):
#
#     # product = Product('p0001','mouse', 'Aser', '500.00', '120')
#     # productList.append(product)
#     # product = Product('p0002', 'keyboard', 'Aser', '500.00', '120')
#     # productList.append(product)
#     # product = Product('p0003', 'screen', 'Aser', '500.00', '120')
#     # productList.append(product)
#     context = {'products': productList}
#     return render(request,'show.html',context)
#
#
# def newProduct(request):
#     if request.method=='POST':
#         id = request.POST['id']
#         name = request.POST['name']
#         brand = request.POST['brand']
#         price = request.POST['price']
#         net = request.POST['net']
#         product = Product(id,name,brand,price,net)
#         productList.append(product)
#         return  redirect('show')
#     else:
#         return render(request,'productnormal.html')

# Create your views here.

lstOurProduct = []

def listProduct(requset):
    context = {'products':lstOurProduct}
    return render(requset,"listProduct.html",context)
def inputProduct(requset) :
    if requset.method == "POST":
        form = ProductForm(requset.POST)
        if form.is_valid() :
            form = form.cleaned_data
            PID = form.get('PID')
            name = form.get('PName')
            price = form.get('Price')
            brand = form.get('Brand')
            size = form.get('Size')
            type = form.get('Type')
            amount = form.get('Amount')
            # id = form.cleaned_data['PID']
            # name = form.cleaned_data['PName']
            # price = form.cleaned_data['Price']
            # brand = form.cleaned_data['Brand']
            # size = form.cleaned_data['Size']
            # type = form.cleaned_data['Type']
            # amount = form.cleaned_data['Amount']
            # product = Productinit(id,name,price,brand,size,type,amount)
            product = Productinit(PID, name, price,brand,size,type,amount)
            lstOurProduct.append(product)
            return redirect('listProduct')

        else:
            form =ProductForm(form)
    else:
        form =ProductForm()
    context = {'form':form,"CHECK":requset.method}
    return render(requset,'inputProduct.html',context)


    # if request.method == 'POST':
    #     ID = request.POST['ID']
    #     name = request.POST['name']
    #     brand = request.POST['brand']
    #     price = request.POST['price']
    #     size = request.POST['size']
    #     type = request.POST['type']
    #     total = request.POST['total']
    #     discount = request.POST['discount']
    #     net = request.POST['net']
    #     product = Product(ID, name, brand, price, size, type, total, discount, net)
    #     lstOurProduct.append(product)
    #     return redirect('listProduct')
    # else:
    #     from = Pro
    #     return render(request, 'listProduct.html')
