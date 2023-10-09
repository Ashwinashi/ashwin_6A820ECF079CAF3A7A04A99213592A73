def linearSearchProduct(ProductList, targetProduct):
  indices = []

  for index, product in enumerate(ProductList):
    if product == targetProduct:
      indices.append(index)

  return indices

  


Products = ["shoes", "boat", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = "mangoes"
result = linearSearchProduct(Products, target)

print(result)
