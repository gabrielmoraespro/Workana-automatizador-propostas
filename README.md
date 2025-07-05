# 🚀 Gerador de Propostas Workana

Uma aplicação web inteligente para criar propostas comerciais personalizadas e mensagens de interesse profissionais para freelancers no Workana, powered by IA.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📸 Preview

```
🎯 Gerador de Propostas Workana
├── 📩 Mensagem de Interesse
│   ├── Nome do Cliente
│   ├── Descrição do Projeto
│   ├── Comentário Específico
│   └── Pergunta de Abertura
└── 📋 Proposta Personalizada
    ├── Informações Básicas
    ├── Resumo do Problema
    ├── Sua Solução
    ├── Microgarantias
    ├── Preço e Prazo
    └── Call to Action
```

## ✨ Funcionalidades

### 📩 **Mensagem de Interesse**
- Gera primeira mensagem profissional para despertar interesse
- Personalização com nome do cliente e detalhes do projeto
- Comentários específicos demonstrando compreensão
- Pergunta engajadora para iniciar conversa
- Ideal para primeiros contatos

### 📋 **Proposta Completa**
- Proposta comercial estruturada e convincente
- Análise automática do problema do cliente
- Apresentação de soluções e diferenciais
- Inclusão de garantias e credibilidade
- Definição clara de preços e prazos
- Call to action persuasivo

### 🤖 **Inteligência Artificial**
- Integração com OpenRouter API
- Modelo Claude-3-Haiku para geração otimizada
- Prompts especializados em propostas comerciais
- Tom profissional, empático e objetivo
- Resultados personalizados para cada cliente

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)

### Passo a passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/workana-proposal-generator.git
cd workana-proposal-generator
```

2. **Instale as dependências**
```bash
pip install streamlit requests
```

3. **Configure a API Key**
```python
# No arquivo app.py, linha 13
OPENROUTER_API_KEY = "sua-api-key-aqui"
```

4. **Execute a aplicação**
```bash
streamlit run app.py
```

5. **Acesse no navegador**
```
http://localhost:8501
```

## 🚀 Como Usar

### Para Mensagem de Interesse:

1. **Preencha os campos obrigatórios:**
   - Nome do cliente
   - Descrição do projeto (copie do Workana)

2. **Adicione informações extras:**
   - Comentário específico sobre o projeto
   - Pergunta de abertura para engajamento

3. **Clique em "Gerar Mensagem de Interesse"**

4. **Copie o resultado** e envie no Workana

### Para Proposta Completa:

1. **Informações básicas:**
   - Nome do cliente
   - Descrição completa do projeto
   - Comentário específico

2. **Detalhe a solução:**
   - Resumo do problema do cliente
   - Como você resolve (diferenciais)
   - Microgarantias oferecidas

3. **Finalize com:**
   - Preço e prazo sugeridos
   - Call to action convincente

4. **Clique em "Gerar Proposta Completa"**

5. **Revise e envie** no Workana

## 💡 Dicas de Sucesso

### ✅ **Melhores Práticas:**
- **Seja específico** nos comentários sobre o projeto
- **Demonstre conhecimento** da área do cliente
- **Personalize** cada proposta para o projeto
- **Use linguagem profissional** mas acessível
- **Inclua garantias** para gerar confiança

### 🎯 **Para Mensagens de Interesse:**
- Mantenha **conciso** (100-150 palavras)
- **Termine sempre** com pergunta engajadora
- **Referencie detalhes** específicos do projeto
- **Demonstre interesse** genuíno no trabalho

### 📋 **Para Propostas Completas:**
- **Estruture bem** a apresentação da solução
- **Destaque seus diferenciais** competitivos
- **Seja claro** sobre preços e prazos
- **Inclua call to action** convincente

## 🔧 Personalização

### Modificar Prompts da IA:
```python
# Função generate_message_prompt() - linha 65
# Função generate_proposal_prompt() - linha 80
```

### Customizar Interface:
```python
# CSS personalizado - linha 95
# Modificar cores, fontes e layout
```

### Adicionar Novos Campos:
```python
# Seções das tabs - linha 180 e 220
# Adicionar novos st.text_input() ou st.text_area()
```

## 🎨 Interface

### **Design Moderno:**
- Gradientes profissionais
- Botões animados com hover effects
- Layout responsivo em duas colunas
- Área de resultado destacada

### **Organização Intuitiva:**
- Duas abas principais claramente separadas
- Campos organizados por categorias
- Sidebar com instruções e dicas
- Feedback visual durante geração

## 📊 Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.8+ | Linguagem principal |
| **Streamlit** | 1.28+ | Framework web |
| **OpenRouter** | API | Integração com IA |
| **Claude-3-Haiku** | Model | Geração de conteúdo |
| **Requests** | 2.31+ | Requisições HTTP |

## 🔐 Segurança

- **API Key** armazenada em variável (mova para .env em produção)
- **Validação** de campos obrigatórios
- **Tratamento** de erros da API
- **Limite** de tokens para controle de custos

## 📈 Melhorias Futuras

- [ ] Sistema de templates personalizáveis
- [ ] Histórico de propostas geradas
- [ ] Integração com banco de dados
- [ ] Sistema de usuários e login
- [ ] Métricas de sucesso das propostas
- [ ] Exportação em PDF
- [ ] Integração direta com Workana API

## 🤝 Contribuindo

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🆘 Suporte

### Problemas Comuns:

**❌ Erro na API:**
```
Erro na geração: 401 Unauthorized
```
**✅ Solução:** Verifique se a API key está correta

**❌ Módulo não encontrado:**
```
ModuleNotFoundError: No module named 'streamlit'
```
**✅ Solução:** Execute `pip install streamlit requests`

**❌ Porta em uso:**
```
Port 8501 is already in use
```
**✅ Solução:** Use `streamlit run app.py --server.port 8502`

### Contato:
- 📧 Email: seu-email@exemplo.com
- 💬 Issues: [GitHub Issues](https://github.com/seu-usuario/workana-proposal-generator/issues)
- 📱 Telegram: @seu_usuario

## 🎯 Resultados Esperados

### **Antes:**
- ⏰ 30-45 minutos por proposta
- 📝 Propostas genéricas
- 🎯 Baixa taxa de conversão
- 😰 Estresse na criação

### **Depois:**
- ⚡ 2-5 minutos por proposta
- 🎯 Propostas personalizadas
- 📈 Maior taxa de conversão
- 😊 Processo automatizado

---

**🚀 Transforme seu processo de vendas no Workana com IA!**

*Feito com ❤️ para freelancers que querem vender mais e melhor.*
