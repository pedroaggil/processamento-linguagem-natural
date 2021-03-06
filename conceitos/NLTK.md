# Natural Language Toolkit - NLTK

NLTK é uma sigla que significa "Natural Language Toolkit"; é uma biblioteca Python com diversas ferramentas essenciais para a utilização dos princípios da PLN; suas principais funcionalidades estão voltadas para a manipulação de strings, com interfaces padrões para realizar tarefas como etiquetar textos, frequência de palavras, lematização e stemmização de palavras, entre vários outros. Pode ser acessada pelo site oficial, no URL < https://www.nltk.org/index.html >. Quanto ao "toolkit" citado em seu acrônimo, pode-se exemplificar entre seus itens estruturas como corpus (conjunto de textos), classificadores, anotações de corpus e diversos métodos que nos auxiliam a trabalhar com PLN.

##

Para ser instalado, requer ao menos a versão 3.6 do Python previamente instalada em seu sistema, sendo possível instalá-la em OS como Linux, MacOS e Windows. Note que no Google Colab, o NLTK vêm instalado por padrão e, portanto, esse passo deve ser pulado na plataforma.

Após instalar, importe-a para seu projeto com a função import, da seguinte maneira:
	
	import nltk

Além disso, é importante ressaltar que você, dessa forma, baixou apenas o núcleo da biblioteca; os dados ainda faltam. Para baixá-los, você usa a função download(), dessa forma:

	nltk.download()

No Windows, é aberta uma janela, enquanto no colab é uma tela de texto. Contudo, o procedimento é semelhante. Você lista, a partir do comando oferecido, os itens possíveis de serem baixados. Para instalá-los, basta digitar sua chave (mostrada na lista) ou baixar tudo de uma vez, com a chave 'all'. Para baixar, antes deve-se, tal como ao listar, indicar que quer baixar os itens, com a função de download. Assim que aparecer a mensagem "Done downloading collection all", feche com 'quit' e estará tudo pronto.

##

Para acessar funções da biblioteca, usa-se estrutura parecida com a de eventos DOM em JavaScript: a.b.c.d(), ou seja, você destrinchará um objeto até chegar ao objeto que se queira manipular com determinado método. Ao acessarmos essas funções através dessa árvore, estamos manuseando módulos dentro de uma biblioteca. Exemplo:
```
nltk.corpus.mac_morpho.words()
		>> ['Jersei', 'atige', 'média', 'de', 'Cr$', '1,4', ...]
```

Essa função pega um caminho do NLTK, ou seja, o corpus, que o leva para todos os corpus disponíveis. Entre eles está o mac_morpho, usado no exemplo. Esse corpus será manipulado pela função words(), que lista as palavras de uma string. O mac_morpho, como arquivo, será listado todas as palavras em seu conteúdo como uma lista. Isso abre margem para, por exemplo, o uso da função len() para saber quantas palavras há neste documento. Exemplo:

	len(nltk.corpus.mac_morpho.words())
		>> 1170095

Sim, nesse arquivo há mais de um milhão de palavras.

##

Paralelas à função words(), que exibe as palavras, existem muitas outras - tais como a sents(), que lista todas as sentenças, tagged_words(), que exibe a etiquetação morfosintática de cada palavra etc.

	nltk.corpus.mac_morpho.sents()
		>> [['Jersei', 'atinge', 'média', 'de', 'Cr$', '1,4', 'milhão', 'em', 'a', 'venda', 'de', 'a', 'Pinhal', 'em', 'São', 'Paulo'], ['Programe', 'sua', 'viagem', 'a', 'a', 'Exposição', 'Nacional', 'do', 'Zebu', ',', 'que', 'começa', 'dia', '25'], ...]

Nota-se que cada sentença está em uma lista própria, sendo o resultado uma lista de listas.

Como lista, seu conteúdo pode ser acessado por índices. É possível exibir a sentença 68 separadamente. Exemplo:

	nltk.corpus.mac_morpho.sents()[67] # Note que é um número aleatório, mas poderia não ser.
		>> ['Com', '5.774', 'unidades', 'comercializadas', 'em', 'esse', 'primeiro', 'trimestre', ',', 'a', 'previsão', 'é', 'de', 'vender', '28', 'mil', 'em', '94']

A função tagged_words(), contudo, cria uma lista de tuplas onde cada palvra é exibida junto à sua etiqueta morfosintática (substantivos, adjetivos, pronomes etc.), no seguinte formato: [('palavra', 'e'), ...].

	nltk.corpus.mac_morpho.tagged_words()
		>> [('Jersei', 'N'), ('atinge', 'V'), ('média', 'N'), ...]

