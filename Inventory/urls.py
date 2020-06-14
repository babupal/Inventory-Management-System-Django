from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:item_id>/',views.details,name='details'),
    path('<int:item_id>/transact',views.transitm,name='transitm'),
    path('<int:item_id>/transfer',views.transferitm,name='transferitm'),
    path('<int:item_id>/return',views.returnitm,name='returnitm'),
    path('<int:item_id>/sale',views.saleitm,name='saleitm'),
    path('accounts/',views.clients,name='clients'),
    path('accounts/<int:client_id>/',views.account_details,name='account_details'),
]
