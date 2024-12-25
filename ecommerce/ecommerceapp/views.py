from math import ceil
from django.shortcuts import render
from ecommerceapp.models import Contact,Product
from django.contrib import messages
# Create your views here.
def index(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        nSlides=len(prod)//4 + ceil((len(prod)/4)-(len(prod)//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return render(request, 'index.html',params)



def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        phonenumber = request.POST['pnumber']
        myquery=Contact(name=name, email=email, desc=desc, phonenumber=phonenumber)
        print(name, email, desc, phonenumber) 
        myquery.save()
        messages.success(request, 'Your message has been sent!')
        return render(request, 'contact.html')
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')