No modelo, 'e' se referia à etiqueta; no teste prático, contudo, foram mostradas algumas etiquetas como a 'N' e 'V', que significam, respectivamente, substantivo e verbo. Elas estão com essas letras devido à origem inglesa da palavra, sendo 'substantivo' vindo de 'noun' e 'verbo', de 'verb'.

Outro exemplo é ainda a função tagged_sents(), onde é exibido uma lista de listas de tuplas - ou seja, uma lista com todas as sentenças que, por sua vez, é dividido por tuplas que exibem a etiquetação de cada palavra. Modelo: [[(), (), ...], [(), (), ...], ...].

Ao longo desta aula, serão abordados conceitos importantes para o NLTK, como as funções de tratamento de textos. Entre elas, cita-se a tokenização, frequência/contagem de palavras, stopwords, n-gramas, stemmer e lemma e etiquetadores. Para testá-las, será feito uso do corpus teste (disponível no Moodle).

##

### Tokenização:

Tokenizar é separar as palavras do texto, tipo um split() (embora o split() não seja tão eficiente quanto essa função em relação à PLN, como por exemplo ao pegar pontuações, visto que pontuações são consideradas tokens). O nível linguístico lexical de um token consiste em uma palavra, número ou pontuação - logo, agora esses itens são tratados como "tokens". Dado o texto que será tokenizado, basta usar a função nltk.word_tokenize(string). Exemplo:

		import nltk
		texto = 'O jogador que está de camiseta verde, marcou o gol da vitória!'
		nltk.word_tokenize(texto) # Inseri uma variável, mas é possível fazer diretamente com o uso de strings
			>> ['O', 'jogador', 'que', 'está', 'de', 'camiseta', 'verde', ',', 'marcou', 'o', 'gol', 'da', 'vitória', '!']

Conforme já comentado, os módulos são acessados de diversas maneiras, como por exemplo no seguinte código:

		nltk.tokenize.RegexpTokenizer(regex)

Essa estrutura será comentada em sequência

Contudo, realizar esse procedimento é cansativo e pode ser simplificado ao importar um módulo em determinado momento de seu texto para poder acessá-lo mais facilmente em outros momentos de seu código, usando do método import. Segue a estrutura necessária para usá-lo, no mesmo exemplo:

		from nltk.tokenize import RegexpTokenizer

Dessa forma, é possível acessar o módulo RegexpTokenizer diretamente sem a necessidade de citar seu caminho (no caso, o 'nltk.tokenize') em todos os momentos. Essa estrutura será usada em diversos momentos.

O tokenizador do NLTK pode ter algumas variações, como por exemplo, retornar apenas os tokens sem as pontuações - aqui, entramos em expressões regulares. Expressões regulares são, essencialmente, uma "mini linguagem de programação" especializada e incluida no Python, disponível através do módulo RegEx (que vem de 'regular expression', inglês para o termo citado) da linguagem. Contudo, diversas linguagens incluem algum módulo para expressões regulares, não sendo exclusivo ao Python. Embora úteis, podem ser complexas e de difícil compreensão e manutenção.

		from nltk.tokenize import RegexpTokenizer # Importe a RegEx no pacote tokenize do NLTK
		tokenizer = RegexpTokenizer(r'\w+') # Essa função recebe a expressão regular

O padrão de construção é (r'').
\w+ significa algo como selecionar qualquer letras, underline e números com uma ou mais ocorrências (ou seja, seleciona o grupo).

		tokens = tokenizer.tokenize(texto)
		print(tokens)
			>> ['O', 'jogador', 'que', 'está', 'de', 'camiseta', 'verde', 'marcou', 'o', 'gol', 'da', 'vitória']

Caso o objetivo seja tokens sem pontuações e numerais, usaríamos:

		texto = 'O jogador que está com a camisa 10, marcou o gol da vitória!'
		from nltk.tokenize import RegexpTokenizer
		tokenizer = RegexpTokenizer(r'[A-z]\w*')

Essa expressão seleciona um conjunto de caracteres (no caso, letras maiúsculas e minúsculas de A a Z).

		tokens = tokenizer.tokenize(texto)
		print(tokens)
			>> ['O', 'jogador', 'que', 'está', 'com', 'a', 'camisa', 'marcou', 'o', 'gol', 'da', 'vitória']

