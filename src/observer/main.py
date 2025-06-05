from src.observer.shop import Product, Purchase

if __name__ == "__main__":

    clothes = Product.create("Clothes", 56000)
    ps5 = Product.create("Ps5", 40000000)

    mahdi_purchase = Purchase.create([clothes, ps5])

    print(mahdi_purchase.check_out())
    print(mahdi_purchase.cancel())