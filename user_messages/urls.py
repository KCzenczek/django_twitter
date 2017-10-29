from django.conf.urls import url


urlpatterns = [
    url(r'message-send/$',
        views.MessageCreateView.as_view(), name='message-create'),

    url(r'messages-list/(?P<pk>\d+)',
        views.SuerMessagesListView.as_view(), name='user-massages-list'),

]
