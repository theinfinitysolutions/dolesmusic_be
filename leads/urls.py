from django.urls import path
from .views import CreateLeadView, CreateBusinessLeadView   

urlpatterns = [
    path('create-lead/', CreateLeadView.as_view(), name='create-lead'),
    path('business-leads/', CreateBusinessLeadView.as_view(), name='create-business-lead'),
]