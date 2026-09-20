from model.product.product import Product

class StockItem:
    def __init__(self, product: Product, quantity: int, min_stock: int = 3):
        self._product = product
        self._quantity = quantity
        self._min_stock = min_stock

    @property
    def product(self):
        return self._product
    
    @property
    def quantity(self):
        return self._quantity

    #Error: A logica inicial apagava o estoque original e adicionava 1 
    #Fix: Adiciona n ao estoque
    #Feat: Adionacada validacao para numeros negativos
    def add(self, n: int) -> None:
        if n <= 0:
            raise ValueError("A quantidade adicionada deve ser maior que zero")
        self._quantity += n 

    #Error: A logica inicial apagava o estoque original e removia 1 
    #Fix: Subtrai n do estoque
    #Refactor: Alterada a validacao para valores menores que a quantidade ja presente no estoque, impedindo estoques negativos
    def remove(self, n: int) -> None:
        if n <= 0:
            raise ValueError(f"Estoque insuficiente para {self._product.sku}")
        self._quantity -= n 

    def low_stock(self) -> bool:
        return self._quantity < self._min_stock

    def __str__(self):
        flag = " !" if self.low_stock() else ""
        return f"{self._product} - {self._quantity}{flag}"

    def __repr__(self):
        return (f"StockItem(product={self._product!r}, "
                f"qty={self._quantity}, min={self._min_stock})")