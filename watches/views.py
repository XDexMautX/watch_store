from django.http import JsonResponse
from django.shortcuts import render
from .models import Watch

def index(request):
    watches = Watch.objects.all()
    return render(request, 'index.html', {'watches': watches})

def get_watch_details(request, id):
    try:
        watch = Watch.objects.get(id=id)
        watch_data = {
            'id': watch.id,
            'name': watch.name,
            'price': watch.price,
            'description': watch.description,
            'image': watch.image.url,
        }
        return JsonResponse(watch_data)
    except Watch.DoesNotExist:
        return JsonResponse({'error': 'Watch not found'}, status=404)
