import plotly.graph_objects as go
import streamlit as st
from PIL import Image
import pandas as pd

def grafico_limite(maximo):

  if(maximo > 0):
    n = 10
  if(maximo > 10):
    n = 15
  if(maximo >= 80):
    n = 50
  if(maximo >= 200):
    n = 100
  if(maximo >= 300):
    n = 200
  if(maximo >= 600):
    n = 400
  if(maximo >= 900):
    n = 500
  return n

def grafico_estudantes(escolha_NOME_IES, escolha_IES, escolha_NOME_CURSO, escolha_CURSO, escolha_CATEGORIA, dados):

  anos = [2019, 2020, 2021]

  if(escolha_CATEGORIA == 'Concluintes'): 

    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(0, len(anos), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_BRANCA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_PRETA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_PARDA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_AMARELA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_INDIGENA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_CORND'].drop_duplicates().dropna().sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_0_17'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_18_24'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_25_29'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_30_34'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_35_39'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_40_49'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_50_59'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_60_MAIS'].drop_duplicates().dropna().sum())) 

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_MASC'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_CONC_FEM'].drop_duplicates().dropna().sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']

    fig1 = go.Figure(data=[go.Bar(name = '2019', x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = '2020', x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)
    fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Cor/Raça', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))  

    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']

    fig2 = go.Figure(data=[go.Bar(name = '2019', x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = '2020', x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = idades, y = lista2[18:27], text = lista2[18:27], marker_pattern_shape="-", marker_color='#179462')])

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)
    fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Idades', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    generos = ['Total', 'Homens', 'Mulheres']

    fig3 = go.Figure(data=[go.Bar(name = '2019', x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = '2020', x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = generos, y = lista3[6:9], text = lista3[6:9], marker_pattern_shape="-", marker_color='#179462')])

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)
    fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Gêneros', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    st.subheader('Gráficos:')
    tab1, tab2, tab3 = st.tabs(["Cor/Raça", "Gêneros", "Idades"])
    with tab1:
      st.plotly_chart(fig1, use_container_width=True)
    with tab2:
      st.plotly_chart(fig3, use_container_width=True)
    with tab3:
      st.plotly_chart(fig2, use_container_width=True)  
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
      pagina_inicial()

  if(escolha_CATEGORIA == 'Ingressantes'):
      
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    for i in range(0, len(anos), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_BRANCA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_PRETA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_PARDA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_AMARELA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_INDIGENA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_CORND'].drop_duplicates().dropna().sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_VESTIBULAR'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_ENEM'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_AVALIACAO_SERIADA'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_SELECAO_SIMPLIFICA'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_VG_REMANESC'].drop_duplicates().dropna().sum()))

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_0_17'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_18_24'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_25_29'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_30_34'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_35_39'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_40_49'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_50_59'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_60_MAIS'].drop_duplicates().dropna().sum()))

      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING'].drop_duplicates().dropna().sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_MASC'].drop_duplicates().dropna().sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_ING_FEM'].drop_duplicates().dropna().sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']

    fig1 = go.Figure(data=[go.Bar(name = '2019', x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = '2020', x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)
    fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Cor/Raça', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    formas_ingresso = ['Total', 'Vestibular', 'Enem', 'Avaliação<br>Seriada', 'Seleção<br>Simplificada', 'Vagas<br>Remanescentes']

    fig2 = go.Figure(data=[go.Bar(name = '2019', x = formas_ingresso, y = lista2[0:6], text = lista2[0:6], marker_pattern_shape="/"), go.Bar(name = '2020', x = formas_ingresso, y = lista2[6:12], text = lista2[6:12], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = formas_ingresso, y = lista2[12:18], text = lista2[12:18], marker_pattern_shape="-", marker_color='#179462')])

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)
    fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Formas de Ingresso', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']

    fig3 = go.Figure(data=[go.Bar(name = '2019', x = idades, y = lista3[0:9], text = lista3[0:9], marker_pattern_shape="/"), go.Bar(name = '2020', x = idades, y = lista3[9:18], text = lista3[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = idades, y = lista3[18:27], text = lista3[18:27], marker_pattern_shape="-", marker_color='#179462')])

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)
    fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Idades', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    generos = ['Total', 'Homens', 'Mulheres']

    fig4 = go.Figure(data=[go.Bar(name = '2019', x = generos, y = lista4[0:3], text = lista4[0:3], marker_pattern_shape="/"), go.Bar(name = '2020', x = generos, y = lista4[3:6], text = lista4[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = generos, y = lista4[6:9], text = lista4[6:9], marker_pattern_shape="-", marker_color='#179462')])

    fig4.update_xaxes(tickfont_size=11)
    fig4.update_yaxes(range = [0, max(lista4)+n], tickfont_size=11, showgrid = False)
    fig4.update_traces(textposition = 'outside', textfont_size=11)
    fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Gêneros', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    st.subheader('Gráficos:')
    tab1, tab2, tab3, tab4 = st.tabs(["Cor/Raça", "Formas de Ingresso", "Gêneros", "Idades"])
    with tab1:
      st.plotly_chart(fig1, use_container_width=True)
    with tab2:
      st.plotly_chart(fig2, use_container_width=True)
    with tab3:
      st.plotly_chart(fig4, use_container_width=True)
    with tab4:
      st.plotly_chart(fig3, use_container_width=True)
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
      pagina_inicial()

  if(escolha_CATEGORIA == 'Matriculados'):

    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(0, len(anos), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_BRANCA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_PRETA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_PARDA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_AMARELA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_INDIGENA'].drop_duplicates().dropna().sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_CORND'].drop_duplicates().dropna().sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_0_17'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_18_24'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_25_29'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_30_34'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_35_39'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_40_49'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_50_59'].drop_duplicates().dropna().sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_60_MAIS'].drop_duplicates().dropna().sum())) 

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_MASC'].drop_duplicates().dropna().sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['CO_IES'] == escolha_IES) & (dados['CO_CURSO'] == escolha_CURSO)]['QT_MAT_FEM'].drop_duplicates().dropna().sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']

    fig1 = go.Figure(data=[go.Bar(name = '2019', x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = '2020', x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)
    fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Cor/Raça', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))   

    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']

    fig2 = go.Figure(data=[go.Bar(name = '2019', x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = '2020', x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = idades, y = lista2[18:27], text = lista2[18:27], marker_pattern_shape="-", marker_color='#179462')])

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)
    fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Idades', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    generos = ['Total', 'Homens', 'Mulheres']

    fig3 = go.Figure(data=[go.Bar(name = '2019', x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = '2020', x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = generos, y = lista3[6:9], text = lista3[6:9], marker_pattern_shape="-", marker_color='#179462')])

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)
    fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_NOME_CURSO} da {escolha_NOME_IES}<br> por Gêneros', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    st.subheader('Gráficos:')
    tab1, tab2, tab3 = st.tabs(["Cor/Raça", "Gêneros", "Idades"])
    with tab1:
      st.plotly_chart(fig1, use_container_width=True)
    with tab2:
      st.plotly_chart(fig3, use_container_width=True)
    with tab3:
      st.plotly_chart(fig2, use_container_width=True)  
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
      pagina_inicial()

