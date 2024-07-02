orders = [
    ("Alice", "Laptpop", 1),
    ("Bob", "Camera", 2),
    ("Johnny", "Batteries", 6),
    ("Sam", "Olive Oil", 2)
]

def order_retrieval():
    for i, order in enumerate(orders):
        print(f"{i + 1}. Customer: {order[0]} Product: {order[1]} Amount: {order[2]}")
    
order_retrieval()