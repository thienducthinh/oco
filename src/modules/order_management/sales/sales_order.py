from modules.warehousing.inventory_transaction import InventoryTransaction

class SalesOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, customer_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.customer_id = customer_id

    def add_line(self, item_id, quantity, unit_price):
        super().add_line(item_id, quantity, unit_price)

    def process_line(self):
        for line in self.lines:
            if line.status == "Created":
                # Process the line
                print(f"Processing line {line.line_id} for item {line.item_id}")
                line.status = "Processed"
                print(f"Line {line.line_id} processed successfully.")