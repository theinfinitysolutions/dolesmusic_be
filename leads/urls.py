from django.urls import path
from .views import CreateLeadView, CreateBusinessLeadView, CreateOldLeadView   

urlpatterns = [
    path('create-lead/', CreateOldLeadView.as_view(), name='create-lead'),
    path('business-leads/', CreateBusinessLeadView.as_view(), name='create-business-lead'),
    path('old-leads/', CreateLeadView.as_view(), name='create-old-lead'),
]