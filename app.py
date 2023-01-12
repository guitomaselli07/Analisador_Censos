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

def grafico_estudantes_evadidos(escolha_IES, escolha_CURSO, dados, dados3):

  lista = []

  MAT_2019 = (dados[(dados['NU_ANO_CENSO'] == 2019) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum())
  ING_2019 = (dados[(dados['NU_ANO_CENSO'] == 2019) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum())
  MAT_2018 = (dados3[(dados3['SG_IES'] == escolha_IES) & (dados3['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum())
  CONC_2018 = (dados3[(dados3['SG_IES'] == escolha_IES) & (dados3['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum())
  
  st.text((1 - ((MAT_2019 - ING_2019)/(MAT_2018 - CONC_2018)))*100)
  
  MAT_2020 =( dados[(dados['NU_ANO_CENSO'] == 2020) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum())
  ING_2020 = (dados[(dados['NU_ANO_CENSO'] == 2020) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum())
  MAT_2019 =(dados[(dados['NU_ANO_CENSO'] == 2019) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum())
  CONC_2019 = (dados[(dados['NU_ANO_CENSO'] == 2019) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum())
  
  lista.append((1 - ((MAT_2020 - ING_2020)/(MAT_2019 - CONC_2019)))*100)
  
  MAT_2021 = (dados[(dados['NU_ANO_CENSO'] == 2021) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum())
  ING_2021 = (dados[(dados['NU_ANO_CENSO'] == 2021) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum())
  MAT_2020 = (dados[(dados['NU_ANO_CENSO'] == 2020) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum())
  CONC_2020 = (dados[(dados['NU_ANO_CENSO'] == 2020) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum())
  
  lista.append((1 - ((MAT_2021 - ING_2021)/(MAT_2020 - CONC_2020)))*100)

  n = grafico_limite(max(lista))

  anos = ['2019', '2020', '2021']

  fig = go.Figure([go.Bar(x = anos, y = lista, text = [f'{lista[0]:.2f}%', f'{lista[1]:.2f}%', f'{lista[2]:.2f}%'], marker_pattern_shape="/" , width = 0.45)])

  fig.update_xaxes(tickfont_size=11)
  fig.update_yaxes(title_text = '%', range = [0, max(lista)+n], tickfont_size=11, showgrid = False)
  fig.update_traces(textposition = 'outside', textfont_size=11)
  fig.update_layout(title_text = f'Taxa de Evasão dos Estudantes do Curso de {escolha_CURSO}<br>da {escolha_IES}')  

  st.subheader('Gráfico:')
  st.plotly_chart(fig, use_container_width=True)
  button_pagina_incical = st.button('Página Inicial')
  if(button_pagina_incical):
    pagina_inicial()

def grafico_estudantes(escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados):

  anos = [2019, 2020, 2021]

  if(escolha_CATEGORIA == 'Concluintes'): 

    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(0, len(anos), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_BRANCA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_PRETA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_PARDA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_AMARELA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_INDIGENA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_CORND'].sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_0_17'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_18_24'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_25_29'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_30_34'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_35_39'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_40_49'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_50_59'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_60_MAIS'].sum())) 

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_MASC'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_FEM'].sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']

    fig1 = go.Figure(data=[go.Bar(name = '2019', x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = '2020', x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)
    fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Cor/Raça', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))  

    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']

    fig2 = go.Figure(data=[go.Bar(name = '2019', x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = '2020', x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = idades, y = lista2[18:27], text = lista2[18:27], marker_pattern_shape="-", marker_color='#179462')])

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)
    fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Idades', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    generos = ['Total', 'Homens', 'Mulheres']

    fig3 = go.Figure(data=[go.Bar(name = '2019', x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = '2020', x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = generos, y = lista3[6:9], text = lista3[6:9], marker_pattern_shape="-", marker_color='#179462')])

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)
    fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Gêneros', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

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

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_BRANCA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_PRETA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_PARDA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_AMARELA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_INDIGENA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_CORND'].sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_VESTIBULAR'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_ENEM'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_AVALIACAO_SERIADA'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_SELECAO_SIMPLIFICA'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_VG_REMANESC'].sum()))

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_0_17'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_18_24'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_25_29'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_30_34'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_35_39'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_40_49'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_50_59'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_60_MAIS'].sum()))

      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_MASC'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_FEM'].sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']

    fig1 = go.Figure(data=[go.Bar(name = '2019', x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = '2020', x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)
    fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Cor/Raça', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    formas_ingresso = ['Total', 'Vestibular', 'Enem', 'Avaliação<br>Seriada', 'Seleção<br>Simplificada', 'Vagas<br>Remanescentes']

    fig2 = go.Figure(data=[go.Bar(name = '2019', x = formas_ingresso, y = lista2[0:6], text = lista2[0:6], marker_pattern_shape="/"), go.Bar(name = '2020', x = formas_ingresso, y = lista2[6:12], text = lista2[6:12], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = formas_ingresso, y = lista2[12:18], text = lista2[12:18], marker_pattern_shape="-", marker_color='#179462')])

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)
    fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Formas de Ingresso', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']

    fig3 = go.Figure(data=[go.Bar(name = '2019', x = idades, y = lista3[0:9], text = lista3[0:9], marker_pattern_shape="/"), go.Bar(name = '2020', x = idades, y = lista3[9:18], text = lista3[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = idades, y = lista3[18:27], text = lista3[18:27], marker_pattern_shape="-", marker_color='#179462')])

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)
    fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Idades', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    generos = ['Total', 'Homens', 'Mulheres']

    fig4 = go.Figure(data=[go.Bar(name = '2019', x = generos, y = lista4[0:3], text = lista4[0:3], marker_pattern_shape="/"), go.Bar(name = '2020', x = generos, y = lista4[3:6], text = lista4[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = generos, y = lista4[6:9], text = lista4[6:9], marker_pattern_shape="-", marker_color='#179462')])

    fig4.update_xaxes(tickfont_size=11)
    fig4.update_yaxes(range = [0, max(lista4)+n], tickfont_size=11, showgrid = False)
    fig4.update_traces(textposition = 'outside', textfont_size=11)
    fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Gêneros', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

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

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_BRANCA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_PRETA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_PARDA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_AMARELA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_INDIGENA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_CORND'].sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_0_17'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_18_24'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_25_29'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_30_34'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_35_39'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_40_49'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_50_59'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_60_MAIS'].sum())) 

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_MASC'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == anos[i]) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_FEM'].sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']

    fig1 = go.Figure(data=[go.Bar(name = '2019', x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = '2020', x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)
    fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Cor/Raça', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))   

    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']

    fig2 = go.Figure(data=[go.Bar(name = '2019', x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = '2020', x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = idades, y = lista2[18:27], text = lista2[18:27], marker_pattern_shape="-", marker_color='#179462')])

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)
    fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Idades', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    generos = ['Total', 'Homens', 'Mulheres']

    fig3 = go.Figure(data=[go.Bar(name = '2019', x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = '2020', x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = '2021', x = generos, y = lista3[6:9], text = lista3[6:9], marker_pattern_shape="-", marker_color='#179462')])

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)
    fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_IES} por Gêneros', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

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

def pagina_inicial(dados, dados3):

  titulo = st.header('Analisador Gráfico do Censo da Educação Superior')
  espaco = st.text('')
  sobre = st.subheader('Sobre:')
  descricao1 = st.markdown('O site realiza análises gráficas dos dados do Censo da Educação Superior, providos pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira, comparando a quantidade de estudantes entre concluintes, evadidos, ingressantes e matriculados dos cursos e instituições de ensino superior do Brasil.')
  descricao2 = st.markdown('Desenvolvido por Guilherme Tomaselli Borchardt, junto ao grupo de Iniciação Científica sobre Evasão Escolar, orientado pela professora Isabela Gasparini e pertencente à Universidade do Estado de Santa Catarina (UDESC - CCT).')
  st.sidebar.title('Opções:')
  try:
    escolha_ESTADO = estados()
    escolha_IES = st.sidebar.selectbox('Escolha uma instituição de ensino:', ((dados[(dados['CO_UF'] == escolha_ESTADO)]['SG_IES'].drop_duplicates().sort_values().dropna())))
    escolha_CURSO = st.sidebar.selectbox('Escolha um curso:', (dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES)]['NOME_CURSO'].drop_duplicates().sort_values().dropna()))
    if(int((dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum())) > 0):
      if(dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2019)]['QT_ING'].sum() > 0 and dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2020)]['QT_ING'].sum() > 0 and dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2021)]['QT_ING'].sum() > 0):
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Concluintes', 'Evadidos', 'Ingressantes', 'Matriculados'))
        if(escolha_CATEGORIA == 'Evadidos'):
          button_gerar_grafico = st.sidebar.button('Gerar Gráfico')
          if(button_gerar_grafico):
              titulo.empty()
              espaco.empty()
              sobre.empty()
              descricao1.empty()
              descricao2.empty()
              grafico_estudantes_evadidos(escolha_IES, escolha_CURSO, dados, dados3)
        else:
          button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
          if(button_gerar_grafico):
              titulo.empty()
              espaco.empty()
              sobre.empty()
              descricao1.empty()
              descricao2.empty()
              grafico_estudantes(escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
      else:
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Concluintes', 'Ingressantes', 'Matriculados'))
        button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
        if(button_gerar_grafico):
            titulo.empty()
            espaco.empty()
            sobre.empty()
            descricao1.empty()
            descricao2.empty()
            grafico_estudantes(escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
    else:
      if(dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2019)]['QT_ING'].sum() > 0 and dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2020)]['QT_ING'].sum() > 0 and dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2021)]['QT_ING'].sum() > 0):
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Evadidos', 'Ingressantes', 'Matriculados'))
        if(escolha_CATEGORIA == 'Evadidos'):
          button_gerar_grafico = st.sidebar.button('Gerar Gráfico')
          if(button_gerar_grafico):
            titulo.empty()
            espaco.empty()
            sobre.empty()
            descricao1.empty()
            descricao2.empty()
            grafico_estudantes_evadidos(escolha_IES, escolha_CURSO, dados, dados3)
        else:
          button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
          if(button_gerar_grafico):
            titulo.empty()
            espaco.empty()
            sobre.empty()
            descricao1.empty()
            descricao2.empty()
            grafico_estudantes(escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
      else:
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Ingressantes', 'Matriculados'))
        button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
        if(button_gerar_grafico):
          titulo.empty()
          espaco.empty()
          sobre.empty()
          descricao1.empty()
          descricao2.empty()
          grafico_estudantes(escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
  except:
    titulo.empty()
    espaco.empty()
    sobre.empty()
    descricao1.empty()
    descricao2.empty()
    st.error('Desculpa, aconteceu algum erro durante o processo. Estamos trabalhando para resolver.')
  st.sidebar.write('*Versão 4.2.0*')

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

  dados1 = pd.read_csv('dados1.CSV', encoding='latin-1')
  dados2 = pd.read_csv('dados2.CSV', encoding='latin-1')

  dados = pd.concat([dados1, dados2])
  
  dados3 = pd.read_csv('dados3.CSV', encoding='latin-1')

  return dados, dados3

if __name__ == '__main__':

  imagem = Image.open('icone.png')
  st.set_page_config(page_title='Analisador Censos', page_icon=imagem)
  dados, dados3 = load_data_alunos()
  pagina_inicial(dados, dados3)
