# Definição de uma exceção personalizada para indicar que uma conta não foi encontrada.
class AccountNotFoundError(Exception):
    pass

# Definição de uma exceção personalizada para erros de negócio.
class BusinessError(Exception):
    pass
