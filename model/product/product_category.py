from enum import Enum

#Error: Todos os valores de enum recebiam 1
#Fixed - Valores do Enum foram atualizados
class ProductType(Enum):
    ELECTRONICS = 1
    CLOTHING = 2
    BOOKS = 3
    FOOD = 4
