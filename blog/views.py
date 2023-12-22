from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from datetime import datetime
from django.contrib.auth.models import User
from .forms import BlogForm
# Create your views here.


def index(request):
    blogs = Blog.objects.all().order_by('-id')
    
    return render(request, "index.html", {"blogs":blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    return render(request, "blog_detail.html", {"blog":blog})


def blog_yarat(request):  # blog_yarat degan funksiya yaratish
    form = BlogForm()  # forma yaratish
    if request.method == 'POST': # agar POST request kelayotgan bo'lsa
        form = BlogForm(data=request.POST, files=request.FILES) # forma bilan uni ichidagi ma'lumotlarni olish
        if form.is_valid(): # agar forma yaroqli bo'lsa
            form.save()  # formani saqlash
            return redirect("index")  # indez sahifasiga jo'natish
        else:  #aks holsa
           return render(request, "blog_yarat.html", {'form':form}) #sahifani xatolari bilan qayta ko'rsatish
        
    return render(request, "blog_yarat.html", {'form':form}) # sahifani ko'rsatish



def blog_tahrirlash(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(instance=blog, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id)
        else:
            return render(request, "blog_tahrirlash.html", {'form':form, 'blog':blog})
    
    return render(request, "blog_tahrirlash.html", {'form':form, 'blog':blog})



def blog_ochirish(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    if request.method == 'POST':
        blog.delete()
        return redirect("index")
    
    return render(request, 'blog_ochirish.html', {'blog':blog})