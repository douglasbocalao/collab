# Toolkit de collabs · framework de aplicação

Versão navegável do framework integrativo de gestão de collabs entre marcas, desenvolvido na dissertação **"Collab de dentro para fora: uma investigação qualitativa sobre como são construídas as collabs entre grandes marcas no Brasil"** (Douglas R. Bocalão, Mestrado Profissional em Administração, FGV EAESP, 2026. Orientador: Prof. Dr. Felipe Zambaldi).

**Acesse:** https://douglasbocalao.github.io/collab/

**English version:** https://douglasbocalao.github.io/collab/eng/ (arquivo `eng/index.html`, mesmo CSS e mesma lógica, conteúdo traduzido). As duas páginas têm um botão PT/EN no cabeçalho. As manchetes da vitrine de notícias continuam em português nas duas, porque são links para a imprensa brasileira.

## O que é

O toolkit organiza em cinco etapas o processo que dez organizações brasileiras seguem para identificar, estruturar, cocriar, lançar e aprender com uma collab. Para cada etapa são apresentados:

- o que é feito;
- como é feito, com o nome de cada frente e um parágrafo de detalhamento;
- as áreas envolvidas;
- as ferramentas utilizadas;
- materiais de apoio;
- um checklist e o critério de passagem para a etapa seguinte.

A home tem diagramação de capa de revista: manchete, texto curto de apresentação, três números de resumo, dois painéis sobre o que conta como collab e quando ela faz sentido, e um índice das cinco etapas. O material de referência (fatores críticos, lentes teóricas, matriz de capacidades por etapa, fonte e limites) fica recolhido em acordeões.

Além das cinco etapas, o menu tem o **Guia resumido**, que reúne em uma página só os checklists, as ferramentas e as áreas de todas as etapas, com botões de baixar e imprimir. O cabeçalho dá acesso a **A pesquisa** (pergunta, método, lentes, conclusões e limites, em cerca de uma página) e a **O autor**.

Ao final da home há uma vitrine com as 20 publicações mais recentes sobre collabs no **Meio & Mensagem** e no **Propmark**, com imagem, título e link que abre em nova janela. É contexto de mercado, não material da pesquisa. A lista não inclui notícias que citem as empresas entrevistadas, para não reassociar o toolkit a elas.

O toolkit não identifica entrevistados nem empresas.

## Procedência do conteúdo

O conteúdo das cinco etapas vem do Quadro 5 da dissertação, item 4.8.

Duas ressalvas importantes, as mesmas registradas no documento:

- **É material de apoio, não artefato validado.** O framework é uma sistematização descritiva das práticas observadas em dez casos, não um artefato submetido a ciclos de construção e avaliação. Sua validação empírica permanece como agenda de pesquisa futura.
- **Os "exemplos de mercado" indicados nas ferramentas** (Brandwatch, Miro, Looker Studio e outros) são acréscimo de apoio à aplicação, feito pelo autor. Não foram mencionados pelos entrevistados nem derivam da pesquisa.

## Características técnicas

Arquivo único, sem build. Funciona com duplo clique no `index.html`. As dependências externas são as fontes do Google (Montserrat e Source Code Pro) e as imagens das notícias, servidas pelos próprios veículos. Sem internet a página cai para as fontes do sistema e os cards aparecem sem foto; o resto funciona normalmente.

A paleta e a tipografia vêm do relatório da Pesquisa de Clima da Ampfy (`~/Documents/CLAUDE/CLIMA/saida`): papel claro quente (`#F5F2EC`), branco nas superfícies, verde (`#5C7A47`) e vermelho (`#C74E32`) de apoio, linhas de 1px e cantos retos. DM Sans no texto, Montserrat 300 em caixa alta nos títulos, Source Code Pro nos rótulos, números e abas.

A cor de destaque não é o âmbar da Ampfy: no lugar dele entra turquesa `#2DD4BF` (token `--acc`), que mantém praticamente o mesmo contraste sobre a tinta quase preta (10,4:1 contra 11,2:1 do âmbar). Ela aparece na faixa do topo, na aba corrente, nos botões e como marca-texto nas frases-chave.

O tema segue a preferência do sistema, claro ou escuro. Não há botão de alternância.

- Tema claro e escuro, acompanhando a preferência do sistema.
- Contador de visitas por GoatCounter (`collab.goatcounter.com`), sem cookies e sem nada visível na página. O script fica antes do `</body>` nas duas versões, e cada idioma aparece como um caminho separado no painel.
- Progresso do checklist salvo no navegador (`localStorage`, chave `collab-toolkit-v3`). É por navegador e por endereço: não sincroniza entre dispositivos.
- Exportação do checklist em Markdown.
- Navegação por teclado: `1` a `5` para as etapas, `0`, `h` ou `Esc` para o início, setas para avançar e voltar.
- Deep link por seção: `#etapa-3`, `#guia`, `#pesquisa`, `#autor`, `#inicio`.
- Clique no título do cabeçalho volta ao início.
- O checklist aparece duas vezes (na etapa e no guia resumido) e os dois ficam sincronizados.
- Botão de retomada na home ("continuar na etapa N"), limpeza do checklist por etapa e geral.
- Funciona mesmo quando o navegador bloqueia `localStorage`: nesse caso o progresso não é salvo, mas a interface não quebra.

## Como atualizar

Edite o `index.html` e faça commit na branch principal. O GitHub Pages publica em seguida.

Em `DATA`, o campo `frentes` de cada etapa é uma lista de objetos `{ t, d }`, com o título da frente e o parágrafo de detalhe.

Os **materiais de apoio** de cada etapa têm slots vazios, marcados com `"#"` na lista `mats` dentro da constante `DATA`. Enquanto ficarem com `#`, aparecem com borda tracejada e sem link.

As notícias ficam na constante `NEWS`, no formato `[título, link, imagem, data, veículo]`, e a data do levantamento em `NEWS_DATA`. Para atualizar a vitrine, substitua essa lista: os dois veículos expõem a API do WordPress em `/wp-json/wp/v2/posts?search=collab&per_page=20&_embed=1`.

## Como citar

> BOCALÃO, Douglas R. **Toolkit de collabs: framework de aplicação**. Versão 1.0. São Paulo, 2026. Disponível em: https://douglasbocalao.github.io/collab/. Acesso em: DATA.

A versão arquivada com DOI, quando publicada no Zenodo, é a referência preferencial para citação acadêmica.

## Licença

Sugestão: Creative Commons Atribuição 4.0 Internacional (CC BY 4.0), que permite uso e adaptação com atribuição. Ajuste conforme sua preferência antes de publicar.
