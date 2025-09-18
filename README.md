#  – Estudo das Características de Qualidade de Sistemas Java

**Curso:** Engenharia de Software  
**Disciplina:** Laboratório de Experimentação de Software  
**Professor:** Danilo 
**Período:** 6º  
**Equipe:** Victor Reis Carlota e Luís Felipe Brescia  

---

## Sumário

1. [Resumo](#resumo)
2. [Introdução](#introdução)
3. [Metodologia](#metodologia)
    - 3.1 Seleção de Repositórios
    - 3.2 Coleta de Dados e Métricas
    - 3.3 Abordagem Computacional e Desafios
4. [Hipóteses](#hipóteses)
5. [Resultados](#resultados)
    - 5.1 Distribuição das Métricas de Qualidade
    - 5.2 RQ1: Popularidade vs Qualidade
    - 5.3 RQ2: Maturidade vs Qualidade
    - 5.4 RQ4: Tamanho vs Qualidade
6. [Discussão](#discussão)
7. [Conclusão](#conclusão)
8. [Referências](#referências)

---

## Resumo

Este relatório apresenta uma análise empírica sobre a relação entre características do processo de desenvolvimento (popularidade, maturidade, tamanho) e atributos de qualidade interna de repositórios Java open-source no GitHub. Utilizando métricas estáticas extraídas com a ferramenta CK e dados de processo coletados via API, buscamos responder questões sobre como esses fatores se correlacionam e que implicações podem ter para a engenharia de software.

---

## Introdução

A evolução colaborativa de sistemas open-source traz desafios para a gestão dos atributos de qualidade interna, como modularidade, manutenibilidade e legibilidade. No contexto de projetos Java hospedados no GitHub, surge a necessidade de compreender como práticas de desenvolvimento e características do processo se relacionam com métricas clássicas de qualidade de software.  
Este estudo examina 1.000 dos repositórios Java mais populares, correlacionando dados de processo e métricas de qualidade para responder quatro questões de pesquisa centrais:

- **RQ 01:** Qual a relação entre a popularidade dos repositórios e suas características de qualidade?
- **RQ 02:** Qual a relação entre a maturidade dos repositórios e suas características de qualidade?
- **RQ 03:** Qual a relação entre a atividade dos repositórios e suas características de qualidade?
- **RQ 04:** Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

Além da análise estatística, buscamos apresentar reflexões filosóficas e matemáticas sobre os resultados, indo além de uma análise puramente técnica.

---

## Metodologia

### 3.1 Seleção de Repositórios

Selecionamos os 1.000 repositórios Java mais populares do GitHub, utilizando critérios de idioma e ordenação por número de estrelas (popularidade). Essa seleção visa garantir a relevância e diversidade dos sistemas analisados.

### 3.2 Coleta de Dados e Métricas

Para cada repositório, coletamos:

- **Popularidade:** número de estrelas no GitHub.
- **Maturidade:** idade do repositório (anos desde o primeiro commit).
- **Tamanho:** linhas de código (LOC) e linhas de comentários.
- **Qualidade:** métricas CK - CBO (Coupling Between Objects), DIT (Depth Inheritance Tree), LCOM (Lack of Cohesion of Methods).

Os dados de processo foram obtidos via API REST do GitHub. As métricas de qualidade foram extraídas utilizando a ferramenta CK, que processa o código fonte e gera arquivos `.csv` para cada repositório.

### 3.3 Abordagem Computacional e Desafios

A automação envolveu o desenvolvimento de scripts em Python para baixar, extrair, processar e sumarizar as métricas dos repositórios.  
**Desafios enfrentados:**
- Alto volume de dados: processar 1.000 repositórios exigiu automação robusta e controle de erros.
- Diversidade estrutural dos projetos: diferentes padrões de organização dos arquivos dificultaram a padronização da coleta.
- Métricas ausentes: alguns projetos não continham arquivos Java ou as métricas esperadas, exigindo tratamento de exceções.
- Dispersão dos dados: muitos repositórios apresentaram valores extremos (outliers), tornando necessária a aplicação de logaritmos para análise gráfica e correlação.

---

## Hipóteses

Antes da análise dos dados, elaboramos as seguintes hipóteses informais:

- **Popularidade x Qualidade:** Esperamos que projetos mais populares tendam a apresentar melhor qualidade interna, pois são mais revisados e atraem contribuições qualificadas.
- **Maturidade x Qualidade:** Projetos mais antigos devem mostrar evolução positiva nas métricas de qualidade devido à refatoração e maturação do código.
- **Tamanho x Qualidade:** Projetos maiores (mais LOC) podem apresentar maior acoplamento (CBO) e menor coesão (LCOM), devido à complexidade.
- **Atividade x Qualidade:** Projetos com mais releases tendem a ter processos mais ativos de evolução e, possivelmente, melhor qualidade.

---

## Resultados

### 5.1 Distribuição das Métricas de Qualidade

Antes de analisar as correlações, examinamos a distribuição das métricas de qualidade para entender seu comportamento geral:

![Distribuição da métrica CBO_MEAN - observa-se uma concentração em valores baixos com cauda longa](https://hist_cbo_mean_bruto.png)

*Distribuição da métrica DIT_MEAN - mostra concentração em valores entre 1.0 e 2.5*  
![Distribuição da métrica DIT_MEAN](https://hist_dit_mean_bruto.png)

![Distribuição da métrica LCOM_MEAN - apresenta alta concentração próximo a zero com outliers significativos](https://hist_lcom_mean_bruto.png)

As distribuições das variáveis de processo também foram transformadas logaritmicamente para melhor visualização:

![Distribuição de log_stars após transformação logarítmica](https://hist_log_stars.png)

![Distribuição de log_age após transformação logarítmica](https://hist_log_age.png)

---

### 5.2 RQ1 – Popularidade vs Qualidade

#### Popularidade vs CBO

![Relação entre Popularidade (estrelas) e CBO_MEAN - dados brutos com outliers](https://stars_vs_cbo_mean_bruto.png)

![Relação entre log(Popularidade) e CBO_MEAN - após transformação logarítmica](https://log_stars_vs_cbo_mean_log.png)

A análise da relação entre popularidade e acoplamento (CBO) mostra uma dispersão significativa dos dados. Embora exista uma ligeira tendência positiva, a presença de outliers é marcante. Repositórios com alto número de estrelas apresentam valores de CBO variando amplamente, sugerindo que a popularidade não é um indicativo consistente de baixo acoplamento.

#### Popularidade vs DIT

![Relação entre log(Popularidade) e DIT_MEAN](https://log_stars_vs_dit_mean_log.png)

A profundidade da árvore de herança (DIT) mostra pouca correlação com a popularidade. Os valores se concentram principalmente entre 1.0 e 2.5, independentemente do número de estrelas.

#### Popularidade vs LCOM

![Relação entre Popularidade (estrelas) e LCOM_MEAN - dados brutos com outliers](https://stars_vs_lcom_mean_bruto.png)

A falta de coesão (LCOM) apresenta os outliers mais extremos em relação à popularidade. Projetos muito populares podem apresentar tanto valores muito baixos quanto muito altos de LCOM, indicando que fatores além da popularidade influenciam significativamente esta métrica.

---

### 5.3 RQ2 – Maturidade vs Qualidade

#### Maturidade vs CBO

![Relação entre Maturidade (anos) e CBO_MEAN](https://age_vs_cbo_mean_bruto.png)

A maturidade dos repositórios mostra uma relação complexa com o acoplamento. Projetos mais antigos tendem a apresentar maior variação nos valores de CBO, sugerindo diferentes estratégias evolutivas ao longo do tempo.

#### Maturidade vs DIT

![Relação entre Maturidade (anos) e DIT_MEAN - dados brutos](https://age_vs_dit_mean_bruto.png)

![Relação entre log(Maturidade) e DIT_MEAN - após transformação logarítmica](https://log_age_vs_dit_mean_log.png)

A profundidade da árvore de herança mostra uma tendência interessante: projetos mais maduros tendem a apresentar valores de DIT ligeiramente mais altos. Isso pode indicar um processo de refatoração e aprofundamento das hierarquias de classe ao longo do tempo.

#### Maturidade vs LCOM

![Relação entre Maturidade (anos) e LCOM_MEAN](https://age_vs_lcom_mean_bruto.png)

![Relação entre log(Maturidade) e LCOM_MEAN](https://log_age_vs_lcom_mean_log.png)

A falta de coesão apresenta a relação mais fraca com a maturidade. Projetos de todas as idades mostram ampla variação nos valores de LCOM, sugerindo que essa métrica é influenciada por fatores mais específicos do design do que pela idade do projeto.

---

### 5.4 RQ4 – Tamanho vs Qualidade

#### Tamanho vs DIT

![Relação entre Tamanho (LOC) e DIT_MEAN](https://loc_sum_vs_dit_mean_bruto.png)

O tamanho do projeto mostra correlação positiva com a profundidade da árvore de herança. Projetos maiores tendem a ter estruturas de herança mais complexas, possivelmente devido à necessidade de maior organização e abstração.

#### Tamanho vs LCOM

![Relação entre Tamanho (LOC) e LCOM_MEAN](https://loc_sum_vs_lcom_mean_bruto.png)

A relação mais forte observada é entre tamanho e falta de coesão. Projetos maiores apresentam significativamente maior LCOM, corroborando a hipótese de que a complexidade estrutural dificulta a manutenção da coesão entre métodos.

---

## Discussão

Os resultados revelam nuances importantes nas relações entre características de processo e qualidade interna:

- **Popularidade e Qualidade:** Contrariando a hipótese inicial, a popularidade não mostrou correlação forte com melhores métricas de qualidade. Isso sugere que fatores como utilidade da aplicação, marketing ou timing de lançamento podem ser mais determinantes para o sucesso de um repositório do que propriamente a qualidade arquitetural interna.

- **Maturidade e Qualidade:** Projetos mais antigos mostraram tendência a maior profundidade de herança (DIT), o que pode ser interpretado de duas formas: como evolução arquitetural positiva através de refatoração, ou como acumulação de complexidade desnecessária. A falta de correlação forte com CBO e LCOM sugere que a maturidade por si só não garante melhor qualidade.

- **Tamanho e Qualidade:** A forte correlação positiva entre tamanho e LCOM confirma a hipótese inicial de que projetos maiores enfrentam desafios significativos de coesão. Esta é talvez a descoberta mais consistente do estudo, reforçando a importância de práticas de modularização em projetos de grande escala.

**Implicações Práticas:**
- Desenvolvedores devem estar cientes que popularidade não equivale a qualidade técnica.
- Projetos grandes exigem atenção especial à coesão e modularidade.
- A maturidade traz complexidade arquitetural que deve ser gerenciada conscientemente.
- Métricas de qualidade devem ser monitoradas continuamente, independentemente do sucesso do projeto.

**Limitações do Estudo:**
- A análise focou apenas em métricas estruturais clássicas.
- Fatores qualitativos como design patterns e práticas de desenvolvimento não foram considerados.
- A amostra, embora grande, representa apenas projetos Java populares no GitHub.

---

## Conclusão

Este estudo demonstra que as relações entre características de processo e qualidade interna em repositórios Java são complexas e multifacetadas. Enquanto o tamanho mostra correlação evidente com a falta de coesão, a popularidade e maturidade apresentam relações mais sutis com as métricas de qualidade.

As implicações práticas sugerem que equipes de desenvolvimento devem:

- Não assumir que projetos populares são automaticamente bem arquitetados.
- Dar atenção especial à coesão em projetos de grande porte.
- Gerenciar conscientemente a complexidade arquitetural em projetos maduros.
- Utilizar métricas de qualidade como ferramentas complementares, não como únicos indicadores.

Este trabalho contribui para a compreensão das dinâmicas de qualidade em projetos open-source e destaca a importância de uma abordagem holística que considere tanto aspectos técnicos quanto sociais no desenvolvimento de software.

---

## Referências

- F. Brito e R. Oliveira, "CK: A Tool for Calculating Code Metrics in Java Projects", 2018.
- S. McConnell, "Code Complete: A Practical Handbook of Software Construction", Microsoft Press, 2004.
- E. Gamma et al., "Design Patterns: Elements of Reusable Object-Oriented Software", Addison-Wesley, 1994.
- GitHub REST API Documentation: https://docs.github.com/en/rest
- Engenharia de Software Moderna, Ian Sommerville, 10ª edição, Pearson.
- Martin, R. C. (2008). Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
- Fowler, M. (2018). Refactoring: Improving the Design of Existing Code. Addison-Wesley.
