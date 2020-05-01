from django.shortcuts import render

# Create your views here.
from store.models import Customer, OrderItem, Order, Product, Shipping
from django.http import JsonResponse
import json


def home(request):

    return render(request, 'store/main.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # #order = Order.objects.get(customer=customer)
        # print(Order.objects.get(customer=customer))
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0, 'shipping': False}
        cartitems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'store/cart.html', context)


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # #order = Order.objects.get(customer=customer)
        # print(Order.objects.get(customer=customer))
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartitems': cartitems}
    return render(request, 'store/store.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # #order = Order.objects.get(customer=customer)
        # print(Order.objects.get(customer=customer))
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=productId)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
