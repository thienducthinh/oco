from datetime import datetime
from price_book import PriceBook
# from inventory_transaction_line import InventoryTransactionLine

class InventoryTransaction:
    def __init__(self, transaction_id, warehouse_id, transaction_date):
        self.transaction_id = transaction_id
        self.warehouse_id = warehouse_id
        self.tradatensaction_ = transaction_date
        self.lines = []

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = InventoryTransactionLine(line_id, item_id, quantity, unit_price)
        self.lines.append(line)

    def process_line(self):
        for line in self.lines:
            if line.status == "Created":
                # Process the line
                print(f"Processing line {line.line_id} for item {line.item_id}")
                line.status = "Processed"
                print(f"Line {line.line_id} processed successfully.")

class InventoryTransactionLine:
    def __init__(self, line_id, item_id, quantity, unit_price):
        self.line_id = line_id
        self.item_id = item_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = quantity * unit_price
        self.status = "Created"

class PurchaseOrder(InventoryTransaction):
    def __init__(self, transaction_id, warehouse_id, transaction_date, supplier_id):
        super().__init__(transaction_id, warehouse_id, transaction_date)
        self.supplier_id = supplier_id
        self.transaction_type = "Purchase Order"

    def add_line(self, item_id, quantity, unit_price):
        line_id = len(self.lines) + 1
        line = PurchaseOrderLine(line_id, item_id, quantity, unit_price)
        self.lines.append(line)

    def process_line(self):
        super().process_line()

class PurchaseOrderLine(InventoryTransactionLine): 

    def __init__(self, line_id, item_id, quantity, unit_price):
        super().__init__(line_id, item_id, quantity, unit_price)



price_books = [
    PriceBook(1, 101, 5.0),
    PriceBook(1, 102, 10.0),
    PriceBook(2, 101, 6.0),
    PriceBook(2, 102, 12.0),]

purchase_order_1 = PurchaseOrder(1, 1, datetime.now(), 1)
item_id = 101
quantity = 10
# Correctly retrieve the price from price_books
price = next(x.price for x in price_books if x.supplier_id == purchase_order_1.supplier_id and x.item_id == item_id)
purchase_order_1.add_line(item_id, quantity, price)




transaction = InventoryTransaction(1, 101, datetime.now())
transaction.add_line(1, 10, 5.0)


for line in transaction.lines:
    print(f"Line ID: {line.line_id}, Item ID: {line.item_id}, Quantity: {line.quantity}, Unit Price: {line.unit_price}, Total Price: {line.total_price}, Status: {line.status}")

transaction.process_line()
for line in transaction.lines:
    print(f"Line ID: {line.line_id}, Item ID: {line.item_id}, Quantity: {line.quantity}, Unit Price: {line.unit_price}, Total Price: {line.total_price}, Status: {line.status}")


transaction.add_line(2, 5, 10.0)
print("After adding another line:")

for line in transaction.lines:
    print(f"Line ID: {line.line_id}, Item ID: {line.item_id}, Quantity: {line.quantity}, Unit Price: {line.unit_price}, Total Price: {line.total_price}, Status: {line.status}")

transaction.process_line()

for line in transaction.lines:
    print(f"Line ID: {line.line_id}, Item ID: {line.item_id}, Quantity: {line.quantity}, Unit Price: {line.unit_price}, Total Price: {line.total_price}, Status: {line.status}")