from django.urls import path
from .views import post_list, post_detail, post_create, post_update,post_delete

urlpatterns = [
    path('', post_list),
    path('create/', post_create),
    path('<id>/', post_detail),
    path('update/<id>/', post_update),
    path('delete/<id>/',post_delete)
]
