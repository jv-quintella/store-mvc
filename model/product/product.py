from dataclasses import dataclass
from model.product.product_category import ProductType
from model.product.pricing import PricingPolicy

#https://docs.python.org/3/library/dataclasses.html
#https://stackoverflow.com/questions/67432117/if-else-in-python-dataclasses
#Refactor: SKU foi transformado em classe para implementar um if que valida precos negativos
class SKU():
    def __init__(self, code):
        if not code.strip():
            raise ValueError("O SKU nao pode estar vazio")
        self.code = code
    def __str__(self):
        return self.code
    
#Refactor: Price foi transformado em classe ao inves de dataclass para verificar se a lista esta vazia
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
    #Fix: Desconto foi substituido por pricing policy para acomodar precos normais tambem
    @policy.setter
    def policy(self, p: PricingPolicy): 
        self._policy = p

    # Métodos
    #Error: Final_price calculava self._price.amount + self._policy.factor(), o que causava precos mais altos
    #Fix: + foi alterado para *, agora aplicando o desconto corretamente
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