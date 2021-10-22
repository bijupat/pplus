from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('encounter/<int:labkey>/', views.encounter, name='encounter'),
    path('report/<int:repokey>', views.report, name='report'),
    path('discount/<int:labkey>', views.discount, name='discount'),
    path('addpayment/<int:labkey>', views.addpayment, name='addpayment'),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
   



]