Existem diversas expressões regulares. Mais delas no link < https://www.w3schools.com/python/python_regex.asp >, sendo que no link < https://pythex.org/ > é possível testar suas expressões regulares.

##

### Frequência/contagem

Com a lista de tokens, é possível fazer a contagem de ocorrência de tokens pelo NLTK, usando da classe FreqDist(). Ademais, a função most_common ordena a frequência dos tokens. Pode ser usado um argumento para informar a quantidade de tokens mais comuns. Exemplo:

		tokens = nltk.word_tokenize(texto)
		frequencia = nltk.FreqDist(tokens)
		frequencia.most_common() # O parâmetro citado viria aqui

Ele mostraria um "pódio" composto pela quantidade especificada (parâmetro), com os tokens mais citados

Ao contar a incidência de tokens, eles levam em consideração que letras maiúsculas e minúsculas são diferentes e, portanto, tokens com essa única diferença (mesmo que sejam a mesma palavra) não são iguais, e as contam separadamente. Isso acontece quando uma palavra aparece no início de uma sentença, por exemplo, onde é obrigatório o uso de letras maiúsculas segundo as normas gramaticais. Visando evitar esse erro, é possível usar o seguinte método:

		tokens = nltk.word_tokenize(texto) # Texto tokenizado

		nova_lista[] # Lista onde será armazenado o texto modificado
		for token in tokens:
		# Para cada token dentro do texto...
			nova_lista.append(token.lower())
			# ... inclua ao final da lista o mesmo token com todas as letras minúsculas

##

### Stopwords:

São as palavras que podem ser consideradas irrelevantes para determinado objetivo; costumam ser consideradas stopwords artigos, preposições, conjunções etc. que, mesmo que mantenham extrema utilidade para a compreensão de uma sentença, não servem para, por exemplo, determinadas análises de textos. Para evitar contabilizar as stopwords, usa-se de métodos que as desconsideram no texto; exemplo:

		nltk.corpus.stopwords.words('portuguese')

Esse código lista diversas stopwords da língua portuguesa.

Para remover stopwords de um texto, usa-se de, por exemplo, o seguinte método:

		from nltk.tokenize import RegexpTokenizer

		tokenizer = RegexpTokenizer(r'[A-z]\w*') # Essa regex ignora números, símbolos e underscore
		tokens = tokenizer.tokenize(corpus)
		stopwords = nltk.corpus.stopwords.words('portuguese')

		lista = []
		for token in tokens:
			if token.lower() not in stopwords:
				lista.append(token.lower())

Esse código agrupa todos os tokens que não sejam números, símbolos e underscores, coloca todos em caixa baixa e depois realiza o seguinte teste lógico: se o token não for uma stopword, imprima ele ao final da lista (em caixa baixa); caso contrário, o token é ignorado. Isso basicamente elimina artigos, conjunções, preposições, pontuações, símbolos, underlines e tudo o que não seja considerado relevante para ser considerado. O texto a ser analisado torna-se consideravelmente menor e mais simples. Lembrando que o texto em questão é um corpus armazenado na variável 'corpus'. Contudo, é possível substituir esse código para um mais avançado e menor. Segue:

		from nltk.tokenize import RegexpTokenizer

		tokenizer = RegexpTokenizer(r'[A-z]\w*') # Essa regex ignora números, símbolos e underscore
		tokens = tokenizer.tokenize(corpus)
		stopwords = nltk.corpus.stopwords.words('portuguese')

Até aqui, nada mudou; a mudança começa na próxima etapa:

		lista = [token.lower() for token in tokens if token.lower() not in stopwords]
		
Traduzindo a linha acima: dentro da lista haverá todos os tokens que estiverem no corpus, exceto stopwords. É basicamente a mesma lógica e estruturas usadas no último exemplo, mas de forma reduzida através do conceito de list comprehension.

##

### N-gramas:

N-gramas são palavras que "acontecem juntas": exemplo é uma entidade nomeada do texto, como por exemplo o nome de organizações, pessoas, eventos etc. "Pedro Antonio" é uma entidade nomeada que leva dois nomes que "acontecem juntos", são a mesma coisa, um nome composto. "São Paulo", "XV Prêmio Econoteen de Ensaios", "Processamento de Linguagem Natural" e "The Witcher" são outros exemplos. Todas essas são n-gramas. "Pedro Antonio", "São Paulo" e "the Witcher" são bigramas (2-gramas), "Processamento de Linguagem Natural" é um trigrama (3-grama) e "XV Prêmio Econoteen de Ensaios" é um quadrigrama (4-grama), além de existirem muitos outros.	Com a lista de tokens, é possível ter os n-gramas necessários para qualquer análise.

