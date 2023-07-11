Ferramenta de Enumeração Rápida utilizando Shodan
=================================================

Este é um script Python desenvolvido para auxiliar no processo de reconhecimento durante um teste de penetração. Durante uma colaboração com a equipe da PROOF, identifiquei a necessidade de uma ferramenta que realizasse uma enumeração inicial rápida enquanto outras ferramentas, como o nmap, estivessem em execução. Com base nessa necessidade, criei este script que utiliza os dados disponíveis no Shodan para realizar uma enumeração rápida, aproveitando as informações já coletadas pela plataforma.

Shodan e seu uso
----------------

O Shodan é um mecanismo de busca que permite encontrar dispositivos conectados à Internet, incluindo servidores, câmeras IP, roteadores e muito mais. Diferente dos motores de busca convencionais, o Shodan se concentra em encontrar dispositivos específicos, em vez de páginas da web. Ele indexa informações sobre os serviços em execução nos dispositivos, como portas abertas, banners e outras informações detalhadas. Isso pode ser extremamente útil para os profissionais de segurança, pois permite identificar alvos potenciais e avaliar a exposição de dispositivos conectados à Internet.

História
--------

Durante a realização de um teste de penetração em parceria com a equipe da PROOF, deparei-me com a necessidade de uma ferramenta que fornecesse uma enumeração inicial rápida enquanto outras ferramentas estavam em execução. Essa enumeração inicial poderia fornecer informações valiosas que poderiam ser usadas para direcionar os esforços durante o teste.

Foi então que decidi criar esse script Python, que utiliza os dados disponíveis no Shodan para realizar uma enumeração inicial rápida. Ele aproveita as informações já coletadas pela plataforma Shodan, como portas abertas e detalhes da organização proprietária dos dispositivos. Essas informações são fundamentais para encontrar outros hosts pertencentes à mesma organização e expostos na Internet. Além disso, o script realiza a verificação de hosts ativos para fornecer um panorama mais atualizado.

O script armazena todas as informações coletadas de forma organizada em uma planilha, permitindo uma fácil análise e compreensão dos resultados. Ele também vai incluir a funcionalidade de tirar prints da página inicial dos sites encontrados, facilitando a visualização e a posterior análise dos alvos identificados.

Funcionalidades atuais e futuras
--------------------------------

As principais funcionalidades atuais do script são:

*   Enumeração rápida de hosts utilizando o Shodan.
*   Levantamento de portas abertas e detalhes da organização proprietária.
*   Verificação de hosts ativos.
*   Lista de Vulnerabilidades presentes nos serviços que são de conhecimento do Shodan
*   Armazenamento das informações em uma planilha.
*   Armazenamento dos Jsons das consultas realizadas
*   Possibilidade de escolha do formato de saida CSV ou XLSX

Funcionalidades planejadas para futuras versões do script incluem:

*   Implementação da função para acessar os hosts e capturar prints da página inicial dos sites encontrados.
*   Inclusão do protocolo utilizado em cada porta identificada.
*   Inclusão do Banner do serviços encontrados
*   Coleta de links conhecidos pelo The wayBack Machine de todos os alvos fornecidos

Essas melhorias visam fornecer uma visão mais abrangente e facilitar o processo de reconhecimento durante um teste de penetração.

Utilização do script
--------------------

1.  Certifique-se de ter o Python instalado no seu sistema.
2.  Faça o download do código-fonte do script a partir do seguinte repositório: \[URL DO REPOSITÓRIO\].
3.  Abra o terminal ou prompt de comando e navegue até o diretório onde o script foi salvo.
4.  Execute o script utilizando o seguinte comando:
    
      
    ```bash
    python3 resolver-banners.py  -h
    ```

Aqui estão algumas capturas de tela que demonstram o uso do script:

1.  Executando o script com a opção `-b` para exibir todos os banners disponíveis:
    
    ![Exibição de banners](screenshots/banners.png)
    
2.  Executando o script com os argumentos de arquivo de entrada e chave de API:
    
    ![Executando com arquivo de entrada e chave de API](screenshots/execution.png)
    
3.  Resultados salvos em uma planilha (formato XLSX ou CSV):
    
    ![Planilha de resultados](screenshots/results.xlsx)
    

O processo de reconhecimento é uma etapa essencial em um teste de penetração. Ele permite coletar informações valiosas sobre os alvos, identificar possíveis vulnerabilidades e traçar estratégias adequadas para o restante do teste. A ferramenta desenvolvida visa automatizar parte desse processo, fornecendo uma enumeração rápida e organizada dos hosts, facilitando a análise posterior.

Note que essa é uma versão inicial da ferramenta, e novas funcionalidades e aprimoramentos estão planejados para futuras versões.

Agradecimentos
--------------------

Agradeço pela colaboração do meu colega Gabriel Comonian que me ajudou com os testes iniciais do script e ao chat GPT pela ajuda com o desenvolvimento