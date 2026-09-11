# Toolkit de collabs · framework de aplicação

Versão navegável do framework integrativo de gestão de collabs entre marcas, desenvolvido na dissertação **"Collab de dentro para fora: uma investigação qualitativa sobre como são construídas as collabs entre grandes marcas no Brasil"** (Douglas R. Bocalão, Mestrado Profissional em Administração, FGV EAESP, 2026. Orientador: Prof. Dr. Felipe Zambaldi).

**Acesse:** https://douglasbocalao.github.io/collab/

## O que é

O toolkit organiza em cinco etapas o processo que dez organizações brasileiras seguem para identificar, estruturar, cocriar, lançar e aprender com uma collab. Para cada etapa são apresentados:

- o que é feito e como é feito;
- as áreas envolvidas;
- as ferramentas utilizadas;
- materiais de apoio;
- um checklist e o critério de passagem para a etapa seguinte.

A tela inicial traz apenas as cinco etapas e o progresso do checklist. O material de referência (definição de collab, fatores críticos, lentes teóricas, matriz de capacidades por etapa, fonte e limites) fica recolhido em acordeões ao final da página.

O toolkit não identifica entrevistados nem empresas.

## Procedência do conteúdo

O conteúdo das cinco etapas vem do Quadro 5 da dissertação, item 4.8.

Duas ressalvas importantes, as mesmas registradas no documento:

- **É material de apoio, não artefato validado.** O framework é uma sistematização descritiva das práticas observadas em dez casos, não um artefato submetido a ciclos de construção e avaliação. Sua validação empírica permanece como agenda de pesquisa futura.
- **Os "exemplos de mercado" indicados nas ferramentas** (Brandwatch, Miro, Looker Studio e outros) são acréscimo de apoio à aplicação, feito pelo autor. Não foram mencionados pelos entrevistados nem derivam da pesquisa.

## Características técnicas

Arquivo único, sem dependência externa, sem build. Funciona offline com duplo clique no `index.html`.

- Tema claro e escuro, acompanhando a preferência do sistema, com alternância manual.
- Progresso do checklist salvo no navegador (`localStorage`, chave `collab-toolkit-v3`). É por navegador e por endereço: não sincroniza entre dispositivos.
- Exportação do checklist em Markdown.
- Navegação por teclado: `1` a `5` para as etapas, `0`, `h` ou `Esc` para o início, setas para avançar e voltar.
- Deep link por etapa: `#etapa-3`.
- Botão de retomada na home ("continuar na etapa N"), limpeza do checklist por etapa e geral.
- Funciona mesmo quando o navegador bloqueia `localStorage`: nesse caso o progresso não é salvo, mas a interface não quebra.

## Como atualizar

Edite o `index.html` e faça commit na branch principal. O GitHub Pages publica em seguida.

Os **materiais de apoio** de cada etapa têm slots vazios, marcados com `"#"` na lista `mats` dentro da constante `DATA`. Enquanto ficarem com `#`, aparecem na interface como pendentes.

## Como citar

> BOCALÃO, Douglas R. **Toolkit de collabs: framework de aplicação**. Versão 1.0. São Paulo, 2026. Disponível em: https://douglasbocalao.github.io/collab/. Acesso em: DATA.

A versão arquivada com DOI, quando publicada no Zenodo, é a referência preferencial para citação acadêmica.

## Licença

Sugestão: Creative Commons Atribuição 4.0 Internacional (CC BY 4.0), que permite uso e adaptação com atribuição. Ajuste conforme sua preferência antes de publicar.
