from django import forms
from user_messages.models import UserMessage

class MessageCreateForm(forms.ModelForm):

    class Meta:
        model = UserMessage
        fields = '__all__'
