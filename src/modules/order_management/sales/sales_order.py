from src.modules.warehousing.inventory_transaction import InventoryTransaction, InventoryTransactionLine

class SalesOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, customer_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.customer_id = customer_id
        self.transaction_type = "Sales Order"

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = SalesOrderLine(line_id, item_id, quantity, unit_price)
        self.lines.append(line)

    def process_line(self):
        super().process_line()

class SalesOrderLine(InventoryTransactionLine):
    def __init__(self, line_id, item_id, quantity, unit_price):
        super().__init__(line_id, item_id, quantity, unit_price)