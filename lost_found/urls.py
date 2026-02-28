from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('report-lost/', views.report_lost, name='report_lost'),
    path('report-found/', views.report_found, name='report_found'),
    path('search/', views.search_results, name='search_items'),
    path('register/', views.register_view, name='register'), # Idagdag ito
    path('mark-found/<int:item_id>/', views.mark_as_found, name='mark_as_found'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('about/', views.about, name='about'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='lost_found/login.html'), name='login'),
]
