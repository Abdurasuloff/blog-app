from django.shortcuts import render, redirect
from .forms import MyUserCreationForm


# Create your views here.
def signup(request):
    form = MyUserCreationForm
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, 'registration/signup.html', {'form':form})
    return render(request, 'registration/signup.html', {'form':form})

