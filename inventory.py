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

