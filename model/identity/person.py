from dataclasses import dataclass
from abc import ABC

#https://www.reddit.com/r/learnpython/comments/7dks3q/what_is_the_purpose_of_property/
#Refactor: Endereco foi transformado em uma classe para implementar um if que verifica se as strings estao vazias
#Refactor: Implementado ._ antes das variaveis para replicar o "frozen" utilizado no dataclass original
class Address:
    def __init__(self, street:str, city:str, zip_code:str):
        if not street.strip():
            raise ValueError("A rua nao pode ser um valor vazio")
        if not city.strip():
            raise ValueError("A cidade nao pode ser um valor vazio")
        if not zip_code.strip():
            raise ValueError("O CEP nao pode ser um valor vazio")
        
        self._street = street
        self._city = city
        self._zip_code = zip_code

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    @property
    def zip_code(self):
        return self._zip_code

    def __str__(self):
        return f"{self._street}, {self.city} - {self.zip_code}"
    
#Refactor: Contato foi transformado em uma classe para implementar um if que verifica se as strings estao vazias
#Refactor: Implementado ._ antes das variaveis para replicar o "frozen" utilizado no dataclass original
class Contact:
    def __init__(self, email: str, phone: str):
        if not email.strip():
            raise ValueError("O email nao pode estar vazio")
        if not phone.strip():
            raise ValueError("O telefone nao pode estar vazio")
        
        self._email = email
        self._phone = phone

    @property
    def email(self):
        return self._email
        
    @property
    def phone(self):
        return self._phone

    def __str__(self):
        return f"{self._email} / {self._phone}"

#Refactor: Implementado um if para verificar se nome esta vazio
class Person(ABC):
    def __init__(self, name: str, address: Address, contact: Contact):
        if not name.strip():
            raise ValueError("O nome nao pode estar vazio")
        self._name = name
        self._address = address
        self._contact = contact

    @property
    def name(self):
        return self._name
    @property
    def address(self):
        return self._address
    @property
    def contact(self):
        return self._contact