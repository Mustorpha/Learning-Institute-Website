from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from . import models
from django.db.models import Q 
from django.views.generic import ListView, DetailView
from datetime import date
from .forms import CommentForm, RegistrationForm
from django.core.mail import EmailMessage

def index(request):
    context = {
        'Pricing_table' : models.Pricing_table.objects.all()[:3],
        'FAQ' : models.FAQ.objects.all(),
        'Recent' : models.Course.objects.all()[:10],
        'Course' : models.Course.objects.all(),
        'Event' : models.Event.objects.all()[:6],
        'Speech' : models.Speech.objects.filter(speech_type=True),
        'News' : models.News.objects.all()[:7],
        'title' : 'Home'
    }
    return render(request, "hosannaWebsite/home.html", context)

class Course(ListView):
    def get_queryset(self):
        if self.request.GET.get('category'):
            category = self.request.GET.get('category')
            return models.Course.objects.filter(section = category).order_by('-reviews')
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            return models.Course.objects.filter(Q(name__icontains=search) |Q(short_note=search)).order_by('-reviews')
        else:
            return models.Course.objects.all().order_by('-reviews')

    def get_context_data (self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the courses
        context['Section'] = models.Section.objects.all()
        context['Recent'] = models.Course.objects.all().order_by('-date_added')[:2]
        context['title'] = 'Course'
        return context
    template_name = "hosannaWebsite/courses.html"
    context_object_name = "Course"
    paginate_by = 9

class course_detail(DetailView):
    model = models.Course

    def get_context_data (self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course'
        return context

    template_name = "hosannaWebsite\course-details.html"
    context_object_name = "Course"

def about(request):
    context = {
        'title' : 'About',
        'Testimonial' : models.Speech.objects.filter(speech_type=False)
    }
    return render(request, "hosannaWebsite/about.html", context)

class Event(ListView):
    model = models.Event

    def get_context_data (self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Event'
        context['today'] = date.today()
        return context
    template_name = "hosannaWebsite/event.html"
    context_object_name = "Event"
    paginate_by = 10

class EventDetail (DetailView):
    model = models.Event

    def get_context_data (self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Event'
        return context

    template_name = "hosannaWebsite\event-details.html"
    context_object_name = "Event"

class News(ListView):
    def get_queryset(self):
        if self.request.GET.get('tag'):
            tag = self.request.GET.get('tag')
            return models.News.objects.filter(tag = tag).order_by('-date_created')
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            return models.News.objects.filter(Q(title__icontains=search) | Q(content__icontains=search)).order_by('-date_created')
        else:
            return models.News.objects.order_by('-date_created')

    def get_context_data (self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        context['Recent'] = models.News.objects.order_by('-date_created')[:3]
        context['Tag'] = models.Tag.objects.all()
        return context
    template_name = "hosannaWebsite/news.html"
    context_object_name = "News"
    paginate_by = 10

class NewsDetail (DetailView):
    model = models.News

    def get_context_data (self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = models.News.objects.get(slug=slug)
        comments = post.comment_set.filter(active=True)
        reply = post.comment_set.filter(active=True).exclude(parent=None)
        no_comment = comments.count()
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['title'] = 'News'
        context['Recent'] = models.News.objects.all().order_by('-date_created')[:3]
        context['Tag'] = models.Tag.objects.all()
        context['comments'] = comments
        context['Reply'] = reply
        context['no_comment'] = no_comment
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = models.News.objects.get(slug=slug)
        comments = post.comment_set.filter(active=True)
        no_comment = comments.count()
        new_comment = None
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():

                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()
                context['title'] = 'News'
                context['Recent'] = models.News.objects.all().order_by('-date_created')[:3]
                context['Tag'] = models.Tag.objects.all()
                context['new_comment'] = new_comment
                context['no_comment'] = no_comment
                return self.render_to_response(context=context)
        else:
            comment_form = CommentForm()
        return self.render_to_response(context=context)

    template_name = "hosannaWebsite/news-detail.html"
    context_object_name = "News"

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        #mail = EmailMessage(
            #subject,
            #'email : ' + email + message,
            #to=['demo@example.com'],
        #)
        #mail.send()

        context = {
            'text' : 'Your message has been sent',
            'title' : 'Contact',
        }
        return render(request, 'hosannaWebsite/contact.html', context)

    context = {
        'title' : 'Contact',
    }
    return render(request, 'hosannaWebsite/contact.html', context)

def subscription (request):
    email = request.POST['subscription']
    pre_page = request.POST['next']
    models.Subscription.objects.create(email_address=email)
    return HttpResponseRedirect(redirect_to=pre_page)

def page_not_found_view(request, exception):
    return render(request, 'hosannaWebsite/404.html', status=404)

def register(request, name=""):
    if request.method == 'POST':
        registration = RegistrationForm(request.POST, request.FILES)
        if registration.is_valid():
            registration.save()
            context = {
                'Course' : name,
                'text' : 'Your application has been submitted successfully!',
                'finishing' : 'Proceed to the institute location for Payment or with your proof of Payment to complete the Application Process'

            }
            return render(request, 'hosannaWebsite/register.html', context)

    course = models.Course.objects.get(name=name)
    context = {
        'form' : RegistrationForm(initial={'course' : course}),
        'Course' : name,

    }
    return render(request, 'hosannaWebsite/register.html', context)

def download_file(request):
    import os
    import mimetypes

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filename = 'form.pdf'
    filepath = BASE_DIR + '/media/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
