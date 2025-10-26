from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

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
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    transaction = Transaction.objects.all()
    today = timezone.now().date()

    # If no filter is applied, default to current month
    if not start_date and not end_date:
        first_day_of_month = today.replace(day=1)
        transaction = transaction.filter(date__gte=first_day_of_month, date__lte=today)
    else:
        if start_date:
            transaction = transaction.filter(date__gte=start_date)
        if end_date:
            transaction = transaction.filter(date__lte=end_date)
    earnings = transaction.filter(category__is_expense=False).aggregate(total=Sum('amount'))['total'] or 0
    expense = transaction.filter(category__is_expense=True).aggregate(total=Sum('amount'))['total'] or 0
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
