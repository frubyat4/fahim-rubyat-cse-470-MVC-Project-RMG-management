from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from django.utils import timezone
import datetime

# Create your views here.
def home(request):
    return render(request, 'HomePage.html')

def collab(request):
    return render(request, 'collaboration.html')

def abt(request):
    return render(request, 'aboutUs.html')

def admin_login(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    else:
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user_ref = authenticate(username=user_name, password=pass_word)
        if user_ref:
            if user_ref.is_active and user_ref.is_staff and not user_ref.is_superuser:
                login(request, user_ref)
                return redirect('/')
            else:
                return HttpResponse("<h1> You are not authorized to view Dashboard</h1>")
        else:
            return HttpResponse("login failed")


@login_required(login_url='/login/')
def admin_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/login/')
def AddEmployee(request):
    if request.method != "POST":
        depts = Department.objects.all()
        return render(request, 'AddEmployee.html', {'depts': depts})
    else:
        name = request.POST["name"]
        department = Department.objects.get(pk=request.POST["department"])
        Id = request.POST["EmpId"]
        salary = request.POST["salary"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        status = request.POST["status"]
        employee = Employee()
        employee.Name = name
        employee.EmployeeID = int(Id)
        employee.department = department
        employee.salary = salary
        employee.Phone = phone
        employee.address = address
        employee.status = status
        employee.save()

        return redirect('/employees/')


@login_required(login_url='/login/')
def ShowEmployees(request):
    if request.method != "POST":
        username = request.user.username
        user = User.objects.get(username=username)
        userdata = Deparment_Admin.objects.get(user_ref=user)
        if userdata.Department.Name == 'SuperAdmin':
            list = Employee.objects.all()
        else:
            list = Employee.objects.filter(department=userdata.Department)
        return render(request, 'ShowEmployees.html', {'list': list})
    else:
        data = request.POST.get('searchname', False)
        if data == False:
            data = int(request.POST["searchid"], 10)
            list = Employee.objects.filter(pk=data)
            return render(request, 'ShowEmployees.html', {'list': list})
        else:
            list = Employee.objects.filter(Name=data)
            return render(request, 'ShowEmployees.html', {'list': list})


@login_required(login_url='/login/')
def EditEmployee(request, pk):
    if request.method != "POST":
        data = Employee.objects.get(pk=pk)
        depts = Department.objects.all()
        context = {'data': data, 'depts': depts}
        return render(request, 'EditEmployee.html', context)
    else:
        name = request.POST["name"]
        department = Department.objects.get(pk=request.POST["department"])
        salary = request.POST["salary"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        status = request.POST["status"]

        employee = Employee.objects.get(pk=pk)
        employee.Name = name
        employee.department = department
        employee.salary = salary
        employee.Phone = phone
        employee.address = address
        employee.status = status
        employee.save()
        return redirect('GarmentsManagementApp:ShowEmployee')


@login_required(login_url='/login/')
def deleteEmployee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('GarmentsManagementApp:ShowEmployee')


@login_required(login_url='/login/')
def AddProduct(request):
    if request.method != "POST":
        garments = Garment.objects.all()
        return render(request, 'Addproduct.html', {'garments': garments})
    else:
        garments = Garment.objects.get(pk=request.POST["Garment"])
        p = Products()
        p.Name = request.POST["name"]
        id = request.POST["PrdId"]
        p.garment = garments
        p.workingHoursPerItem = int(request.POST["workingDay"])
        p.product_id = int(id)
        p.price = request.POST["price"]
        p.description = request.POST["description"]
        p.save()
        return redirect('/ShowProducts/')


@login_required(login_url='/login/')
def ShowProducts(request):
    list = Products.objects.all()
    return render(request, 'ShowProducts.html', {'list': list})


@login_required(login_url='/login/')
def editProduct(request, pk):
    if request.method != "POST":
        data = Products.objects.get(pk=pk)
        list = Garment.objects.all()
        return render(request, 'EditProduct.html', {'data': data, 'list': list})
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]

        p = Products.objects.get(pk=pk)
        p.Name = name
        p.price = price
        garment = request.POST["Garment"]
        garments = Garment.objects.get(pk=garment)
        p.workingHoursPerItem = int(request.POST["workingDay"])
        p.current_stock = request.POST["stock"]
        p.garment = garments
        p.description = description
        p.save()
        return redirect('GarmentsManagementApp:ShowProducts')


@login_required(login_url='/login/')
def deleteProduct(request, pk):
    prd = Products.objects.get(pk=pk)
    prd.delete()
    return redirect('GarmentsManagementApp:ShowProducts')


@login_required(login_url='/login/')
def AddGarment(request):
    if request.method != "POST":
        return render(request, 'AddGarment.html')
    else:
        name = request.POST["name"]
        type = request.POST["type"]
        G = Garment()
        G.name = name
        G.type = type
        G.save()
        return redirect('GarmentsManagementApp:ShowGarments')


@login_required(login_url='/login/')
def ShowGarments(request):
    list = Garment.objects.all()
    return render(request, 'ShowGarments.html', {'list': list})


@login_required(login_url='/login/')
def EditGarment(request, pk):
    if request.method != "POST":
        data = Garment.objects.get(pk=pk)
        return render(request, 'EditGarment.html', {'data': data})
    else:
        name = request.POST["name"]
        type = request.POST["type"]
        Gr = Garment.objects.get(pk=pk)
        Gr.name = name
        Gr.type = type
        Gr.save()
        return redirect('GarmentsManagementApp:ShowGarments')


@login_required(login_url='/login/')
def deleteGarment(request, pk):
    prd = Garment.objects.get(pk=pk)
    prd.delete()
    return redirect('GarmentsManagementApp:ShowGarments')


@login_required(login_url='/login/')
def createOrder(request):
    if request.method != "POST":
        list = Products.objects.all()
        return render(request, 'createOrder.html', {'list': list})
    else:
        r = int(request.POST["product"], 10)
        cust_name = request.POST["customer_name"]
        id = request.POST["OrdId"]
        phn = request.POST["customer_phn"]
        product = Products.objects.get(pk=r)
        qty = int(request.POST["quantity"], 10)
        O = Order()
        O.CustomerName = cust_name
        O.OrderID = id
        O.department = Department.objects.get(Name='Production')
        O.Status = 'Processing'
        O.CustomerPhn = phn
        O.product = product
        O.quantity = qty
        O.TotalPrice = qty * product.price
        if qty > product.current_stock:
            return HttpResponse("<h3> Not Enough Stock for this product quantity </h3>")
        else:
            O.save()
        return redirect('GarmentsManagementApp:ShowOrders')


@login_required(login_url='/login/')
def ShowOrders(request):
    username = request.user.username
    user = User.objects.get(username=username)
    userdata = Deparment_Admin.objects.get(user_ref=user)
    if userdata.Department.Name == 'SuperAdmin':
        list = Order.objects.all()
    else:
        list = Order.objects.filter(department=userdata.Department)
    return render(request, 'ShowOrders.html', {'list': list})


@login_required(login_url='/login/')
def forward(request, pk):
    order = Order.objects.get(pk=pk)
    if order.department.Name == 'QualityChecking':
        order.department = Department.objects.get(Name='Shipment')
        order.save()
    elif order.department.Name == 'Production':
        order.department = Department.objects.get(Name='QualityChecking')
        order.save()
    elif order.department.Name == 'Shipment':
        newShipment = Shipments()
        newShipment.product = order.product
        prod = Products.objects.get(pk=order.product.pk)
        prod.current_stock = prod.current_stock - order.quantity
        prod.save()
        newShipment.order = order
        newShipment.delivaryDate = timezone.now().date() + datetime.timedelta(days=3)
        newShipment.save()
        order.department = None
        order.Status = 'Shipped'
        order.save()
    return redirect('GarmentsManagementApp:ShowOrders')


@login_required(login_url='/login/')
def reject(request, pk):
    order = Order.objects.get(pk=pk)
    if order.department.Name == 'QualityChecking':
        order.department = Department.objects.get(Name='Production')
        order.save()
    elif order.department.Name == 'Shipment':
        order.department = Department.objects.get(Name='QualityChecking')
        order.Status = 'processing'
        order.save()
    return redirect('GarmentsManagementApp:ShowOrders')


@login_required(login_url='/login/')
def deleteOrder(request, pk):
    Order.objects.get(pk=pk).delete()
    return redirect('GarmentsManagementApp:ShowOrders')


@login_required(login_url='/login/')
def showdepartments(request):
    list = Department.objects.all()
    return render(request, 'showDepartment.html', {'list': list})


@login_required(login_url='/login/')
def showSuppliers(request):
    list = Supplier.objects.all()
    return render(request, 'showSupplier.html', {'list': list})


@login_required(login_url='/login/')
def showShipments(request):
    list = Shipments.objects.all()
    return render(request, 'showShipments.html', {'list': list})


@login_required(login_url='/login/')
def calculateDeliveryDate(request):
    if request.method == "POST":
        product = Products.objects.get(pk=request.POST["product"])
        quantity = int(request.POST["quant"])
        products = Products.objects.all()
        noOfWorkinghour = int(product.workingHoursPerItem * quantity)
        noOfWorkingDays = int(noOfWorkinghour / 10) + 1  # 10 = working hour perday
        delivarydate = timezone.now().date()

        while noOfWorkingDays != 0:
            delivarydate = delivarydate + datetime.timedelta(days=1)
            if delivarydate.isoweekday() != 5 and delivarydate.isoweekday() != 6:
                noOfWorkingDays -= 1
        # else:
        # print(delivarydate.day)
        return render(request, 'calculateDelivery.html', {'products': products, 'delivarydate': delivarydate})
    else:
        products = Products.objects.all()
        return render(request, 'calculateDelivery.html', {'products': products})
