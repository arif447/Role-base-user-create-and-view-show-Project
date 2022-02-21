from django.urls import path
from Account_App import views
app_name = 'Account_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_page, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('logout/', views.user_logout, name='logout'),
    path('post/', views.createpost, name='post'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.profile, name='profile'),
    path('payment/', views.payment, name='payment'),

]