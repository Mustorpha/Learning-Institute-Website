from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
import os

class Section (models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Tag (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class News (models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    featured_image = models.ImageField(default = _('default.jpg'), upload_to=_('news'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField(null = True)
    tag = models.ManyToManyField(Tag)
    date_created = models.DateField(default=timezone.now)
    time_created = models.TimeField(default=timezone.now)

    def get_absolute_url (self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'



class Course (models.Model):

    class Choice(models.IntegerChoices):
        Yes = True
        No = False

    class level(models.TextChoices):
        Beginner = 'Beginner'
        Intermidiate = 'Intermidiate'
        Advanced = 'Advanced'

    name = models.CharField(max_length = 256)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    short_note = models.CharField(max_length=500, null=True)
    course_description = RichTextUploadingField(null=True)
    topic = models.CharField(max_length=128, null=True)
    host = models.CharField(max_length=128, null=True)
    duration = models.CharField(max_length=128, null=True)
    skill_level = models.CharField(max_length=128, null=True, choices=level.choices)
    language = models.CharField(max_length=128, null=True)
    student = models.CharField(max_length=128, null=True)
    certification = models.IntegerField(choices=Choice.choices, null=True, default=Choice.Yes)
    previous_price = models.CharField(max_length=128)
    present_price = models.CharField(max_length=128)
    featured_image = models.ImageField(default = _('default.jpg'), upload_to=_('course'))
    reviews = models.IntegerField()
    popular = models.IntegerField(choices=Choice.choices, null=True, default=Choice.No)
    date_added = models.DateTimeField(default = timezone.now)
    purchase_link = models.CharField(max_length=128, null=True)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url (self):
        return reverse('course-detail', kwargs={'slug': self.slug})
    
    def is_popular (self):
        return self.popular
    
    is_popular.admin_order_field = 'date_added'
    is_popular.boolean = True
    is_popular.short_description = 'Is Popular?'

    def __str__(self):
        return self.name

class Event (models.Model):

    class Choice(models.IntegerChoices):
        Yes = True
        No = False

    title = models.CharField(max_length=256)
    short_note = models.CharField(max_length=500)
    event_description = RichTextUploadingField(null=True)
    featured_image = models.ImageField(default = _('default.jpg'), upload_to=_('events'))
    topic = models.CharField(max_length=128)
    host = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    skill_level = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url (self):
        return reverse('event-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title   

class Speech (models.Model):

    class Choice(models.TextChoices):
        quote = True
        testimonial = False

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(default=_('comment/avatar.jpg'), upload_to=_('comment'))
    content = models.TextField()
    speech_type = models.CharField(choices=Choice.choices, max_length=50, default=Choice.testimonial)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Speeches'

class Content (models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.content

class Pricing_table(models.Model):
    name = models.CharField(max_length=128)
    sub_text = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    duration = models.CharField(max_length=128)
    linked_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = 'Pricing Tables'

class Feature (models.Model):
    table = models.ForeignKey(Pricing_table, on_delete=models.CASCADE, null=True)
    feature = models.CharField(max_length=128)

    def __str__(self):
        return self.feature

class FAQ (models.Model):
    question = models.CharField(max_length=256)
    answer = models.TextField()

    def __str__ (self):
        return self.question

class Outcome (models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    learning_outcomes = models.CharField(max_length=256)
    
    def __str__(self):
        return self.learning_outcomes

class Curriculum (models.Model):
    order_number = models.IntegerField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)

    def __str__(self):
        return '{} Curriculm: {}. {}'.format(self.course,self.order_number, self.title)

class Lesson (models.Model):
    level = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    lesson = models.CharField(max_length=256)
    duration = models.CharField(null=True, max_length=128, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.level, self.lesson)

class Comment(models.Model):
    post = models.ForeignKey(News,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.CharField(blank=True, max_length=200, default='')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_query_name='replies', verbose_name='reply to')

    def __str__(self):
        return '{} by {}'.format(self.body, self.name)

class System (models.Model):
    author = models.CharField(max_length=100)
    system_name = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True)
    address = models.CharField(max_length=500)
    telphone = models.CharField(max_length=14)
    email_address = models.EmailField(null=True, max_length=50)
    whatsapp_link = models.CharField(null=True, max_length=100)
    facebook_link = models.CharField(null=True, max_length=100)
    twitter_link = models.CharField(null=True, max_length=100)
    linkedin_link = models.CharField(null=True, max_length=100)

class Subscription (models.Model):
    email_address = models.EmailField()

    def __str__(self):
        return 'Newsletter Subsciption: {}'.format(self.email_address)

class Application (models.Model):

    class Gender(models.Choices):
        Male = 'Male'
        Female = 'Female'

    class Status(models.IntegerChoices):
        Paid = True
        waiting = False

    class Title(models.Choices):
        Mr = 'Mr.'
        Mrs = 'Mrs.'
        Miss = 'Miss.'
        Engr = 'Engr.'
        Dr = 'Dr.'

    title = models.CharField(choices=Title.choices, max_length=5, default=Title.Mr)
    full_name = models.CharField(max_length=300)
    gender = models.CharField(choices=Gender.choices, max_length=7, default=Gender.Male)
    address = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    photograph = models.ImageField(default=_('anonymous.jpg'), upload_to=_('applications'))
    form = models.FileField(upload_to=_('forms'), default=_('form.pdf'))
    date_added = models.DateTimeField(default=timezone.now)
    payment_status = models.IntegerField(choices=Status.choices, default=Status.waiting, null=True)

    def status (self):
        return self.payment_status
    
    status.admin_order_field = 'date_added'
    status.boolean = True
    status.short_description = 'Payment Status'

    def __str__(self):
        return 'Application for {}. {}'.format(self.title, self.full_name)

@receiver(models.signals.post_delete, sender=Application)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Application` object is deleted.
    """
    if instance.photograph:
        if os.path.isfile(instance.photograph.path):
            os.remove(instance.photograph.path)
    if instance.form:
        if os.path.isfile(instance.form.path):
            os.remove(instance.form.path)

@receiver(models.signals.pre_save, sender=Application)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Application.objects.get(pk=instance.pk).photograph
    except Application.DoesNotExist:
        return False

    new_file = instance.photograph
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    try:
        old_file = Application.objects.get(pk=instance.pk).form
    except Application.DoesNotExist:
        return False

    new_file = instance.form
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
