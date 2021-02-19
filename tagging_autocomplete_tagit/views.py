from tagging.models import Tag
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError

def list_tags(request):
	try:
	    tags = Tag.objects.filter(name__istartswith=request.GET['term']).values_list('name', flat=True)
	except MultiValueDictKeyError:
		tags = []

	return JsonResponse([x.encode('utf-8') for x in tags], safe=False)
