from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ExpenseCategory
from .forms import ExpenseCategoryForm
from external.exclude_list import exclude_list

@login_required
def expense_category_list(request):
    qs = ExpenseCategory.objects.all()
    form = ExpenseCategoryForm()
    context = {
        'expense_categories': qs,
        'form': form
    }
    return render(request, 'expense_category/expense_category_list.html', context=context)


@login_required
def expense_category_view(request, category_id):
    category = get_object_or_404(ExpenseCategory, id=category_id)
    data = {}
    for field in category._meta.get_fields():
        if field.concrete and not field.many_to_many and not field.auto_created:
            if field.name not in exclude_list:
                data[field.verbose_name] = getattr(category, field.name)
    return JsonResponse(data)