from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import GuardReal
# Import the logging module
import logging

from .forms import BookingRealForm
# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
       # Log a message
    logger.debug("jrllpe") 
    guards = GuardReal.objects.all()
        # Log a message
    logger.debug(guards)

    return render(request, 'index.html', {'guards': guards}) 
def book_guard(request, guard_id):
    if request.method == 'POST':
        form = BookingRealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success URL
    else:
        form = BookingRealForm(initial={'guard': guard_id})
    return render(request, 'book_booking.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
