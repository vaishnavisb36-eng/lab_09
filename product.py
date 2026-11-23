def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: Rs. {price}"
    )

if __name__ == "__main__":
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    print(product_details(pid, name, quantity, price))


