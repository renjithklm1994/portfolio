
from django.urls import path
from . import views
urlpatterns = [
      
      path('', views.home),
           
     path('index/',views.index,name='index'),
     path('hero/',views.hero,name='hero'),
    path('about/',views.about,name='about'),
    path('resume/',views.resume,name='resume'),
        path('portfolio/',views.portfolio,name='portfolio'),
          path('service/',views.service,name='service'),
            path('contact/',views.contact,name='contact'),
     
]
