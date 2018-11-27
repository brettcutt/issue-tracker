from django.conf.urls import url
from .views import bugs_features, add_bug, bug_detail, add_comment_bugs, add_comment_features, add_feature, feature_detail

urlpatterns = [
    url(r'^$', bugs_features, name='bugs_features'),
    url(r'^bug_detail/(?P<id>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^feature_detail/(?P<id>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^add_bug$', add_bug, name='add_bug'),
    url(r'^add_feature$', add_feature, name='add_feature'),
    url(r'^add_comment_bugs/(?P<id>\d+)/$',
        add_comment_bugs, name='add_comment_bugs'),
    url(r'^add_comment_features/(?P<id>\d+)/$',
        add_comment_features, name='add_comment_features'),
]
