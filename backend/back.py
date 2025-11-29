products =[
    ["arabica", 90],
    ["colombian coffee", 85],
    ["mocha haraz", 125],
    ["excelsa", 65],
    ["ethiopian coffee", 70],
    
]
print(":أسعار القهوة حصريا")

for i in range(len (products)):
    print(i+ 1, "-" , products[i][0], "price", products[i][1])
    
    choice = input("اكتب اسم المنتج الذي تريد شراءه :")
    
    if choice.isdigit():
        choice = int(choice)
        
        if 1 <= choice <= len(products):
            price = products[choice -1][1]
            total = price + (price* 0.15)
            print ("السعر شامل الضريبة =", total)
        else:
            print ("المنتج خاطئ غير متوفر في القائمة")
    else:
            print ("الرجاء ادخال رقم المنتج فقط")