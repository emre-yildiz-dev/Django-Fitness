from django.views.generic import ListView, DetailView
from .models import Image, Service, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


class ClassesPageView(ListView):
    model = Service
    context_object_name = 'service_list'
    template_name = 'classes.html'


class ClassDetailPageView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'class-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClassDetailPageView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(
            status='True')
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(ClassDetailPageView, self).get_context_data(**kwargs)
    #     context['image_list'] = Image.objects.all()
    #     return context


class PricingPageView(ListView):
    model = Service
    context_object_name = 'service'
    template_name = 'pricing.html'


def comment_post(request):
    if request.method == "POST":
        message = Comment()
        message.name = request.POST.get('name')
        message.comment = request.POST.get('message')
        message.email = request.POST.get('email')
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            message.ipaddress = x_forw_for.split(',')[0]
        else:
            message.ipaddress = request.META.get('REMOTE_ADDR')

        message.service = Service.objects.get(
            pk=int(request.POST.get('service')))

        service = message.service
        if(request.user.is_authenticated):
            message.user = request.user
        print(request.POST)
        message.save()
        return HttpResponseRedirect("/classes/{id}/".format(id=service.id))

    return render(request, "comment-post")


class SearchResultsListView(ListView):
    model = Service
    context_object_name = 'service_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Service.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(keywords__icontains=query))
