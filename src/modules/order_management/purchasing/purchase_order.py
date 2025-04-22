from modules.warehousing.inventory_transaction import InventoryTransaction, InventoryTransactionLine

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
