import json
from typing import List

import requests


def get_product(id: str):
    """
    Get the product from the API
    :param id: ID of the product
    :return: dict containing product information
    """
    response = requests.get(f"http://127.0.0.1:5000/api/v1/get_product/{id}")
    if response.status_code == 200:
        product = json.loads(response.content)
    else:
        raise Exception("Could not get product information from the database")
    return {
        "name": product[1],
        "price_in_euros": 0.01 * product[2]
    }


class OrderReport:
    base_url = "http://127.0.0.1:5000"

    def create_report(self) -> List[str]:
        """
        read orders
        get price of a product
        get costumer name
        sum products

        :return:
        """
        report_lines = []

        orders = json.loads(
            requests.get(f"{self.base_url}/api/v1/get_orders").content
        )

        # Get the products in the order
        for order in orders:
            products = []
            price = 0
            order_id = order[0]
            response = requests.get(f"{self.base_url}/api/v1/read_order/{order_id}")
            if response.ok:
                for order_item in json.loads(response.content):
                    product_id = order_item[1]
                    product = get_product(product_id)
                    products.append(product)
                    price += order_item[2] * product["price_in_euros"]

            product_names = ", ".join(product["name"] for product in products)
            report_lines.append(f"Order {order[0]} for {order[1]} has price €{price} and products: {product_names}")

        return report_lines


if __name__ == "__main__":
    order_report = OrderReport()
    report = order_report.create_report()

    for line in report:
        print(line)
