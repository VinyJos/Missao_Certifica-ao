# Missao_Certifica-ao

![logo](Aspose.Words.9f9abab3-8257-428d-85ca-db27cd5b5774.001.png)

**Desenvolvimento Full Stack: Mundo 1** 

**Sistema de Agendamento de Ferramentas** 

Especificação de Requisitos e Documento do Projeto 

Semestre 2022.1 Turma xxxxxxx 

![](Aspose.Words.9f9abab3-8257-428d-85ca-db27cd5b5774.002.png)



|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |2 de 3 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |


||
| :- |
|**Stakeholder Principal** |
||
|Professor Roberto Maia (Mestre dos Magos) |


||
| :- |
|**Equipe do Projeto: Grupo 1** |
||
|**Nome** |**Matrícula** |**Atribuições** |
|Flávio Borges Nunes ||Desenvolvimento Backend, Dados, realizando as atividades xxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxx e apoio no desenvolvimento Frontend, realizando as atividades xxxxxxxxxxxxxxx. |
|João Gustavo Morielo ||Apoio no desenvolvimento do sistema (Backend, Frontend e Dados) e apoio na documentação do projeto. |
|Raila Nascimento Sousa |202204455331 |Levantamento dos requisitos, responsável pela documentação do projeto e apoio no desenvolvimento do sistema. |
|Vinícius José da Silva ||Desenvolvimento Frontend, realizando as atividades xxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxx e apoio no desenvolvimento Backend e Dados realizando as atividades xxxxxxxxx. |
![](Aspose.Words.9f9abab3-8257-428d-85ca-db27cd5b5774.003.png)

|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |3 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |
**Sumário** 

1. SOBRE O PROJETO  ........................................................................................................................................................ 1 
1. OBJETIVO DO DOCUMENTO  .......................................................................................................................................... 1 
1. REGRAS DE NEGÓCIOS .................................................................................................................................................. 1 
1. USUÁRIOS E DIAGRAMA DE CASO DE USO.................................................................................................................. 1 
1. REQUISITOS FUNCIONAIS  ............................................................................................................................................. 1 
1. REQUISITOS NÃO FUNCIONAIS  ..................................................................................................................................... 1 
1. INPUTS  ............................................................................................................................................................................. 1 
1. OUTPUTS  ......................................................................................................................................................................... 1 
1. FLUXO DOS PROCESSOS  .............................................................................................................................................. 1 
1. INTERFACE GRÁFICA  ..................................................................................................................................................... 1 
1. VÍDEO DE FUNCIONAMENTO DO SISTEMA  .................................................................................................................. 1 



|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |4 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |
1. **SOBRE O PROJETO** 

O projeto consiste no desenvolvimento de um Sistema de Agendamento de Ferramentas, que possibilitará aos técnicos de manutenção audiovisual, realizarem o agendamento de retirada e devolução de equipamentos. Será possível  ao responsável da central de ferramentaria realizar  a  gestão  do  sistema,  através  do  cadastro  e  consulta  de  todos  as  ferramentas existentes, consulta dos agendamentos e técnicos cadastrados. 

2. **OBJETIVO DO DOCUMENTO** 

O objetivo deste documento é especificar as regras e detalhar o processo de cadastro de técnico, cadastro de ferramenta, consulta de técnico, consulta de ferramenta, agendamento de ferramenta e devolução de ferramenta. 

3. **REGRAS DE NEGÓCIOS** 
1. Reserva com até 24hs de antecedência. 
1. Central de ferramentas precisa ter ao menos 1 unidade de cada ferramenta em estoque. 
1. As  solicitações  de  reserva  precisam  ser  enviadas  por  e-mail  para  o  responsável  da Central de Ferramentaria, com as informações do técnico responsável, ferramenta, data e hora da retirada e devolução. 
1. Cada ferramenta precisa ter um tempo máximo permitido para reserva. 
1. Todos os técnicos precisam ser cadastrados no sistema. 
1. Deve ser possível excluir o cadastro de Técnico e Ferramenta quando necessário. 
1. Reserva de ferramenta deve ficar associada ao técnico responsável pela retirada. 
1. Deve ser possível que o responsável pela Central de Ferramentaria realize a consulta de todas as ferramentas cadastradas, técnicos e agendamentos. 

|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |5 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |
**4.  USUÁRIOS E DIAGRAMA DE CASO DE USO** 

1. Responsável da Central de Ferramentas. 
1. Técnico de Manutenção. 

![](Aspose.Words.9f9abab3-8257-428d-85ca-db27cd5b5774.004.jpeg)

|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |6 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |
**5.  REQUISITOS FUNCIONAIS** 

