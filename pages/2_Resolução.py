import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st 
import plotly.graph_objects as go



st.title('Questões')
#st.info('Respostas')

with st.expander('Questão 4.1'):

    dados_principais = {
    'Item':['Mão-de-obra direta',
            'Matéria-prima direta',
            'Energia elétrica','Outros custos',
            'Despesas de vendas','Vendas = produção',
            'Preço unitário de venda','Depreciação'],

            'Custo/Unidade':[2,1,0.5,1.3,2.5,5000,10,6000,],

            'Incremento Anual Projetado/%a.a':[7,8,10,5,7,3,0,0]
    }


    df_principal = pd.DataFrame(dados_principais)

    imposto_renda = (3400/100)

    dados_imposto_renda = {
        'Imposto de renda':[imposto_renda]
    }
    df_imposto_renda = pd.DataFrame(dados_imposto_renda)

    st.write(df_principal)


    dados = {
        'Categoria': [
            'Vendas', 'Receita de vendas',
            'Mão-de-obra direta', 'Matéria-prima direta', 'Energia elétrica', 'Outros custos',
            'Lucro bruto',
            'Despesa de vendas', 'Depreciação',
            'Lucro antes de juros e IR (Lajir)', 'Imposto de renda', 'Lucro após IR', 'Depreciação',
            'Fluxo de caixa livre (FCL)', 'FCL incremental (C - S)'
        ],
        'Custo unitário S': ['', '', '2,0', '1,0', '0,5', '1,3', '', '2,5', '', '11,05', '', '', '', '', ''],
        'Custo unitário C': ['', '', '1,9', '1,1', '0,4', '1,3', '', '2,5', '', '11,10', '', '', '', '', ''],
        'Ano 1 S': [5000, 50000, -10600, -5400, -2650, -6825, 24425, -13737, 0, 11005, -3757, 7293, 0, 7293, ''],
        'Ano 1 C': [5150, 51500, -6551, -5562, -2626, -7370, 29091, -14511, -6000, 13403, -3814, 7403, 6000, 13403, 6110],
        'Ano 2 S': [5305, 51000, -11236, -5832, -2562, -7166, 22204, -14211, 0, 8430, -3214, 5636, 0, 5636, ''],
        'Ano 2 C': [5000, 50000, -7112, -4687, -2327, -7203, 24930, -12613, 0, 12781, -3193, 9588, 0, 12781, 7218],
        'Ano 3 S': [5000, 53045, -11910, -6287, -3328, -7528, 20993, -15133, 0, 5626, -1913, 6714, 0, 6714, ''],
        'Ano 3 C': [5464, 54640, -8709, -7683, -3660, -8292, 28914, -16495, 0, 12452, -3133, 9319, 0, 12452, 8329],
        'Ano 4 S': [5000, 50000, -10289, -5622, -2376, -7221, 19492, -13654, 0, 5838, -1987, 3842, 0, 3842, ''],
        'Ano 4 C': [5628, 56725, -8526, -7556, -3054, -8896, 27906, -14699, 0, 7277, -2664, 5172, 6000, 11172, 9439]
    }

    df_resolucao = pd.DataFrame(dados)
    st.write(df_resolucao)


with st.expander('Questão 4.2'):

    # Dados da análise de sensibilidade
    dados = {
        'Variável Alterada': [
            'Participação de mercado –20%',
            'Custo variável unitário +20%',
            'Custo fixo total +20%'
        ],
        'VPL Recalculado': [-413.48, -577.18, -467.06],
        'Variação Absoluta': [-4.42, -159.28, -49.16],
        'Variação (%)': [-1.06, -38.11, -11.76]
    }

    # Criar DataFrame
    df_sensibilidade = pd.DataFrame(dados)

    # Mostrar o DataFrame
    st.write("Análise de Sensibilidade - VPL do Cenário Pessimista")
    st.write(df_sensibilidade)

    # Plotando o gráfico de barras
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df_sensibilidade['Variável Alterada'], df_sensibilidade['Variação Absoluta'], color=['#3366cc', '#dc3912', '#ff9900'])

    # Adicionando valores no topo das barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f'{yval:.2f}', ha='center', va='bottom')

    plt.title('Análise de Sensibilidade - Variação do VPL (R$)', fontsize=14)
    plt.ylabel('Variação no VPL (R$)')
    plt.xlabel('Variável Alterada')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


