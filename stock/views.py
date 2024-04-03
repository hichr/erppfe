from django.shortcuts import render, redirect
from .models import stock


def insert_stock(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        codestock = request.POST['codestock']
        data = stocke(name=name, description=description, codestock=codestock)
        data.save()

        return redirect('show_stock/')
    else:
        return render(request, 'insert_stock.html')

def show_stock(request):
    stocks = stock.objects.all()
    return render(request,'show_stock.html',{'stocks':stocks} )

# Update stock

def edit_stock(request,pk):
    stocks = stock.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            stocks.name = request.POST['name']
            stocks.description = request.POST['description']
            stocks.codestock = request.POST['codestock']
            stocks.save()
            return redirect('/show_stock')
    context = {
        'stocks': stocks,
    }

    return render(request,'edit_stock.html',context)
def remove_stock(request, pk):


    stocks = stock.objects.get(id=pk)

    if request.method == 'POST':
        stocks.delete()
        return redirect('/show_stock')

    context = {
        'stocks': stocks,
    }

    return render(request, 'delete_stock.html', context)

