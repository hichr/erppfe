from django.shortcuts import render, redirect
from .models import statproduit


def insert_statproduit(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codestatproduit = request.POST['codestatproduit']
        data = statproduite(name=name, description=description, codestatproduit=codestatproduit)
        data.save()

        return redirect('show_statproduit/')
    else:
        return render(request, 'insert_statproduit.html')

def show_statproduit(request):
    statproduits = statproduit.objects.all()
    return render(request,'show_statproduit.html',{'statproduits':statproduits} )

# Update statproduit

def edit_statproduit(request,pk):
    statproduits = statproduit.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            statproduits.name = request.POST['name']
            statproduits.description = request.POST['description']
            statproduits.codestatproduit = request.POST['codestatproduit']
            statproduits.save()
            return redirect('/show_statproduit')
    context = {
        'statproduits': statproduits,
    }

    return render(request,'edit_statproduit.html',context)
def remove_statproduit(request, pk):


    statproduits = statproduit.objects.get(id=pk)

    if request.method == 'POST':
        statproduits.delete()
        return redirect('/show_statproduit')

    context = {
        'statproduits': statproduits,
    }

    return render(request, 'delete_statproduit.html', context)

