from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.login, name='login_page'),
    path('register/', views.register, name='register_page'),
    path('logout/', views.logout_page, name='logout_page'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Standards CRUD
    path('standards/', views.standards, name='standards_page'),
    path('standards/add/', views.add_standard, name='add_standard'),
    path('standards/edit/<int:id>/', views.edit_standard, name='edit_standard'),
    path('standards/delete/<int:id>/', views.delete_standard, name='delete_standard'),

    # Protocols CRUD
    path('protocols/', views.protocols, name='protocols_page'),
    path('protocols/add/', views.add_protocol, name='add_protocol'),
    path('protocols/edit/<int:id>/', views.edit_protocol, name='edit_protocol'),
    path('protocols/delete/<int:id>/', views.delete_protocol, name='delete_protocol'),

    # Regulations CRUD
    path('regulations/', views.regulations, name='regulations_page'),
    path('regulations/add/', views.add_regulation, name='add_regulation'),
    path('regulations/edit/<int:id>/', views.edit_regulation, name='edit_regulation'),
    path('regulations/delete/<int:id>/', views.delete_regulation, name='delete_regulation'),
]