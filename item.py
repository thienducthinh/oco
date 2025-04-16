class Item:
    def __init__(self, item_id, name, description, unit_price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.unit_price = unit_price

class ItemManager:
    def __init__(self):
        self.items = {}  # Dictionary to store items, keyed by item_id

    def add_item(self, item_id, name, description, unit_price):
        """Add a new item to the system."""
        if item_id in self.items:
            raise ValueError("Item ID already exists.")
        new_item = Item(item_id, name, description, unit_price)
        self.items[item_id] = new_item
        return new_item

    def update_item(self, item_id, name=None, description=None, unit_price=None):
        """Update an existing item's attributes."""
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        item = self.items[item_id]
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if unit_price is not None:
            item.unit_price = unit_price

    def remove_item(self, item_id):
        """Remove an item from the system."""
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        del self.items[item_id]

    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        return self.items.get(item_id, None)    