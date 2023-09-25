from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoicesViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_invoices(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        Invoice.objects.create(**invoice_data)

        url = reverse("Invoice-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_create_invoice(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        url = reverse("Invoice-list")
        response = self.client.post(url, invoice_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)  

    def test_retrieve_invoice(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        url = reverse("Invoice-detail", kwargs={"pk": invoice.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer_name"], invoice_data["customer_name"])

    def test_update_invoice(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        updated_data = {"customer_name": "Jane Doe"}
        url = reverse("Invoice-detail", kwargs={"pk": invoice.id})
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        invoice.refresh_from_db()
        self.assertEqual(invoice.customer_name, updated_data["customer_name"])

    def test_delete_invoice(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        url = reverse("Invoice-detail", kwargs={"pk": invoice.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)  

class InvoiceDetailsViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_invoice_details(self):
        # Create some test data
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        invoice_detail_data = {
            "invoice": invoice,
            "description": "Product 1",
            "quantity": 5,
            "unit_price": 10.0,
            "price": 50.0,
        }
        InvoiceDetail.objects.create(**invoice_detail_data)

        url = reverse("InvoiceDetails-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if one invoice detail is returned

    def test_create_invoice_detail(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        invoice_detail_data = {
            "invoice": invoice.id,
            "description": "Product 1",
            "quantity": 5,
            "unit_price": 10.0,
            "price": 50.0,
        }
        url = reverse("InvoiceDetails-list")
        response = self.client.post(url, invoice_detail_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 1)  # Check if a new invoice detail is created

    def test_retrieve_invoice_detail(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        invoice_detail_data = {
            "invoice": invoice,
            "description": "Product 1",
            "quantity": 5,
            "unit_price": 10.0,
            "price": 50.0,
        }
        invoice_detail = InvoiceDetail.objects.create(**invoice_detail_data)

        url = reverse("InvoiceDetails-detail", kwargs={"pk": invoice_detail.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], invoice_detail_data["description"])

    def test_update_invoice_detail(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        invoice_detail_data = {
            "invoice": invoice,
            "description": "Product 1",
            "quantity": 5,
            "unit_price": 10.0,
            "price": 50.0,
        }
        invoice_detail = InvoiceDetail.objects.create(**invoice_detail_data)

        updated_data = {"description": "Updated Product"}
        url = reverse("InvoiceDetails-detail", kwargs={"pk": invoice_detail.id})
        response = self.client.put(url, updated_data, format="json")
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        invoice_detail.refresh_from_db()
        self.assertNotEqual(invoice_detail.description, updated_data["description"])

    def test_delete_invoice_detail(self):
        invoice_data = {
            "customer_name": "John Doe",
        }
        invoice = Invoice.objects.create(**invoice_data)

        invoice_detail_data = {
            "invoice": invoice,
            "description": "Product 1",
            "quantity": 5,
            "unit_price": 10.0,
            "price": 50.0,
        }
        invoice_detail = InvoiceDetail.objects.create(**invoice_detail_data)

        url = reverse("InvoiceDetails-detail", kwargs={"pk": invoice_detail.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InvoiceDetail.objects.count(), 0)  # Check if the invoice detail is deleted
