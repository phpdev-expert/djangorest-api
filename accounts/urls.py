from django.urls import path
from .views import UpdateUserPermissions

urlpatterns = [
   path('account',UpdateUserPermissions.as_view()),
]
