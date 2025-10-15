# Plano de Aula: Disciplina de Machine Learning Engineering

## Estrutura Geral
- **Carga horária por semana**: 2 aulas (1 teórica + 1 prática), cada uma com duração de 1h30 a 2h.
- **Plataforma de gestão**: Teams
- **Critérios de participação**: Conhecimento intermediário em Python, básico em Docker e AWS.
- **Avaliação**: Entregas práticas + projeto final em equipe + planilha avaliativa com justificativas.
- **Certificação**: A ser definido conforme desempenho e participação.

---

## Semana 1 – Apresentação do Curso

### Aula Teórica
**Objetivo**: Engajar e motivar os alunos para o programa completo.

**Conteúdo**:
- Apresentação do curso e seus objetivos
- Visão geral dos temas abordados
- Introdução ao MLOps: conceito, importância e contexto atual
- Rotina de um engenheiro de Machine Learning
- Orquestração de pipelines de ML
- Maturidade de esteiras MLOps: níveis e evolução
- Apresentação do desafio final e critérios de avaliação

---

## Semana 2 – Dados

### Aula Teórica
**Conteúdo**:
- Introdução ao MLFlow: rastreamento de experimentos
- Tipos de dados: estruturados, não estruturados, semi-estruturados, qualitativos e quantitativos
- Fontes de dados: APIs, bancos, arquivos, web scraping
- Engenharia de features: criação, transformação, seleção
- Armazenamento de features: Feature Store, versionamento

### Aula Prática
**Notebook Hands-On**:
- Setup inicial com MLFlow
- Importação de datasets do Kaggle
- Análise exploratória e interpretação dos dados
- Limpeza e tratamento de dados
- Manipulação de dados qualitativos (label encoding, one-hot)
- Manipulação de dados quantitativos (normalização, padronização)

---

## Semana 3 – Modelagem

### Aula Teórica
**Conteúdo**:
- Bibliotecas clássicas: Scikit-learn, XGBoost, LightGBM
- Redes neurais: arquitetura, forward/backpropagation
- IA generativa: conceitos, aplicações, agentes e multiagentes com langraph, direcionar para assistir cruso da IOX para complementar.
- Otimização de modelos: grid search, random search, Bayesian optimization
- Armazenamento e versionamento de treinamentos com MLFlow

### Aula Prática
**Notebook Hands-On (MOdelos clássicos)**:
- Treinamento com bibliotecas clássicas
- Ajuste de hiperparâmetros
- Uso de técnicas de boosting
- Registro e versionamento de modelos com MLFlow
- Comparação de consumo de recursos entre modelos

### Aula Prática
**Notebook Hands-On (Modelos Generativos)**:
- Construção de um agente com weavite
- Uso de técnicas para aplicação de guardrails
- Registro e versionamento de modelos com MLFlow
- Comparação de consumo de recursos entre modelos

---

## Semana 4 – Deploy

### Aula Teórica
**Conteúdo**:
- Tipos de serving: batch, online, streaming
- Estratégias de deploy: blue/green, canary, shadow
- Introdução à cloud: AWS
  - CI/CD pipelines
  - Infraestrutura como código (IaC): CloudFormation
- Validações pós-deploy: testes, métricas, rollback

### Aula Prática
**Notebook Hands-On**:
- Execução de modelos localmente a partir de APIs contruidas com flask ou fast API
- Comparação de resultados entre modos de execução usando logs para monitoramento
- Trocar modelos que estão sendo servidos em memória a partir de um endpoint
- Avaliação de performance (latência, throughput)
- Análise de consumo de recursos (CPU, RAM, GPU)

---

## Semana 5 – Monitoração

### Aula Teórica
**Conteúdo**:
- O que monitorar: métricas de modelo, uso de recursos, erros
- Ferramentas: MLFlow, Datadog
- Alertas: thresholds, notificações, logs estruturados
- Monitoramento de drift e performance em produção

### Aula Prática
**Notebook Hands-On**:
- Configuração de alertas com MLFlow e Datadog
- Adição de logs customizados
- Visualização de dashboards com Datadog
- Simulação de drift e análise de impacto

---

## Semana 6 – Finalização

### Aula Teórica
**Conteúdo**:
- Coleta de feedbacks dos alunos
- Boas práticas de programação: modularização, testes, documentação
- Explicação detalhada do projeto final
  - Critérios de avaliação
  - Planilha avaliativa com justificativas
  - Regras de entrega e submissão via Git

---

## Semanas 7 e 8 – Projeto Final

### Aula Prática
**Formato**: Trabalho individual

**Atividades**:
- Execução do projeto final com base nos temas abordados
- Entrega via GitHub com README explicativo
- Avaliação dos projetos com base na planilha de critérios
- Seleção dos 3 melhores projetos
- Apresentação dos finalistas na semana seguinte
- Premiação do melhor projeto

---

## Observações Finais
- A presença no curso não garante vaga nos processos para MLE, mas prepara o aluno para oportunidades futuras.
- A entrega dos notebooks práticos soma pontos para a seleção dos projetos finalistas.
- Feedbacks estruturados serão fornecidos para cada aluno ao final do curso.
