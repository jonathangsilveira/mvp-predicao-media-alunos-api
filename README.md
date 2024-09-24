# Classificação de média com base em performance de estudantes - API

Esta API (Application Programming Interface) é um MVP para prever a classificação da média de estudantes utilizando como entrada dados demográficos, hábitos de estudo, envolvimento dos pais na educação e atividades extracurriculares.
A previsão é feita com base em um modelo pré-treinado de _Machine Learning_ com base no _dataset_ disponível em [Kaggle](https://www.kaggle.com/code/annastasy/predicting-students-grades/input).
Tem como objetivo validar os conteúdos passados nas disciplinas da sprint de Qualidade de Software, Segurança e Sistemas Inteligentes da especialização em Eng. Software, pela PUC-Rio.

# Requisitos

- **Integração do modelo de machine learning com a aplicação full stack:** a aplicação deverá fazer a carga do arquivo do modelo de machine learning no back-end, possibilitar a entrada de novos dados no front-end e exibir o resultado da predição na tela.
- **Teste automatizado do modelo no back-end da aplicação:** o teste deverá assegurar que o modelo atenda aos requisitos de desempenho estabelecidos.
- **Código limpo, capricho e qualidade dos códigos:** seu código deve estar legível e organizado, utilizando as boas práticas de codificação em Python.

# Funcionalidades

Este componente da arquitetura persiste as informações sobre as ações do usuário em relação a filmes fornecidos pelo componente A:

- Predição de média do estudante.
- Listagem de registros de classificações.
- Exclusão de registros de classificação.

# Arquitetura da aplicação

![fluxograma](https://github.com/jonathangsilveira/mvp-predicao-media-alunos-api/blob/main/diagram/mvp-predicao-media-aluno-arch-diagram.svg)

# Notebook

O processo de treinamento do modelo está documentado neste [notebook](https://github.com/jonathangsilveira/mvp-predicao-media-alunos-api/blob/main/machine_learning/mvp_predicao_media_alunos_notebook.ipynb).

# Tecnologias

- Python 3.11.8;
- SQLite (Persistencia em banco de dados);
- Flask;
- SQLALchemy;
- Protocolo de comunicação Rest/JSON
- Documentação da API no padrao Swagger.
- Jupyter
- Pytest

# Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Este comando criar o ambiente virtual para o projeto:

```
py -3 -m venv .venv
```

Este comando ativa o ambiente virtual para o terminal:

```
.\.venv\Scripts\activate
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

Para executar a API basta executar:

```
flask --app .\app\app.py  run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
flask --app .\app\app.py  run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/api/](http://localhost:5000/api) no navegador para verificar o status da API em execução.

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker buildx build -t  mvp-predicao-media-alunos-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000  mvp-predicao-media-alunos-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/api/](http://localhost:5000/api/) no navegador.
