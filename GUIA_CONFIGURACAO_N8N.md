# 🤖 Guia de Configuração — Nola Bot (N8N + Groq + Google Sheets)

> **Tempo estimado:** 30–45 minutos para montar tudo do zero.

---

## PASSO 1 — Criar conta no Groq (API de IA gratuita)

1. Acesse [https://console.groq.com](https://console.groq.com)
2. Clique em **"Sign Up"** e crie sua conta (pode usar o Google)
3. No painel, vá em **"API Keys"** → **"Create API Key"**
4. Dê um nome (ex: `nola-bot`) e copie a chave gerada
5. **Guarde essa chave** — você vai precisar no Passo 3

---

## PASSO 2 — Criar conta no N8N Cloud

1. Acesse [https://app.n8n.cloud](https://app.n8n.cloud)
2. Clique em **"Get started for free"**
3. Crie sua conta e acesse o painel
4. Você verá o editor visual do N8N (canvas em branco)

---

## PASSO 3 — Configurar o Google Sheets (Base de Conhecimento)

### 3.1 — Criar a planilha
1. Acesse [https://sheets.google.com](https://sheets.google.com)
2. Crie uma nova planilha e nomeie como **"Base de Conhecimento - Nola"**
3. Na primeira aba, adicione os cabeçalhos na linha 1:
   ```
   ID | Categoria | Pergunta | Resposta | Tags
   ```
4. Importe o arquivo `base_conhecimento_nola.csv`:
   - Clique em **Arquivo → Importar → Upload**
   - Selecione o arquivo CSV
   - Escolha **"Substituir planilha atual"** e confirme

### 3.2 — Copiar o ID da planilha
Na URL da planilha, copie o ID que aparece entre `/d/` e `/edit`:
```
https://docs.google.com/spreadsheets/d/ESTE_ID_AQUI/edit
```
**Guarde esse ID** — você vai precisar no Passo 5.

---

## PASSO 4 — Importar o Workflow no N8N

1. No N8N, clique no menu de hambúrguer (☰) no canto superior esquerdo
2. Clique em **"Workflows"** → **"Add workflow"** → **"Import from file"**
3. Selecione o arquivo `workflow_nola_chatbot.json`
4. O fluxo será importado com todos os 4 nós configurados

---

## PASSO 5 — Conectar as Credenciais

### 5.1 — Conectar o Google Sheets
1. Clique no nó **"Buscar Base de Conhecimento"** (ícone do Sheets)
2. Em **"Credential"**, clique em **"Create new credential"**
3. Selecione **"OAuth2"** e faça login com sua conta Google
4. Autorize o acesso ao Google Sheets
5. No campo **"Document ID"**, cole o ID copiado no Passo 3.2
6. Em **"Sheet Name"**, selecione **"Base de Conhecimento"** (ou a aba que aparecer)

### 5.2 — Conectar o Groq
1. Clique no nó **"Groq Chat Model"**
2. Em **"Credential"**, clique em **"Create new credential"**
3. Cole a **API Key do Groq** copiada no Passo 1
4. Clique em **"Save"**

---

## PASSO 6 — Ativar e Testar

1. Clique no botão **"Activate"** (toggle no canto superior direito do workflow)
2. Clique no nó **"When chat message received"**
3. Clique em **"Open chat"** — uma janela de chat abrirá
4. Envie uma mensagem de teste, por exemplo:
   - *"Esqueci minha senha, como faço para recuperar?"*
   - *"Como cadastrar um produto no cardápio?"*
   - *"Minha impressora parou de imprimir, o que fazer?"*
5. O bot deve consultar o Sheets e responder com base na base de conhecimento

---

## PASSO 7 — Verificar que o Sheets está sendo chamado

Para o vídeo, é importante mostrar que a integração com o Sheets funciona:

1. Com o chat aberto, envie uma pergunta
2. Volte para o canvas do N8N — você verá as execuções aparecendo nos nós
3. Clique em qualquer execução para ver os dados que passaram por ela
4. No nó **"Buscar Base de Conhecimento"**, você verá as linhas do Sheets retornadas
5. Isso prova que o bot está consultando o Google Sheets em tempo real

---

## DICAS PARA O VÍDEO (5 minutos)

Sugestão de roteiro:

| Tempo | O que mostrar |
|-------|---------------|
| 0:00–0:30 | Apresentar o contexto: o problema de escala no suporte de CS |
| 0:30–1:30 | Mostrar a planilha do Google Sheets aberta (a base de conhecimento) |
| 1:30–3:00 | Mostrar o fluxo no N8N explicando cada nó brevemente |
| 3:00–4:30 | Demonstração ao vivo: 3 perguntas no chat → bot responde |
| 4:30–5:00 | Mostrar no N8N que o Sheets foi consultado (log de execução) |

**Perguntas recomendadas para demo:**
- "Como recupero minha senha?" *(resposta clara e direta)*
- "Minha impressora não imprime, o que faço?" *(resposta com checklist)*
- "Quero saber sobre integração com maquininha" *(resposta mais elaborada)*
- Faça uma pergunta FORA da base: "Como faço para integrar com iFood?" *(bot escalará para especialista — mostra que ele não inventa respostas)*

---

## SOLUÇÃO DE PROBLEMAS

| Problema | Solução |
|----------|---------|
| Bot não responde | Verifique se o workflow está **Activated** (toggle verde) |
| Erro no Google Sheets | Confirme o ID da planilha e que a credencial OAuth está autorizada |
| Erro no Groq | Verifique se a API Key está correta e sem espaços |
| Resposta genérica demais | Verifique no log de execução se os dados do Sheets chegaram ao Code Node |

---

*Qualquer dúvida, revise cada passo com calma. O N8N tem logs detalhados de cada execução que facilitam muito o debug.*
