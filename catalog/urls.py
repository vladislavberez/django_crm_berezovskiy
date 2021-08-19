from django.urls import path
from .views import CompanyListView, CompanyDetailView, UserDetailView, ProjectListView, \
    ProjectDetailView, CompanyUpdate, CompanyCreate, ProjectUpdate, ProjectCreate, \
    ConnectionListView, ConnectionDetailView, ConnectionCreate, ConnectionUpdate, UserUpdate

urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('create/', CompanyCreate.as_view(), name='company-create'),
    path('<int:pk>/update/', CompanyUpdate.as_view(), name='company-update'),
    path('project/', ProjectListView.as_view(), name='project-list'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('connection/', ConnectionListView.as_view(), name='connect-list'),
    path('connection/create/', ConnectionCreate.as_view(), name='connect-create'),
    path('connection/<int:pk>/', ConnectionDetailView.as_view(), name='connect-detail'),
    path('connection/<int:pk>/update/', ConnectionUpdate.as_view(), name='connect-update'),
    path('employee/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('employee/<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
]