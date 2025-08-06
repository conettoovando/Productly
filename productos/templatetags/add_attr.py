from django import template
register = template.Library()

@register.filter(name='add_attr')
def add_attr(field, css):
    """
    Add an attribute to a form field.
    """
    attrs = {}
    clase, valor = css.split(':')
    attrs[clase] = valor
    return field.as_widget(attrs=attrs)
