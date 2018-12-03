from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm
from django.conf import settings
from django.utils import timezone
from features.models import Features
from .models import Upvote
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        print("test1")
        if payment_form.is_valid():
            print('test2')
            cart = request.session.get('cart', {})
            total = 0
            upvote_list = []
            for id, quantity in cart.items():
                feature = get_object_or_404(Features, pk=id)
                upvote_list.append(id)
                total += quantity * 10
            print(upvote_list)
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="AUD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")

                print(upvote_list)

                for id in upvote_list:
                    feature_name = get_object_or_404(
                        Features, id=id)
                    try:
                        upvote = get_object_or_404(
                            Upvote, user=request.user, upvoted_feature=feature_name)
                    except:
                        upvote = Upvote()

                    upvote.user = request.user
                    upvote.upvoted_feature = feature_name
                    feature_name.upvotes += 1
                    feature_name.save()
                    upvote.save()

                request.session['cart'] = {}
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()

    return render(request, "checkout.html", {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
