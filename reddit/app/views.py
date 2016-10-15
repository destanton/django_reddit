from django.shortcuts import render
from app.models import Subreddit, Post, Comment
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def index_view(request):
    # for item in Subreddit.objects.all():
    #     print(item.current_count())
    context = {
        "count": Subreddit.objects.all(),
        "time": Subreddit.objects.all(),
        "post": Post.objects.all(),
        "test": Subreddit.objects.all().count()
    }
    return render(request, "index.html", context)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class SubredditDetailView(DetailView):
    model = Subreddit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class SubpostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context
    # def get_comment(self):
    #     comment = Comment.objects.all()
    #     return comment
    # for item in Comment.objects.all():
    #     print(item.comment)


class SubCreateView(CreateView):
    model = Subreddit
    success_url = "/"
    fields = ('name', 'description')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class SubUpdateView(UpdateView):
    model = Subreddit
    success_url = "/"
    fields = ('name', 'description')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class PostCreateView(CreateView):
    model = Post
    success_url = "/"
    fields = ('title', 'description', 'url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    success_url = "/"
    fields = ('title', 'description', 'url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class CommentCreateView(CreateView):
    model = Comment
    success_url = "/"
    fields = ('comment',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class CommentUpdateView(UpdateView):
    model = Comment
    success_url = "/"
    fields = ('comment',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context
