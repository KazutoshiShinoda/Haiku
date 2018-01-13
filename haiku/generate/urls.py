from django.conf.urls import url
from generate import views


urlpatterns = [
    url(r'^haiku/list$', views.generation_list),
]
