from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactHome
from django.views.generic import ListView
from django.contrib.auth.models import User

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ContactListHome(ListView):
    context_object_name = "contacts"
    paginate_by = 4  # add this

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return ContactHome.objects.filter(homecreated_by=self.request.user)
        return ContactHome.objects.filter(homecreated_by=None)


# detail contact


###@login_required(login_url="/login/")
def contact_detailsHome(request, id):
   contact = get_object_or_404(ContactHome, id=id)
   context = {"contact": contact}
   return render(request, "contact/contact_details.html", context)

# Add new contact


def new_contactHome(request):
    if request.method == "POST":
        user1 = User.objects.create_user(
            'jj', 'lennon@thebeatles.com', 'johnpassword')
        homecreated_by = user1
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        contact = ContactHome.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            homecreated_by=homecreated_by
        )
        contact.save()
        return redirect("/contacts/")

    return render(request, "contact/new_contact.html")


# Update a contact
#@login_required(login_url="/login/")
def update_contactHome(request, id):
    contact = get_object_or_404(ContactHome, id=id)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        ContactHome.objects.filter(pk=contact.id).update(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email
        )
        return redirect("/contacts/")
    context = {"contact": contact}
    return render(request, "contact/update_contact.html", context)

# Remove a contact
#@login_required(login_url="/login/")


def delete_contactHome(request, id):
    contact = get_object_or_404(ContactHome, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect("/contacts/")
    context = {"contact": contact}
    return render(request, "contact/delete_contact.html", context)


