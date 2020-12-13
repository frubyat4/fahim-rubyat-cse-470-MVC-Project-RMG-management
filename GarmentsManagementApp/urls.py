from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'GarmentsManagementApp'
urlpatterns = [
    path('',views.home),
    path('login/',views.admin_login,name='login'),
    path('logout/',views.admin_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addEmployee/',views.AddEmployee,name='AddEmployee'),
    path('employees/',views.ShowEmployees,name='ShowEmployee'),
    path('editEmployee/<int:pk>/',views.EditEmployee,name='editEmployee'),
    path('deleteEmployee/<int:pk>/',views.deleteEmployee,name='deleteEmployee'),

    path('createproduct/',views.AddProduct,name='AddProduct'),
    path('ShowProducts/',views.ShowProducts,name='ShowProducts'),
    path('editProduct/<int:pk>/',views.editProduct,name='editProduct'),
    path('deleteProduct/<int:pk>/',views.deleteProduct,name='deleteProduct'),

    path('addGarment/',views.AddGarment,name='AddGarment'),
    path('ShowGarments/',views.ShowGarments,name='ShowGarments'),
    path('editGarment/<int:pk>/',views.EditGarment,name='editGarment'),
    path('deleteGarment/<int:pk>/',views.deleteGarment,name='deleteGarment'),

    path('createorder/',views.createOrder,name='createOrder'),
    path('showorders/',views.ShowOrders,name='ShowOrders'),
    path('deleteOrder/<int:pk>/', views.deleteOrder, name='deleteOrder'),
    path('forward/<int:pk>/',views.forward,name='forwardOrder'),
    path('reject/<int:pk>/',views.reject,name='rejectOrder'),
    path('showdepartments/',views.showdepartments,name='ShowDepartments'),
    path('showSuppliers/',views.showSuppliers,name='ShowSuppliers'),
    path('showShipments/',views.showShipments,name='showShipments'),
    path('calculateDate/',views.calculateDeliveryDate,name='calculateDate'),
    path('collaboration/', views.collab),
    path('aboutUs/', views.abt),
]
