# Standard library imports
from datetime import datetime

# Local module imports
from price_book import PriceBook
from src.modules.warehousing.inventory_transaction import InventoryTransaction
from src.modules.order_management.sales.sales_order import SalesOrder
from src.modules.order_management.purchasing.purchase_order import PurchaseOrder

price_books = [
    PriceBook(1, 101, 5.0),
    PriceBook(1, 102, 10.0),
    PriceBook(2, 101, 6.0),
    PriceBook(2, 102, 12.0),]

purchase_order_1 = PurchaseOrder(1, 1, datetime.now(), 2)
item_id = 101
quantity = 10
purchase_order_1.add_line(item_id, quantity)

print("Purchase Order Lines:")
for line in purchase_order_1.lines:
    print(f"Line ID: {line.line_id}, Item ID: {line.item_id}, Quantity: {line.quantity}, Unit Price: {line.unit_price}, Total Price: {line.total_price}")
print("Processing Purchase Order Lines:")
purchase_order_1.process_line()
print("Purchase Order Lines after processing:")
for line in purchase_order_1.lines:
    print(f"Line ID: {line.line_id}, Item ID: {line.item_id}, Quantity: {line.quantity}, Unit Price: {line.unit_price}, Total Price: {line.total_price}")