- Bigramas: from nltk import bigrams
- Trigramas: from nltk import trigrams
- Quadrigrama ou mais: from nltk import ngrams

Ou seja, são análogos a janelas onde são feitas uma conexão entre os tokens com o token que virá em sequência, avançando no formato especificado (pares, trios, quádruplos etc), como no exemplo:

		texto = "Com um passe de Eli Manning"
		from nltk import bigrams
		list(bigrams(tokens)) # já com o texto tokenizado
		list
			>> [('Com', 'um'), ('um', 'passe'), ('passe', 'de'), ('de', 'Eli'), ('Eli', 'Manning')]

Conforme visto, todas as palavras são consideradas bigramas neste exemplo. Aqui, fora usada a especificação 'bigram', mas pode ser feito com trigrams e ngrams da mesma forma, mudando apenas a referência (deve-se ter importado o módulo e o método na listagem muda conforme o pedido). A exceção fica em ngrams, que deve-se listar um parâmetro a mais se comparado aos demais além do texto tokenizado, que é o tamanho do ngram. Nota-se que em bigram e trigram já é especificado o tamanho, que são respectivamente 2 e 3, contudo, em ngram não há esse parâmetro oculto, devendo especificá-lo da seguinte maneira:

			from nltk import ngrams
			list(ngrams(tokens, n)) # n >= 4

Contudo, foi citado como uma utilidade possível para essa ferramenta o reconhecimento facilitado de entidades nomeadas entre tokens. Segue uma forma de realizar esse procedimento:

		from nltk import bigrams
		from nltk import trigrams

		bigramas = list(bigrams(tokens))
		trigramas = list(trigrams(tokens))

		for bigrama in bigramas:
			if bigrama[0][0].isupper() and bigrama[1][0].isupper():
				print(bigrama)

Lembre-se que: dentro de listas, tuplas, dicionários, strings etc. há um sistema de níveis baseados em índices que são referências aos elementos. Exemplo: ao entrar em uma lista comum, o primeiro elemento é, por exemplo, uma palavra. Em uma lista de listas, o primeiro elemento é uma lista - e assim continuamente. Quanto mais "níveis", mais distante o índice estará de um caractere específico de um token. Porém, para contornar isso, pode-se referenciar o índice de um índice - e assim continuamente², visando ultrapassar essa "barreira".

Para traduzir o código, deve-se ter em conta que, no for, eu acessei o primeiro nível ao declará-lo: a lista contida na variável 'bigramas' foi acessada e o for está "caminhando" por seus elementos, ao qual eu chamei de 'bigrama' - ou seja, o nível um. Contudo, como trata-se de uma lista de tuplas, há ainda mais dois níveis possíveis (aquele que acessa o elemento dentro da tupla, e aquele que acessa o elemento dentro do elemento da tupla - no caso, o caractere de uma palavra, de um token). Como esse nível já foi acessado, o primeiro índice não deve ser declarado, visto que ele já foi acessado, está oculto na lógica do sistema (no caso de uma lista de tuplas, como no exemplo, o for está caminhando entre as tuplas). A partir daí, segue:

Para cada tupla dentro de bigramas, teste se o primeiro caractere do primeiro e do segundo token dessa tupla têm a letra maiúscula (ou seja, se a primeira letra das palavras é maiúscula - esse teste é realizado a partir da função isupper()). Caso o seja, imprima esse bigrama (em que ambas as palavras são destacadas com a primeira letra maiúscula) na tela.

Veja que essa lógica tem falhas nítidas: existem entidades nomeadas que tem apenas uma palavra. Existem aquelas que, mesmo que tenham duas ou mais, algumas delas não tem todas as primeiras letras maiúsculas (como no caso do próprio curso, que é "Python para Processamento de Linguagem Natural" - o 'para' está com letras minúsculas pois é uma stopword), e outras ainda, como no exemplo citado, que tem mais de duas palavras no nome. O sistema não retornará nenhum desses casos, e sim apenas aqueles em que tem duas palavras, e essas palavras devem ter as primeiras letras maiúsculas. Além disso, deve-se comparar os resultados pois o sistema pode considerar, entre esses bigramas, trigramas e ngramas - neste caso, muitos dos resultados obtidos seriam irrelevantes e inassertivos. Contudo, há como melhorar esse código de diversas formas, como ao tirar antes do teste lógico as stopwords, realizar mais de um teste lógico, onde é considerado trigramas e ngramas e por aí vai, mas não é o intuito apresentar todas as soluções possíveis para cada problema, e sim introduzir ao fato de que é possível essa solução, e como ela seria feita - através da lógica.

