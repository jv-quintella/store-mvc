from dataclasses import dataclass
from model.product.product_category import ProductType
from model.product.pricing import PricingPolicy

#https://docs.python.org/3/library/dataclasses.html
#Feat: Changed dataclasses to normal classes so that if statements could be used to verify empty lists or negative prices
class SKU():
    def __init__(self, code):
        if not code.strip():
            raise ValueError("O SKU nao pode estar vazio")
        self.code = code
    def __str__(self):
        return self.code

class Price:
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("O preco deve ser maior que zero")
        self.amount = amount
    def __str__(self):
        return f"R$ {self.amount:.2f}"

class Product:
    def __init__(self, sku: SKU, name: str, price: Price, category: ProductType, policy: PricingPolicy = None):
        self._sku = sku
        self._name = name
        self._price = price
        self._category = category
        self._policy = policy

    # Getters
    @property
    def sku(self):
        return self._sku
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def category(self):
        return self._category

    @property
    def policy(self):
        return self._policy
    
    # Setters
    #Feat: Changed discount to pricing policy so that it can accommodate normal prices too
    @policy.setter
    def policy(self, p: PricingPolicy): 
        self._policy = p

    # Métodos
    #Error: Final_price calculated self._price.amoumt + self._policy.factor(), which lead to higher prices
    #Fix: Changed + to *, applying the discount properly
    def final_price(self) -> float:
        return self._price.amount * self._policy.factor()

    def __repr__(self):
        return (f"Product(sku={self._sku!r}, name={self._name!r}, "
                f"price={self._price!r}, category={self._category.name})")

    def __str__(self):
        return (f"[{self._sku}] {self._name} "
                f"({self._category.name}) - {self._price} "
                f"\nFinal price: R$ {self.final_price():.2f}")

    def __eq__(self, other):
        return isinstance(other, Product) and self._sku == other._sku