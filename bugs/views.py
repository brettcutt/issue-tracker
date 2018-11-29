from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import BugsForm, CommentForm
from .models import Comments, Bugs, BugUpvote
from accounts.models import ProfilePicture
from django.utils import timezone
from django.contrib.auth.models import User


def bugs(request):
    """Renders a view with all bug tickets"""
    tickets = Bugs.objects.all()
    return render(request, 'bugs.html', {'tickets': tickets})


def bug_detail(request, id):
    """Renders a view of an individual ticket"""
    try:
        user = User.objects.get(username=request.user)
    except:
        user = None

    bug = get_object_or_404(Bugs, id=id)
    upvote = BugUpvote.objects.filter(upvoted_bug=bug)

    upvoted = False
    for item in upvote:
        if str(item) == str(user):
            upvoted = True
    print(upvoted)
    print(user)
    comments = Comments.objects.filter(ticket=id).order_by('-created_date')
    comment_form = CommentForm()
    bug.views += 1
    bug.save()
    return render(request, "bug_detail.html", {'upvoted': upvoted, 'user': user, 'items': bug, 'comment_form': comment_form, 'comments': comments})


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


def add_edit_bug(request, id=None):
    bug = get_object_or_404(Bugs, id=id) if id else None
    pic = ProfilePicture.objects.filter(user=request.user)
    image = ''
    for item in pic:
        image = item
        print(item)

    if request.method == "POST":
        form = BugsForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            if image == "":
                form.picture = ProfilePicture.objects.get(user="missing")
            else:
                form.picture = image
            form.save()
            return redirect(reverse(bugs))
    else:
        form = BugsForm(instance=bug)

    return render(request, 'add_ticket.html', {'form': form})


def upvote_bug(request, id=id):
    bug = get_object_or_404(Bugs, id=id)
    print("here", bug)
    bug.upvotes += 1
    bug.views -= 1
    bug.save()

    try:
        upvote = get_object_or_404(
            BugUpvote, upvoted_bug=bug, user=request.user)
    except:
        upvote = BugUpvote()
    upvote.upvoted_bug = bug
    upvote.user = request.user
    upvote.save()
    return(redirect(bug_detail, id))
