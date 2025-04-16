from datetime import datetime
from inventory_transaction_line import InventoryTransactionLine

class InventoryTransaction:
    def __init__(self, transaction_id, warehouse_id, transaction_date):
        self.transaction_id = transaction_id
        self.warehouse_id = warehouse_id
        self.transaction_date = transaction_date
        self.lines = []

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        if self.transaction_type == "Purchase Order":
            line = PurchaseOrderLine(line_id, item_id, quantity, unit_price)
        elif self.transaction_type == "Sales Order":
            line = SalesOrderLine(line_id, item_id, quantity, unit_price)
        self.lines.append(line)

