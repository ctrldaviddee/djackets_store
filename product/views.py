from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

# tell django what you're going to put in or get from the model
from .models import Product
from .serializers import ProductSerializer

class LatestProductList(APIView):
    def get(self, request, format=None):
        """
        Handle GET request to retrieve all products.

        Retrieves all products and returns their serialized representation.

        Args:
            request (Request): The incoming request object.
            format (str, optional): The format of the response. Defaults to None.

        Returns:
            Response: The serialized list of product data.
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)

class ProductDetail(APIView):
    """
    Retrieve a product by its category slug and product slug.

    Handles GET requests to retrieve a specific product based on its category and slug.
    """
    def get_object(self, category_slug, product_slug):
        """
        Retrieve a product instance.

        Attempts to fetch a product matching the given category slug and product slug.
        Raises Http404 if no matching product is found.

        Args:
            category_slug (str): The slug of the product's category.
            product_slug (str): The slug of the product.

        Returns:
            Product: The retrieved product instance.

        Raises:
            Http404: If no product matches the given slugs.
        """
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, category_slug, product_slug, format=None):
        """
        Handle GET request to retrieve a product.

        Retrieves a specific product and returns its serialized representation.

        Args:
            request (Request): The incoming request object.
            category_slug (str): The slug of the product's category.
            product_slug (str): The slug of the product.
            format (str, optional): The format of the response. Defaults to None.

        Returns:
            Response: The serialized product data.
        """
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)