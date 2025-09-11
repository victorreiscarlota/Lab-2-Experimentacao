# Laboratório 2 de Experimentação de Software

Este projeto utiliza a ferramenta **CK (Chidamber & Kemerer Metrics Suite)** para extrair métricas de código-fonte Java, permitindo a análise de **complexidade, acoplamento, coesão e tamanho** de classes, métodos, atributos e variáveis.

---

## 🚀 Objetivo

O objetivo deste laboratório é aplicar técnicas de análise estática em código-fonte Java para coletar métricas que auxiliem na compreensão de características internas do software.

Essas métricas permitem investigar aspectos de qualidade como **complexidade, reutilização, manutenibilidade e acoplamento** entre classes.

### Questões de Pesquisa (RQs)

- **RQ01:** Qual o tamanho médio das classes e métodos do sistema?  
  _Métrica:_ LOC (Lines of Code).

- **RQ02:** O sistema possui classes com alta complexidade?  
  _Métrica:_ WMC (Weighted Methods per Class).

- **RQ03:** Qual o nível de acoplamento entre as classes?  
  _Métrica:_ CBO (Coupling Between Objects).

- **RQ04:** O sistema apresenta boa coesão interna?  
  _Métrica:_ LCOM (Lack of Cohesion of Methods) e TCC (Tight Class Cohesion).

- **RQ05:** Há evidências de código excessivamente grande ou difícil de manter?  
  _Métrica:_ combinações de LOC, RFC (Response For a Class) e Fan-In/Fan-Out.

---

## ⚙️ Como Executar

1. **Compilar ou preparar um projeto Java**  
   É necessário ter uma pasta com código-fonte Java (ex.: `project/src`).

2. **Criar a pasta de saída**

   ```bash
   mkdir output
   ```

3. **Executar o script de análise**  
   O comando segue o formato:

   ```bash
   java -jar lab2.jar <path_to_project> <useJars=true|false> <maxFilesPerPartition> <printVariablesAndFields=true|false> <output_path>
   ```

   Exemplo prático:

   ```bash
   java -jar lab2.jar ./project/src true 0 true ./output
   ```

---

## 📊 Saída Esperada

A execução gera arquivos **CSV** na pasta `output/`, contendo métricas extraídas em diferentes granularidades:

- 📦 **outputclass.csv** → métricas por classe
- 🔧 **outputmethod.csv** → métricas por método
- 🧩 **outputfield.csv** → métricas por atributos (campos)
- 📐 **outputvariable.csv** → métricas por variáveis locais

Cada arquivo pode ser importado em ferramentas de análise (Excel, Python, R, Pandas, etc.) para gerar estatísticas e visualizações.

---

## 👨‍💻 Autores

- [Luís Felipe Teixeira Dias Brescia](https://luisbrescia.tech)
- [Victor Reis Carlota](https://carlotavictor.vercel.app)

---

## 📚 Referências

Repositório usado como exemplo: [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java)
