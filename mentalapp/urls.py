# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views

# urlpatterns = format_suffix_patterns([
# path('', views.api_root),
# path('users/', views.UserList.as_view(),name='user-list' ),
# path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# path('profiles/', views.ProfileList.as_view(), name='profile-list'),
# path('profiles/<int:pk>/',views.ProfileDetail.as_view()),
# path('professionals/', views.ProfessionalList.as_view()),
# path('professionals/<int:pk>/', views.ProfessionalDetail.as_view()),
# path('resources/', views.ResourceList.as_view()),
# path('resources/<int:pk>/',views.ResourceDetail.as_view()),
# path('posts/', views.PostList.as_view()),
# path('posts/<int:pk>/', views.PostDetail.as_view()),
# path('comments/', views.CommentList.as_view()),
# path('comments/<int:pk>/',views.CommentDetail.as_view()),
# path('appointments/', views.AppointmentList.as_view()),
# path('appointments/<int:pk>/', views.AppointmentDetail.as_view()),
# path('availability/', views.AvailabilityList.as_view()),
# path('availability/<int:pk>/', views.AvailabilityDetail.as_view()),
# ])

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about", views.AboutPageView.as_view(), name="about"),
    path("resources/", views.ResourcesListView.as_view(), name="resources"),
    path('resources/add/', views.ResourceCreateView.as_view(), name='add-resource'),
    path("professionals/", views.ProfessionalsListView.as_view(), name="professionals"),
    path('professional/<pk>/', views.ProfessionalDetailView.as_view(), name="professional_details"),
    path('dashboard/<pk>', views.UserDashboardView.as_view(), name='dashboard'),
    path('professional-dashboard/<pk>', views.ProfessionalDashboardView.as_view(), name='professional-dashboard'),
    path('appointments/create/', views.AppointmentView.as_view(), name='create_appointment'),
    path('community', views.PostListView.as_view(), name='community'),
    path('post/new/', views.create_post, name='post_create'),
    path('approve-appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
]