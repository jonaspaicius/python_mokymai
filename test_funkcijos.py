# import funkcijos

# def test_text_in_reverse():
#     assert funkcijos.text_in_reverse('Jonas') == 'sanoJ'

# def test_text_in_reverse_double_two_words():
#     assert funkcijos.text_in_reverse("Jonas ponas") == 'sanop sanoJ'

# def test_list_sum():
#     list_to_test = [0, 5, -5, 10.5]
#     assert funkcijos.list_sum(list_to_test) == 10.5

# def test_list_sum_none():
#     list_to_test = []
#     assert funkcijos.list_sum(list_to_test) == 0

# def test_sum_of_positives():
#     list_to_test = [5,-10,7,-4,8]
#     assert funkcijos.sum_of_positives(list_to_test) == 20

# def test_sum_of_positives_only_negatives():
#     list_to_test = [-5,-10,-7,-4,-8]
#     assert funkcijos.sum_of_positives(list_to_test) == 0

# def test_sort_list():
#     list_to_test = [7,5,6,1,2,4,10,3]
#     assert funkcijos.sort_list(list_to_test, 'asc') == [1,2,3,4,5,6,7,10]
    
# def test_sort_list_reverse():
#     list_to_test = [7,5,6,1,2,4,10,3]
#     assert funkcijos.sort_list(list_to_test, 'desc') == [10,7,6,5,4,3,2,1]

# from funkcijos import rikiuoti, rikiuoti_didejant, rikiuoti_mazejanciai

# def test_rikiuoti_mazejant():
#     assert rikiuoti(rikiuoti_mazejanciai, [1,3,5,4,2]) == [5,4,3,2,1]

# def test_rikiuoti_didejant():
#     assert rikiuoti(rikiuoti_didejant, [1,3,5,4,2]) == [1,2,3,4,5]

import pytest
import matematika

@pytest.mark.parametrize('sarasas, tiketinas_rezultatas', [
    ([1,2,3,4], 1),
    (['a', 'b', 'c'], 'a'),
    ([], None),
    ([[1,2],[3,4], [5,6]], [1,2])
])

def test_gauti_pirma_elementa(sarasas, tiketinas_rezultatas):
    assert matematika.pirmas_sarase(sarasas) == tiketinas_rezultatas