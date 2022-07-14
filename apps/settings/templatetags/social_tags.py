from django import template
from ..models import Setting

register = template.Library()


@register.simple_tag
def facebook_url():
    return Setting.objects.get(pk=1).facebook


@register.simple_tag
def instagram_url():
    return Setting.objects.get(pk=1).instagram


@register.simple_tag
def twitter_url():
    return Setting.objects.get(pk=1).twitter


@register.simple_tag
def title_meta():
    return Setting.objects.get(pk=1).title


@register.simple_tag
def description_meta():
    return Setting.objects.get(pk=1).description


@register.simple_tag
def keywords_meta():
    return Setting.objects.get(pk=1).keywords
