import spacy

nlp = spacy.load("pt_core_news_lg") # Referente ao pacote de linguagem baixado
doc = nlp(palavras)

tokens = [token.orth_ for token in doc] # Tokenizando o texto; o atributo orth_ converte o dado em string

'''
Caso queir procurar por caracteres específicos (como letras, números ou pontuações) separadamente,
pode-se usar, respectivamente, dos atributos ao adicioná-los, ainda na lista:

Para letras: is_alpha
Para números: is_digit
Para pontuações: is_punct

	tokens = [token.orth_ for token in doc if token.is_alpha]

O que essa linha faz: ela tokeniza o texto, converte-o em string (visto que o spaCy usa de um tipo de dado específico
para token), e os exibe conforme avança pelo texto - caso o token seja composto por letras. Caso os parâmetros mudassem,
a lógica também mudaria e o resultado seria adaptado às necessidades expostas no comando.
'''