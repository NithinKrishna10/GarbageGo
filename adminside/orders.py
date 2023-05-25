from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from orders.models import Order



#  customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     waste_type = models.ForeignKey(WasteCategory,on_delete=models.CASCADE)
#     address = models.ForeignKey(Address,on_delete=models.CASCADE)
#     pickup_date = models.DateField()
#     additional_notes = models.TextField(blank=True)
#     is_ordered = models.BooleanField(default=False)
#     waste_weight = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Booked')
#     def __str__(self):
#         return f"Order #{self.pk} - {self.customer.name}"

class OrderListAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:

            order = self.get_object(pk)
            print(order,"before")
            print(request.data['additional_notes'])
            order.price = request.data['price']
            order.status =request.data['status']
            order.waste_weight=request.data['waste_weight']
            order.save()
            print(order,"after")
            if 1<9:
                return Response("aa yeah")
            serializer = OrderSerializer(data=order)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

