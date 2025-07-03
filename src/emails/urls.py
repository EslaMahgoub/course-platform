
from django.urls import path
from . import views

urlpatterns = [
    path('hx/login/', views.email_token_login_view, name="login-email"),
    path('hx/logout/', views.logout_btn_hx_view, name="logout-email"),
    path('verify/<uuid:token>/', views.verify_email_token_view, name="verify-email"),
]
