
from abc import ABC, abstractmethod


class ProductBase(ABC):

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def shipping(self):
        pass


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass

class RugsShipping(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f'rugs shipping: {self.rugs._shipping}'


class GiftCardShipping(DetailBase):
    def __init__(self, gift_card):
        self.gift_card = gift_card

    def show(self):
        return f'rugs shipping: {self.gift_card._shipping}'



class RugsDetail(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs detail: {self.rugs._name}"


class RugsPrice(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs price: {self.rugs._price}"


class GiftCardDetail(DetailBase):
    def __init__(self, card):
        self.giftCard = card

    def show(self):
        return f"company : {self.giftCard.company},"


class GiftCardPrice(DetailBase):
    def __init__(self, card):
        self.giftCard = card

    def show(self):
        return f"gift card min price : {self.giftCard.min_price},max price : " \
               f"{self.giftCard.max_price} "


class Rugs(ProductBase):
    def __init__(self, name, price, shipping):
        self._name = name
        self._price = price
        self._shipping = shipping

    @property
    def detail(self):
        return RugsDetail(self)

    @property
    def price(self):
        return RugsPrice(self)

    @property
    def shipping(self):
        return RugsShipping(self)


class GiftCard(ProductBase):

    def __init__(self, company, min_price, max_price, shipping):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price
        self._shipping = shipping


    @property
    def detail(self):
        return GiftCardDetail(self)

    @property
    def price(self):
        return GiftCardPrice(self)

    @property
    def shipping(self):
        return GiftCardShipping(self)


if __name__ == '__main__':
    r1 = Rugs('persian', 135, 'ship')
    r2 = Rugs('armani', 155, 'plane')

    g1 = GiftCard("google", 20, 50, 'email')
    g2 = GiftCard("Apple", 40, 100, 'post')

    products = [r1, r2, g1, g2]
    for product in products:
        print(product.detail.show())
        print(product.price.show())
        print(product.shipping.show())