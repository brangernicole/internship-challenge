# Salutho - Desafio de Estágio para Desenvolvedor de Software

## Visão Geral

Este desafio consiste em desenvolver uma aplicação em React que interage com uma API Django para calcular o menor número inteiro divisível por todos os números dentro de um intervalo específico. Você deverá demonstrar competência tanto em desenvolvimento frontend com React quanto em backend com Django.

## Requisitos do Projeto

### Funcionalidades

- **Frontend:**

  - [x] A aplicação deve ter um formulário com dois campos de entrada para que o usuário possa inserir os números que definem o intervalo (x a y).
  - [x] Os números inseridos devem ser validados para garantir que:
    - [x] Ambos os números são inteiros positivos.
    - [x] O valor de x deve ser menor que y.
    - [x] O intervalo não deve ser menor ou igual a zero.
  - [x] Após a inserção e validação dos números, o frontend deve fazer uma requisição à API Django para obter o resultado do cálculo.
  - [x] A resposta deve ser exibida na mesma página.

- **Backend (API Django):**
  - [x] Desenvolver uma rota que receba dois números (x e y) via solicitação HTTP.
  - [x] A API deve calcular o menor número inteiro que é divisível por todos os números do intervalo x a y.
  - [x] Retornar o resultado para o frontend.

### Tecnologias

- **Frontend:** React
- **Backend:** Django
- **Estilização:** Escolha livre entre CSS puro, pré-processadores (como SASS ou LESS) ou bibliotecas de componentes estilizados (como styled-components).

### Critérios de Avaliação

- Corretude do cálculo realizado pela API.
- Qualidade do código em ambas as partes, frontend e backend.
- Implementação e eficácia das validações de entrada no frontend.
- Design e usabilidade da interface do usuário.
- Integração eficiente entre React e Django.

## Exemplo de Teste

Para garantir a corretude do seu código, utilize o seguinte exemplo:

- **Entrada:** 1 e 10
- **Saída esperada:** 2520

### Verificação:

2520 é o menor número divisível por todos os números de 1 a 10, como demonstrado abaixo:

- 2520 / 1 = 2520 (Divisível)
- 2520 / 2 = 1260 (Divisível)
- 2520 / 3 = 840 (Divisível)
- 2520 / 4 = 630 (Divisível)
- 2520 / 5 = 504 (Divisível)
- 2520 / 6 = 420 (Divisível)
- 2520 / 7 = 360 (Divisível)
- 2520 / 8 = 315 (Divisível)
- 2520 / 9 = 280 (Divisível)
- 2520 / 10 = 252 (Divisível)

Assegure-se de que sua aplicação calcula corretamente este exemplo como parte do processo de desenvolvimento.

## 🚀 Setup e Execução

Este projeto está dividido em duas partes: **Backend (Django)** e **Frontend (React + Vite)**.

### Pré-requisitos

- **Python 3.8+** (para o backend)
- **Node.js 16+** e **npm** (para o frontend)
- **Git**

---

## 📋 Backend - API Django

### 1️⃣ Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd internship-challenge/backend
```

### 2️⃣ Criar Ambiente Virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar Migrações

```bash
python manage.py migrate --run-syncdb
```

### 5️⃣ Executar o Servidor Django

```bash
python manage.py runserver 0.0.0.0:8000
```

O servidor estará disponível em: **http://localhost:8000**

#### Endpoint da API

- **GET:** `http://localhost:8000/api/lcm/?x=1&y=10`
- **POST:** `http://localhost:8000/api/lcm/` com corpo JSON: `{"x": 1, "y": 10}`

**Resposta esperada:**

```json
{
  "x": 1,
  "y": 10,
  "result": 2520
}
```

### 6️⃣ Executar Testes (Opcional)

```bash
python manage.py test
```

---

## 🎨 Frontend - React + Vite

### 1️⃣ Navegar para a Pasta Frontend

```bash
cd ../frontend
```

### 2️⃣ Instalar Dependências

```bash
npm install
```

### 3️⃣ Executar em Modo Desenvolvimento

```bash
npm run dev
```

A aplicação estará disponível em: **http://localhost:5173**

### 4️⃣ Build para Produção (Opcional)

```bash
npm run build
```

A versão otimizada será criada na pasta `dist/`.

---

## 🔗 Conectando Backend e Frontend

1. **Certifique-se de que o servidor Django está rodando** em `http://localhost:8000/api/lcm/`
2. **Inicie o frontend** com `npm run dev`

## 📂 Estrutura do Projeto

```
internship-challenge/
├── backend/                    # API Django
│   ├── api/                   # Aplicação principal
│   │   ├── views.py          # Lógica do cálculo MMC
│   │   ├── serializers.py    # Validação de dados
│   │   ├── urls.py           # Rotas da API
│   │   ├── models.py         # Modelos (se houver)
│   │   └── tests.py          # Testes unitários
│   ├── config/               # Configurações Django
│   │   ├── settings.py       # Configurações principais
│   │   ├── urls.py           # URLs principais
│   │   └── wsgi.py           # WSGI para produção
│   ├── manage.py             # Gerenciador do Django
│   ├── requirements.txt      # Dependências Python
│   ├── db.sqlite3            # Banco de dados SQLite
│   └── README.md             # Documentação do backend
│
├── frontend/                  # Aplicação React + Vite
│   ├── src/
│   │   ├── components/       # Componentes React
│   │   │   ├── LCMForm.jsx  # Formulário principal
│   │   │   └── ui/          # Componentes UI reutilizáveis
│   │   ├── context/         # Context API
│   │   ├── App.jsx          # Componente raiz
│   │   └── main.jsx         # Entrada da aplicação
│   ├── package.json         # Dependências Node.js
│   ├── vite.config.js       # Configuração do Vite
│   ├── tailwind.config.cjs  # Configuração Tailwind CSS
│   └── README.md            # Documentação do frontend
│
└── README.md                 # Este arquivo

```

---

## 🛠️ Tecnologias Utilizadas

### Backend

- **Django 4.2.0** - Framework web Python
- **Django REST Framework 3.14.0** - API REST
- **Django CORS Headers 4.0.0** - Controle de CORS

### Frontend

- **React 18.2.0** - Biblioteca JavaScript
- **Vite 5.0.8** - Build tool ultra-rápido
- **Tailwind CSS 3.3.6** - Framework CSS utilitário
- **React Hook Form 7.45.1** - Gerenciamento de formulários
- **Zod 4.1.12** - Validação de schemas
- **Radix UI** - Componentes UI acessíveis

---

## ✅ Checklist de Funcionalidades

### Frontend

- ✅ Formulário com campos para x e y
- ✅ Validação de entrada (inteiros positivos, x < y)
- ✅ Requisição à API Django
- ✅ Exibição do resultado na página

### Backend

- ✅ Endpoint que recebe x e y
- ✅ Cálculo correto do MMC
- ✅ Retorno do resultado em JSON

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError" no Backend

```bash
# Certifique-se de estar na pasta backend e ambiente virtual ativado
pip install -r requirements.txt
```

### Erro: "CORS error" no Frontend

- Certifique-se de que Django está rodando com CORS ativado
- Verifique `settings.py` no backend para `CORS_ALLOWED_ORIGINS`

### Erro: "Port 8000 already in use"

```bash
# Use uma porta diferente
python manage.py runserver 0.0.0.0:8001
```

### Erro: "Port 5173 already in use" (Frontend)

```bash
npm run dev -- --port 5174
```

---
