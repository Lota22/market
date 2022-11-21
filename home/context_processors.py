from store.models import Cart

def cartcount(request):
    reading = Cart.objects.filter(user__username = request.user.username , paid = False)

    cartcount = 0
    for items in reading:
        cartcount += items.quantity

    context ={
        'cartcount':cartcount
    } 

    return context   