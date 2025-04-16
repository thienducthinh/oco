class Inventory:
    def __init__(self, warehouse_id, item_id, quantity):
        self.warehouse_id = warehouse_id
        self.item_id = item_id
        self.quantity = quantity

    # Retrieve the inventory for a specific warehouse and item.
    def get_inventory(self, warehouse_id, item_id):
        if self.warehouse_id == warehouse_id and self.item_id == item_id:
            return self.quantity
        else:
            raise ValueError(f"No inventory found for warehouse_id={warehouse_id} and item_id={item_id}.")
        
    # Update the inventory for a specific warehouse and item.
    def update_inventory(self, warehouse_id, item_id, new_quantity):
        if self.warehouse_id == warehouse_id and self.item_id == item_id:
            self.quantity = new_quantity
        else:
            raise ValueError(f"No inventory found for warehouse_id={warehouse_id} and item_id={item_id}.")

inventory_transctions = []  # List to store inventory transactions

class InventoryTransaction:
    def __init__(self, transaction_id, warehouse_id, transaction_date):
        self.transaction_id = transaction_id
        self.warehouse_id = warehouse_id
        self.transaction_date = transaction_date

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

class PurchaseOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, supplier_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.supplier_id = supplier_id
        self.lines = []

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = PurchaseOrderLine(line_id, item_id, quantity, unit_price)
        print(line)
        # Update inventory when a line is added
        self.lines.append(line)

class PurchaseOrderLine:
    def __init__(self, line_id, item_id, quantity, unit_price):
        self.line_id = line_id
        self.item_id = item_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = quantity * unit_price

class InventoryAdjustment(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.adjustments = []

    def add_adjustment(self, item_id, quantity):
        adjustment_id = len(self.adjustments) + 1
        adjustment = InventoryAdjustmentLine(adjustment_id, item_id, quantity)
        print(adjustment)
        # Update inventory when an adjustment is added
        self.adjustments.append(adjustment)

class InventoryAdjustmentLine:
    def __init__(self, adjustment_id, item_id, quantity):
        self.adjustment_id = adjustment_id
        self.item_id = item_id
        self.quantity = quantity

