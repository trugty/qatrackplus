from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()


@register.filter
def as_qavalue(form, include_admin):
    template = get_template("qavalue_form.html")
    c = Context({"form": form,"include_admin":include_admin})
    return template.render(c)
