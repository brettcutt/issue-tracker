from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import BugsForm, CommentForm, FeaturesForm
from .models import Comments, Bugs, Features
from accounts.models import ProfilePicture
from django.utils import timezone
from django.contrib.auth.models import User


def bugs_features(request):
    """Renders a view with all bug and feature tickets"""
    bugs_tickets = Bugs.objects.all()

    features_tickets = Features.objects.all()
    return render(request, 'bugs-features.html', {'bugs_tickets': bugs_tickets, 'features_tickets': features_tickets})


def bug_detail(request, id):
    """Renders a view of an individual ticket"""
    user = User.objects.get(username=request.user)
    print(user)
    bug = get_object_or_404(Bugs, id=id)
    comments = Comments.objects.filter(ticket=bug).order_by('-created_date')
    comment_form = CommentForm()
    bug.views += 1
    bug.save()
    return render(request, "bug_detail.html", {'user': user, 'items': bug, 'comment_form': comment_form, 'comments': comments})


def feature_detail(request, id):
    """Renders a view of an individual ticket"""
    feature = get_object_or_404(Features, id=id)
    comments = Comments.objects.filter(
        feature_ticket=feature).order_by('-created_date')
    comment_form = CommentForm()
    feature.views += 1
    feature.save()
    return render(request, "feature_detail.html", {'items': feature, 'comment_form': comment_form, 'comments': comments})


def add_comment_bugs(request, id=id):
    bug = get_object_or_404(Bugs, id=id)
    pic = ProfilePicture.objects.filter(user=request.user)

    image = ''
    for item in pic:
        image = item

    comment_form = CommentForm(request.POST, request.FILES)
    if comment_form.is_valid():
        instance = comment_form.save(commit=False)
        instance.username = request.user
        instance.ticket = bug
        if image == "":
            instance.picture = ProfilePicture.objects.get(user="missing")
        else:
            instance.picture = image

        comment_form.save()

    return redirect(bug_detail, id)


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


def add_bug(request):
    pic = ProfilePicture.objects.filter(user=request.user)
    image = ''
    for item in pic:
        image = item
        print(item)

    if request.method == "POST":
        form = BugsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            if image == "":
                form.picture = ProfilePicture.objects.get(user="missing")
            else:
                form.picture = image
            form.save()
            return redirect(reverse(bugs_features))
    else:
        form = BugsForm()

    return render(request, 'add_ticket.html', {'form': form})


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
            return redirect(reverse(bugs_features))
    else:
        form = FeaturesForm()

    return render(request, 'add_ticket.html', {'form': form})
