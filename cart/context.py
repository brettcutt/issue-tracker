from django.shortcuts import get_object_or_404
from bugs.models import Features


def cart_contents(request):
    """Ensures that the cart contents are avaliable when rendering every page"""

    # requests the cart object if there is one or a blank dictionary if there's not
    cart = request.session.get('cart', {})

    cart_items = []
    upvote_list = []
    price = 10
    total = 0
    ticket_count = 0
    for id, quantity in cart.items():
        ticket = get_object_or_404(Features, pk=id)
        upvote_list.append(id)
        ticket_count += quantity
        total += quantity * price
        cart_items.append({'id': id, 'quantity': quantity,
                           'ticket': ticket, 'price': price})
    print(upvote_list)

    return {'ticket_count': ticket_count,
            'cart_items': cart_items,
            'total': total,
            'upvote_list': upvote_list}
