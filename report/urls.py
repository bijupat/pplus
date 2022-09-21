from django.urls import path

from . import views


app_name = 'report'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('encounter/<int:labkey>/', views.encounter, name='encounter'),
    path('report/<int:repokey>', views.report, name='report'),
    path('discount/<int:labkey>', views.discount, name='discount'),
    path('addpayment/<int:labkey>', views.addpayment, name='addpayment'),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("editrate/<int:invkey>", views.editrate, name="editrate"),
    path('reportview/<int:labkey>/', views.reportview, name='reportview'),
    path('find/', views.find, name='find'),
    path('paymentupdate/<int:oprkey>/', views.paymentupdate, name='paymentupdate'),


    

]

