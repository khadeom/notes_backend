"""
URL configuration for notes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from notes.views import SignUpView, LoginView, NoteListView, NoteDetailView, CreateNoteView, UpdateNoteView, DeleteNoteView, ShareNoteView, SearchNotesView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth View
    path('api/auth/signup/', SignUpView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    
    # Notes View
    path('api/notes/', NoteListView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('api/notes/share/<int:pk>/', ShareNoteView.as_view(), name='note-share'),
    path('api/search/', SearchNotesView.as_view(), name='note-search'),
]


