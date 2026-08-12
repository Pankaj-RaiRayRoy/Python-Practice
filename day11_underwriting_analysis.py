def calculate_final_premium(base_price, percentage):
  adjustable_amount = base_price * (percentage / 100)
  return base_price + adjustable_amount


base_price_list = [100, 150, 200, 250, 300]
flat_risk_rate = 10

for counter in range(len(base_price_list)):
  final_premium = calculate_final_premium(base_price_list[counter], flat_risk_rate)
  print("Final Premium is : ", final_premium)
