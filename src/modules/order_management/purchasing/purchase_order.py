from inventory_transaction import InventoryTransaction

class PurchaseOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, supplier_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.supplier_id = supplier_id

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = PurchaseOrderLine(line_id, item_id, quantity, unit_price)
        print(line)
        # Update inventory when a line is added
        self.lines.append(line)

class PurchaseOrderLine(InventoryTransactionLine):
    def __init__(self, line_id, item_id, quantity, unit_price):
        super().__init__(line_id, item_id, quantity)
        self.unit_price = unit_price
        self.total_price = quantity * unit_price 

class InventoryTransaction:
    def __init__(self, transaction_id, warehouse_id, transaction_date):
        self.transaction_id = transaction_id
        self.warehouse_id = warehouse_id
        self.transaction_date = transaction_date
        self.lines = []

    def add_line(self, item_id, quantity):
        line_id = len(self.lines) + 1
        line = InventoryTransactionLine(line_id, item_id, quantity)
        self.lines.append(line)

class InventoryTransactionLine:
    def __init__(self, line_id, item_id, quantity):
        self.line_id = line_id
        self.item_id = item_id
        self.quantity = quantity

po = PurchaseOrder(1, 1, "2023-10-01", 1)
print(po.__dict__)