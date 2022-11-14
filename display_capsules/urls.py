from display_capsules import views
from django.urls import path, include, re_path

#from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^capsule$',views.get_capsules)
    #url(r'^department/([0-9]+)$',views.departmentApi),
   ] 

