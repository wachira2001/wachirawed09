from django.shortcuts import render
from static import images
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





# Create your views here.
