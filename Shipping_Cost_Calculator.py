weight = float(input("Enter package weight in kg: "))
rate = float(input("Enter shipping rate per kg: "))
shipping_cost = weight * rate
print(f"Shipping Cost: {shipping_cost} USD")
