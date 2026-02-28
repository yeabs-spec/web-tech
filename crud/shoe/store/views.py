from django.shortcuts import render, redirect
from .models import Shoe, Country




def admin_home(request):
    shoes = Shoe.objects.all()
    countries = Country.objects.all()
    return render(request, 'admin.html', {
        'all': shoes,
        'c': countries
    })


def add_shoe(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        country_id = request.POST.get('country')

        Shoe.objects.create(
            brand=brand,
            price=price,
            image=image,
            country_id=country_id
        )

        return redirect('admin_url')

    return redirect('admin_url')


def add_country(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Country.objects.create(name=name)

    return redirect('admin_url')