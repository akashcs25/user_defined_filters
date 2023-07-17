from django import template
register=template.Library()


@register.filter()
def swap(data):
    return data.swapcase()

# register.filter('swap',swap)
@register.filter
def replace(data):
    x=data.split()
    a,b=x.pop(0),x.pop(-1)
    c=' '.join(x).upper()
    return(a+' '+c+' '+b)

@register.filter
def trim(data,x):
    c=0
    for i in range(len(data)):
        if(data[i:i+len(x)]==x):
            c+=1
    return c


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

