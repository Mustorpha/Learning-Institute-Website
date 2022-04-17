# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Section, Course, Pricing_table, News, Tag, FAQ, Comment, Feature, Outcome, Lesson, Speech, Curriculum, Content, Event, System, Subscription, Application
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.utils.text import Truncator

admin.site.site_header = "Administration Panel"
admin.site.site_title = "Hosanna Computer Institute"
admin.site.index_title = "Hosanna Computer Institute"

class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 7

class OutcomeInline(admin.StackedInline):
    model = Outcome
    extra = 3

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 3

class ContentInline(admin.StackedInline):
    model = Content
    extra = 3

class Event_admin(admin.ModelAdmin):
    fieldsets = [
        (
            'Description', {'fields': ['title', 'short_note', 'event_description', 'featured_image', 'slug']}            
        ),
        (
            'Additional Information', {'classes':('collapse',),
                'fields': ['topic', 'host', 'location', 'skill_level', 'language', 'date', 'time']}
        )
    ]
    list_display = ['title', 'get_image', 'host', 'skill_level', 'language', 'date']
    list_max_show_all = 10
    list_filter = ['date', 'host', 'skill_level', 'language']
    inlines = [ContentInline]
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

    def get_image (self, obj):
        return format_html('''
            <img src="%(photo_url)s" alt="" width="180" style="border-radius : 8px"/>'''%{
            'photo_url' : obj.featured_image.url,
        })
    get_image.short_description = _("Featured Image")
    get_image.allow_tags = True

class System_admin(admin.ModelAdmin):
    fieldsets = [
        (
            'System Information', {'fields': ['author', 'system_name', 'description', 'address', 'email_address']}            
        ),
        (
            'Social Links', {'fields': ['whatsapp_link', 'facebook_link', 'linkedin_link', 'twitter_link']}
        )
    ]

class Curriculum_admin(admin.ModelAdmin):
    list_max_show_all = 50
    list_filter = ['course', 'order_number']
    search_fields = ['title']
    ordering = ('-course','order_number')
    inlines = [LessonInline]

def speech(obj):
    speech = "%s" % obj.content
    return Truncator(speech).chars(60)

class Speech_admin(admin.ModelAdmin):
    list_display = ['name', 'get_image', 'title', 'speech_type', speech]
    list_max_show_all = 10
    list_filter = ['name', 'speech_type', 'title']
    def get_image (self, obj):
        return format_html('''
            <img src="%(photo_url)s" alt="" width="60" style="border-radius : 8px"/>'''%{
            'photo_url' : obj.image.url,
        })
    get_image.short_description = _("Image")
    get_image.allow_tags = True

class Pricing_table_admin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {'fields': [('name', 'sub_text'), 'linked_course']}),
        ('Pricing and Duration', {'fields': ['price', 'duration']}),
    ]
    inlines = [FeatureInline]
    list_display = ['name', 'price', 'duration']

class Course_admin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {'fields': [('name', 'slug'), 'section', 'featured_image', 'short_note', 'course_description']}),
        ('Additional Information', {'classes' : ('collapse',),
            'fields' : ['topic', 'host', 'duration', 'skill_level', 'language', 'student', 'certification']}),
        ('Pricing & Reviews', {'fields': [('previous_price', 'present_price'), 'reviews', 'popular', 'date_added']})
    ]
    list_display = ['name', 'get_image', 'section', 'present_price', 'reviews', 'date_added', 'is_popular']
    list_max_show_all = 10
    list_filter = ['date_added', 'section', 'popular']
    search_fields = ['name']
    radio_fields = {"popular": admin.HORIZONTAL, "certification" : admin.HORIZONTAL}
    inlines = [OutcomeInline]
    prepopulated_fields = {'slug': ('name',)}
    actions = ['make_popular']

    def get_image (self, obj):
        return format_html('''
            <img src="%(photo_url)s" alt="" width="180" style="border-radius : 8px"/>'''%{
            'photo_url' : obj.featured_image.url,
        })
    get_image.short_description = _("Featured Image")
    get_image.allow_tags = True

    def make_popular(self, request, queryset):
        queryset.update(popular=True)

def name(obj):
    name = "%s" % obj
    return Truncator(name).chars(30)


class Application_admin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields' : [('title', 'full_name'), 'gender', 'address', 'date_of_birth', 'email']}),
        ('Course Information', {'fields' : ['course', ('photograph', 'form'), 'payment_status', 'date_added']})
    ]
    
    list_display = [name, 'get_image', 'gender', 'course', 'date_added', 'status']
    list_display_links = [name]
    radio_fields = {"payment_status" : admin.HORIZONTAL, "gender" : admin.HORIZONTAL}
    search_fields = ['full_name', 'email']
    list_filter = ['course', 'date_added', 'gender', 'title', 'payment_status']

    def get_image (self, obj):
        return format_html('''
            <img src="%(photo_url)s" alt="" width="60" style="border-radius : 8px"/>'''%{
            'photo_url' : obj.photograph.url,
        })
    get_image.short_description = _("Photograph")
    get_image.allow_tags = True
    list_max_show_all = 20
    ordering = ['full_name','-date_added']

class News_admin(admin.ModelAdmin):
    fieldsets = [
        ('Blog', {'fields': ['title', 'featured_image', 'content', 'slug']}),
        ('Optional Information', {'classes' : ('collapse',),
            'fields': ['author', 'date_created', 'time_created', 'tag']})
    ]
    list_display = ['title', 'get_image', 'author', 'date_created', 'time_created']
    list_max_show_all = 10
    list_filter = ['date_created', 'author', 'tag']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tag']

    def get_image (self, obj):
        return format_html('''
            <img src="%(photo_url)s" alt="" width="180" style="border-radius : 8px"/>'''%{
            'photo_url' : obj.featured_image.url,
        })
    get_image.short_description = _("Featured Image")
    get_image.allow_tags = True


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active', 'parent')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    list_max_show_all = 20

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class SubAdmin(admin.ModelAdmin):
    list_display = ['email_address']
    list_max_show_all = 20
    search_fields = ['email_address']

admin.site.register(Pricing_table, Pricing_table_admin)
admin.site.register(Section)
admin.site.register(Course, Course_admin)
admin.site.register(FAQ)
admin.site.register(Tag)
admin.site.register(Curriculum, Curriculum_admin)
admin.site.register(Event, Event_admin)
admin.site.register(Speech, Speech_admin)
admin.site.register(News, News_admin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscription, SubAdmin)
admin.site.register(Application, Application_admin)