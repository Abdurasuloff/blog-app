from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from datetime import datetime
from django.contrib.auth.models import User
from .forms import BlogForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# import requests
# Create your views here.


def index(request):
    blogs = Blog.objects.all().order_by('-id')
    
    return render(request, "index.html", {"blogs":blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    return render(request, "blog_detail.html", {"blog":blog})

@login_required
def blog_yarat(request):  # blog_yarat degan funksiya yaratish
    form = BlogForm()  # forma yaratish
    if request.method == 'POST': # agar POST request kelayotgan bo'lsa
        form = BlogForm(data=request.POST, files=request.FILES) # forma bilan uni ichidagi ma'lumotlarni olish
        if form.is_valid(): # agar forma yaroqli bo'lsa
            blog = form.save(commit=False)  # formani saqlash
            blog.avtor = request.user
            form.save()
            messages.success(request, "Blog muvaffaqiyatli yaratildi.")
            # bot_text = blog.sarlavha
            
            # bot_text += f"\n\n {blog.tanasi}"
            
            # requests.get(
            #     f"https://api.telegram.org/bot6736046604:AAHrr6HxPyOTFXedv5pea6z8OEI-gErHFIE/sendMessage?chat_id=-1002036568014&text={bot_text}"
            # )
            
            return redirect("index")  # indez sahifasiga jo'natish
        else:  #aks holsa
           return render(request, "blog_yarat.html", {'form':form}) #sahifani xatolari bilan qayta ko'rsatish
        
    return render(request, "blog_yarat.html", {'form':form}) # sahifani ko'rsatish


@login_required
def blog_tahrirlash(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.user == blog.avtor:
        form = BlogForm(instance=blog)
        if request.method == 'POST':
            form = BlogForm(instance=blog, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Blog muvaffaqiyatli tahrirlandi.")
                return redirect('blog_detail', blog_id)
            else:
                return render(request, "blog_tahrirlash.html", {'form':form, 'blog':blog})
        
        return render(request, "blog_tahrirlash.html", {'form':form, 'blog':blog})
    else:
        messages.error(request, "Siz ushbu postni tahrirlay olmaysiz.")
        messages.info(request, "Siz o'zingizga tegishli bo'lmagan postni tahrirrlay olmaysiz.kcfdskf;;kd ;skj s;ktrjdkjjpython mskldfn kfjsdfkjs skfjskflj sskfjskfgdfefkjekrj wkjbvdlkbdblkjgdj")

        return redirect("index")
    
    # python ,snsdjfs,vjnvdjbfv


@login_required
def blog_ochirish(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    if blog.avtor == request.user:
    
        if request.method == 'POST':
            blog.delete()
            messages.success(request, "Blog muvaffaqiyatli o'chirildi.")
            return redirect("index")
        
        return render(request, 'blog_ochirish.html', {'blog':blog})
    
    else:
        messages.error(request, "Bu blogni tahrirlay o'chira olmaysiz.")
        return redirect("index")

