from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from django_twitter.posts.models import Posts

class PostView(View):
    def get(self, request, pk):
        post = Posts.objects.get(pk=pk)
        comment = Comments.object.filter()
        return TemplateResponse (request, 'post_view.html', {
            "post-view": post,
            "comment":comment
        })


class PostListView(View):
    pass