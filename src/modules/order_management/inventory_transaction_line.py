class InventoryTransactionLine:
    def __init__(self, line_id, item_id, quantity, unit_price):
        self.line_id = line_id
        self.item_id = item_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = quantity * unit_price