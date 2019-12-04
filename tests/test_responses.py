from collections import OrderedDict
from unittest import TestCase

from clearsale.responses import OrderReturn, OrderStatusResponse, SendOrdersResponse

from . import ORDER_STATUS_RESPONSE_XML, SEND_ORDERS_RESPONSE_XML


class OrderReturnTestCase(TestCase):
    def setUp(self):
        self.order_return = OrderReturn(id=1969, status="APA", score=69)

    def test_get_id(self):
        order_return_id = self.order_return.getID()
        self.assertEqual(order_return_id, 1969)

    def test_get_status(self):
        order_return_status = self.order_return.getStatus()
        self.assertEqual(order_return_status, "APA")

    def test_get_score(self):
        order_return_score = self.order_return.getScore()
        self.assertEqual(order_return_score, 69)

    def test_approved(self):
        approved = self.order_return.approved()
        self.assertTrue(approved)

    def test_not_approved(self):
        not_approved = self.order_return.not_approved()
        self.assertFalse(not_approved)

    def test_waiting_for_approval(self):
        waiting_for_approval = self.order_return.waiting_for_approval()
        self.assertFalse(waiting_for_approval)

    def test_has_error(self):
        has_error = self.order_return.has_error()
        self.assertFalse(has_error)

    def test_get_analysis(self):
        analysis = self.order_return.get_analysis()
        self.assertEqual(analysis, 1)

    def test_get_analysis_label(self):
        analysis_label = self.order_return.get_analysis_label()
        self.assertEqual(analysis_label, "Aprovado")

    def test_get_status_label(self):
        status_label = self.order_return.get_status_label()
        expected_label = (
            "(Aprovação Automática) – Pedido foi aprovado automaticamente segundo ",
            "parâmetros definidos na regra de aprovação automática.",
        )
        self.assertEqual(status_label, expected_label)


class ResponseAbstractTestCase:
    def test_parse_xml_to_dict(self):
        parsed_xml = self.response._parse_xml_to_dict(self.xml)
        self.assertTrue(isinstance(parsed_xml, OrderedDict))

    def test_get_transaction_id(self):
        transaction_id = self.response.getTransactionID()
        self.assertFalse(transaction_id)

    def test_get_status_code(self):
        status_code = self.response.getStatusCode()
        self.assertFalse(status_code)

    def test_get_message(self):
        message = self.response.getMessage()
        self.assertFalse(message)

    def test_get_dict(self):
        response_dict = self.response.get_dict()
        self.assertTrue(isinstance(response_dict, OrderedDict))

    def test_get_xml(self):
        xml = self.response.get_xml()
        self.assertTrue(xml)
        self.assertTrue(isinstance(xml, str))

    def test_get_pretty_xml(self):
        pretty_xml = self.response.get_pretty_xml()
        self.assertTrue(pretty_xml)
        self.assertTrue(isinstance(pretty_xml, str))


class OrderStatusResponseTestCase(TestCase, ResponseAbstractTestCase):
    def setUp(self):
        self.xml = ORDER_STATUS_RESPONSE_XML
        self.response = OrderStatusResponse(xml=self.xml)

    def test_get_orders(self):
        orders = self.response.getOrders()
        self.assertEqual(len(orders), 1)
        self.assertTrue(isinstance(orders[0], OrderReturn))


class SendOrdersResponseTestCase(TestCase, ResponseAbstractTestCase):
    def setUp(self):
        self.xml = SEND_ORDERS_RESPONSE_XML
        self.response = SendOrdersResponse(xml=self.xml)

    def test_get_orders(self):
        orders = self.response.getOrders()
        self.assertEqual(len(orders), 0)
