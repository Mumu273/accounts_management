

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
    form = CategoryForm(instance=category)
    return render(request, 'view_modal.html', {"form":form})

@login_required
def add_new_category(request, is_expense):
    if request.method == "POST":
        request_data = request.POST.copy()
        request_data['is_expense'] = is_expense == "True"
        form = CategoryForm(request_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            html = render(request, "partials/category_form.html", {"form": form}).content.decode("utf-8")
            return JsonResponse({"success": False, "form_html": html})
    else:
        form = CategoryForm(initial={"is_expense": is_expense})
        return render(request, "add_form.html", {"form": form})


@login_required
def category_edit(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if request.method == "POST":
        request_data = request.POST.copy()
        request_data['is_expense'] = category.is_expense
        form = CategoryForm(request_data, instance=category)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            html = render(request, "partials/category_form.html", {"form": form}).content.decode("utf-8")
            return JsonResponse({"success": False, "form_html": html})
    else:
        form = CategoryForm(instance=category)
        return render(request, "edit_form.html", {"form": form})


@login_required
def category_delete(request, category_id):
    url = reverse('category_list')
    category = Category.objects.filter(id=category_id).first()
    is_expense = category.is_expense
    category.delete()
    return redirect(f"{url}?is_expense={is_expense}")