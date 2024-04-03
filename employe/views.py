from django.shortcuts import render, redirect
from .models import employe


def insert_employe(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codeproduit = request.POST['codeproduit']
        data = Employee(name=name, description=description, codeproduit=codeproduit)
        data.save()

        return redirect('show_employe/')
    else:
        return render(request, 'insert_employe.html')

def show_employe(request):
    employes = employe.objects.all()
    return render(request,'show_employe.html',{'employes':employes} )

# Update employe

def edit_employe(request,pk):
    employes = employe.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            employes.name = request.POST['name']
            employes.description = request.POST['description']
            employes.codeproduit = request.POST['codeproduit']
            employes.save()
            return redirect('/show_employe')
    context = {
        'employes': employes,
    }

    return render(request,'edit_employe.html',context)
def remove_employe(request, pk):


    employes = employe.objects.get(id=pk)

    if request.method == 'POST':
        employes.delete()
        return redirect('/show_employe')

    context = {
        'employes': employes,
    }

    return render(request, 'delete_employe.html', context)

