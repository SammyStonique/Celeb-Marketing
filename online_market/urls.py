from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name = 'main-homepage'),
    path('cart/',views.cart, name = 'cart'),
    path('checkout/',views.checkout, name = 'checkout'),
    path('contact/',views.contact, name = 'contact'),
    path('products/',views.product, name = 'product-list'),
    path('product-details/',views.product_details, name = 'product-details'),
    path('my-account/',views.account, name = 'my-account'),
    path('customer-register/',views.customer_register, name = 'customer-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'online_market/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'online_market/logout.html'), name = 'logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='online_market/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='online_market/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="online_market/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='online_market/password_reset_complete.html'), name='password_reset_complete'), 
]

urlpatterns += staticfiles_urlpatterns()