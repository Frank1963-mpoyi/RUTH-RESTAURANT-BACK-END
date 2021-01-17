from    django.shortcuts    import      render
from    .models             import      Restaurant




def home (request):
    template_name   = 'blog/home.html'
    items         =  Restaurant.objects.all()
    context =  { 'items' : items }
    
    return render(request, template_name, context)
