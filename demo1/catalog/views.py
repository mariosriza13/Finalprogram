
from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Item
from .forms import ItemSearchForm


def catalog(request):
    # Retrieve all categories
    categories = Category.objects.all()
    return render(request, 'catalog/catalog.html', {'categories': categories})

def category_detail(request, category_id):
    # Retrieve the category object
    category = get_object_or_404(Category, pk=category_id)
    # Retrieve subcategories related to the category
    subcategories = category.subcategory_set.all()
    return render(request, 'catalog/category_detail.html', {'category': category, 'subcategories': subcategories})


def subcategory_detail(request, subcategory_id):
    # Retrieve the subcategory object
    subcategory = get_object_or_404(SubCategory, pk=subcategory_id)
    # Retrieve items related to the subcategory
    items = Item.objects.filter(sub_category=subcategory)

    
    for item in items:
        item.likes_count = item.like_count()  # Get the number of likes for each item

    
    # Pass them to the template for rendering
    return render(request, 'catalog/subcategory_detail.html', {'catalog/subcategory': subcategory, 'items': items})
    # Fetch the user's rating for each item
    



def items_search(request):
    # Create a form instance with the data from the request
    form = ItemSearchForm(request.GET)
     # Get all items from the database
    items = Item.objects.all()

    if form.is_valid():
        # Get the search query from the form data
        query = form.cleaned_data.get('query')
        # If there is a search query, filter the items by name or description
        if query:
            items = items.filter(name__icontains=query) | items.filter(description__icontains=query)
    # Render the search page with the form and the filtered items
    return render(request, 'catalog/search.html', {'form': form, 'items': items})