from django.shortcuts import render, get_object_or_404, redirect
from .models import MobilePhone, Brand
from .forms import MobilePhoneForm, BrandForm

# ── Phone Views ─────────────────────────────────────────────────────────────

def phone_list(request):
    """List all phones with optional search/filter."""
    phones = MobilePhone.objects.select_related('brand').all()
    query = request.GET.get('q', '')
    brand_filter = request.GET.get('brand', '')

    if query:
        phones = phones.filter(model_name__icontains=query)
    if brand_filter:
        phones = phones.filter(brand__id=brand_filter)

    brands = Brand.objects.all()
    return render(request, 'phones/phone_list.html', {
        'phones': phones,
        'brands': brands,
        'query': query,
        'brand_filter': brand_filter,
    })


def phone_detail(request, pk):
    """Detail page for a single phone."""
    phone = get_object_or_404(MobilePhone, pk=pk)
    return render(request, 'phones/phone_detail.html', {'phone': phone})


def phone_add(request):
    """Add a new phone."""
    form = MobilePhoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('phone_list')
    return render(request, 'phones/phone_form.html', {'form': form, 'title': 'Add Phone'})


def phone_edit(request, pk):
    """Edit an existing phone."""
    phone = get_object_or_404(MobilePhone, pk=pk)
    form = MobilePhoneForm(request.POST or None, instance=phone)
    if form.is_valid():
        form.save()
        return redirect('phone_detail', pk=pk)
    return render(request, 'phones/phone_form.html', {'form': form, 'title': 'Edit Phone'})


def phone_delete(request, pk):
    """Delete a phone (POST confirmation)."""
    phone = get_object_or_404(MobilePhone, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'phones/phone_confirm_delete.html', {'phone': phone})


# ── Brand Views ──────────────────────────────────────────────────────────────

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'phones/brand_list.html', {'brands': brands})


def brand_add(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('brand_list')
    return render(request, 'phones/brand_form.html', {'form': form, 'title': 'Add Brand'})
