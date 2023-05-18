from django.contrib import admin
from django.urls import path, include
from myapp.views import HomePageView, FormView, MessagesView, register_view, login_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(HomePageView.as_view()), name='home'),
    path('form/', login_required(FormView.as_view()), name='form'),
    path('messages/', login_required(MessagesView.as_view()), name='messages'),
    path('register/', register_view, name='register'),
]
