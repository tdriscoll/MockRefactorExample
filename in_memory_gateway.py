class InMemoryDataGateway(object):
    def __init__(self):
        self.values = {}

    def get_value_for_date(self, query_date):
        return self.values.get(query_date)

    def get_value_for_dates(self, query_dates):
        return [(date, value) for date, value in self.values.iteritems() if date in query_dates]