def revenue_growth_rate(current_revenue, previous_revenue):
    if previous_revenue == 0:
        return float('inf')  # Avoid division by zero
    return ((current_revenue - previous_revenue) / previous_revenue) * 100

def gross_margin(sales_revenue, cost_of_goods_sold):
    if sales_revenue == 0:
        return float('inf')  # Avoid division by zero
    return ((sales_revenue - cost_of_goods_sold) / sales_revenue) * 100

def operating_margin(operating_income, sales_revenue):
    if sales_revenue == 0:
        return float('inf')  # Avoid division by zero
    return (operating_income / sales_revenue) * 100

def inventory_turnover_ratio(cost_of_goods_sold, average_inventory):
    if average_inventory == 0:
        return float('inf')  # Avoid division by zero
    return cost_of_goods_sold / average_inventory

def days_inventory_outstanding(inventory_turnover_ratio):
    if inventory_turnover_ratio == 0:
        return float('inf')  # Avoid division by zero
    return 365 / inventory_turnover_ratio

