from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import BugsForm, CommentForm
from .models import Comments, Bugs, BugUpvote
from accounts.models import ProfilePicture
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def bugs(request):
    """Renders a view with all bug tickets"""
    tickets = Bugs.objects.all().order_by('-created_date')
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

    comments = Comments.objects.filter(ticket=id).order_by('created_date')
    comments_number = comments.count()
    comment_form = CommentForm()
    bug.views += 1
    bug.save()

    paginator = Paginator(comments, 10)
    page = request.GET.get('page')

    if not page:
        page = paginator.num_pages
    try: 
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request, "bug_detail.html", {'upvoted': upvoted, 
                                               'user': user, 
                                               'items': bug, 
                                               'comment_form': comment_form, 
                                               'comments': comments,
                                               'comments_number':comments_number})


@login_required
def add_comment_bugs(request, id=id):
    """Saves a posted comment  """

    bug = get_object_or_404(Bugs, id=id)
    pic = get_object_or_404(ProfilePicture, user=request.user)

    comment_form = CommentForm(request.POST, request.FILES)

    if comment_form.is_valid():
        instance = comment_form.save(commit=False)
        instance.username = request.user
        instance.ticket = bug
        instance.picture = pic

        comment_form.save()

    return redirect(bug_detail, id)


@login_required
def add_edit_bug(request, id=None):
    """Renders the add or edit page and saves posted tickets  """
    
    bug = get_object_or_404(Bugs, id=id) if id else None
    pic = get_object_or_404(ProfilePicture, user=request.user)
    
    user = str(request.user)
    add_edit = True
    if bug == None:
        add_edit = False
    if request.method == "POST":
        form = BugsForm(request.POST, request.FILES, instance=bug)

        if form.is_valid():
            form = form.save(commit=False)
            if user == 'admin':
                form.status = request.POST.get('status')
                if str(form.status) == 'In Progress':

                    form.waiting_date = None
                    form.in_progress_date = timezone.now()
                elif str(form.status) == 'Completed':
                    form.in_progress_date = None
                    form.completion_date = timezone.now()

            if bug == None:
                form.username = request.user
                form.picture = pic
                form.views = 0
                form.created_date = timezone.now()
                form.waiting_date = timezone.now()
                form.save()
                return redirect(reverse(bugs))
            else:
                form.username = bug.username
                form.picture = bug.picture
                form.views -= 1
                form.save()
                return redirect(bug_detail, id)
    else:
        form = BugsForm(instance=bug)

    return render(request, 'add_ticket.html', {'add_edit': add_edit, 'form': form})


@login_required
def upvote_bug(request, id=id):
    """Adds one upvote point to the ticket  """
    bug = get_object_or_404(Bugs, id=id)
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
