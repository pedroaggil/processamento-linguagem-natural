import spacy

nlp = spacy.load("pt_core_news_lg") # Referente ao pacote de linguagem baixado
doc = nlp(palavras)

etiq = [(token.orth_, token.pos_) for token in doc] # Retorna as etiquetas de cada token no texto

'''
Para visualizar as etiquetas dos tokens no texto, basta chamar o atributo pos_ em um token e nos é retornado a
classe gramatical relativa a ele.
A lista de etiquetas é composta por:

	- ADJ: adjetivo;
	- ADP: adposição (preposições, posposições e circumposições);
	- ADV: advérbio;
	- AUX: verbo auxiliar;
	- CONJ: conjunção coordenativa;
	- DET: determinativo;
	- INTJ: interjeição;
	- NOUN: substantivo;
	- NUM: numeral;
	- PART: partícula;
	- PRON: pronome;
	- PROPN: substantivo próprio;
	- PUNCT: pontuação;
	- SCONJ: conjunção subornativa;
	- SYM: símbolo;
	- VERB: verbo;
	- X: outro

Para uma análise mais detalhada sobre cada token, usa-se o atributo morph_, da seguinte forma:
	etiq = [(token.orth_, token.morph) for token in doc]

Pode-se citar entre as características detalhadas o genêro, se é singular ou plural, a pessoa (1°, 2° ou 3°), o tempo
(passado, presente, futuro etc.), se é artigo e várias outras, a depender de cada token.

Sobre o etiquetador, o modelo de linguagem para o português usado no spaCy tem como fonte o Bosque; a acurácia desse
modelo é de mais de 95% (quando usado o pacote de linguagem grande).

Existem outros etiquetadores para o português que alcançam uma maior acurácia - no caso, o NLPNet (gratuito) com
97,33% e o PALAVRAS (pago), com 98%. É importante frisar que esses etiquetadores são plenamente focados no português.
Mais informações sobre o NLPNet podem ser acessadas a partir dos links: < http://nilc.icmc.usp.br/nlpnet/intro.html >
e < https://github.com/erickrf/nlpnet >.
'''