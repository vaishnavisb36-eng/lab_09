from product import product_details

def test_product():
    assert product_details(101, "Laptop", 2, 50000) == "Product ID: 101\nProduct Name: Laptop\nQuantity: 2\nPrice: Rs. 50000"

def test_product_mobile():
    assert product_details(102, "Mobile", 5, 15000) == "Product ID: 102\nProduct Name: Mobile\nQuantity: 5\nPrice: Rs. 15000"

def test_product_zero_quantity():
    assert product_details(103, "Mouse", 0, 500) == "Product ID: 103\nProduct Name: Mouse\nQuantity: 0\nPrice: Rs. 500"

