from django.views.generic import CreateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from user_messages.forms import MessageCreateForm
from user_messages.models import UserMessage


class UserMessagesListView(LoginRequiredMixin, ListView):

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
    template_name = 'user_messages/message_delete.html'
    success_url = '/'


class MessageDetailView(DetailView):
    model = UserMessage
    template_name = 'user_messages/message_detail.html'
