from django.urls import path
from . import views
#path("", views.index)
#path("blog", views.IndexList.as_view()),
urlpatterns = [
     path("", views.BlogListView.as_view(), name="home"),
     path("blog/", views.BlogListView.as_view(), name="blogs"),
     path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog"),
]