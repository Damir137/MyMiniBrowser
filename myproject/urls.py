
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from accounts.views import ProtectedView
from accounts import views
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('logined/', ProtectedView.as_view(), name='protected_class'),
    path('', views.home),
    path('allgames/', views.allgames),
    path('calculator/', views.calc),
    path('timer/', views.timer),
    path('typing/', views.typing),
    path('flappybird/', views.flappybird),
    path('pong/', views.pong),
    path('rpc/', views.rpc),
    path('tictaktoe/', views.tictaktoe),
    path('notes/', views.note),
    path('snake/', views.snake),

]
   