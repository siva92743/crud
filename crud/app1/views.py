from django.core.checks import messages
from django.shortcuts import render, redirect

# Create your views here.
from app1.forms import LoginForm
from app1.models import Login


def home(request):
    return render(request, 'home.html')


def user_register(request):
    data = LoginForm()
    if request.method == 'POST':
        data = LoginForm(request.POST)
        print(data)
        if data.is_valid():
            user = data.save(commit=False)
            user.is_trainer = True
            user.save()
            return redirect('home')
    return render(request, 'user_register.html', {'data': data})


def user_view(request):
    data = Login.objects.filter(is_trainer=True)
    return render(request, 'user_view.html', {'data': data})


def user_view2(request):
    data = Login.objects.filter(is_trainer=True)
    return render(request, 'user_view2.html', {'data': data})


def user_update(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        form = LoginForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('user_view')
    else:
        form = LoginForm(instance=data)
    return render(request, 'user_update.html', {'form': form})


def user_delete(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('user_view')
    else:
        return redirect('user_view')
