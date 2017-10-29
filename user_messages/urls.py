from django.conf.urls import url
from user_messages import views


urlpatterns = [

    url(r'message-send/$',
        views.MessageCreateView.as_view(), name='message-create'),

    url(r'messages-list/$',
        views.UserMessagesListView.as_view(), name='user-massages-list'),

    url(r'messages-delete/(?P<pk>\d+)/$',
        views.MessageDeleteView.as_view(), name='message-delete'),

    url(r'message-detail/(?P<pk>\d+)$/',
        views.MessageDetailView.as_view(), name='message-detail'),

]
