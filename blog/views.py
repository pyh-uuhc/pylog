from django.shortcuts import render
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)

    context = {
        "post": post,
    }
    return render(request, 'post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        print("method POST")
        title = request.POST['title']
        content = request.POST['content']
        print(title)
        print(content)
    else:
        print("method GET")

    # POST/GET 중 어느 요청이든 render 결과를 리턴
    return render(request, 'post_add.html')
