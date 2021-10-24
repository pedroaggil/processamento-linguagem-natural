# spaCy

É uma biblioteca Python para processamento de textos (tal como em NLTK) em escala industrial (feito para uso em produção - diferentemente do NLTK), ou seja, criações de aplicações que conseguem processar um grande volume de dados. Tem suporte para mais de 61 linguagens e possui o parser sintático mais rápido do mundo (segundo estudos de 2015). Atualmente está na versão 3.1.3. Além disso, tem acurácia de 92,6% em seus resultados.

##

Para instalá-lo, é necessário ter previamente instalado o Python versão igual ou superior à 3.6 (no momento atual, a versão mais recente é a 3.10). Após isso, a instalação é comum às plataformas Linux, Windows e MacOS, sendo através de linha de comando usando de, por exemplo, o pip. São recomendadas 3 linhas pelos desenvolvedores:

	pip install -U pip setuptools wheel
	pip install -U spacy
	pip install -U spacy-lookups-data
	python -m spacy download pt_core_news_md

### Modelo de linguagem

Para o spaCy conseguir realizar suas funções, é necessário que um modelo de linguagem esteja presente. Na última linha, é adicionado um modelo disponível para o português (entre os três nessa condição) e para alterá-los, é possível mudar os dois últimos caracteres por lg caso opte por maior precisão em detrimento da eficiência/desempenho; ou por md caso opte por algo balanceado entre eficiência/acurácia. São siglas do inglês para pequeno (sm), médio (md) e grande (lg). Todos eles são baseados no corpus WikiNER (então encontra-se aqui vetores de tokens e classes gramaticais, análise de dependência, entidades nomeadas etc).

É também necessário (tal como em NLTK), o download posterior de dados adicionais ao pacote. Exemplo; dados adicionais para lematização.
	
### Uso

Para o uso das funções poderosas do spaCy, é preciso entender dois objetos importantes: o Doc e o Token.

Doc: é uma sequência de objetos Token, ou seja, um documento com vários tokens manipuláveis. Métodos da classe Doc levam em consideração a manipulação desses tokens; exemplo: quantidade de tokens no documento.

Token: é o mesmo token que aprendemos em NLTK: pode ser uma palavra, pontuação, número, espaço etc.

Assim como outras bibliotecas, para usar o spaCy é necessário que a ferramenta seja incluída no projeto, usando do import. Além disso, é necessário dois outros comandos:

	import spacy

	nlp = spacy.load("pt_core_news_md")
	doc = nlp(palavras) # Texto não tokenizado

A primeira linha é simples: o framework foi importado para o projeto. A partir daí, foram criadas duas variáveis referentes a, a primeira que armazena o modelo de linguagem, e a segunda que armazena o TEXTO - e não os tokens!

Essa é uma informação importante: no NLTK, é utilizado sempre a lista de tokens, mas no spaCy o parâmetro é sempre a string do texto. Portanto, todas as funções, aqui, são provenientes da variável doc.

Aqui, vamos começar a usar as funções mais interessantes do spaCy: tokenização, stemming e lematizador, etiquetador e entidades nomeadas. Utilizaremos um corpus padrão. É claro que o spaCy tem muitas outras funções ainda. Faremos um procedimento parecido com o que foi feito em NLTK, sendo possível comparar as ferramentas de forma fácil. Existem muitas formas de realizar esses procedimentos em spaCy, mas foram escolhidos os métodos mais simples.

##

### Tokenização

Para recuperar os tokens, basta usar o conceito de list comprehension:

	tokens = [token for token in doc]

A tokenização já está pronta em spaCy! Basta "caminhar" sobre ela com um for; declará-las.

CUIDADO! Os elementos dessa lista não são strings. A biblioteca trabalha sobre o objeto Token (próprio do spaCy), e não deve ser trabalhado como string.

Para recuperar o texto, usa-se do atributo orth_, da seguinte forma:

	tokens = [token.orth_ for token in doc]

O objeto token reconhece números, símbolos, pontuações, letras e outros e, ainda, é possível retornar esse tipo, recuperar apenas as palavras/números/pontuações. Para isso, basta realizar, ainda na última estrutura, um teste lógico pedindo por isso, usando dos atributos abaixo; veja um exemplo onde é retornado apenas pontuações:

