from django.shortcuts import render
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

# Create your views here.
