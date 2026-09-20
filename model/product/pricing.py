#abc - abstract base class 
#https://docs.python.org/3/library/abc.html
from abc import ABC, abstractmethod
 
class PricingPolicy(ABC):
    @abstractmethod
    def factor(self) -> float: ...

class Normal(PricingPolicy):
    def factor(self):
        return 1.0

#Error: O original fazia 100 * percentage, o que causava resultados como 100 * 30% = 0,3. Isso daria um desconto incorreto, pois descontos sao calculados usando 100 - percentage
#Fix * foi alterado para -
#Refactor: Adicionado conversor que divide o input por 100 para que inputs como 20 sejam convertidos para 0.2 
class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        percentage = percentage / 100
        self._factor = 1.0 - percentage
    
    def factor(self):
        return self._factor
