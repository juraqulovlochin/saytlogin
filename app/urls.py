from django.urls import path
from .views import PostView,DetalView,CretView,UpdatView,DeletView

urlpatterns=[
    path('post/<int:pk>/del',DeletView.as_view(),name='delet'),
    path('post/<int:pk>/edit',UpdatView.as_view(),name='updat'),
    path('post/new',CretView.as_view(),name='cret'),
    path('',PostView.as_view(),name='home'),
    path('post/<int:pk>/',DetalView.as_view(),name='detal')
]