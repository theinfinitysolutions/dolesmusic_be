from django.urls import path
from .views import CreateLeadView

urlpatterns = [
    path('create-lead/', CreateLeadView.as_view(), name='create-lead'),
]