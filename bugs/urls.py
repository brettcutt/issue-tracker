from django.conf.urls import url
from .views import bugs, add_bug, bug_detail, add_comment_bugs

urlpatterns = [
    url(r'^$', bugs, name='bugs'),
    url(r'^bug_detail/(?P<id>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^add_bug$', add_bug, name='add_bug'),
    url(r'^add_comment_bugs/(?P<id>\d+)/$',
        add_comment_bugs, name='add_comment_bugs'),
]
