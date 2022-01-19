from django.urls import include, path
from .views import CutomerCreate, CustomerList, CustomerDetail, CustomerUpdate, CustomerDelete

urlpatterns = [
    path('', CustomerList.as_view()),
    path('create/', CutomerCreate.as_view(), name='create-customer'),
    path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer'),
]