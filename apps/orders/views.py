from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from apps.orders.models import Order
from apps.services.models import Image, Service
from apps.services.views import ClassesPageView
from dateutil.relativedelta import relativedelta
from django.views.generic import ListView


class ServiceOrderView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'order-post.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceOrderView, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        return context


class UserOrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'user-orders.html'


def get_user_orders(request):
    order_list = Order.objects.filter(user_id=request.user.id)
    context = {
        'order_list': order_list
    }
    return render(request, 'user-orders.html', context)


@login_required
def order_post(request):
    if request.method == 'POST':
        order = Order()
        order.user = request.user
        order.service = Service.objects.get(id=request.POST.get('service_id'))
        order.months = int(request.POST.get('monthly'))
        order.total = request.POST.get('price')
        order.price = request.POST.get('price')
        order.StartDate = datetime.today()
        order.EndDate = datetime.today() + relativedelta(months=int(request.POST.get('monthly')))
        order.payment = 'Cash'

        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            order.ipaddress = x_forw_for.split(',')[0]
        else:
            order.ipaddress = request.META.get('REMOTE_ADDR')
        order.save()
        # return render(request, "classes.html")
        return HttpResponseRedirect('/classes/')

    return render(request, "order-post.html")
