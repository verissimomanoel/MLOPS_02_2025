# Serviço de Deploy de Modelos de Machine Learning

Este projeto implementa uma API robusta para servir modelos de machine learning em produção, construída com FastAPI e práticas modernas de desenvolvimento.

## 🏗 Estrutura do Projeto

```
serving/
├── app/
│   ├── api/
│   │   └── endpoints.py      # Handlers das rotas da API
│   ├── core/
│   │   ├── config.py        # Configurações da aplicação
│   │   └── model_manager.py  # Gerenciamento do modelo ML
│   └── models/
│       └── schemas.py        # Modelos de validação de dados
├── main.py                   # Ponto de entrada da aplicação
├── Dockerfile               # Configuração para containerização
└── pyproject.toml          # Dependências do projeto
```

## 🚀 Funcionalidades Principais

- **API REST com FastAPI**: Interface moderna e de alta performance
- **Gerenciamento de Modelo**: Carregamento e serving eficiente de modelos ML
- **Validação de Dados**: Schemas Pydantic para garantir integridade dos dados
- **Logging**: Sistema de logs estruturados em JSON
- **Containerização**: Docker multi-stage build para implantação otimizada
- **Healthcheck**: Monitoramento da saúde do serviço
- **CORS**: Suporte configurado para requisições cross-origin

## 🛠 Requisitos Técnicos

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- NumPy
- scikit-learn
- Docker (opcional)

## 🔧 Configuração e Instalação

### Instalação Local

```bash
# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# ou
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -e ".[all]"
```

### Usando Docker

```bash
# Construa a imagem
docker build -t ml-serving .

# Pra rodar o MLFlow (caso necessário)
mlflow server --host 0.0.0.0 --port 8080

# Execute o container
docker run -d \
  -p 8000:8000 \
  -e MODEL_NAME=random-forest \
  -e MODEL_VERSION_ALIAS=latest \
  --name ml-serving \
  ml-serving
```

## 🚀 Executando o Serviço

### Localmente

```bash
# Configure o modelo MLflow (opcional)
export MODEL_NAME="random-forest"
export MODEL_VERSION_ALIAS="latest"

# Execute o servidor
python main.py
# ou
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📡 Endpoints da API

### Predição

- **URL**: `/api/v1/predict`
- **Método**: POST
- **Corpo da Requisição**:

```json
{
	"features": {
		"job": "management",
		"marital": "married",
		"education": "tertiary",
		"contact": "unknown",
		"housing": "yes",
		"loan": "no",
		"default": "no",
		"day": 5
	}
}
```

- **Resposta de Sucesso**:

```json
{
	"prediction": 1.0,
	"status": "success"
}
```

### Health Check

- **URL**: `/api/v1/health`
- **Método**: GET
- **Resposta**:

```json
{
	"status": "healthy",
	"model_loaded": true
}
```

## 🔍 Exemplo de Uso com cURL

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Fazer uma predição
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "features": {
         "job": "management",
         "marital": "married",
         "education": "tertiary",
         "contact": "unknown",
         "housing": "yes",
         "loan": "no",
         "default": "no",
         "day": 5
      }
  }'
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "features": {
        "job": "management",
         "marital": "single",
         "education": "tertiary",
         "contact": "unknown",
         "housing": "yes",
         "loan": "no",
         "default": "no",
         "day": 8
    }
  }'

```

## ⚙️ Variáveis de Ambiente

- `MODEL_NAME`: Nome do modelo no registro do MLflow
- `MODEL_VERSION_ALIAS`: Versão ou alias do modelo (ex: 'production', 'staging', '1')
- `PORT`: Porta do servidor (padrão: 8000)
- `HOST`: Host do servidor (padrão: 0.0.0.0)

## 🔐 Segurança

- Validação de entrada com Pydantic
- Logs estruturados para auditoria
- Containerização segura com imagem slim
- Healthchecks para monitoramento

## 📦 Estrutura do Modelo Manager

O `ModelManager` é responsável por:

- Carregamento eficiente do modelo
- Pré-processamento de dados de entrada
- Execução de predições
- Formatação das respostas
- Tratamento de erros

## 🔄 CI/CD e Deploy

### Docker

- Build multi-stage para imagens otimizada
- Healthcheck integrado
- Configuração via variáveis de ambiente

## 📊 Monitoramento

- Endpoint de health check para status do serviço
- Logs estruturados em JSON
- Informações sobre carregamento do modelo
- Tracking de erros de predição

## 🐛 Resolução de Problemas

### Problemas Comuns

1. **Modelo não carrega**:

   - Verifique se o caminho do modelo está correto
   - Confirme se o arquivo do modelo existe
   - Verifique as permissões do arquivo

2. **Erro nas predições**:

   - Confirme o formato dos dados de entrada
   - Verifique se todas as features necessárias estão presentes
   - Consulte os logs para mais detalhes

3. **Servidor não inicia**:
   - Verifique se a porta está disponível
   - Confirme se todas as dependências estão instaladas
   - Verifique os logs de inicialização

## 📝 Notas de Desenvolvimento

- O serviço usa FastAPI para performance máxima
- Implementação assíncrona para melhor escalabilidade
- Sistema de logging estruturado para facilitar debugging
- Design modular para fácil manutenção e extensão
