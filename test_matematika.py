from matematika import sudetis
from matematika import daugyba
from matematika import rask_didziausia
import matematika

def test_sudetis():
    assert sudetis(1,2) == 3

def test_sudetis_neigiami():
    assert sudetis(-1,-5) == -6

def test_daugyba():
    assert daugyba(5,2) == 10
    assert daugyba(-5,-5) > 0
    assert daugyba(5,10) != -1
    assert daugyba(-5,5) < 0

def test_sudetis_2():
    num1, num2 = 5, 3
    rezultatas = 10
    faktinis_rezultatas = sudetis(num1, num2)
    assert rezultatas == faktinis_rezultatas, f'sudeties testas nepavyko: {num1} + {num2} turetu buti {rezultatas}, bet gavome {faktinis_rezultatas}'

def test_rask_didziausia():
    num1, num2 = 10, 20
    rezultatas = 20
    faktinis_rezultatas = rask_didziausia(num1, num2)
    assert faktinis_rezultatas == rezultatas

def test_rask_didziausia_2():
    assert rask_didziausia(10,5) == 10
    assert rask_didziausia(5,10) == 10
    assert rask_didziausia(10, 10) == 10

def test_pirmas_sarase():
    skaiciai = [1,2,3,4,5]
    assert matematika.pirmas_sarase(skaiciai) == 1

def test_pirmas_sarase_none():
    skaiciai = []
    assert matematika.pirmas_sarase(skaiciai) == None

import pytest
@pytest.mark.parametrize('a, b, c, turis', [
    (1,1,1,1),
    (2,3,2,12)
])

def test_kubo_turis(a, b, c, turis):
    assert matematika.kubo_turis(a, b, c) == turis

@pytest.mark.parametrize('number_to_test, result_string', [
    (7,False),
    (9,True),
    (0,True),
])

def test_division_by_3(number_to_test, result_string):
    assert matematika.division_by_3(number_to_test) == result_string

@pytest.mark.parametrize('word_list_to_test, result_list', [
    (['labas', 'bitė', 'sviestas', 'lauke'],['labas', 'sviestas']),
    (['valio', 'valgau', 'alio', 'sviestą'],['valgau', 'sviestą'])
])

def test_words_with_same_letters(word_list_to_test, result_list):
    assert matematika.words_with_same_letters(word_list_to_test) == result_list

@pytest.mark.parametrize('number_to_test, result_string', [
    (-10, False),
    (0, False),
    (1, False),
    (7, True),
    (10, False),

])

def test_check_if_prime(number_to_test, result_string):
    assert matematika.check_if_prime(number_to_test) == result_string