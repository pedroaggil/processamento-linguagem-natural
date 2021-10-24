# Processamento de Linguagem Natural

A PLN consiste em, essencialmente, instruir o computador a lidar com a língua, ou como se diz informalmente, a "ler e escrever".

##

Pode-se notar como algumas das ferramentas cotidianas trazidas por este setor, multidisciplinar entre computação e linguística, a:
  * Interpratação de textos;
  * Tradução automática;
  * Revisão gramatical;
  * Busca de respostas para perguntas/chatbox;
  * Sumarização (resumo de textos);
  * Auxílio a escrita e a aprendizado de línguas;
  * E muitas outras.
  
  ##
  
 A Língua Natural é a língua humana - que está em oposição às línguas artificiais (como as de programação, matemática, lógica etc).
 Há diferenças entre língua e linguagem. Destacam-se:
  * Linguagem: capacidade humana de comunicação e suas manifestações verbais (ou não), como a fala, gestos, música, dança, pintura, sorriso etc. Envolve o aparato físico e mental/cognitivo.
  * Língua: código de comunicação utilizado por uma comunidade, com suas regras específicas (citam-se exemplos o português, inglês, LIBRAS etc).
  
 É, portanto, correto estabelecer a PLN como o "Processamento de **Língua** Natural" (ao invés do uso de *Linguagem*)? Não necessariamente.
 No Brasil, que é falante da língua portuguesa, ambos os termos são corretos; afinal, o termo vem do inglês "language" e, por este motivo, está sendo mantido essa tradução.
 Contudo, o uso de "língua" ainda é mais adequado à PLN por ela trabalhar com o código, e não com a habilidade em si.
 
 Ela pode ser chamada ainda de:
  * Linguística Computacional
  * Mecanolinguística
  * Processamento de Dados e Linguagem Automática
  * Engenharia das Línguas Naturais
  * E outras ainda. Todas estão corretas.
 
 ##
 
 A PLN é tradicionalmente visto como uma subárea da Inteligência Artificial & Computação, visto que a habilidade linguística é um tipo de inteligência.
 
 Ela nasceu durante a Segunda Guerra Mundial quando houve a necessidade de traduzir, automaticamente, as ordens nazistas para uso dos Estados Unidos - tais como estratégias, alvos etc.
 Recomenda-se assistir o filme **"Jogo da Imitação"**.
 
 Ela se desenvolveu a partir de então com a globalização, internet, tecnologia da informação, com o advento da Google e por aí vai.
 
 Recentemente, cita-se a web, redes sociais, smartphones, big data e ciência de dados e deep learning.
 
 ##

A PLN vem para auxiliar as tarefas humanas. Ela ainda não substitui o humano - não é possível, por enquanto, "automatizar" toda a língua, apenas alguns de seus aspectos.
O computador ainda é uma máquina estúpida (eles fazem somente o que os humanos mandam fazer)!

"Conversar" com uma máquina não é mais tão difícil - fazer a máquina "entender", contudo, ainda o é (talvez até mesmo impossível).

A sugestão de possíveis sinônimos, revisão ortográfica e gramatical e outros softwares são exemplos de programas úteis para a PLN.

##

De forma básica, é necessário para entender uma língua:
  * O conhecimento de palavras e como são formadas;
  * O significado das palavras;
  * Como referenciar entidades do mundo;
  * Como conectar frases;
  * Protocolos de comunicação na língua/cultura
  * Etc.
  
A língua possui vários níveis de conhecimento. São tradicionalmente distinguidos em PLN, apesar dos limites entre eles serem nebulosos na maioria dos casos.

Serão focados neste projeto a:
  * Semântica (significado da palavra);
  * Sintaxe (como as sentenças são formadas, como as palavras podem se combinar);
  * Morfologia (como a palavra é construída, os componentes de formação).

Os níveis de conhecimento precisam ser representados (formalizados) e manipulados automaticamente.

Os humanos lidam naturalmente com ambiguidade, irregularidade, vagueza, variedade etc., mas as máquinas ainda não.

Ferramentas:

		* Segmentadores textuais: palavras (tokenizador), sentenças, parágrafos, tópicos
		* Stemmers, lematizadores, nominalizadores
		* Etiquetadores morfossintático (taggers)
		* Analisadores sintáticos shallow (chunkers) e deep (parsers)
		* Analisadores semânticos e discursivos
		* Alinhadores textuais: lexicais, sentenciais etc.
		* Concordanceadores, word counting, ...
		* Classificadores de polaridade
		* etc.
    
##

* Polissemia: palavras diferentes mas com escrita/fonética semelhantes/idênticas, mas com algo em comum

Exemplo: as variações da palavra BANCO, como o banco (assento), banco de sangue, banco de areia, banco (relativo à instituição financeira), banco de provas etc.

É uma polissemia visto que todas abrangem uma semelhança, que é o DEPÓSITO. Todas são relativas a um depósito: depósito de dinheiro, de sangue, de areia, de provas, de humanos (no caso do assento) etc.

É a mesma palavra, mas dependendo do contexto são diferentes, embora com uma base comum.

* Homonímia: palavras diferentes mas com escrita/fonética semelhantes/idênticas.

Exemplo: a palavra "manga", que pode ser uma fruta ou um item de uma camisa/camiseta.

É uma homonímia pelo fato de não identificarmos uma primitiva de significado em comum para elas; são a mesma palavra, mas dependendo do contexto são absolutamente diferentes.

Muitas vezes, não conhecemos a origem das palavras - nesse caso, a palavra "manga" pode ter uma primitiva e significado que até então desconhecíamos, e neste momento a PLN deverá se atualizar ao fato. Isso se dá por a história ter se perdido ao longo do tempo, sendo possível recuperá-las em algum momento por N motivos.