with st.expander('Questão 4.3'):
    st.write('Análise de Fluxo de Caixa - Cenários Otimista e Pessimista"')
    df_fluxo = pd.DataFrame({
    'Ano': [1, 2, 3, 4, 5, 6],
    'Otimista': [4100000, 5600000, 7500000, 8400000, 11900000, 13500000],
    'Pessimista': [3100000, 3125000, 3840000, 3810000, 5900000, 7100000]
})

    # Média e Desvio
    df_fluxo['Média'] = df_fluxo[['Otimista', 'Pessimista']].mean(axis=1)
    df_fluxo['Desvio_Padrão'] = df_fluxo[['Otimista', 'Pessimista']].std(axis=1)

    # Variabilidade Ano a Ano
    df_variabilidade = pd.DataFrame({'Ano': [2, 3, 4, 5, 6]})
    for cenário in ['Otimista', 'Pessimista']:
        variabilidade = df_fluxo[cenário].pct_change().dropna() * 100
        df_variabilidade[cenário] = variabilidade.round(2)

    # Estatísticas
    variabilidade_media = df_variabilidade[['Otimista', 'Pessimista']].mean()
    desvio_variabilidade = df_variabilidade[['Otimista', 'Pessimista']].std()

    df_estatisticas = pd.DataFrame({
        'Variabilidade Média (%)': variabilidade_media,
        'Desvio Padrão (%)': desvio_variabilidade
    }).round(2)

    # ---- Layout Streamlit ---- #
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Fluxo de Caixa por Cenário")
        st.dataframe(df_fluxo, use_container_width=True)

    with col2:
        st.subheader("📉 Variabilidade (%) Ano a Ano")
        st.dataframe(df_variabilidade, use_container_width=True)

    st.subheader("📌 Estatísticas de Variabilidade")
    st.dataframe(df_estatisticas)

    # ---- Gráficos ---- #
    st.subheader("📊 Gráficos Interativos")

    # Gráfico de linhas - Fluxo de Caixa
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df_fluxo['Ano'], y=df_fluxo['Otimista'], mode='lines+markers', name='Otimista'))
    fig1.add_trace(go.Scatter(x=df_fluxo['Ano'], y=df_fluxo['Pessimista'], mode='lines+markers', name='Pessimista'))
    fig1.add_trace(go.Scatter(x=df_fluxo['Ano'], y=df_fluxo['Média'], mode='lines+markers', name='Média'))
    fig1.update_layout(title="Fluxo de Caixa por Ano", xaxis_title="Ano", yaxis_title="R$", height=500)
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de barras - Variabilidade
    fig2 = go.Figure(data=[
        go.Bar(name='Otimista', x=df_variabilidade['Ano'], y=df_variabilidade['Otimista']),
        go.Bar(name='Pessimista', x=df_variabilidade['Ano'], y=df_variabilidade['Pessimista'])
    ])
    fig2.update_layout(title="Variabilidade dos Fluxos de Caixa (%)", barmode='group', xaxis_title="Ano", yaxis_title="%")
    st.plotly_chart(fig2, use_container_width=True)

