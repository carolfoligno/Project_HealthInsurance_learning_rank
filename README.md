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

O modelo é aproximadamente 2,5 vezes melhor que fazer ligações a clientes aleatórios. Com a limitação de 20mil ligações, com a lista ordenada dos mais propensos temos 65% dos clientes interessados. Ou seja, de todos os clientes interessados, 65% deles estão presentes nas 20mil ligações.

**Curva de ganhos acumulativos**

É uma curva de avaliação que avalia o desempenho do modelo e compara os resultados com a escolha aleatória.

![](https://user-images.githubusercontent.com/80589529/227256369-2e9b8587-a24d-4408-8c95-965c93d04547.png)

No eixo X, temos a proporção de amostra do nosso conjunto de dados. No eixo Y, é a porcentagem de ganho. 

**Curva de Lift**


![](https://user-images.githubusercontent.com/80589529/227258530-673efc7b-79dd-4b72-b465-f1999f28a5dc.png)

No eixo X temos a proporção de nossa amostra que corresponde a um determinado Lift, plotado no eixo Y. Clientes mais propensos a aceitarem a oferta aparace à esquerda do gráfico, tendo pontuações mais altas de Lift. 

A linha traçada em vermelho corresponde a proporção de 20 mil clientes, que seriam as 20mil ligações. 
