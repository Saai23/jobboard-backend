from django.urls import path
from .views import JobListingCreateView, JobListingListView, JobListingDetailView, ApplicationCreateView, ApplicationListView, ApplicationDetailView

urlpatterns = [
    path('jobs/', JobListingListView.as_view(), name='job-list'),
    path('jobs/create/', JobListingCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/', JobListingDetailView.as_view(), name='job-detail'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/create/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
]
