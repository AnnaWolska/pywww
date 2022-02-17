from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Post
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from posts.forms import PostForm


def posts_list(request):
    posts = Post.objects.all()
    # template = loader.get_template('posts/list.html')
    # context = {'posts_list':posts}
    # return HttpResponse(template.render(context=context))
    context = {'posts_list': posts}
    return render(request, "posts/list.html", context)


def first_post(request):
    post = Post.objects.first()
    html = "<h2>" + post.title + "</h2> "
    html += f'''<div> 
        <small> Utworzono {post.created} , zmodyfikowano {post.modified} </small> 
        </div> 
        <div> <p> {post.content} </p> </div>'''
    return HttpResponse(html)


def post_details(request, post_id):
    posts = Post.objects.get(pk=post_id)
    title = posts.title
    content = posts.content
    published = posts.published
    sponsored = posts.sponsored
    user = posts.user
    tags = posts.tags
    categories = posts.categories
    exemple_file = posts.exemple_file
    image = posts.image
    return render(request, "posts/details.html", context={
        'title' : title,
        'content': content,
        'published' : published,
        'sponsored' : sponsored,
        'user' : user,
        'tags' : tags,
        'categories' : categories,
        'exemple_file' : exemple_file,
        'image' : image
    })


def post_sponsored(request):
    posts = Post.objects.all()
    sponsored = posts.sponsored
    return render(request, "posts/list.html", context={'sponsored': sponsored})


def add_post(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data['user'] = request.user
            # post = Post.objects.create(**form.cleaned_data)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse("posts:add_post"))
    else:
        form = PostForm()
    return(
        render(request, "posts/add.html", {"form": form})
    )


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(
        request,
        "posts/add.html",
        {"form": form}
    )