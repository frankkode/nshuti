import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponse
from blog.models import Blog
from .forms import ContactForm, BlogForm
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.paginator import Paginator, PageNotAnInteger



def home(request):
    posts = Blog.objects.all().order_by('-created_at')[:3]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"New message from {email}"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
        )
        return render(request, 'thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def services(request):
    return render(request, 'services.html')


def resume(request):
     return render(request, 'resume.html')


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})

def blog(request):
    posts = Blog.objects.order_by('-created_at')
    paginator = Paginator(posts, 10) # paginate after 10 entries

    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': paginated_posts})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def download_cv(request):
    cv_path = staticfiles_storage.path('static/cv.pdf')
    if os.path.exists(cv_path):
        with open(cv_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
            return response
    else:
        return HttpResponseNotFound("The requested CV was not found.")

