from django.shortcuts import get_object_or_404
from bugs.models import Features


def cart_contents(request):
    """Ensures that the cart contents are avaliable when rendering every page"""

    # requests the cart object if there is one or a blank dictionary if there's not
    cart = request.session.get('cart', {})

    cart_items = []
    price = 10
    total = 0
    for id, quantity in cart.items():
        ticket = get_object_or_404(Features, pk=id)
        total += quantity * 10
        cart_items.append({'id': id, 'quantity': quantity,
                           'ticket': ticket, 'price': price})
    return {'cart_items': cart_items, 'total': total}
