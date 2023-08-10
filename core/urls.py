from django.urls import path
from .views import AuthorViewSet, BookViewSet, ReaderViewSet

urlpatterns = [
    path('authors/', AuthorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='author-list'),
    path('authors/<int:pk>/', AuthorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='author-detail'),
    path('books/', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='book-list'),
    path('books/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='book-detail'),
    path('readers/', ReaderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='reader-list'),
    path('readers/<int:pk>/', ReaderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='reader-detail'),
]
