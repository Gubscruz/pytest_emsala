import pytest
from ..validacao import valida_cpf, valida_idade


@pytest.mark.cpf
def test_valida_cpf_valido():
    # * passa um input valido e espera que retorne true
    assert valida_cpf("33652827610") == True

@pytest.mark.cpf
def test_valida_cpf_mais_de_11_dig():
    assert valida_cpf("132074234297364") == False

@pytest.mark.cpf
def test_valida_cpf_menos_de_11_dig():
    assert valida_cpf("3189276") == False

@pytest.mark.cpf
def test_valida_cpf_somente_numeros():
    assert valida_cpf("abcde123456") == False

@pytest.mark.cpf
def test_valida_cpf_somente_strings():
    assert valida_cpf(12345678901) == False


@pytest.mark.idade
def test_valida_idade_positiva():
    assert valida_idade(-5) == False