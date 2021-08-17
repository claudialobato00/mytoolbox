from mytoolbox.nlp_preprocessing import remove_punctuation, lower_all, remove_numbers
import pandas as pd
a = pd.DataFrame({'col1': ['this with . full stop and CAPITAL and 9843numbers']})
    
def test_for_puntuation():
    assert '.' not in remove_punctuation(a['col1'])

def test_lower_case():
    assert 'A' not in lower_all(a['col1'])

def test_remove_numbers():
    assert '5' not in remove_numbers(a['col1'])
