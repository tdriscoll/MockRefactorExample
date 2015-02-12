from data_gateway import DataGateway
from report import Report
from datetime import date


report = Report(DataGateway())

print(report.is_value_increasing(date(2015, 1, 15), date(2015, 1, 19)))
