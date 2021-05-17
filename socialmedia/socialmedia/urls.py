"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
# from .views import DasboardPageView
from SocialMediaThreats import views

urlpatterns = [
    # path('redirect/', views.beforelogindashboard),
    path('admin/', admin.site.urls),
    # path('', DashboardPageView.as_view(), name='dashboard'),
    path('dashboard/', views.dashboard),
    path('', views.beforelogindashboard, name='beforelogindashboard'),
    path('threatreporting/', views.threatreporting),
    path('Analysis/', views.Analysis),
    path('addthreat/', views.addthreat),
    path('viewthreat/', views.viewthreat),
    path('viewtechnique/', views.viewtechnique),
    path('viewawareness/', views.viewawareness),
    path('monthlyanalysis/', views.monthlyanalysis),

    path('Reportthreat/', views.Reportthreat),
    path('Reporttechnique/', views.Reporttechnique),
    path('ReportAwareness/', views.Reportawareness),
    
    # path('viewHistoricalTechniques/', views.viewHistoricalTechniques),
    path('AuditTrail/', views.AuditTrail),
    
    
    path('annualanalysis/', views.annualanalysis),
    path('techniques/', views.techniques),
    path('awareness/', views.awareness),
    path('help/', views.help),
    path('edittechnique/<int:id>/', views.edittechnique, name='edittechnique'),
    path('editthreat/<int:id>/', views.editthreat, name='editthreat'),
    
    path('editawareness/<int:id>/', views.editawareness, name='editawareness'),
    # path('contacts/edit/<int:pk>/', views.edit, name='editthreat'),
    path('loginPage/', views.loginPage),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
    name="reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
    name="password_reset_complete"),
]
