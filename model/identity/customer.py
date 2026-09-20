from model.identity.person import Person, Address, Contact

class Customer(Person):
    def __init__(self, customer_id: str, name: str, address: Address, contact: Contact):
        if not customer_id.strip():
            raise ValueError("O ID do cliente nao pode ser um valor vazio")
        #https://www.w3schools.com/python/ref_func_super.asp
        super().__init__(name, address, contact) # Usa a inicializacao do pai (Person)
        self._customer_id = customer_id
        self._loyalty_points = 0

    @property
    def customer_id(self):
        return self._customer_id

    # Vou apresentar essa ideia pro Rodrigo amanhã
    #Feat: Implementado um if para validar se n e' maior que zero, garantindo que o saldo de pontos nao seja negativo
    def add_points(self, n: int) -> None:
        if n > 0:
            self._loyalty_points += n
        else:
            raise ValueError("n nao pode ser um valor negativo")
    
    def __repr__(self):
        # o que será que esse !r faz aqui?
        #DOCS: !r retorna um string "crua", que imprime exatamente o que e' lido, por exemplo \n sera interpretado como \n e nao como uma quebra de linha
        return (f"Customer(id={self._customer_id!r}, "
                f"name={self._name!r}, "
                f"address={self._address!r}, "
                f"contact={self._contact!r})")

    def __str__(self):
        return (f"[{self._customer_id}] {self._name}\n"
                f"  {self._address}\n"
                f"  {self._contact}")