from django.shortcuts import render, redirect
from .models import client


def insert_client(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codeproduit = request.POST['codeproduit']
        data = Employee(name=name, description=description, codeproduit=codeproduit)
        data.save()

        return redirect('show_client/')
    else:
        return render(request, 'insert_client.html')

def show_client(request):
    clients = client.objects.all()
    return render(request,'show_client.html',{'clients':clients} )

# Update client

def edit_client(request,pk):
    clients = client.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            clients.name = request.POST['name']
            clients.description = request.POST['description']
            clients.codeproduit = request.POST['codeproduit']
            clients.save()
            return redirect('/show_client')
    context = {
        'clients': clients,
    }

    return render(request,'edit_client.html',context)
def remove_client(request, pk):


    clients = client.objects.get(id=pk)

    if request.method == 'POST':
        clients.delete()
        return redirect('/show_client')

    context = {
        'clients': clients,
    }

    return render(request, 'delete_client.html', context)

