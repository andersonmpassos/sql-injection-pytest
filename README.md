Análise de Vulnerabilidade com SQL Injection e Testes Automatizados

Este projeto foi desenvolvido como parte da disciplina de Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas. O objetivo é demonstrar, de forma prática, como uma vulnerabilidade de SQL Injection pode ocorrer em um sistema e como ela pode ser identificada e corrigida utilizando testes automatizados.

Objetivo

O trabalho busca simular um cenário real de falha de segurança em um sistema de autenticação, permitindo compreender como ataques podem explorar vulnerabilidades e como boas práticas de desenvolvimento podem evitar esse tipo de problema.

Tecnologias Utilizadas
Python 3
SQLite
Pytest
Estrutura do Projeto
banco.py: responsável pela criação do banco de dados e da tabela de usuários
login_vulneravel.py: implementação de autenticação vulnerável a SQL Injection
login_seguro.py: versão corrigida utilizando consultas parametrizadas
test_login.py: teste automatizado que comprova a vulnerabilidade
test_login_seguro.py: teste automatizado que valida a correção
Funcionamento

O sistema simula um processo de login simples. Na versão vulnerável, a consulta SQL é construída por concatenação de strings, permitindo a inserção de comandos maliciosos. Isso possibilita que um usuário consiga acesso sem fornecer credenciais válidas.

O teste automatizado executa um ataque de SQL Injection e verifica se o acesso é concedido. Como esperado, o sistema vulnerável permite a autenticação indevida.

Na versão corrigida, a consulta é feita utilizando parâmetros, impedindo a execução de código malicioso. Um novo teste é executado, demonstrando que o ataque não é mais possível.

Como Executar
Criar e ativar um ambiente virtual:
python -m venv venv
venv\Scripts\activate
Instalar as dependências:
pip install pytest
Executar os testes:
pytest
Resultados Esperados

A execução dos testes deve apresentar dois cenários:

O teste do sistema vulnerável deve passar, indicando que a falha existe
O teste do sistema seguro também deve passar, confirmando que a vulnerabilidade foi corrigida
Conclusão

O projeto evidencia como uma implementação simples pode introduzir falhas críticas de segurança. Também demonstra a importância de testes automatizados no processo de desenvolvimento, permitindo identificar e corrigir vulnerabilidades de forma eficiente.

A utilização de consultas parametrizadas se mostrou essencial para garantir a segurança do sistema, reforçando a necessidade de boas práticas desde as etapas iniciais do desenvolvimento.