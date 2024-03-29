from pyrae import dle

dle.set_log_level(log_level='CRITICAL')

def validate_word(word):
    search = dle.search_by_word(word=word)
    if search.meta_description == 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.':
        raise Exception("Palabra no encontrada en diccionario")
    else:
        return True;