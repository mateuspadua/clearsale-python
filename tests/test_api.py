from unittest import TestCase
from unittest.mock import patch

from clearsale.api import ClearSaleConnector, ClearSaleService
from . import OrderMock


class ClearSaleConnectorTestCase(TestCase):
    def setUp(self):
        self.entity_code = "neil"
        self.connector = ClearSaleConnector(
            entity_code=self.entity_code, use_sandbox=True
        )
        self.homolog_url = (
            "https://homologacao.clearsale.com.br/integracaov2/service.asmx?wsdl"
        )
        self.production_url = (
            "https://homologacao.clearsale.com.br/integracaov2/service.asmx?wsdl"
        )

    @patch("clearsale.api.Client")
    def test_get_ws_client_homolog_env(self, mocked_client):
        mocked_client.return_value = "client"
        client = self.connector.get_ws_client()
        mocked_client.assert_called_once_with(self.homolog_url)
        self.assertEqual(client, "client")

    @patch("clearsale.api.Client")
    def test_get_ws_client_production_env(self, mocked_client):
        mocked_client.return_value = "client"
        connector = ClearSaleConnector(entity_code=self.entity_code, use_sandbox=True)
        client = connector.get_ws_client()
        mocked_client.assert_called_once_with(self.production_url)
        self.assertEqual(client, "client")

    def test_get_entity_code(self):
        entity_code = self.connector.get_entity_code()
        self.assertEqual(entity_code, self.entity_code)


class ClearSaleServiceTestCase(TestCase):
    def setUp(self):
        self.entity_code = "neil"
        self.connector = ClearSaleConnector(
            entity_code=self.entity_code, use_sandbox=True
        )
        self.service = ClearSaleService(self.connector)

    @patch("clearsale.api.SendOrdersResponse")
    @patch("clearsale.api.Client")
    def test_send_orders(self, mocked_client, mocked_send_orders):
        mocked_client.return_value.service.SendOrders.return_value.format.return_value = (  # noqa
            "neil"
        )
        mocked_send_orders.return_value = "1969"
        order = OrderMock()
        response = self.service.send_orders(order)
        mocked_send_orders.assert_called_once_with("neil")
        self.assertEqual(response, "1969")

    @patch("clearsale.api.OrderStatusResponse")
    @patch("clearsale.api.Client")
    def test_get_order_status(self, mocked_client, mocked_order_status_response):
        mocked_client.return_value.service.GetOrderStatus.return_value.format.return_value = (  # noqa
            "neil"
        )
        mocked_order_status_response.return_value = "armstrong"
        order_id = "1969"
        response = self.service.get_order_status(order_id)
        mocked_order_status_response.assert_called_once_with("neil")
        self.assertEqual(response, "armstrong")

    def test_get_connector(self):
        self.assertEqual(self.service.get_connector(), self.connector)

    def test_set_connector(self):
        self.service.set_connector("neil")
        self.assertEqual(self.service.get_connector(), "neil")
