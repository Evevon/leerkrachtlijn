from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""

    category_key = "{}-{}".format(arg.super_category.number, arg.number)
    category_mapping = {
        '1-1' : 'a',
        '1-2' : 'b',
        '1-3' : 'c',
        '2-1' : 'd',
        '2-2' : 'e',
        '2-3' : 'f',
        '2-4' : 'g',
    }

    try:
        fieldname = 'cat_{}_note'.format(category_mapping[category_key])
    except:
        return "category number out of bounds"
    try :
        return value[fieldname]
    except:
        return "INVALID"

register.filter('getattribute', getattribute)
