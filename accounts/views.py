from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
# @login_required:  if the user trys to access logout through the endpoint this redirects them to the login page
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from bugs.models import Comments, BugUpvote
from features.models import UpvoteFeature
from django.contrib.auth.models import User
from .forms import ProfilePicForm
from .models import ProfilePicture


@login_required
def logout(request):
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('login'))


def login(request):
    """login the user"""
    """ If the user is already logged in and they try to access login through the endpoint redirect them back to index.html"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                messages.success(request, "You have successfully logged in!")
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                messages.warning(
                    request, "Your username or password is incorrect!")
                # login_form.add_error(
                # None, "Your username or password is incorrect!")

    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """Render the registration page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)

                messages.success(
                    request, "You have been successfully registered!")
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request, "Unable to register your account at this time!")

    else:
        registration_form = UserRegistrationForm()

    return render(request, "registration.html", {'registration_form': registration_form})


def user_profile(request):
    """The user's profile page"""

    user = User.objects.get(email=request.user.email)
    bug_upvotes = BugUpvote.objects.filter(user=user).count()
    features_upvoted = UpvoteFeature.objects.filter(user=user).count()

    try:
        picture = get_object_or_404(ProfilePicture, user=request.user)
    except:
        picture = ProfilePicture()
        picture.user = user
        picture.picture = 'images/missing-profile-pic.png'
        picture.save()
    if request.method == 'POST':
        print('#1')
        pic_form = ProfilePicForm(
            request.POST, request.FILES, instance=picture)

        if pic_form.is_valid():
            print('#2')
            pic_form = pic_form.save(commit=False)
            pic_form.user = request.user
            pic_form.save()

            try:
                comment_pic = get_object_or_404(Comments, user=request.user)
                comment_pic.picture = picture
                comment_pic.save()
            except:
                comment_pic = Comments()

            return redirect(reverse('profile'))
    else:
        pic_form = ProfilePicForm(instance=picture)
    return render(request, 'profile.html', {'features_upvoted': features_upvoted, 'bug_upvotes': bug_upvotes, 'profile': user, 'pic_form': pic_form, 'picture': picture})