##

### Stemmer e Lemmatizer:

Stemming é uma técnica que consiste em reduzir a palavra ao seu radical; exemplo:
- amig: amigo, amiga, amigão, ...
- gat: gato, gata, gatos, ...
- prop: propõem, propuseram, propondo, ...

Lematizar é uma técnica que consiste em reduzir a palavra à forma canônica, levando em conta sua classe gramatical; exemplo:
- propor: propõem, propuseram, propondo, ...
- estudar: estudando, estudioso, estudei, ...

O NLTK tem implementato diversos algoritmos relativos a stemmer (tais como o RSLP, Porter, ISRI, Lancaster, Snowball etc). Por exemplo, RSLP é um acrônimo para Removedor de Sulfixos da Língua Portuguesa, e pode ser acessado da seguinte forma:

		stemmer = nltk.RSLPStemmer()
		stemmer.stem(palavra)

Alguns exemplos dele em execução; em alguns casos, mostra-se não tão eficiente, como nos exemplos de 'propuseram', 'propondo' e 'propõem' - nenhum método é 100% eficiente, afinal:

		stemmer.stem('amigão')
			>> 'amig'
		stemmer.stem('propuseram')
			>> 'propus'
		stemmer.stem('propõem')
			>> 'propõ'
		stemmer.stem('propondo')
			>> 'prop'

Quanto à lematização, o NLTK não foi implementado com um lematizador "bom o bastante" para nosso idioma; contudo, no próximo framework a ser estudado (spaCy), essa funcionalidade está disponível para a língua portuguesa. É possível testar essa função para o inglês usando, por exemplo, do instrumento "WordNet Lemmatizer"; exemplos:

		lemmatizer = nltk.stem.WordNetLemmatizer()
		lemmatizer.lemmatize(palavra, pos='e') # 'string', 'etiqueta' respectivamente

Exemplos dele em execução:

		lemmatizer.lemmatize('studied', pos='v')
			>> 'study'
		lemmatizer.lemmatize('studying', pos='v')
			>> 'study'

##

### Etiquetadores:

O NLTK possui dois corpus que servem como base para o etiquetador em português (sendo eles o "Floresta" e o "Mac Morpho"); para o inglês, já existe um etiquetador padrão treinado: o nltk.pos_tag(). Os etiquetadores passam primeiramente por uma fase de treinamento com as sentenças presentes:
- Floresta: 9266 sentenças etiquetadas;
- Mac Morpho: 51397 sentenças etiquetadas;
Como resultado, os etiquetadores retornam uma tupla composta pela seguinte estrutura; nela, a classe gramatical depende do treinamento que é realizado:

('palavra', 'classe gramatical')

Segue um exemplo do etiquetador no Mac Morpho em ação:

    from nltk.corpus import mac_morpho # Base para etiquetação
    from nltk.tag import UnigramTagger # Etiquetador

		tokens = nltk.word_tokenize(corpus_teste.read()) # Este é o texto que deverá ser etiquetado

		sentencas_treino = mac_morpho.tagged_sents() # Sentenças de treino para o UnigramTagger
		etiquetador = UnigramTagger(sentencas_treino) # O treinamento
		tags = etiquetador.tag(tokens) # A etiquetização

		print(tags)
			>> [('Giants', 'NPROP'), ('batem', 'V'), ('os', 'ART'), ('Patriots', None), ('no', 'KC'), ...]

O UnigramTagger traz a classe gramatical mais provável usando um token; exemplo: se 'substantivo' for a classe gramatical mais provável para 'casa', ele retornará que 'casa' é um substantivo.

A partir disso, segue a tradução do código: declarei as sentenças de treino, ou seja, as sentenças que vamos treinar (que são as sentenças que foram disponibilizadas no Mac Morpho - elas são acessadas pelo método tagged_sents()). Após isso, é declarado o etiquetador, que será composto pela função UnigramTagger(), que leva como parâmetro as sentenças de treino, para realizar o treinamento em si, usando de base a estatística dos tokens.

Assim, é passado os tokens que devem ser etiquetados através do método tag() para que seja realizado o processo (usando como base o córpus Mac Morpho para as etiquetas).

