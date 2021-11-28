from django import template
register = template.Library()

class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

@register.tag (name = 'set')
def setvar(value,new):
    value = new
    return SetVarNode(value, new)

@register.filter
def flip_var(value):
    if(value == 'true'):
        value = 'false'
    else:
        value = 'true'
    return value