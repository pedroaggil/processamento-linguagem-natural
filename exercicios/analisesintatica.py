import spacy

nlp = spacy.load("pt_core_news_lg") # Referente ao pacote de linguagem baixado
doc = nlp(palavras)

sintatica = [(token.orth_, token.dep_) for token in doc] # Faz uma análise sintática de cada token

'''
Outra função importante do spaCy é a representação sintática do texto (ele mostra as relações entre os tokens).
O atributo dep_ retorna a dependência do token em questão.
Guia:
	
	- acl: modificador clausal do substantivo;
	- acomp: complemento adjetival;
	- advcl: modificador adverbial clausal;
	- advmod: modificador adverbial;
	- agent: agente (passivo);
	- appos: edição aposicional;
	- attr: atributo;
	- aux: verbo auxiliar;
	- auxpass: verbo auxiliar (passivo);
	- case: marcador de caixa;
	- cc: conjunção coordenativa;
	- ccomp: complemento clausal;
	- compound: palavra composta;
	- conj: conjunto;
	- csubj: sujeito da oração;
	- csubjpass: sujeito da oração (passivo);
	- dative: dativo;
	- dep: dependente não classificado;
	- det: determinativo;
	- discourse: elemento do discurso;
	- dobj: objeto direto;
	- expl: palavrão;
	- mark: marcador;
	- meta: meta dados;
	- neg: edição de negação;
	- nmod: modificador nominal;
	- npadvmod: frase nominal como modificador adverbial;
	- nsubj: sujeito nominal;
	- nsubjpass: sujeito nominal (passivo);
	- oprd: predicado de objeto;
	- parataxis: parataxe;
	- pcomp: complemento de preposição;
	- pobj: objeto de preposição;
	- poss: edição de posse;
	- preconj: conjunção pré-correlativa;
	- predet: predeterminante;
	- prep: edição preposicional;
	- prt: partícula de verbo;
	- punct: pontuação;
	- qmod: edição quantitativa;
	- relcl: modificação de cláusula relativa;
	- root: raiz;
	- vocative: edição vocativa;
	- xcomp:  complemento de oração aberta

Visualize graficamente essa relação com o displaCy! Use da seguinte forma:

	sintGraf = spacy.displacy.render(doc, style='dep')
	op = open("sintaxe_grafica.svg", "w", encoding="utf-8")
	op.write(sintGraf)
	op.close()
'''