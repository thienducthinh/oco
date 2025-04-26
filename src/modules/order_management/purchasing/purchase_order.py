from src.modules.warehousing.inventory_transaction import InventoryTransaction, InventoryTransactionLine
from db.connect_db import execute_command

class PurchaseOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, supplier_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.supplier_id = supplier_id
        self.transaction_type = "Purchase Order"

    def add_line(self, item_id, quantity):
        line_id = len(self.lines) + 1
        # Retrieve the price from the price book
        price = self.get_price(item_id, self.supplier_id)
        line = PurchaseOrderLine(line_id, item_id, quantity, price)
        self.lines.append(line)

    def get_price(self, item_id, supplier_id):
        # TODO: Replace with actual price book from Database
        query = """
        SELECT price FROM price_book WHERE item_id = %s AND supplier_id = %s
        """
        return execute_command(query, (item_id, supplier_id))
    
    def process_line(self):
        super().process_line()

class PurchaseOrderLine(InventoryTransactionLine):
    def __init__(self, line_id, item_id, quantity, unit_price):
        super().__init__(line_id, item_id, quantity, unit_price)
