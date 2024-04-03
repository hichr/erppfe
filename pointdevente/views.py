from django.shortcuts import render, redirect
from .models import pointdevente


def insert_pointdevente(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codeproduit = request.POST['codeproduit']
        data = pointdeventee(name=name, description=description, codeproduit=codeproduit)
        data.save()

        return redirect('show_pointdevente/')
    else:
        return render(request, 'insert_pointdevente.html')

def show_pointdevente(request):
    pointdeventes = pointdevente.objects.all()
    return render(request,'show_pointdevente.html',{'pointdeventes':pointdeventes} )

# Update pointdevente

def edit_pointdevente(request,pk):
    pointdeventes = pointdevente.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            pointdeventes.name = request.POST['name']
            pointdeventes.description = request.POST['description']
            pointdeventes.codeproduit = request.POST['codeproduit']
            pointdeventes.save()
            return redirect('/show_pointdevente')
    context = {
        'pointdeventes': pointdeventes,
    }

    return render(request,'edit_pointdevente.html',context)
def remove_pointdevente(request, pk):


    pointdeventes = pointdevente.objects.get(id=pk)

    if request.method == 'POST':
        pointdeventes.delete()
        return redirect('/show_pointdevente')

    context = {
        'pointdeventes': pointdeventes,
    }

    return render(request, 'delete_pointdevente.html', context)

