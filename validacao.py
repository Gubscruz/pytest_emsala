def valida_cpf(cpf: str) -> bool:

    if not isinstance(cpf, str):
        return False

    if len(cpf) != 11:
        return False
    
    if not cpf.isdigit():
        return False

    return True

def valida_idade(idade: int) -> bool:
    pass
