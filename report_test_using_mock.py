from unittest import TestCase
from mock import Mock, call
from report import Report
from datetime import date


class ReportTestUsingMock(TestCase):
    def setUp(self):
        self.start_date = date(2015, 1, 15)
        self.end_date = date(2015, 1, 20)

    def _get_gateway_mock(self, values):
        gateway = Mock()
        gateway.get_value_for_date = Mock(side_effect=lambda query_date: values.get(query_date))
        return gateway

    def _verify_result(self, gateway, expected):
        self.assertEquals(expected, Report(gateway).is_value_increasing(self.start_date, self.end_date))
        gateway.get_value_for_date.assert_has_calls([call(self.start_date), call(self.end_date)])

    def test_given_no_values_return_false(self):
        gateway = Mock()
        gateway.get_value_for_date = Mock(return_value=None)
        self._verify_result(gateway, False)

    def test_given_no_start_value_return_true(self):
        gateway = self._get_gateway_mock({self.end_date: 3})
        self._verify_result(gateway, True)

    def test_given_start_greater_than_end_return_false(self):
        gateway = self._get_gateway_mock({self.start_date: 7, self.end_date: 3})
        self._verify_result(gateway, False)


