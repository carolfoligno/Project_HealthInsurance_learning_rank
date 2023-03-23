# Health Insurance Project
<img src="https://user-images.githubusercontent.com/80589529/227253968-02ff9967-0253-474a-83c3-101b6553337c.jpg" width="400" height="350">

## O PROBLEMA DE NEGÓCIO

**A Empresa Insurance All - Empresa Ficticia**

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, **um novo produto: Um seguro de automóveis.**

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma **pesquisa** com cerca de **380 mil clientes** sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou **127 mil novos clientes que não responderam a pesquisa** para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas. Contudo, o time de vendas tem uma **capacidade de realizar 20 mil ligações** dentro do período da campanha.

**OBJETIVO:**

- Ordenar uma lista de clientes mais propensos a aceitar o novo produto, pela limitada capacidade de ligações.

## Resultados

Como resolução do problema de negócio, foi realizado o treinamento dos dados com algoritmo de Machine Learning para criar uma lista ordenada de clientes mais propensos a aceitarem a oferta do novo produto da empresa. 

Tal ordenação é realizada com uma nova função criada no google sheets do modelo já treinado, classificando os score de propensão dos clientes de forma descrescentes.

- Planilha disponivel no [Google Sheets](https://docs.google.com/spreadsheets/d/114t748UXUME_M5E4ogLUyjBAzWom4olS2MyKlCMuobY/edit?usp=sharing), com uma amostra de 60 registro de clientes, onde com a função "Propensity Score" criada, é possivel ordenar os cliente mais propensos a aceitarem a oferta do novo seguro de automovel. 

https://user-images.githubusercontent.com/80589529/227308510-7907d3ec-613b-45ce-b67b-7a693b75a7c1.mp4

O modelo é aproximadamente 2,5 vezes melhor que fazer ligações a clientes aleatórios. Com a limitação de 20mil ligações, com a lista ordenada dos mais propensos temos 65% dos clientes interessados. Ou seja, de todos os clientes interessados, 65% deles estão presentes nas 20mil ligações.

**Curva de ganhos acumulativos**

É uma curva de avaliação que avalia o desempenho do modelo e compara os resultados com a escolha aleatória.

![](https://user-images.githubusercontent.com/80589529/227256369-2e9b8587-a24d-4408-8c95-965c93d04547.png)

No eixo X, temos a proporção de amostra do nosso conjunto de dados. No eixo Y, é a porcentagem de ganho. 

**Curva de Lift**


![](https://user-images.githubusercontent.com/80589529/227258530-673efc7b-79dd-4b72-b465-f1999f28a5dc.png)

No eixo X temos a proporção de nossa amostra que corresponde a um determinado Lift, plotado no eixo Y. Clientes mais propensos a aceitarem a oferta aparace à esquerda do gráfico, tendo pontuações mais altas de Lift. 

A linha traçada em vermelho corresponde a proporção de 20 mil clientes, que receberam as ligações com a oferta do nosso produto.

## Principais Insights dos dados

É na Análise Exploratória de dados que buscamos validar hipoteses possibilitando descobrir informações novas sobre o negócio. Podendo corroborar com crenças já presentes na empresa ou até retratar tais crenças. 

### ****Hipotese 1: Automóvel com mais idade o cliente tem menos interesse de obter o seguro.****

FALSO. Nos dados da empresa, a idade do automovel é classificada em: Menor que 1 ano, entre 1 a 2 anos e maior que 2 anos de idade. Levando em consideração a distribuição dos dados, os clientes que tem automovel maior que 2 anos 30% deles tem interesse no novo seguro, já os clientes que tem automoveis entre 1 a 2 anos 17% tem interesse, em contrapartida de 4% dos que tem automovel menor que 1 ano tem interesse. 

### ****Hipotese 2: Automóveis que já ocorreu alguma danificação no passado, o dono tem mais interesse de obter o seguro.****

VERDADEIRO, 23% dos que já danificaram o carro tem interesse de obter o seguro. Já aqueles que nunca danificaram o carro, 0,5% tem o interesse de obter o seguro.

### ****Hipotese 3: Clientes mais velhos tem mais interesse de obter o seguro****

VERDADEIRO, clientes entre 46 a 60 são os que mais tem interesse em obter o seguro, 19% tem interesse de obter o seguro. Os clientes entre os 18 a 25 anos, 3% deles tem interesse. 

## Algoritmos de Machine Learning

Para esse problema de negócio, sendo um Learning to Rank, que tenta classificar uma lista de itens com base em sua relevância. Foram utilizados 3 algoritmos de Machine Learning nesse primeiro ciclo de CRISP ([artigo no Medium](https://medium.com/comunidadeds/voc%C3%AA-tem-os-dados-tem-o-problema-de-neg%C3%B3cio-mas-e-agora-o-que-fazer-bf3b2d06482)). 

- KNeighborsClassifier
- LogisticRegression
- RandomForestClassifier 

Os algoritmos eram treinados e logo depois a sua performace medida pelas métricas de Precision e Recall. Para melhor performace de aprendizado nesse caso de classificação de classes binária é preferivel uma amostragem estratificada, então para isso, foi realizado Cross Validation no dataset, obtendo os seguintes valores.

![](https://user-images.githubusercontent.com/80589529/227278726-85087ed4-87d7-45cb-8353-0e2495ffca01.png)

Escolhido o modelo, no caso Random Forest, é necessário descobrir quais são os melhores parametros. Utilizando o GridShearch, foi selecionado os parametros para treinar o modelo e medido o poder de generalização com dados que ele nunca viu. 

![](https://user-images.githubusercontent.com/80589529/227278967-6055cf94-c45d-4358-b72e-91217b22e73c.png)

## Conclusão

Com a utilização de um modelo de Machine Learning, foi possivel ordenar uma lista de clientes mais propensos a aceitarem uma oferta de um novo produto da empresa. Com certeza, sendo melhor do que realizar ligações de clientes aleatoriamente.

## Próximos passos

- No próximo cliclo de CRISP, investigar mais os dados em busca de outros Insights.
- Pesquisar mais sobre o modelo de negócio para beneficiar a criação de novos atributos que irão melhorar a performace do modelo.
- Buscar outros algoritmos de Machine Learning.

## Ferramentas

- Linguagem de Programação: Python
- IDE: VSCode, Jupyter Notebook
- Algoritmos de Classificação - pacote sklearn.
- Render Cloud
- Google Sheets Apps Script

## Referências

- [Comundade DS](https://comunidadeds.com/formacao-em-ciencia-de-dados/?utm_source=google&utm_medium=cpc&utm_campaign=search_cientistadados&utm_content=institucional_descobertas&utm_term=comunidade%20ds&gclid=Cj0KCQjw8e-gBhD0ARIsAJiDsaWBa9RedU8DsWpgYM8GZOdWi5te8nPdxYtP_WsSJuIUaScVkeUDSw8aAtSFEALw_wcB).
- Dataset disponovel no [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).



