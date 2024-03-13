from django.urls import path
from .views import CreateRequestView, ListRequestByUsers, ListRequestView, UpdateRequestView, DestroyRequestView

urlpatterns = [
    path('list/',ListRequestView.as_view(), name='requestList'),
    path('create/',CreateRequestView.as_view(), name='requestcreate'),
    path('list/<int:pk>/',ListRequestByUsers.as_view(), name='requestListbyUser'),
    path('update/<int:pk>/',UpdateRequestView.as_view(), name='requestupdate'),
    path('destroy/<int:pk>/',DestroyRequestView.as_view(), name='requestDestroy'),
]