def pagina_inicial(dados):

  titulo = st.header('Analisador Gráfico do Censo da Educação Superior')
  espaco = st.text('')
  sobre = st.subheader('Sobre:')
  descricao1 = st.markdown('O site realiza análises gráficas dos dados do Censo da Educação Superior, providos pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira, comparando a quantidade de estudantes entre concluintes, ingressantes e matriculados presentes nos cursos e instituições de ensino superior do Brasil.')
  descricao2 = st.markdown('Desenvolvido por Guilherme Tomaselli Borchardt, junto ao grupo de Iniciação Científica sobre Evasão Escolar, orientado pela professora Isabela Gasparini e pertencente à Universidade do Estado de Santa Catarina (UDESC - CCT).')
  st.sidebar.title('Opções:')
  try:
    escolha_ESTADO = estados()
    escolha_CIDADE = st.sidebar.selectbox('Escolha uma cidade:', (dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['QT_VG_TOTAL'] > 0)]['NO_MUNICIPIO'].drop_duplicates().sort_values().dropna()))
    escolha_NOME_IES = st.sidebar.selectbox('Escolha uma instituição de ensino:', ((dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['NO_MUNICIPIO'] == escolha_CIDADE) & (dados['QT_VG_TOTAL'] > 0)]['SG_IES'].drop_duplicates().sort_values().dropna())))
    escolha_IES = int(dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_NOME_IES) & (dados['NO_MUNICIPIO'] == escolha_CIDADE) & (dados['QT_VG_TOTAL'] > 0)]['CO_IES'].drop_duplicates())
    escolha_NOME_CURSO = st.sidebar.selectbox('Escolha um curso:', (dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_NOME_IES) & (dados['NO_MUNICIPIO'] == escolha_CIDADE) & (dados['QT_VG_TOTAL'] > 0)]['NO_CURSO'].str.upper().drop_duplicates().sort_values().dropna()))
    escolha_CURSO = (dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['CO_IES'] == escolha_IES) & (dados['NO_CURSO'] == escolha_NOME_CURSO) & (dados['NO_MUNICIPIO'] == escolha_CIDADE) & (dados['QT_VG_TOTAL'] > 0)]['CO_CURSO'].drop_duplicates())
    if(int((dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['CO_IES'] == escolha_IES) & (dados['NO_CURSO'] == escolha_NOME_CURSO) & (dados['NO_MUNICIPIO'] == escolha_CIDADE) & (dados['QT_VG_TOTAL'] > 0)]['QT_CONC'].sum())) > 0):
      escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Concluintes', 'Ingressantes', 'Matriculados'))
    else:
      escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Ingressantes', 'Matriculados'))
    button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
    if(button_gerar_grafico):
        titulo.empty()
        espaco.empty()
        sobre.empty()
        descricao1.empty()
        descricao2.empty()
        grafico_estudantes(escolha_NOME_IES, escolha_IES, escolha_NOME_CURSO, int(escolha_CURSO), escolha_CATEGORIA, dados)
  except:
    titulo.empty()
    espaco.empty()
    sobre.empty()
    descricao1.empty()
    descricao2.empty()
    st.error('Desculpa, aconteceu algum erro durante o processo. Estamos trabalhando para resolver.')
  st.sidebar.write('*Versão 4.0.1*')

