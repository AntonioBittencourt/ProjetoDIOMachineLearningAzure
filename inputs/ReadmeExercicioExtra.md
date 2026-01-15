# Introdução
Agora extendemos o machine learning do desafio proposto na plataforma DIO para um exemplo mais complicado. Vamos analisar a poluição de um lago ao longo do tempo. As variáveis estudadas que interferem nessa poluição são.
- data e mes (época do ano),
- Posições x e y,
- profundidade em metros,
- temperatura da água em graus célsius,
- velocidade da corrente em mps,
- direção da corrente em graus,
- precipitacao em mm,
- pH da água,
- oxigenio dissolvido em mgL e
- intensidade do despejo
Para por fim calcularmos a poluição em mgL.

# Implementação

Novamente Ffram feitas análises de Machine Learning na plataforma Azure. Duas estratégias foram usadas a AutoML que funciona mais como uma "caixa preta", nele são permitidas o uso de diversas estratégias simultâneas como, por exemplo, KNN, árvores de decisão, random forest entre outras. Porém para garantir agilidade do processo foi usado apenas o método XGBoostRegressor.

Na primeira figura temos exemplo gerado por IA de todas as variáveis analisadas

![Tabela Gerada por IA](imagens/DadosIA.jpg)

Em primeira análise vamos testar a implementação feita por um pipeline no designer. Ele está descrito na figura abaixo.

![Implementação do Pipeline](imagens/RepresentacaodoPipeline.jpg)



Os resultados estão na tabela abaixo, vemos que chegamos a uma arpoximação muito boa da previsão por meio da regressão com os resultados tabelados. As maiores discrepâncias se encontram para os valores muito altos ou muito baixos de temperatura ou venda de sorvetes.

![Resultados do Pipeline Parte 1](imagens/ResultadosPipeline.jpg)
![Resultados do Pipeline Parte 2](imagens/ResultadosPipeline2.jpg)
![Resultados do Pipeline Parte 3](imagens/ResultadosPipeline3.jpg)


E os valores de erro se encontram represntados abaixo.
![Desempenho do Pipeline](imagens/DesempenhoPipeline.jpg)

Com isso o dono da sorveteria pode nos casos de maior discrepância prever uma maior margem de erro nos extremos dos dados. Podendo nesse caso produzir mais sorvetes que o previsto por precaução ou manter o número atual, analisando se é preferível deixar de vender sorvetes para não haver desperdício ou garantir a venda, havendo o risco de que esses desperdícios ocorram.
Em AutoML foram obtidas também previsões de alta qualidade, inclusive melhores que no designer na técnica que performou melhor, VotingEnsemble, com correlação de spearman de 0,98441 e erro absoluto de média 2,0149. Demais dados estão presentes na figura abaixo.
![Métodos de maior desempenho](imagens/MetodosMaiorDesempenho.jpg)
![Méricas do AUtoML](imagens/MetodosMetricasAutoML.jpg)


# Conclusão
Foram testadas duas abordagens, a AutoML que pode ser usada por qualquer um mesmo sem grandes conhecimentos de Machine Learning, pois funciona como uma "caixa preta" e um pipeline descrito no designer que permite maior configuração e controle sobre o que está sendo feito. Com o AutoML foi obtido resultados melhores, o que mostra a robustez e a qualidade dessa solução, porém um melhor design no pipeline pode vir a alterar esse resultado.
