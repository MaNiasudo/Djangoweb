from django import template
register = template.Library()
from blog.models import Post

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count
    return posts

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:4]
    return {'posts':posts}