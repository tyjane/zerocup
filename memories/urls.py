from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.sign_in_and_personal_page, name='sign_in'),
    url(r'^stories/', views.stories, name='stories'),
    url(r'^post_story/', views.post_story, name='post_story'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
]
