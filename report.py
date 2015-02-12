class Report(object):
    def __init__(self, data_gateway):
        self.data_gateway = data_gateway

    def is_value_increasing(self, start_date, end_date):
        start_value = self.data_gateway.get_value_for_date(start_date)
        end_value = self.data_gateway.get_value_for_date(end_date)
        if not end_value:
            return False
        if not start_value:
            return True
        return end_value > start_value