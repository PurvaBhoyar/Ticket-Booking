from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from booking.models import Show, Booking

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class AdminDashboardView(AdminRequiredMixin, View):
    def get(self, request):
        shows = Show.objects.all().order_by('-date')
        bookings = Booking.objects.all().order_by('-booking_date')
        return render(request, 'admin_panel/dashboard.html', {
            'shows': shows,
            'bookings': bookings
        })

class AddShowView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'admin_panel/add_show.html')
    
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        duration = request.POST.get('duration')
        venue = request.POST.get('venue')
        total_seats = request.POST.get('total_seats')
        price_per_seat = request.POST.get('price_per_seat')
        
      
        errors = {}
        if not title:
            errors['title'] = 'Title is required'
        if not date:
            errors['date'] = 'Date is required'
        if not total_seats:
            errors['total_seats'] = 'Total seats is required'
        else:
            try:
                total_seats = int(total_seats)
                if total_seats <= 0:
                    errors['total_seats'] = 'Total seats must be positive'
            except ValueError:
                errors['total_seats'] = 'Invalid number of seats'
        if not price_per_seat:
            errors['price_per_seat'] = 'Price per seat is required'
        else:
            try:
                price_per_seat = float(price_per_seat)
                if price_per_seat <= 0:
                    errors['price_per_seat'] = 'Price must be positive'
            except ValueError:
                errors['price_per_seat'] = 'Invalid price'
        
        if errors:
            return render(request, 'admin_panel/add_show.html', {'errors': errors, 'data': request.POST})
        
        
        show = Show.objects.create(
            title=title,
            description=description,
            date=date,
            duration=duration,
            venue=venue,
            total_seats=total_seats,
            price_per_seat=price_per_seat
        )
        
        messages.success(request, f'Show "{show.title}" added successfully')
        return redirect('admin_dashboard')

class EditShowView(AdminRequiredMixin, View):
    def get(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        return render(request, 'admin_panel/edit_show.html', {'show': show})
    
    def post(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        
        show.title = request.POST.get('title', show.title)
        show.description = request.POST.get('description', show.description)
        show.date = request.POST.get('date', show.date)
        show.duration = request.POST.get('duration', show.duration)
        show.venue = request.POST.get('venue', show.venue)
        
    
        errors = {}
        total_seats = request.POST.get('total_seats', show.total_seats)
        price_per_seat = request.POST.get('price_per_seat', show.price_per_seat)
        
        try:
            show.total_seats = int(total_seats)
            if show.total_seats <= 0:
                errors['total_seats'] = 'Total seats must be positive'
        except ValueError:
            errors['total_seats'] = 'Invalid number of seats'
        
        try:
            show.price_per_seat = float(price_per_seat)
            if show.price_per_seat <= 0:
                errors['price_per_seat'] = 'Price must be positive'
        except ValueError:
            errors['price_per_seat'] = 'Invalid price'
        
        if errors:
            return render(request, 'admin_panel/edit_show.html', {'show': show, 'errors': errors})
        
        show.save()
        messages.success(request, f'Show "{show.title}" updated successfully')
        return redirect('admin_dashboard')

class DeleteShowView(AdminRequiredMixin, View):
    def post(self, request, pk):
        show = get_object_or_404(Show, pk=pk)
        title = show.title
        show.delete()
        messages.success(request, f'Show "{title}" deleted successfully')
        return redirect('admin_dashboard')
