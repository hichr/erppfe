from django.shortcuts import render, redirect
from .models import categorie_produit


def insert_categorieproduit(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codeproduit = request.POST['codeproduit']
        data = Employee(name=name, description=description, codeproduit=codeproduit)
        data.save()

        return redirect('show_categorieproduit/')
    else:
        return render(request, 'insert_categorieproduit.html')
def insert_categorie_produit(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codeproduit = request.POST['codeproduit']
        data = Employee(name=name, description=description, codeproduit=codeproduit)
        data.save()

        return redirect('show_categorieproduit/')
    else:
        return render(request, 'insert_categorieproduit.html')


def show_categorieproduit(request):
    categorie_produits = categorie_produit.objects.all()
    return render(request,'show_categorieproduit.html',{'categorie_produits':categorie_produits} )

def show_categorie_produit(request):
    categorie_produits = categorie_produit.objects.all()
    return render(request,'show_categorieproduit.html',{'categorie_produits':categorie_produits} )


# Update categorie_produit
def edit_categorie_produit(request,pk):
    categorie_produits = categorie_produit.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            categorie_produits.name = request.POST['name']
            categorie_produits.description = request.POST['description']
            categorie_produits.codeproduit = request.POST['codeproduit']
            categorie_produits.save()
            return redirect('/show_categorieproduit')
    context = {
        'categorie_produits': categorie_produits,
    }

    return render(request,'edit_categorieproduit.html',context)


def edit_categorieproduit(request,pk):
    categorie_produits = categorie_produit.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            categorie_produits.name = request.POST['name']
            categorie_produits.description = request.POST['description']
            categorie_produits.codeproduit = request.POST['codeproduit']
            categorie_produits.save()
            return redirect('/show_categorieproduit')
    context = {
        'categorie_produits': categorie_produits,
    }

    return render(request,'edit_categorieproduit.html',context)
def remove_categorieproduit(request, pk):


    categorie_produits = categorie_produit.objects.get(id=pk)

    if request.method == 'POST':
        categorie_produits.delete()
        return redirect('/show_categorieproduit')

    context = {
        'categorie_produits': categorie_produits,
    }

    return render(request, 'delete_categorieproduit.html', context)
def remove_categorie_produit(request, pk):


    categorie_produits = categorie_produit.objects.get(id=pk)

    if request.method == 'POST':
        categorie_produits.delete()
        return redirect('/show_categorieproduit')

    context = {
        'categorie_produits': categorie_produits,
    }

    return render(request, 'delete_categorieproduit.html', context)