def estados():

  escolha_ESTADO = st.sidebar.selectbox('Escolha um estado:', ('Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul','Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'))
  if(escolha_ESTADO == 'Rondônia'):
    escolha_ESTADO = 11
  if(escolha_ESTADO == 'Acre'):
    escolha_ESTADO = 12
  if(escolha_ESTADO == 'Amazonas'):
    escolha_ESTADO = 13  
  if(escolha_ESTADO == 'Roraima'):
    escolha_ESTADO = 14
  if(escolha_ESTADO == 'Pará'):
    escolha_ESTADO = 15 
  if(escolha_ESTADO == 'Amapá'):
    escolha_ESTADO = 16
  if(escolha_ESTADO == 'Tocantins'):
    escolha_ESTADO = 17 
  if(escolha_ESTADO == 'Maranhão'):
    escolha_ESTADO = 21
  if(escolha_ESTADO == 'Piauí'):
    escolha_ESTADO = 22
  if(escolha_ESTADO == 'Ceará'):
    escolha_ESTADO = 23
  if(escolha_ESTADO == 'Rio Grande do Norte'):
    escolha_ESTADO = 24
  if(escolha_ESTADO == 'Paraíba'):
    escolha_ESTADO = 25
  if(escolha_ESTADO == 'Pernambuco'):
    escolha_ESTADO = 26
  if(escolha_ESTADO == 'Alagoas'):
    escolha_ESTADO = 27
  if(escolha_ESTADO == 'Sergipe'):
    escolha_ESTADO = 28
  if(escolha_ESTADO == 'Bahia'):
    escolha_ESTADO = 29
  if(escolha_ESTADO == 'Minas Gerais'):
    escolha_ESTADO = 31
  if(escolha_ESTADO == 'Espírito Santo'):
    escolha_ESTADO = 32
  if(escolha_ESTADO == 'Rio de Janeiro'):
    escolha_ESTADO = 33
  if(escolha_ESTADO == 'São Paulo'):
    escolha_ESTADO = 35
  if(escolha_ESTADO == 'Paraná'):
    escolha_ESTADO = 41
  if(escolha_ESTADO == 'Rio Grande do Sul'):
    escolha_ESTADO = 43
  if(escolha_ESTADO == 'Santa Catarina'):
    escolha_ESTADO = 42
  if(escolha_ESTADO == 'Mato Grosso do Sul'):
    escolha_ESTADO = 50
  if(escolha_ESTADO == 'Mato Grosso'):
    escolha_ESTADO = 51
  if(escolha_ESTADO == 'Goiás'):
    escolha_ESTADO = 52
  if(escolha_ESTADO == 'Distrito Federal'):
    escolha_ESTADO = 53
  return escolha_ESTADO
  
@st.cache(allow_output_mutation=True, show_spinner=False)
def load_data_alunos():

  dados1 = pd.read_csv('dados1.CSV', encoding='utf8')
  dados2 = pd.read_csv('dados2.CSV', encoding='utf8')
  dados3 = pd.read_csv('dados3.CSV', encoding='utf8')
  dados4 = pd.read_csv('dados4.CSV', encoding='utf8')
  dados5 = pd.read_csv('dados5.CSV', encoding='utf8')
  dados6 = pd.read_csv('dados6.CSV', encoding='utf8')
  dados7 = pd.read_csv('dados7.CSV', encoding='utf8')
  dados8 = pd.read_csv('dados8.CSV', encoding='utf8')
  dados9 = pd.read_csv('dados9.CSV', encoding='utf8')
  dados10 = pd.read_csv('dados10.CSV', encoding='utf8')
  dados11 = pd.read_csv('dados11.CSV', encoding='utf8')
  dados12 = pd.read_csv('dados12.CSV', encoding='utf8')
  dados13 = pd.read_csv('dados13.CSV', encoding='utf8')
  dados14 = pd.read_csv('dados14.CSV', encoding='utf8')

  dados = pd.concat([dados1, dados2, dados3, dados4, dados5, dados6, dados7, dados8, dados9, dados10, dados11, dados12, dados13, dados14])
  
  dados_2018 = pd.read_csv('dados_2018.CSV', encoding='utf8')

  return dados, dados_2018

if __name__ == '__main__':

  imagem = Image.open('icone.png')
  st.set_page_config(page_title='Analisador Censos', page_icon=imagem)
  titulo_inicial = st.title('Realizando a Leitura dos Dados...')
  espaco_inicial = st.subheader('')
  descricao_inicial = st.subheader('Por favor aguarde um momento, a aplicação já irá iniciar.')
  dados, dados_2018 = load_data_alunos()
  titulo_inicial.empty()
  espaco_inicial.empty()
  descricao_inicial.empty()
  pagina_inicial(dados)
