from django.shortcuts import render, redirect

data_dict = {}

def create(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        data_dict[key] = value
        return redirect('read')
    return render(request, 'create.html')

def read(request):
    return render(request, 'read.html', {'data_dict': data_dict})

def update(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if key in data_dict:
            data_dict[key] = value
        return redirect('read')
    return render(request, 'update.html')

def delete(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        if key in data_dict:
            del data_dict[key]
        return redirect('read')
    return render(request, 'delete.html')
