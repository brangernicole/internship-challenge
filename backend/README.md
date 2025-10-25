# Backend - API MMC

API Django que calcula o Mínimo Múltiplo Comum (MMC) de um intervalo de números.

## Setup

### Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
```

### Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
```

Servidor rodando em: **http://localhost:8000/api/lcm/**

## Endpoint

**GET** `http://localhost:8000/api/lcm/?x=1&y=10`  
**POST** `http://localhost:8000/api/lcm/` com `{"x": 1, "y": 10}`

**Response:**
```json
{
    "x": 1,
    "y": 10,
    "result": 2520
}
```

## Exemplo Principal

Entrada: x=1, y=10  
Saída: 2520 ✓

Verificação: 2520 é divisível por 1,2,3,4,5,6,7,8,9,10

## Testes

```bash
python manage.py test
python test_api.py  # Teste manual
```

## Estrutura

```
api/
├── views.py       - Lógica do cálculo MMC
├── serializers.py - Validação
├── urls.py        - Rotas
└── tests.py       - Testes
```

## Algoritmo

MMC(a,b) = (a × b) / MDC(a,b) usando Algoritmo de Euclides
