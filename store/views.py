from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
# Create your views here.


def index(request):
    products = Product.objects.all()
    category = Category.objects.all()
    # print(products.query)
    # print(category.query)
    # print(products)
    # print(len(products))
    context = {
        'products': products,
        'categories': category
    }
    return render(request, 'index.html', context)


# def get_all_products_by_id(request, category_id):
#     if category_id:
#         products = Category.objects.filter(category=category_id)
#     else:
#         products = Product.objects.all()
#     return products

def validateUser(customer):
    """ Validations """
    error_msg = ""
    confirm_password = customer.password
    if not customer.first_name:
        error_msg = "First Name is Required!"
    elif (len(customer.first_name) < 4):
        error_msg = "First Name should be minimun 4 characters long."
    elif not customer.last_name:
        error_msg = "Last Name is Required!"
    elif (len(customer.last_name) < 4):
        error_msg = "Last Name should be minimum 4 Characters long."
    elif not customer.phone:
        error_msg = "Contact Number is Required!"
    elif (len(customer.phone) < 10):
        error_msg = "Enter a Valid Phone Number."
    elif not customer.email:
        error_msg = "Email ID is Required!"
    elif (len(customer.password) < 8):
        error_msg = "Password should be atleast 8 Characters long."
    elif customer.password != confirm_password:
        error_msg = "Confirm Password mismatch!"
        # Email Unique Validation
    elif customer.isEmail_exists():
        error_msg = "Email ID already exists, Try Another!"
    return error_msg


def registerUser(request):
    """ New User Registration """
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    phone = request.POST.get("phone")
    email = request.POST.get("emailId")
    password = request.POST.get("password")
    print(first_name, last_name, phone, email, password)

    # Customer Object
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        password=password,
    )

    error_msg = validateUser(customer)

    values = {
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'phone': customer.phone,
        'email': customer.email,
    }

    # Password Hashing
    customer.password = make_password(customer.password)

    # saving
    if not error_msg:
        customer.register()
        return redirect('home')
    else:
        data = {
            'error': error_msg,
            'values': values,
        }
        return render(request, 'signup.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
