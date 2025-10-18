from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm
from external.exclude_list import exclude_list

@login_required
def category_list(request):
    is_expense = request.GET.get('is_expense')
    categories = Category.objects.all()
    if is_expense == 'True':
        categories = categories.filter(is_expense=True)
    else:
        categories = categories.filter(is_expense=False)
    form = CategoryForm()
    context = {
        'is_expense': is_expense,
        'categories': categories,
        'form': form
    }
    return render(request, 'category/category_list.html', context=context)


@login_required
def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    data = {}
    for field in category._meta.get_fields():
        if field.concrete and not field.many_to_many and not field.auto_created:
            if field.name not in exclude_list and field.name != 'is_expense':
                data[field.verbose_name] = getattr(category, field.name)
    return JsonResponse(data)

@login_required
def add_new_category(request, is_expense):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            html = render(request, "partials/category_form.html", {"form": form}).content.decode("utf-8")
            return JsonResponse({"success": False, "form_html": html})
    else:
        form = CategoryForm(initial={"is_expense": is_expense})
        return render(request, "add_modal.html", {"form": form})