1. Cadastro de acesso 
1. Login de usuário 
1. Cadastro do técnico, com validação através do CPF. 
1. Cadastro da ferramenta, com geração de código. 
1. Consulta da lista dos técnicos cadastrados. 
1. Exclusão de técnico cadastrado. 
1. Consulta da lista de ferramentas cadastradas. 
1. Exclusão de ferramenta cadastrada. 
1. Cadastro de agendamento de ferramenta, com técnico associado. 
1. Consulta da lista de agendamentos. 
1. Devolução de ferramenta, com exclusão na lista de agendamentos. 

**6.  REQUISITOS NÃO FUNCIONAIS** 

(todos  os  requisitos  não  funcionais  devem  ser  indicados.  ex:  quais  foram  as  escolhas realizadas que melhoraram o desempenho do programa? quais os itens de interação que melhoram a experiência do usuário com o programa - usabilidade/botões/formulário/etc) 

1. Sistema multiplataforma (Windows, Linux e MacOS). 
1. Desenvolvido na linguagem Python. 
1. Sistema deve ser executado na IDE PyCharm ou Visual Studio Code. 
1. A execução do sistema deve ser realizada com acesso à internet para instalação de diferentes bibliotecas. 
1. Após instalação de bibliotecas, deve ser possível o programa funcionar no modo oflline. 
1. Interface gráfica será desenvolvida através da biblioteca Tkinter. 
1. Tempo máximo de 60 segundos durante processamentos. 
1. Os dados imputados (técnico, ferramenta, agendamentos) serão salvos em arquivo CSV, integrado ao sistema. Será possível inserir, excluir, atualizar e consultar dados. 
1. Necessária a instalação dos seguintes pacotes para a execução do sistema: tkinter,csv shutil, tempfile. 

|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |7 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |
7. **INPUTS** 



|**Ferramentas** |**Técnico** |**Agenda** |
| - | - | - |
|Descrição da Ferramenta |CPF |Código |
|Fabricante |Nome |Descrição |
|Voltagem (110/220)|Telefone |Retirada |
|Tamanho |Turno |Devolução |
|Unidade de Media |Nome da equipe |Técnico |
|Tipo de Ferramenta (manual/mecânica/grande porte)|||
|Material da Ferramenta |||
|Tempo Máximo da Reserva |||
|Quantidade |||
8. **OUTPUTS** 

Os  dados  cadastrados  nos  módulos  ferramentas,  técnico  e  agenda,  serão  salvos respectivamente nos arquivos csv a seguir:** 

1. ferramentas.csv 
1. técnicos.csv 
1. agenda.csv 

As  permissões  de  consulta  dos  dados  acima  serão  disponibilizadas  para  os  usuários, conforme definido na seção 3 deste documento (Usuários e Diagrama de Caso de Uso). 

**9.  FLUXOS DOS PROCESSOS** 

1. **Cadastro de usuário** 

Fluxo principal de sucesso 

1. O sistema apresenta o formulário de cadastro de usuário; 
1. O convidado insere os dados como nome, login, senha,xxxx; 

|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |8 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |


3. O convidado clica em salvar; 
3. O sistema salva os dados no banco de dados (csv); 
3. O sistema avisa que o cadastro foi efetuado. 

Fluxo alternativo: Campo em banco 

iv.  O sistema informa que há campo em branco. 

Fluxo alternativo: Usuário já existente 

iv.  O sistema informa que o usuário informado já está cadastrado. 

2. **Login de usuário** 

Fluxo principal de sucesso 

1. O convidado insere os dados de usuário e senha; 
1. O convidado clica em entrar; 
1. O sistema direciona para a página inicial. 

Fluxo alternativo: Campo em banco 

iii.  O sistema informa que há campo em branco. 

Fluxo alternativo: Usuário não encontrado 

iii.  O sistema informa que o usuário não foi encontrado. 

3. **Cadastro do técnico, com validação através do CPF.** 

|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |9 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |


4. **Cadastro da ferramenta, com geração de código.** 
4. **Consulta da lista dos técnicos cadastrados.** 
4. **Exclusão de técnico cadastrado.** 
4. **Consulta da lista de ferramentas cadastradas.** 
4. **Exclusão de ferramenta cadastrada.** 
4. **Cadastro de agendamento de ferramenta, com técnico associado.** 
4. **Consulta da lista de agendamentos.** 
4. **Devolução de ferramenta, com exclusão na lista de agendamentos.** 



|*Titulo do Documento* |*Página* |
| - | - |
|**SISTEMA DE AGENDAMENTO DE FERRAMENTAS** |10 de 5 |
|*Código* |*Revisão* |*Data* |
|Especificação de Requisitos e Documento do Projeto\_001\_Rev.00 |0 |02/09/2022 |
10. **INTERFACE GRÁFICA** 

(print das telas com breve explicação) 

11. **VÍDEO DE FUNCIONAMENTO DO SISTEMA** (link do youtube)** 
![](Aspose.Words.9f9abab3-8257-428d-85ca-db27cd5b5774.005.png)
