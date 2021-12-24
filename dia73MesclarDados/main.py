'''Como combinar um Notebook com HTML Markup.

Aplique as técnicas de fatiamento da Lista Python aos DataFrames do Pandas.

Como agregar dados usando a função .agg ().

Como criar gráficos de dispersão, gráficos de barras e gráficos de linhas com dois eixos no Matplotlib.

Compreenda os esquemas de banco de dados que são organizados por chaves primárias e estrangeiras.

Como mesclar DataFrames que compartilham uma chave comum

Encontre os conjuntos de LEGO mais antigos e maiores
Solução de Desafio de Markdown

Veja como você organizaria as células do markdown com os títulos das seções e tags de imagem. Você também pode ter notado que o texto delimitado pelo símbolo de asterisco duplo ** o deixará em negrito.


Explorando o sets.csv

O sets.csv contém uma lista de conjuntos de LEGO. Mostra em que ano o conjunto foi lançado e o número de peças no conjunto.

Você pode dar os primeiros passos para explorar este conjunto de dados? Leia o .csv e dê uma olhada nas colunas.

Em seguida, tente responder às seguintes perguntas:

Em que ano foram lançados os primeiros conjuntos de LEGO e como foram chamados esses conjuntos?

Quantos produtos diferentes a empresa LEGO vendeu em seu primeiro ano de operação?

Quais são os 5 principais conjuntos de LEGO com o maior número de peças?



Role para baixo para ver a solução abaixo ...

.

..

...

..

.

Solução

A primeira etapa, como sempre, é ler o arquivo .csv e verificar o que ele contém. Vemos que há algum tipo de
id para cada conjunto (o set_num), o nome do conjunto, o ano em que foi lançado, o theme_id
(o código para o nome do tema) e o número de partes.

Portanto, parece que temos tudo o que temos aqui para responder às nossas duas perguntas.

Para encontrar o ano em que os primeiros conjuntos de LEGO foram lançados,
temos que classificar pela coluna do ano. O método .sort_values ​​()
 irá por padrão classificar em ordem crescente.

Parece que o LEGO começou em 1949! 😮 Os nomes para esses conjuntos
não são nada dignos de nota, mas vamos descobrir quantos produtos
diferentes a empresa vendeu em seu primeiro ano desde o lançamento:


Em 1949, a LEGO começou a vender apenas 5 conjuntos diferentes! Observe
que aqui estamos filtrando nosso DataFrame em uma condição. Estamos recuperando
as linhas em que a coluna do ano tem o valor 1949: sets ['year'] == 1949.

Agora vamos encontrar o conjunto LEGO com o maior número de peças. Se quisermos encontrar o maior
número de partes, temos que definir o argumento ascendente como False quando classificamos pela coluna num_parts.


O maior conjunto de LEGO já produzido tem cerca de 10.000 peças! Aparentemente, apenas duas dessas
caixas foram produzidas, então se você queria colocar as mãos em um conjunto de LEGO ridiculamente grande,
você terá que se contentar com 7.541 peças do Millennium Falcon.
'''


'''"# Introdução \ n",
    "\ n",
    "Hoje vamos mergulhar fundo em um conjunto de dados sobre LEGO. A partir do conjunto de dados, podemos fazer um monte de perguntas interessantes sobre a história da empresa LEGO, sua oferta de produtos e qual conjunto de LEGO, em última análise, governa todos eles: \ n",
    "\ n",
    "<ul type =  square \ "> \ n",
    "<li> Qual é o conjunto de LEGO mais enorme já criado e quantas peças ele tinha? </li> \ n",
    "\ n",
    "<li> Como a empresa LEGO começou? Em que ano foram lançados os primeiros conjuntos LEGO e quantos conjuntos a empresa vendeu quando foi lançado? </li> \ n",
    "\ n",
    "<li> Qual tema de LEGO tem mais conjuntos? É um dos próprios temas de LEGO, como Ninjago, ou um tema licenciado como Harry Potter ou Super-heróis da Marvel? </li> \ n",
    "\ n",
    "<li> Quando a empresa LEGO realmente expandiu sua oferta de produtos? Podemos detectar uma mudança na estratégia da empresa com base em quantos temas e conjuntos ela lançou ano a ano? </li> \ n",
    "\ n",
    "<li> Os conjuntos de LEGO aumentaram em tamanho e complexidade com o tempo? Os LEGO mais antigos \ n",
    "os conjuntos tendem a ter mais ou menos peças do que os conjuntos mais recentes? </li> \ n",
    "</ul> \ n",
    "\ n",
    "** Fonte de dados ** \ n",
    "\ n",
    "[Rebrickable] (https://rebrickable.com/downloads/) compilou dados sobre todas as peças LEGO existentes. Recomendo que você baixe os arquivos .csv fornecidos nesta lição."
   ]
  },'''