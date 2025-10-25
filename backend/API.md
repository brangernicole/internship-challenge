## Backend - API MMC

API Django que calcula o Mínimo Múltiplo Comum (MMC) de um intervalo.

### Setup

```bash
setup.bat  # Windows
bash setup.sh  # Linux/Mac
```

### Rodar

```bash
venv\Scripts\activate  # Windows
python manage.py runserver
```

### Usar

- **GET**: `http://localhost:8000/api/lcm/?x=1&y=10`
- **POST**: `/api/lcm/` com `{"x": 1, "y": 10}`

**Response**: `{"x": 1, "y": 10, "result": 2520}`

### Testes

```bash
python manage.py test
```

### Exemplo Principal

Entrada: x=1, y=10 → Saída: 2520 ✓
(2520 é divisível por 1,2,3,4,5,6,7,8,9,10)

### Estrutura

```
api/views.py   - Lógica MMC
api/tests.py   - Testes
```
