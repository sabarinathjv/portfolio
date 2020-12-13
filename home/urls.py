
from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = 'developer sabari' #inside display
admin.site.site_title='welcome'
admin.site.index_title='welcome to portal'#changes title




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact')
]
