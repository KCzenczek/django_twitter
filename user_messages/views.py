from django.views.generic import CreateView, DeleteView, ListView, DetailView
from user_messages.forms import MessageCreateForm
from user_messages.models import UserMessage


class UserMessagesListView(ListView):

    def get_queryset(self):
        user = self.request.user
        queryset = UserMessage.objects.filter(sender=user)
        return queryset


class MessageCreateView(CreateView):
    model = UserMessage
    form_class = MessageCreateForm
    template_name = 'user_messages/message_add.html'
    success_url = '/'


class MessageDeleteView(DeleteView):
    model = UserMessage
    form_class = 'user_messages/message_delete.html'
    success_url = '/'


class MessageDetailView(DetailView):
    pass