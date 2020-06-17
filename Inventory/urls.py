from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

from Inventory import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('',views.home,name='home'),
    path('<int:item_id>/',views.details,name='details'),
    path('<int:item_id>/transact',views.transitm,name='transitm'),
    path('accounts/',views.clients,name='clients'),
    path('accounts/<int:client_id>/',views.account_details,name='account_details'),
]
    # 
    # 
    # path('<int:item_id>/transfer',views.transferitm,name='transferitm'),
    # path('<int:item_id>/return',views.returnitm,name='returnitm'),
    # path('<int:item_id>/sale',views.saleitm,name='saleitm'),
    # 
    # 
    # path('signup/', accounts_views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),    
 