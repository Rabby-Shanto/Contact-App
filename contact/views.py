from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_contact = request.GET.get('search-area')
    if search_contact:
        contacts = Contact.objects.filter(FullName__icontains=search_contact)
    else:
        contacts = Contact.objects.all()
        search_contact = ''
    return render(request,'index.html',{'contacts' : contacts,'search_contact': search_contact})

def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            FullName = request.POST['fullname'],
            RelationShip = request.POST['relationship'],
            Email = request.POST['email'],
            PhoneNumber = request.POST['phone-number'],
            Address =  request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request,'new.html')

def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request,'contact-profile.html',{'contact' : contact})

def editContact(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
            contact.FullName = request.POST['fullname']
            contact.RelationShip = request.POST['relationship']
            contact.Email = request.POST['email']
            contact.PhoneNumber = request.POST['phone-number']
            contact.Address =  request.POST['address']
            contact.save()
            response = ('/profile/'+str(contact.id))
            return redirect(response)
    return render(request,'edit.html',{'contact' : contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request,'delete.html',{'contact' : contact})