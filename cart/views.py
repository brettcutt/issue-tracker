from django.shortcuts import render, redirect, reverse
from features.views import feature_detail

# Create your views here.


def view_cart(request):
    """  A view that renders the cart contents page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    cart[id] = quantity
    print(cart)
    request.session['cart'] = cart
    return redirect(feature_detail, id)


def remove_ticket(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
