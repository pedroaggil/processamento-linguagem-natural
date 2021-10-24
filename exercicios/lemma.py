import spacy

nlp = spacy.load("pt_core_news_lg") # Referente ao pacote de linguagem baixado
doc = nlp(palavras)

lemmas = [token.lemma_ for token in doc if token.pos_ == 'VERB'] # Lematiza o texto

'''
O atributo lemma_ lematiza o texto.
A lematização se refere, no spaCy, à forma canônica do verbo (embora seja útil para todas, o framework decidiu
reduzir sua funcionalidade somente para essa classe); foi passado como parâmetro, em consequência disso (a partir
do atributo pos_), que fosse selecionado apenas os verbos (visto que a etiqueta de verbo, em spaCy, é 'VERB').
'''