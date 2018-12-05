from django.conf.urls import url
from .views import view_cart, add_to_cart, remove_ticket

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)/$', add_to_cart, name='add_to_cart'),
    url(r'^remove_ticket/(?P<id>\d+)/$', remove_ticket, name='remove_ticket'),

]
