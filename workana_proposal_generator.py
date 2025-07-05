import streamlit as st
import requests
import json
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Gerador de Propostas Workana",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuração da API OpenRouter
OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_with_ai(prompt, tipo_conteudo="proposta"):
    """Gera conteúdo usando a API do OpenRouter"""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = f"""
    Você é um redator profissional especialista em propostas comerciais para freelancers no Workana. 
    Sua tarefa é gerar {tipo_conteudo} personalizada, profissional e convincente.
    
    Características do seu estilo:
    - Tom profissional, empático e objetivo
    - Linguagem simples mas com autoridade
    - Foco em resultados e valor para o cliente
    - Estrutura clara e organizada
    - Call to action convincente
    
    Se for mensagem de interesse: seja conciso, demonstre interesse genuíno e termine com pergunta engajadora.
    Se for proposta completa: organize de forma fluida, destacue diferenciais e inclua garantias.
    """
    
    data = {
        "model": "anthropic/claude-3-haiku",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Erro na geração: {str(e)}"

def generate_message_prompt(nome_cliente, descricao_projeto, comentario_especifico, pergunta_abertura):
    """Cria prompt para mensagem de interesse"""
    return f"""
    Gere uma mensagem de interesse profissional para o Workana com base nas informações:
    
    Nome do Cliente: {nome_cliente}
    Descrição do Projeto: {descricao_projeto}
    Comentário Específico: {comentario_especifico}
    Pergunta de Abertura: {pergunta_abertura}
    
    Estrutura desejada:
    1. Saudação personalizada
    2. Referência específica ao projeto
    3. Comentário que demonstre compreensão
    4. Pergunta engajadora para iniciar conversa
    
    Mantenha entre 100-150 palavras, tom profissional mas caloroso.
    """

def generate_proposal_prompt(nome_cliente, descricao_projeto, comentario_especifico, 
                           resumo_problema, como_resolvo, microgarantias, preco_prazo, call_to_action):
    """Cria prompt para proposta completa"""
    return f"""
    Gere uma proposta comercial completa para o Workana com base nas informações:
    
    Nome do Cliente: {nome_cliente}
    Descrição do Projeto: {descricao_projeto}
    Comentário Específico: {comentario_especifico}
    Resumo do Problema: {resumo_problema}
    Como Resolvo: {como_resolvo}
    Microgarantias: {microgarantias}
    Preço e Prazo: {preco_prazo}
    Call to Action: {call_to_action}
    
    Estruture a proposta de forma fluida incluindo:
    1. Saudação personalizada
    2. Demonstração de compreensão do problema
    3. Apresentação da solução e diferenciais
    4. Garantias e credibilidade
    5. Investimento e prazo
    6. Call to action convincente
    
    Mantenha entre 200-300 palavras, tom profissional e convincente.
    """

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .tab-container {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .generated-content {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 1.5rem;
        border-radius: 5px;
        margin-top: 2rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🚀 Gerador de Propostas Workana</h1>
    <p>Crie mensagens e propostas profissionais com IA em segundos</p>
</div>
""", unsafe_allow_html=True)

# Tabs principais
tab1, tab2 = st.tabs(["📩 Mensagem de Interesse", "📋 Proposta Personalizada"])

with tab1:
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    
    st.header("💌 Mensagem de Interesse")
    st.markdown("*Crie uma primeira mensagem profissional para despertar o interesse do cliente*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome_cliente_msg = st.text_input("👤 Nome do Cliente", 
                                       placeholder="Ex: João Silva")
        
        descricao_projeto_msg = st.text_area("📝 Descrição do Projeto", 
                                           placeholder="Cole aqui a descrição completa do projeto do Workana...",
                                           height=100)
    
    with col2:
        comentario_especifico_msg = st.text_area("💭 Comentário Específico", 
                                                placeholder="Seu comentário personalizado sobre o projeto...",
                                                height=100)
        
        pergunta_abertura_msg = st.text_input("❓ Pergunta de Abertura", 
                                            placeholder="Ex: Qual é o prazo ideal para você?")
    
    if st.button("🎯 Gerar Mensagem de Interesse", key="btn_msg"):
        if nome_cliente_msg and descricao_projeto_msg:
            with st.spinner("Gerando mensagem personalizada..."):
                prompt = generate_message_prompt(
                    nome_cliente_msg, descricao_projeto_msg, 
                    comentario_especifico_msg, pergunta_abertura_msg
                )
                
                mensagem_gerada = generate_with_ai(prompt, "mensagem de interesse")
                
                st.markdown('<div class="generated-content">', unsafe_allow_html=True)
                st.markdown("### 📤 Mensagem Gerada:")
                st.markdown(mensagem_gerada)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Botão para copiar
                st.code(mensagem_gerada, language=None)
        else:
            st.error("⚠️ Preencha pelo menos o nome do cliente e a descrição do projeto!")
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    
    st.header("🎯 Proposta Personalizada")
    st.markdown("*Crie uma proposta completa e convincente para fechar negócios*")
    
    # Seção 1: Informações básicas
    st.subheader("📋 Informações Básicas")
    col1, col2 = st.columns(2)
    
    with col1:
        nome_cliente_prop = st.text_input("👤 Nome do Cliente", 
                                        placeholder="Ex: Maria Santos", key="nome_prop")
        
        descricao_projeto_prop = st.text_area("📝 Descrição do Projeto", 
                                            placeholder="Cole aqui a descrição completa do projeto...",
                                            height=100, key="desc_prop")
    
    with col2:
        comentario_especifico_prop = st.text_area("💭 Comentário Específico", 
                                                placeholder="Seu comentário personalizado...",
                                                height=100, key="coment_prop")
        
        resumo_problema = st.text_area("🎯 Resumo do Problema do Cliente", 
                                     placeholder="Descreva o problema principal que o cliente precisa resolver...",
                                     height=100)
    
    # Seção 2: Solução e diferenciais
    st.subheader("⚡ Sua Solução")
    col3, col4 = st.columns(2)
    
    with col3:
        como_resolvo = st.text_area("🔧 Como Você Resolve (Diferenciais)", 
                                  placeholder="Descreva sua abordagem e diferenciais únicos...",
                                  height=100)
        
        microgarantias = st.text_area("🛡️ Microgarantias", 
                                    placeholder="Liste suas garantias e credibilidade...",
                                    height=100)
    
    with col4:
        preco_prazo = st.text_input("💰 Preço e Prazo Sugerido", 
                                  placeholder="Ex: R$ 2.500 em 15 dias úteis")
        
        call_to_action = st.text_area("🚀 Call to Action", 
                                    placeholder="Sua proposta de próximos passos...",
                                    height=100)
    
    if st.button("🎯 Gerar Proposta Completa", key="btn_prop"):
        if nome_cliente_prop and descricao_projeto_prop and resumo_problema:
            with st.spinner("Gerando proposta personalizada..."):
                prompt = generate_proposal_prompt(
                    nome_cliente_prop, descricao_projeto_prop, comentario_especifico_prop,
                    resumo_problema, como_resolvo, microgarantias, preco_prazo, call_to_action
                )
                
                proposta_gerada = generate_with_ai(prompt, "proposta completa")
                
                st.markdown('<div class="generated-content">', unsafe_allow_html=True)
                st.markdown("### 📋 Proposta Gerada:")
                st.markdown(proposta_gerada)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Botão para copiar
                st.code(proposta_gerada, language=None)
        else:
            st.error("⚠️ Preencha pelo menos o nome do cliente, descrição do projeto e resumo do problema!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p>🚀 <strong>Gerador de Propostas Workana</strong> - Powered by IA</p>
    <p>💡 Dica: Quanto mais específico você for nos campos, melhor será o resultado gerado!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar com instruções
with st.sidebar:
    st.markdown("## 📖 Como Usar")
    st.markdown("""
    **Mensagem de Interesse:**
    - Use para primeiro contato
    - Seja específico no comentário
    - Termine com pergunta engajadora
    
    **Proposta Completa:**
    - Para clientes interessados
    - Detalhe bem sua solução
    - Inclua garantias e preços
    
    **💡 Dicas de Sucesso:**
    - Personalize cada proposta
    - Demonstre conhecimento do projeto
    - Seja claro sobre valor entregue
    - Use linguagem profissional
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 Próximos Passos")
    st.markdown("""
    1. Gere sua proposta
    2. Revise e ajuste se necessário
    3. Copie e envie no Workana
    4. Acompanhe respostas
    """)
