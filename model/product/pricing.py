#abc - abstract base class 
#https://docs.python.org/3/library/abc.html
from abc import ABC, abstractmethod
 
class PricingPolicy(ABC):
    @abstractmethod
    def factor(self) -> float: ...

class Normal(PricingPolicy):
    def factor(self):
        return 1.0
#Fixed 
#Error: The original was doing 100 * percentage, which lead to results such as 100 * 30% = 0.3. That would give an incorrect discount, since discounts are calculated using 100 - %
#Feat: added percentage = percentage / 100 so that if the user inputs a number such as 20, it gets converted to 0.2
class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        percentage = percentage / 100
        self._factor = 1.0 - percentage
    
    def factor(self):
        return self._factor
