from .import views
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls.conf import  path,include
router = DefaultRouter()
router.register(r"Invoiceapi", views.Invoices, basename="Invoice")
router.register(r"Invoicedetailsapi", views.InvoiceDetails, basename="InvoiceDetails")
urlpatterns = [
    path('', include(router.urls))
]