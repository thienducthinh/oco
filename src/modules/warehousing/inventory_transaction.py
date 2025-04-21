from datetime import datetime
from inventory_transaction_line import InventoryTransactionLine

class InventoryTransaction:
    def __init__(self, transaction_id, warehouse_id, transaction_date):
        self.transaction_id = transaction_id
        self.warehouse_id = warehouse_id
        self.tradatensaction_ = transaction_date
        self.lines = []

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = InventoryTransactionLine(line_id, item_id, quantity, unit_price)
        self.lines.append(line)

