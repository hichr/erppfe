from django.shortcuts import render, redirect
from .models import produit


def insert_produit(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codeproduit = request.POST['codeproduit']
        data = produite(name=name, description=description, codeproduit=codeproduit)
        data.save()

        return redirect('show_produit/')
    else:
        return render(request, 'insert_produit.html')

def show_produit(request):
    produits = produit.objects.all()
    return render(request,'show_produit.html',{'produits':produits} )

# Update produit

def edit_produit(request,pk):
    produits = produit.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            produits.name = request.POST['name']
            produits.description = request.POST['description']
            produits.codeproduit = request.POST['codeproduit']
            produits.save()
            return redirect('/show_produit')
    context = {
        'produits': produits,
    }

    return render(request,'edit_produit.html',context)
def remove_produit(request, pk):


    produits = produit.objects.get(id=pk)

    if request.method == 'POST':
        produits.delete()
        return redirect('/show_produit')

    context = {
        'produits': produits,
    }

    return render(request, 'delete_produit.html', context)

