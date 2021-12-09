from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('details/',views.details,name='details'),
    path('info/<int:myid>',views.info,name='info'),
]

urlpatterns += staticfiles_urlpatterns()