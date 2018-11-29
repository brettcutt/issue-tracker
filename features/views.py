from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import FeaturesForm
from bugs.forms import CommentForm
from .models import Features
from bugs.models import Comments
from checkout.models import Upvote
from accounts.models import ProfilePicture
from django.utils import timezone
from django.contrib.auth.models import User


def features(request):
    """Renders a view with feature tickets"""

    tickets = Features.objects.all()
    return render(request, 'features.html', {'tickets': tickets})


def feature_detail(request, id):
    """Renders a view of an individual ticket"""
    feature = get_object_or_404(Features, id=id)

    upvotes = Upvote.objects.filter(upvoted_feature=feature)

    upvoted = False
    user = str(request.user)
    for item in upvotes:
        item = str(item)
        if item == user:
            upvoted = True

    comments = Comments.objects.filter(
        feature_ticket=id).order_by('-created_date')
    comment_form = CommentForm()
    feature.views += 1
    feature.save()
    return render(request, "feature_detail.html", {'upvoted': upvoted, 'items': feature, 'comment_form': comment_form, 'comments': comments})


def add_comment_features(request, id=id):
    feature = get_object_or_404(Features, id=id)
    pic = ProfilePicture.objects.filter(user=request.user)
    print(feature)
    image = ''
    for item in pic:
        image = item

    comment_form = CommentForm(request.POST, request.FILES)
    if comment_form.is_valid():
        instance = comment_form.save(commit=False)
        instance.username = request.user
        instance.feature_ticket = feature
        if image == "":
            instance.picture = ProfilePicture.objects.get(user="missing")
        else:
            instance.picture = image

        comment_form.save()

    return redirect(feature_detail, id)


def add_feature(request):
    pic = ProfilePicture.objects.filter(user=request.user)
    image = ''
    for item in pic:
        image = item
        print(item)

    if request.method == "POST":
        form = FeaturesForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            if image == "":
                form.picture = ProfilePicture.objects.get(user="missing")
            else:
                form.picture = image
            form.save()
            return redirect(reverse(features))
    else:
        form = FeaturesForm()

    return render(request, 'add_ticket.html', {'form': form})
