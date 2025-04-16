from modules.order_management.inventory_transaction import InventoryTransaction, InventoryTransactionLine

class PurchaseOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, supplier_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.supplier_id = supplier_id
        self.transaction_type = "Purchase Order"

    def add_line(self, item_id, quantity, unit_price):
        super().add_line(item_id, quantity, unit_price)

class PurchaseOrderLine(InventoryTransactionLine):
    def __init__(self, line_id, item_id, quantity, unit_price):
        super().__init__(line_id, item_id, quantity, unit_price)

class SalesOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, supplier_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.supplier_id = supplier_id
        self.transaction_type = "Sales Order"

    def add_line(self, item_id, quantity, unit_price):
        super().add_line(item_id, quantity, unit_price)

class SalesOrderLine(InventoryTransactionLine):
    def __init__(self, line_id, item_id, quantity, unit_price):
        super().__init__(line_id, item_id, quantity, unit_price)

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

class InventoryTransactionLine:
    def __init__(self, line_id, item_id, quantity, unit_price):
        self.line_id = line_id
        self.item_id = item_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = quantity * unit_price