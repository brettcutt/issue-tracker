from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import FeaturesForm
from bugs.forms import CommentForm
from .models import Features, UpvoteFeature
from bugs.models import Comments
from accounts.models import ProfilePicture
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def features(request):
    """Renders a view with feature tickets"""

    tickets = Features.objects.all().order_by('-created_date')
    return render(request, 'features.html', {'tickets': tickets})


def feature_detail(request, id):
    """Renders a view of an individual ticket"""

    feature = get_object_or_404(Features, id=id)

    upvotes = UpvoteFeature.objects.filter(upvoted_feature=feature)

    upvoted = False
    user = str(request.user)
    for item in upvotes:
        item = str(item)
        if item == user:
            upvoted = True

    comments = Comments.objects.filter(feature_ticket=id).order_by('created_date')
    comments_number = comments.count()
    comment_form = CommentForm()
    feature.views += 1
    feature.save()

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
    return render(request, "feature_detail.html", {'upvoted': upvoted,
                                                   'items': feature,
                                                   'comment_form': comment_form,
                                                   'comments': comments,
                                                   'comments_number':comments_number})


@login_required
def add_comment_features(request, id=id):
    """Saves a posted comment  """

    feature = get_object_or_404(Features, id=id)
    pic = ProfilePicture.objects.filter(user=request.user)
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


@login_required
def add_edit_feature(request, id=None):
    """Renders the add or edit page and saves posted tickets  """

    feature = get_object_or_404(Features, id=id) if id else None
    pic = get_object_or_404(ProfilePicture, user=request.user)
    user = str(request.user)
    add_edit = True
    if feature == None:
        add_edit = False

    if request.method == "POST":
        form = FeaturesForm(request.POST, request.FILES, instance=feature)

        if form.is_valid():
            form = form.save(commit=False)
            if user == 'admin' or user == 'testadmin':
                form.status = request.POST.get('status')
                if str(form.status) == 'In Progress':
                    form.waiting_date = None
                    form.in_progress_date = timezone.now()
                elif str(form.status) == 'Completed':
                    form.in_progress_date = None
                    form.completion_date = timezone.now()
            if feature == None:
                form.username = request.user
                form.picture = pic
                form.views = -1
                form.created_date = timezone.now()
                form.waiting_date = timezone.now()
                form.save()
                return redirect(reverse(features))
            else:
                form.username = feature.username
                form.picture = feature.picture
                form.views -= 1
                form.save()
                return redirect(feature_detail, id)
    else:
        form = FeaturesForm(instance=feature)

    return render(request, 'add_ticket.html', {'add_edit': add_edit,
                                               'form': form})


@login_required
def upvote_feature(request):
    """Adds one upvote point to the ticket  """

    cart = request.session.get('cart', {})
    upvote_list = []

    for id, quantity in cart.items():
        feature = get_object_or_404(Features, pk=id)
        upvote_list.append(id)

    for id in upvote_list:
        feature_name = get_object_or_404(
            Features, id=id)
        try:
            upvote = get_object_or_404(
                UpvoteFeature, user=request.user, upvoted_feature=feature_name)
        except:
            upvote = UpvoteFeature()
        upvote.user = request.user
        upvote.upvoted_feature = feature_name
        feature_name.upvotes += 1
        feature_name.save()
        upvote.save()
    request.session['cart'] = {}
    return redirect(reverse('index'))
