from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Post, Category
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import AnonymousUser
from posts.forms import PostForm
from dal import autocomplete
from django.core.paginator import Paginator


def posts_list(request):
    posts = Post.objects.filter(published=True)
    # q = request.GET("q")
    #
    # if q:
    #     posts = posts.filter(title_incontains=q)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)
    context = {'posts_list': posts_list}
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
    id = posts.id
    title = posts.title
    content = posts.content
    published = posts.published
    sponsored = posts.sponsored
    user = posts.user
    tags = posts.tags.all()
    categories = posts.categories.all()
    exemple_file = posts.exemple_file
    image = posts.image
    created = posts.created
    modified = posts.modified
    return render(request, "posts/details.html", context={
        'id' : id,
        'title' : title,
        'content': content,
        'published' : published,
        'sponsored' : sponsored,
        'user' : user,
        'tags' : tags,
        'categories' : categories,
        'exemple_file' : exemple_file,
        'image' : image,
        'created':created,
        'modified':modified
    })


def post_sponsored(request):
    posts = Post.objects.all()
    sponsored = posts.sponsored
    return render(request, "posts/list.html", context={'sponsored': sponsored})


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            # form.user = request.user
            if form.is_valid():
                # form.save()
                instance = form.save(commit=False)
                instance.user = request.user
                # instance.image = request.FILES
                instance.save()
                form.save_m2m()
            return HttpResponseRedirect(reverse("posts:list"))
            # tu dodam przekierowanie na szczegóły
        else:
            form = PostForm()
        return(
            render(request, "posts/add.html", {"form": form})
        )
    else:
        return redirect(reverse('login'))


def edit_post(request, post_id):
    user = request.user
    posts = user.posts.all()
    for post in posts:
        if request.method == "POST":
            if user.is_authenticated:
                if user == post.user:
                    form = PostForm(request.POST, request.FILES, instance=post)
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(reverse("posts:list"))
                    else:
                        return redirect(reverse('login'))
    else:
        if user.is_authenticated:
            if user == request.user:
                form = PostForm(instance=post)
                return render( request,"posts/edit.html", {"form": form})


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
