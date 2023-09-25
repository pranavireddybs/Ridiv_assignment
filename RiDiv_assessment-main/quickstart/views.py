from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer

class Invoices(viewsets.ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer

class InvoiceDetails(viewsets.ModelViewSet):
    queryset=InvoiceDetail.objects.all()
    serializer_class=InvoiceDetailSerializer
