from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Show, Booking
from django.utils import timezone
from datetime import timedelta

class HomeView(ListView):
    model = Show
    template_name = 'booking/home.html'
    context_object_name = 'shows'
    ordering = ['-date']

class ShowDetailView(DetailView):
    model = Show
    template_name = 'booking/show_detail.html'
    context_object_name = 'show'

class BookShowView(LoginRequiredMixin, View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        return render(request, 'booking/book_show.html', {'show': show})
    
    def post(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        seats = request.POST.get('seats')
        
       
        errors = {}
        if not seats:
            errors['seats'] = 'Number of seats is required'
        else:
            try:
                seats = int(seats)
                if seats <= 0:
                    errors['seats'] = 'Number of seats must be positive'
                elif seats > show.total_seats:
                    errors['seats'] = f'Only {show.total_seats} seats available'
            except ValueError:
                errors['seats'] = 'Invalid number of seats'
        
        if errors:
            return render(request, 'booking/book_show.html', {'show': show, 'errors': errors})
        
        
        total_price = seats * show.price_per_seat
        booking = Booking.objects.create(
            user=request.user,
            show=show,
            seats=seats,
            total_price=total_price,
            is_confirmed=True
        )
        
    
        show.total_seats -= seats
        show.save()
        
        messages.success(request, f'Successfully booked {seats} seats for {show.title}')
        return redirect('booking_history')

class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_history.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date')
    
class AddShowView(View):
    def get(self, request):  
        return render(request, 'booking/add_show.html')
    
    def post(self, request): 
        try:
            hours, minutes = map(int, request.POST['duration'].split(':'))
            Show.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                date=timezone.now(),
                duration=timedelta(hours=hours, minutes=minutes),
                venue=request.POST['venue'],
                total_seats=int(request.POST['seats']),
                price_per_seat=float(request.POST['price'])
            )
            return redirect('home')
        except ValueError:
            return render(request, 'booking/add_show.html', {'error': 'Invalid duration format'})
