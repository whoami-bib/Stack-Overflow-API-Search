# searchapp/views.py

import requests
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.decorators import api_view
from ratelimit import limits
from datetime import timedelta



PER_MINUTES = 60
ONE_DAY = timedelta(days=1).total_seconds()
@api_view(['GET'])
@limits(calls=5, period=PER_MINUTES)
@limits(calls=100, period=ONE_DAY)
def search(request):
    # Get the search query and page number from the request parameters
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))

    # Check if the data is already cached
    cache_key = f'stackoverflow_search_{query}_{page}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data)

    # Check search limit per session
    search_count = cache.get(f'search_count_{request.session.session_key}', 0)
    if search_count >= 100:
        return JsonResponse({'error': 'Daily search limit exceeded.'}, status=429)
    if search_count >= 5:
        return JsonResponse({'error': 'Search limit per session exceeded.'}, status=429)

    # Make the API call
    api_url = 'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'site': 'stackoverflow',
        'key': settings.STACKOVERFLOW_API_KEY,
        'q': query,
        'page': page
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    # Save the data to cache
    cache.set(cache_key, data, 60 * 60 * 24)  # Cache for 24 hours

    # Increment search count per session
    cache.incr(f'search_count_{request.session.session_key}')

    return JsonResponse(data)

