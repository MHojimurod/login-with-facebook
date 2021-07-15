from django.urls import include, path
from . import views
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path('social-auth/', include('social_django.urls', namespace='social'))

]