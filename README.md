# clearsale-python

### Steps to validate a transaction:

```python
from clearsale.api import ClearSaleConnector, ClearSaleService
from clearsale.entities.billing_data import BillingData
from clearsale.entities.common import Address, FingerPrint, Phone
from clearsale.entities.item import Item
from clearsale.entities.order import Order, Orders
from clearsale.entities.payment import Payment
from clearsale.entities.shipping_data import ShippingData

# Create a finger print:
finger_print = FingerPrint("session-0123456789")

# Create an address:
address = Address(
    Street="Rua José de Oliveira Coutinho",
    Number="151",
    County="Barra Funda",
    City="São Paulo",
    State="SP",
    Country="Brasil",
    ZipCode="01144020",
)

# Create a phone:
phone = Phone(Type=1, DDD=16, Number=992771330)

# Create billing:
billing = BillingData(
    ID=1,
    Type=1,
    LegalDocument1="12425366872",
    Name="Neil Armstrong",
    BirthDate="1984-03-12T00:00:00",
    Address=address
)

# Add billing phone:
billing.add_phone(phone)

# Create shipping:
shipping = ShippingData(
    ID=1,
    Type=1,
    LegalDocument1="12425366872",
    Name="Mateus Padua",
    Address=address
)

# Add shipping phone
shipping.add_phone(phone)

# Create order items:
item_a = Item(ID=2, Name="Adaptador USB", ItemValue=2, Qty=3)
item_b = Item(ID=3, Name="Impressora", ItemValue=5, Qty=2)

# Create order:
order = Order(
    ID="TEST-1969",
    FingerPrint=finger_print,
    Date="2016-10-20T12:15:07",
    Email="neil@armstrong.com",
    TotalItems=2,
    TotalOrder=100.0,
    QtyInstallments=2,
    IP="127.0.0.1",
    BillingData=billing,
    ShippingData=shipping,
)

# Add order items:
order.add_item(item_a)
order.add_item(item_b)

# Create payment:
payment = Payment(Date="2016-04-13T23:39:07", Amount=17.5, PaymentTypeID=2)

# Add order payment:
order.add_payment(payment)

# Create orders to send:
orders = Orders()
orders.add_order(order)

# ClearSale service verification:
clearsale_connector = ClearSaleConnector("10072C6C-9DC1-4595-A95D-DB03415DE200", True)
clearsale_service = ClearSaleService(clearsale_connector)
request = clearsale_service.send_orders(orders)
request.get_dict()

status = clearsale_service.get_order_status("TEST-20")
```
