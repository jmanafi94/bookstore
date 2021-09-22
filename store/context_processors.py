from .models import Genre


def categories(request):
    return {
        'categories': Genre.objects.all()
    }