- Somente as palavras: is_alpha
- Somente os números: is_digit
- Somente as pontuações: is_punct

		pontuacoes = [token.orth_ for token in doc if token.is_punct]
			>> [',', '.', ';', '.', '.', ...]


Em NLTK, esse processo é feito de uma forma muito mais complexa, a partir de expressões regulares. O spaCy tem uma forma nativa para realizar esse procedimento, facilitando muito o desenvolvimento.

Entre outros, estão presentes também os itens que serão retornados do objeto Token, tais como a pontuação esquerda ou direita (no caso de parênteses, chaves e colchetes por exemplo), espaços, simbolos financeiros, números, e-mail, stopwords etc.

##

### Stemming e lematização:

Como citado anteriormente, ao contrário do NLTK, o spaCy tem um lematizador padrão para o português - porém, ainda ao contrário do NLTK, ele não tem um stemmer padrão.

Ainda assim, lematizar em spaCy é simples, bastando usar o atributo lemma_, tal como no exemplo:

		lemmas = [token.lemma_ for token in doc if token.pos_ == 'VERB']
			>> ['saltar', 'deixar', 'ficar', 'veem', 'fazer']

A lematização se refere, no spaCy, à forma canônica do verbo (embora seja útil para todas, o framework decidiu reduzir sua funcionalidade somente para essa classe); foi passado como parâmetro, em consequência disso (a partir do atributo pos_), que fosse selecionado apenas os verbos (visto que a etiqueta de verbo, em spaCy, é 'VERB').

##

### Etiquetador:

As etiquetas, tais como os outros itens já citados, também pode ser acessada a partir de um atributo - e, como é de se esperar (devido à lematização, onde esse atributo foi usado), o atributo em questão é o pos_. Basta chamar o atributo em um token e nos é retornado a classe gramatical relativa a ele; exemplo:

		etiq = [(token.orth_, token.pos_) for token in doc] # list comprehension
			>> [('O', 'DET'), ('pescoço', 'NOUN'), ('e', 'CCONJ'), ('a', 'DET'), ('cauda', 'NOUN'), ('de', 'ADP'), ('Queen', 'PROPN'), ('saltam', 'VERB'), ('de', 'ADP'), ('seu', 'DET'), ('corpo', 'NOUN'), (',', 'PUNCT'), ('deixando', 'VERB'), ('suas', 'DET'), ('pernas', 'NOUN'), ('e', 'CCONJ'), ('torso', 'NOUN'), ('para', 'ADP'), ('trás', 'ADV'), ('.', 'PUNCT'), ('Todos', 'DET'), ('os', 'DET'), ('presentes', 'NOUN'), ('no', 'ADP'), ('Palco', 'PROPN'), ('Principal', 'PROPN'), ('(', 'PUNCT'), ('Izou', 'PROPN'), (',', 'PUNCT'), ('Marco', 'PROPN'), (',', 'PUNCT'), ('Kawamatsu', 'PROPN'), (',', 'PUNCT'), ('Chopper', 'PROPN'), (',', 'PUNCT'), ('Hyo', 'PROPN'), (',', 'PUNCT'), ('e', 'CCONJ'), ('Yakuzas', 'PROPN'), (')', 'PUNCT'), ('estão', 'AUX'), ('chocados', 'ADJ'), ('.', 'PUNCT'), ('Eles', 'PRON'), ('ficam', 'VERB'), ('com', 'ADP'), ('cara', 'NOUN'), ('de', 'ADP'), ('Enel', 'NOUN'), ('quando', 'ADV'), ('veem', 'VERB'), ('o', 'PRON'), ('que', 'PRON'), ('Queen', 'PROPN'), ('fez', 'VERB'), ('.', 'PUNCT')]

A lista de etiquetas está no site < https://universaldependencies.org/docs/u/pos/ >, mas deixarei um pequeno guia:

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

Além disso, o spaCy tem um atributo que contém uma análise morfológica - ou seja, informações mais detalhadas: o morph.

		etiq = [(token.orth_, token.morph) for token in doc]
			>> [('O', Definite=Def|Gender=Masc|Number=Sing|PronType=Art), ('pescoço', Gender=Masc|Number=Sing), ('e', ), ('a', Definite=Def|Gender=Fem|Number=Sing|PronType=Art), ...]

Pode-se citar entre as características detalhadas o genêro, se é singular ou plural, a pessoa (1°, 2° ou 3°), o tempo (passado, presente, futuro etc.), se é artigo e várias outras, a depender de cada token.

