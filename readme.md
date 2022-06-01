# Instalação
Criar ambiente virtual
```bash
python3 -m venv venv
```

Ativar o ambiente virtual
```bash
source venv/bin/activate
```

Instalar os pacotes python neste ambiente
```bash
pip install -r requirements.txt
```

# Execução
```bash
python manage.py runserver 0.0.0.0:8000
```

# Manutenção
Sempre que algum model/tabela do banco de dados sofrer uma alteração*, criar as migrações e executá-las
```bash
python manage.py makemigrations
python manage.py migrate
```

*: Executar também no momento inicial da instalação