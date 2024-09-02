from django.urls import path, include
from django.contrib import admin
from accounts import views
from accounts.views import dashboard, non_member_dashboard, member_dashboard, executive_dashboard
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', dashboard, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('non-member/', non_member_dashboard, name='non_member_dashboard'),
    path('member/', member_dashboard, name='member_dashboard'),
    path('executive/', executive_dashboard, name='executive_dashboard'),
]
