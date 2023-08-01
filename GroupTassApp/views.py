from django.shortcuts import render,redirect


from .models import Annonce,Contact,Team,MotDuMembre
# Create your views here.

def home(request):
    citation = MotDuMembre.objects.all()
    annonces=Annonce.objects.all()
    teams=Team.objects.all()
    return render(request,'index.html',context={'annonces':annonces,'teams':teams,'citation':citation})

# def team(request):
#     return render(request,'index.html',context={})


def forms(request):
    return render(request,'contact.php',{})

# def Annonce(request,slug):
#     annonces=Annonce.objects.all()
#     # annonces = Annonce.Object.all()
#     return render(request,'annonce.html',context={'annonces':annonces})

def details(request,id):
    info=Annonce.objects.get(id=id)
    # annonces = Annonce.Object.all()
    return render(request,'detail.html',context={'info':info})


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        objet = request.POST.get('objet')
        message = request.POST.get('message')
        NewContact = Contact.objects.create(name=name, email=email,objet=objet,message=message)

        return redirect('home')