Quanto à tradução das classes gramaticais em si, as citadas em aula foram:
- [MODELO] ETIQUETA: nome da classe gramatical

		- V: verbo;
		- ART: artigo;
		- None: não há classe gramatical provável - isso indica que o sistema não reconhece o token, o que quer dizer que, no corpus usado para treino, não consta o respectivo token;
		- KC: conjunção coordenativa;
		- ADJ: adjetivo;
		- ADV: advérbio;
		- ADV-KS: advérbio conectivo subornativo;
		- ADV-KS-REL: advérbio relativo subornativo;
		- KS: conjunção subornativa;
		- IN: interjeição;
		- NUM: numeral;
		- PDEN: palavra denotativa;
		- PCP: particípio;
		- PROADJ: pronome adjetivo;
		- PRO-KS: pronome conectivo subordinativo;
		- PRO-KS-REL: pronome conectivo subornativo relativo;
		- PROPESS: pronome pessoal;
		- PROSUB: pronome substantivo;
		- CUR: símbolo de moeda corrente;
		- N: substantivo;
		- NPROP: substantivo próprio;
		- VAUX: verbo auxiliar;

	Por ter que passar por uma fase de treinamento, o etiquetador não consegue identificar e classificar todas as palavras; uma solução possível é pré-classificar todas as palavras do texto como substantivos (N) e depois treinar o etiquetador normalmente (usando do pacote DefaultTagger).

		from nltk.corpus import mac_morpho
		from nltk.tag import UnigramTagger
		from nltk.tag import DefaultTagger # Importando o pacote aqui

		tokens = nltk.word_tokenize(corpus_teste.read())

		etiq_padrao = DefaultTagger('N') # Declarando que o padrão é substantivo
		sentencas_treino = mac_morpho.tagged_sents()
		etiquetador = UnigramTagger(sentencas_treino, backoff=etiq_padrao) # Há um padrão a ser seguido!
		tags = etiquetador.tag(tokens)

		print(tags)
				>> [('Giants', 'NPROP'), ('batem', 'V'), ('os', 'ART'), ('Patriots', 'N'), ('no', 'KC'), ...]

	É possível manipular a lista de tuplas resultante de diversas formas, como com análises descritivas, análises sintáticas, chunking (reconhecimento de entidades nomeadas) etc.

	Para realizar o processo de chunking, usaremos de um método RegexpParser:

		from nltk.chunk import RegexpParser

		pattern = 'NP:{<NPROP><NPROP> | <N><N>}' # Padrão de Entidades Nomeadas
		analiseGramatical = RegexpParser(pattern) # Declarando o padrão
		arvore = analiseGramatical.parse(tags) # Passando o padrão junto ao texto previamente etiquetado
		print(arvore) # Exibindo a árvore
		# arvore.draw()
		# Essa função "desenha" a árvore, mas não é realmente necessária
			>> (S # Sentença; é a "raiz" da árvore
				Com/PREP
				um/ART
				de/PREP
				(NP Eli/NPROP Manning/NPROP) # Os pares pedidos foram separados dentro de tuplas
				(NP Plaxico/N Burress/N)
				a/ART
				39/NUM
				segundos/N
				do/NPROP
				fim/N

Traduzindo o código: o que esse código quer fazer é identificar entidades nomeadas. Qual a classe gramatical de uma entidade nomeada? Foi declarado como padrão para essa classe a combinação de dois substantivos ou de dois substantivos próprios (por quê substantivo comum também? Isso se dá pelo fato de algumas entidades no texto indicado estar em inglês que não é etiquetado no Mac Morpho, então ele acaba passando como substantivo comum devido ao DefaultTagger).

Para isso, foi declarado esse padrão dentro de NP:{} - NP vem do inglês e significa algo como sintagma nominal; após isso, esse padrão foi declarado dentro da RE e foi passado junto com o texto previamente etiquetado para ser exibido em seguida. A função draw() desenha a árvore no console (não funciona no Colab); basicamente, ela deixa uma linha horizontal para as palavras normalmente encontradas e cria ramificações gráficas para os pares encontrados.

##

## EXERCÍCIO DE FIXAÇÃO:

Faça uma análise descritiva completa do corpus de teste, utilizando as funções do NLTK.

	Exemplos de atributos:
		- Quantidade de tokens;
		- Quantidade de sentenças / média do tamanho das sentenças;
		- Quantidade de substantivos, adjetivos, advérbios etc.;
		- Quantidade de palavras com o mesmo radical;
		- Quantidade de símbolos de pontuação;
		- Palavras mais frequentes do corpus;
		- ...
