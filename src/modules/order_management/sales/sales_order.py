from modules.order_management.inventory_transaction import InventoryTransaction

class SalesOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, customer_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.customer_id = customer_id
        self.lines = []

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = SalesOrderLine(line_id, item_id, quantity, unit_price)
        print(line)
        # Update inventory when a line is added
        self.lines.append(line)

    def process_line(self):
        for line in self.lines:
            if line.status == "Created":
                # Process the line
                print(f"Processing line {line.line_id} for item {line.item_id}")
                line.status = "Processed"
                print(f"Line {line.line_id} processed successfully.")

class SalesOrderLine:
    def __init__(self, line_id, item_id, quantity, unit_price, status="Created"):
        self.line_id = line_id
        self.item_id = item_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.status = status
        self.total_price = quantity * unit_price