with st.expander('Questão 4.4'):
    # app_streamlit_analise.py
    st.write("🏭 Análise de Investimento: Cenários e Sensibilidade")

    # ================== 1. Parâmetros por cenário ==================
    st.subheader("📋 Parâmetros dos Cenários")

    dados_parametros = {
        'Variável': [
            'Investimento Inicial (I0)',
            'Preço de Venda (P)',
            'Tamanho do Mercado (M)',
            'Custo Fixo Total (CFT)',
            'Duração do Projeto (n)',
            'Custo Variável Unitário (CV)',
            'Participação de Mercado (α)',
            'Imposto de Renda (T)',
            'Depreciação Anual (%)',
            'Custo de Capital (K)'
        ],
        'Esperado': [
            160_000_000, 350, 2_000_000, 60_000_000, 15, 120, 0.20, 0.34, 0.0667, 0.12
        ],
        'Pessimista': [
            160_000_000, 344, 2_000_000, 63_000_000, 15, 130, 0.18, 0.34, 0.0667, 0.12
        ],
        'Otimista': [
            160_000_000, 370, 2_000_000, 58_000_000, 15, 118, 0.22, 0.34, 0.0667, 0.12
        ]
    }

    df_parametros = pd.DataFrame(dados_parametros)
    st.dataframe(df_parametros, use_container_width=True)

    # ================== 2. Fluxo de Caixa e VPL ==================
    st.subheader("📈 Fluxo de Caixa Anual e VPL")

    dados_fluxo = {
        'Item': [
            'Receita (M × α × P)',
            '– Custo Fixo Total (CFT)',
            '– Custo Variável Total (M × α × CV)',
            '– Depreciação (I0 × D)',
            'LAJIR',
            '– Imposto de Renda (34%)',
            'Lucro Operacional Após IR',
            '+ Depreciação',
            'FCL (Fluxo de Caixa Livre)',
            'VPL'
        ],
        'Esperado': [
            140_000_000, -60_000_000, -48_000_000, -10_666_667,
            21_333_333, -7_253_333, 14_080_000, 10_666_667, 24_746_667, 8_546_193
        ],
        'Pessimista': [
            123_840_000, -63_000_000, -46_800_000, -10_666_667,
            3_373_333, -1_146_933, 2_226_400, 10_666_667, 12_893_067, -72_187_070
        ],
        'Otimista': [
            162_800_000, -58_000_000, -51_920_000, -10_666_667,
            42_213_333, -14_352_533, 27_860_800, 10_666_667, 38_527_467, 102_405_355
        ]
    }

    df_fluxo = pd.DataFrame(dados_fluxo)
    st.dataframe(df_fluxo, use_container_width=True)

    # ================== 3. Análise de Sensibilidade ==================
    st.subheader("📉 Análise de Sensibilidade (Variação de 20%)")

    dados_sensibilidade = {
        'Mudança': [
            'Preço de Venda (–20%)',
            'Custo Fixo Total (+20%)',
            'Participação de Mercado (–20%)',
            'Custo Variável Unitário (+20%)'
        ],
        'VPL Esperado': [-117_318_583, -45_395_854, -74_164_945, -34_607_444],
        'Variação Esperado (%)': [-1473, -631, -968, -505],
        'VPL Pessimista': [-183_523_455, -128_826_219, -141_448_658, -114_261_867],
        'Variação Pessimista (%)': [-154, -79, -96, -59],
        'VPL Otimista': [-43_957_399, 50_261_376, 2_720_452, 55_727_503],
        'Variação Otimista (%)': [-143, -51, -97, -46]
    }

    df_sensibilidade = pd.DataFrame(dados_sensibilidade)
    st.dataframe(df_sensibilidade, use_container_width=True)

    # ================== 4. Gráficos ==================
    st.subheader("📊 Gráficos Comparativos")

    # Gráfico VPL por cenário
    fig1 = go.Figure()
    cenarios = ['Esperado', 'Pessimista', 'Otimista']
    vpls = [8_546_193, -72_187_070, 102_405_355]

    fig1.add_trace(go.Bar(
        x=cenarios,
        y=vpls,
        marker_color=['#3366cc', '#dc3912', '#109618'],
        text=[f'R$ {v:,.0f}' for v in vpls],
        textposition='auto'
    ))
    fig1.update_layout(title="💰 VPL por Cenário", yaxis_title="Valor Presente Líquido (R$)")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de Sensibilidade: VPL Esperado por mudança
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=df_sensibilidade['Mudança'],
        y=df_sensibilidade['VPL Esperado'],
        marker_color='#ff9900',
        text=df_sensibilidade['Variação Esperado (%)'].apply(lambda x: f'{x} %'),
        textposition='auto'
    ))
    fig2.update_layout(title="⚠️ Sensibilidade do VPL (Cenário Esperado)", yaxis_title="VPL Recalculado (R$)")
    st.plotly_chart(fig2, use_container_width=True)

    # Rodapé
    st.caption("Desenvolvido por Rxz1 • Engenharia de Produção ")
