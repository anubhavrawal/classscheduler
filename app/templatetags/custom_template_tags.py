from django import template
register = template.Library()


@register.simple_tag
def flipvar(old, new):
    old = new
    return old
