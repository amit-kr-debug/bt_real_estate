from django.shortcuts import render,redirect


def register(request):
    if request.method == "POST":
        return
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        return
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        return
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


