from django.conf.urls import url
from .views import features, add_comment_features, add_feature, feature_detail

urlpatterns = [
    url(r'^$', features, name='features'),
    url(r'^feature_detail/(?P<id>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^add_feature$', add_feature, name='add_feature'),
    url(r'^add_comment_features/(?P<id>\d+)/$',
        add_comment_features, name='add_comment_features'),
]
