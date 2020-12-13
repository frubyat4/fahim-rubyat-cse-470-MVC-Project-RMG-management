from django.contrib import admin
from .models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmployeeID','Name','department','salary','Phone','address','status')


class GarmentAdmin(admin.ModelAdmin):
    list_display = ('name','type')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id','Name','current_stock','garment','price','description','workingHoursPerItem')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('Name','phone','address','note')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('OrderID','CustomerName','CustomerPhn','department','product','quantity','TotalPrice')


class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ('product','order','delivaryDate')



class SupplerAdmin(admin.ModelAdmin):
    list_display = ('name','Company_Name','Company_Address','phone','garment','deliveryDate')


class Department_Admin_Admin(admin.ModelAdmin):
    list_display = ('user_ref','Department','role')




admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Garment, GarmentAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Deparment_Admin, Department_Admin_Admin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Shipments, ShipmentsAdmin)
admin.site.register(Supplier, SupplerAdmin)

# Register your models here.
