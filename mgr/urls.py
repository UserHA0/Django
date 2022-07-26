from django.urls import path
from mgr import customer
from mgr.sing_in_out import signin, signout

urlpatterns = [
    path('customers', customer.dispatcher),
    path('signin', signin),
    path('signout', signout)
]