Sobre o etiquetador, o modelo de linguagem para o português usado no spaCy tem como fonte o Bosque; a acurácia desse modelo é de mais de 95% (quando usado o pacote de linguagem grande).

Existem outros etiquetadores para o português que alcançam uma maior acurácia - no caso, o NLPNet (gratuito) com 97,33% e o PALAVRAS (pago), com 98%. É importante frisar que esses etiquetadores são plenamente focados no português. Mais informações sobre o NLPNet podem ser acessadas a partir dos links: < http://nilc.icmc.usp.br/nlpnet/intro.html > e < https://github.com/erickrf/nlpnet >.

##

### Entidades Nomeadas:

No NLTK, haviam diversas dificuldades para encontrar corretamente essas entidades, sendo que vimos como descobrí-las a partir de ngramas e por chunks. Contudo, o spaCy também facilita essa operação, além de ser mais assertivo. Para acessar esse recurso, faz-se uso da propriedade ents na variável doc. Segue:

		entidades = list(doc.ents)
			>> [Queen, Palco Principal, Izou, Marco, Kawamatsu, Chopper, Hyo, Yakuzas, Enel, Queen]

É digno de nota que, mesmo que retirada a primeira letra maiúscula de alguma das palavras no parentêses, ainda é considerada uma entidade nomeada, como no caso de yakuzas. Até mesmo "Enel" (por exemplo), dado como substantivo comum na etiquetação, foi considerado assertivamente como uma EN.

Para descobrir mais alguns detalhes sobre cada entidade, pode-se usar do atributo label_, como no seguinte exemplo:

		entidades = list(doc.ents)
		detalhesEnt = [(entidade, entidade.label_) for entidade in doc.ents]
			>> [(Queen, 'ORG'),
			(Palco Principal, 'LOC'),
			(Izou, 'LOC'),
			(Marco, 'LOC'),
			(Kawamatsu, 'LOC'),
			(Chopper, 'LOC'),
			(Hyo, 'LOC'),
			(Yakuzas, 'LOC'),
			(Enel, 'PER'),
			(Queen, 'ORG')

Guia:
- ORG: organização;
- LOC: localização;
- PER: pessoa;
- DATE: data;
- MISC: genérico

Nota-se que, de modo geral, a assertividade dessa identificação é alto; não foi tão eficiente nesse caso devido ao fato de os nomes forem de outro idioma (distinto ao português e inglês) e/ou emblemáticos (como no caso do Queen, por exemplo). Parte desses erros se dá ao fato de o pacote utilizado ser o médio, e não o grande (completo). No pacote grande, a acurácia é de mais de 91%.

É possível visualizar graficamente as EN por meio do displaCy. Essa visualização se dá a partir de HTML, ao gerar um documento desse tipo e escrever nele com Python. No Colab, esse arquivo pode ser aberto pela aba do Drive, sendo que deve-se fazer o download do arquivo e abri-lo localmente.

		html = spacy.displacy.render(doc, style="ent")
		output_path = open("entidades_nomeadas.html", "w", encoding="utf-8")
		output_path.write(html)
		output_path.close()

O layout pode ser modificado como preferir. Saiba mais em < https://spacy.io/usage/visualizers/#ent >.

##

### Análise Sintática:

Outra função importante do spaCy é a representação sintática do texto (ele mostra as relações entre os tokens). O atributo dep_ retorna a dependência do token em questão. Segue, após o exemplo, um guia sobre as etiquetas usadas (lembrando que estão disponíveis no link < https://emorynlp.github.io/nlp4j/components/dependency-parsing.html >).

		sintatica = [(token.orth_, token.dep_) for token in doc]
			>> [('O', 'det'), ('pescoço', 'nsubj'), ('e', 'cc'), ('a', 'det'), ('cauda', 'conj'), ...]

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

Ainda com o uso do displaCy, é possível visualizar graficamente essa representação.

		sintGraf = spacy.displacy.render(doc, style='dep')
		op = open("sintaxe_grafica.svg", "w", encoding="utf-8")
		op.write(sintGraf)
		op.close()

### DisplaCy:

O spaCy contém dois sites onde podem ser feitas as análises de entidades nomeadas e de dependências de forma bem simples: < https://explosion.ai/demos/displacy-ent > e < https://explosion.ai/demos/displacy >. Basta selecionar o modelo para português (ou outro idioma qualquer) e brincar!
