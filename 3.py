data = ['蘋果紅茶 2', '香蕉牛奶 3', '蘋果紅茶 3', '香酥雞排 2']


def count_products(data):
    products = {}
    for d in data:
        item, num = d.split()
        num = int(num)
        if item in products.keys():
            products[item] += num  
        else:
            products[item] = num
    print(products)
    return products

count_products(data)
