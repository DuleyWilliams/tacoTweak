""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from models import MenuItem

class MenuItemView(ViewSet):
    """ Menu Items Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a menu item"""
        menu_items = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(menu_items)
        return Response(serializer.data)
    
    def list(self, request):
        """ Handle a GET request for all menu items"""
        pass
    
    class MenuItemSerializer()
    