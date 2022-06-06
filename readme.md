# Descrição

A página inicial (index) contém um gráfico com filtros por datas (Com limite de 5 dias) e moedas (USD, BRL, EUR e JPY), pode acessado por:
```
GET http://localhost:8000
```

O endpoint principal, que preenche o gráfico e salva as informações buscadas no banco de dados pode ser encontrado em:
```
GET http://localhost:8000/cotacao/get-rate/

*query_params obrigatórios: {
    'currency_from': 'USD',
    'currency_to': 'BRL',
    'start_date': '01/01/2000',
    'end_date': '05/01/2000',
}
```

A listagem de endpoints para consulta dos registros feitos no banco de dados podem ser encontrado em:
```
GET http://localhost:8000/cotacao/
```

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

Copiar o arquivo *.env.sample* na pasta core, removendo o *.sample* no final, para ficar *.env* e então preencher com as devidas variáveis de ambiente
```bash
cp core/.env.sample core/.env
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

# Testes
```bash
python manage.py test
```

Para executar os testes com sucesso, é necessário copiar os arquivos estáticos (principalmente por causa do favicon.ico)
```bash
python manage.py collectstatic
```
