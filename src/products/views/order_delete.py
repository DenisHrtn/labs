from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render, redirect
from products.models import Order


@staff_member_required
def all_orders_view(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'products/all_orders.html', {'orders': orders})


@staff_member_required()
def delete_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('all_orders')

    return render(request, 'products/confirm_delete_order.html', {'order': order})

