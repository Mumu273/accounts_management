from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExpenseCategory
from .forms import ExpenseCategoryForm

@login_required
def expense_category_list(request):
    qs = ExpenseCategory.objects.all()
    form = ExpenseCategoryForm()
    context = {
        'expense_categories': qs,
        'form': form
    }
    return render(request, 'expense_category/expense_category_list.html', context=context)
