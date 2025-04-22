from datetime import datetime
from price_book import PriceBook
from warehousing import inventory_transaction
from order_management import sales_order
from order_management import purchase_order

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