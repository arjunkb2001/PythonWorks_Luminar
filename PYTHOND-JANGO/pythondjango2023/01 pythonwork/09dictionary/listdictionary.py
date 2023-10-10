items=[ {"id": 1, "name": "sugar", "price" :40, "avl_qty": 10},
    {"id" :2, "name": "milk", "price": 28, "avl_qty": 40},
    {"id" :3, "name": "teapowder", "price" :230, "avl_qty": 100},
    {"id" :4, "name": "tomatto", "price": 120, "avl_qty":5},
    {"id" :5, "name": "potatto", "price" :45, "avl_qty": 70},
    {"id":6, "name":"carrot", "price":80, "avl_qty":0},
    {"id" :7, "name": "oreo", "price" :45, "avl_qty": 0},
    {"id" :8, "name": "hideandseek", "price" :50, "avl_qty": 50}
]

#print total number  of  product:

# print(len(items),"product")

all_product=[i.get("name") for i in items]
print(all_product)
#print all product name:

for i in items:
    print(i.get("name"))


#print all in stock product name:

# for i in items:
#     if i.get("avl_qty")>0:
#         print(i.get("name"))

instock_product=[i.get("name") for i in items if i.get("avl_qty")>0]



#print product name avialble under 50rs:

# for i in items:
#     if i.get("price"):
#         print(i.get("name"))

price_filter=[i.get("name")for i in items if i.get("price")<=0]



#print all product name avilable in range 20 - 50:
# for i in items:
#     if i.get("price")>20 and i.get("price")<50:
#         print(i.get("name"))


range_filter=[i.get("name") for i in items if i.get("price") in range(20,50) ]
print(range_filter)



#costly product ;

maximim=max([i.get("price") for i in items])
print(maximim)

costly_product=max(items,key=lambda i: i.get("price"))
print(costly_product)


product_sort=sorted(items,reverse=True,key=lambda i: i.get("avl_qty"))
print(product_sort)