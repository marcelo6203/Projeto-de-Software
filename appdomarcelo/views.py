from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Jogos, rejogar
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    jogos = Jogos.objects.all()
    rejogos = rejogar.objects.all()
    return render(request,"home.html", context={
        "jogos": jogos, 
        "rejogos":rejogos
    })

@login_required
def create_jogo(request):
    if request.method == "POST":
        Jogos.objects.create(
            title = request.POST["Title"],
            director = request.POST["Director"],
            genre = request.POST["Genre"],
            release_date = request.POST["Release_date"]
        )
    
        return redirect("home")
    return render(request, "forms.html",context={"Action":"Adicionar","jogo":Jogos})

@login_required
def create_extra(request):
    if request.method == "POST":
        title = request.POST.get("Title")
        how_often = request.POST.get("how_often")
        enjoyability = request.POST.get("Enjoyability")
        
        if not how_often:
            return render(request, "forms_extra.html", {"error": "how_often field is required."})
        
        rejogar.objects.create(
            title=title,
            how_often=how_often,
            enjoyability=enjoyability
        )
        return redirect("home")

    return render(request, "forms_extra.html")

@login_required
def update_jogo(request, id):
    jogo = get_object_or_404(Jogos, id=id)

    if request.method == "POST":
        jogo.title = request.POST.get("Title")
        jogo.director = request.POST.get("Director")
        jogo.genre = request.POST.get("Genre")
        jogo.release_date = request.POST.get("Release_date")

        if None not in [jogo.title, jogo.director, jogo.genre, jogo.release_date]:
            jogo.save()
            return redirect("home")
      
    return render(request, "forms.html", context={"Action":"Atualizar", "jogo":jogo})

@login_required
def update_extra(request, id):
    obj = get_object_or_404(rejogar, id=id)

    if request.method == "POST":
        title = request.POST.get("Title")
        how_often = request.POST.get("how_often")
        enjoyability = request.POST.get("Enjoyability")
        
        if not how_often:
            return render(request, "forms_extra.html", {"error": "how_often field is required."})
        
        obj.title = title
        obj.how_often = how_often
        obj.enjoyability = enjoyability
        obj.save()

        return redirect("home")
    
    return render(request, "forms_extra.html", context={"obj": obj})

@login_required
def delete_jogo(request, id):
    jogo = get_object_or_404(Jogos, id=id)
    if request.method == "POST":
        jogo.delete()
        return redirect('home')
    return render(request, 'delete_confirm.html', {'game': jogo})

@login_required
def delete_rejogo(request, id):
    rejogo = get_object_or_404(rejogar, id=id)
    if request.method == "POST":
        rejogo.delete()
        return redirect('home')
    return render(request, 'delete_confirm.html', {'game': rejogo})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')
