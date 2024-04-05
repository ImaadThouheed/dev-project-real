from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Map to view that renders index.html
    # path('signup',views.signup,name='signup'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='signup'), name='logout'),
  path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('book-guard/<int:guard_id>/', views.book_guard, name='book_guard'),
    path('accounts/', include('django.contrib.auth.urls'))
]