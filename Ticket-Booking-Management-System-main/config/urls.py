from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView, LoginView, LogoutView
from booking.views import HomeView, ShowDetailView, BookShowView, BookingHistoryView
from admin_panel.views import (AdminDashboardView, AddShowView, 
                              EditShowView, DeleteShowView)
from booking.views import AddShowView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
 
    path('shows/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),
    path('shows/<int:pk>/book/', BookShowView.as_view(), name='book_show'),
    path('bookings/', BookingHistoryView.as_view(), name='booking_history'),

    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/shows/add/', AddShowView.as_view(), name='add_show'),
    path('admin/shows/<int:pk>/edit/', EditShowView.as_view(), name='edit_show'),
    path('admin/shows/<int:pk>/delete/', DeleteShowView.as_view(), name='delete_show'),
     path('admin/shows/add/', AddShowView.as_view(), name='add_show'),
]
