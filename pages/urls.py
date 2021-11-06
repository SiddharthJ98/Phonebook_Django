from django.urls import path

from .views import HomePageView
# from .views import (
#     ContactListHome,
#     new_contactHome, contact_detailsHome,
#     update_contactHome, delete_contactHome
# )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
   # path('about/', AboutPageView.as_view(), name='about'),
    # path("contacts/", ContactListHome.as_view(), name="contacts"),
    # path("contacts/new/", new_contactHome, name="new"),
    # path("contacts/<int:id>/details/", contact_detailsHome, name="details"),
    # #path("contacts/<int:id>/update/", update_contactHome, name="update"),
    # path("contacts/<int:id>/delete/", delete_contactHome, name="delete"),
]
