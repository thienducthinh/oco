from warehouse import Warehouse

class Entity:
    def __init__(self, entity_id, entity_name):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.warehouses = []  # List of Warehouse objects

    def add_warehouse(self, warehouse_name):
        """Add a new warehouse to the entity."""
        # Determine the next 2-digit increment for the warehouse_id
        if not self.warehouses:
            next_increment = 1  # Start from 01 if no warehouses exist
        else:
            # Extract the last 2 digits of the warehouse_id from the last warehouse
            last_warehouse_id = self.warehouses[-1].warehouse_id
            next_increment = int(last_warehouse_id[-2:]) + 1
    
        # Generate the new warehouse_id by combining entity_id and the 2-digit increment
        warehouse_id = f"{str(self.entity_id).zfill(6)}{str(next_increment).zfill(2)}"
    
        # Create the new warehouse and add it to the list
        new_warehouse = Warehouse(warehouse_id, self.entity_id, warehouse_name)
        self.warehouses.append(new_warehouse)

    def get_warehouses(self):
        """Retrieve all warehouses associated with the entity."""
        return self.warehouses