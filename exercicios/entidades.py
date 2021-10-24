import spacy

nlp = spacy.load("pt_core_news_lg") # Referente ao pacote de linguagem baixado
doc = nlp(palavras)

entidades = list(doc.ents) # Lista as entidades encontradas

'''
Caso você queira saber o tipo da entidade, use o atributo label_ adicionando a seguinte linha ao código:

	detalhesEnt = [(entidade, entidade.label_) for entidade in doc.ents]

Guia de tipo de entidades:
	- ORG: organização;
	- LOC: localização;
	- PER: pessoa;
	- DATE: data;
	- MISC: genérico

É possível visualizar graficamente por meio do displaCy. Essa visualização se dá a partir de HTML,
ao gerar um documento desse tipo e escrever nele com Python. Saiba mais em < https://spacy.io/usage/visualizers/#ent >.

	html = spacy.displacy.render(doc, style="ent")
	output_path = open("entidades_nomeadas.html", "w", encoding="utf-8")
	output_path.write(html)
	output_path.close()
'''