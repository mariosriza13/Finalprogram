from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Like
from django.shortcuts import HttpResponse
import json
from catalog.models import Item
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


@login_required
def like_item(request, item_id):
    if request.method == 'POST':
        try:
            
            item = Item.objects.get(pk=item_id)
            # Check if the user has already liked the item
            if Like.objects.filter(user=request.user, item=item).exists():
                return JsonResponse({'success': False, 'message': 'You have already liked this item'})
            # Create a new like
            Like.objects.create(user=request.user, item=item)
            return JsonResponse({'success': True, 'message': 'Item liked successfully'})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
def unlike_item(request, item_id):
    if request.method == 'POST':
        try:
            #get the like and delete it
            like = Like.objects.get(user=request.user, item_id=item_id)
            like.delete()
            return JsonResponse({'success': True, 'message': 'Item unliked successfully'})
        except Like.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'You have not liked this item'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})