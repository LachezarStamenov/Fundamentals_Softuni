import re

pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

n = int(input())
digit_list = []
for _ in range(n):

    input_line = input()

    matches = re.findall(pattern, input_line)
    if matches:
        barcode = ''.join(matches)
        product_group = ''.join([x for x in barcode if x.isdigit()])
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')

