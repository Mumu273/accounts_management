from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from transaction.models import Transaction


def login_view(request):
    """User login view that serves as the home page."""
    # If user is already authenticated, redirect to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if not request.POST.get("remember"):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(60 * 60 * 24 * 30)
            messages.success(request, f'Welcome , {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'auth/login.html')


@login_required
def dashboard(request):
    username = request.user.username
    earnings = Transaction.objects.filter(category__is_expense=False).aggregate(total=Sum('amount'))['total'] or 0
    expense = Transaction.objects.filter(category__is_expense=True).aggregate(total=Sum('amount'))['total'] or 0
    balance = earnings - expense

    context = {'username': username,
               'earnings': earnings,
               'expenses': expense,
               'balance': balance
               }
    return render(request, 'dashboard/index.html', context=context)

@login_required
def logout_view(request):
    """
    Custom logout view that logs out the user and redirects to the login page.
    """
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('/')
