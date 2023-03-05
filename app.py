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

def grafico_estudantes_evadidos(escolha_SG_IES, escolha_IES, escolha_CURSO, dados):

  lista = []

  anos = dados[(dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values()
  anos = anos.to_list()
  anos.remove(anos[0])

  for i in anos:

    desvinculados = dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_DESVINCULADO'].sum()
    transferidos = dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANSFERIDO'].sum()
    ingressantes = sum([dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum(),
                dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANCADA'].sum(),
                dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_DESVINCULADO'].sum(),
                dados[(dados['NU_ANO_CENSO'] == int(i)-1) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_DESVINCULADO'].sum(),
                dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANSFERIDO'].sum(),
                dados[(dados['NU_ANO_CENSO'] == int(i)-1) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANSFERIDO'].sum(),
                dados[(dados['NU_ANO_CENSO'] == int(i)-1) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum(),
                dados[(dados['NU_ANO_CENSO'] == i) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_FALECIDO'].sum(),
                dados[(dados['NU_ANO_CENSO'] == int(i)-1) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_FALECIDO'].sum()])

    falecidos = sum([dados[(dados['NU_ANO_CENSO'] == i) & (dados['SG_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_FALECIDO'].sum(), dados[(dados['NU_ANO_CENSO'] == int(i)-1) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_FALECIDO'].sum()])

    lista.append(float(((desvinculados + transferidos)/(ingressantes - falecidos))*100))

  if(len(lista) == 3):

    fig = go.Figure([go.Bar(x = anos, y = lista, text = [f'{lista[0]:.2f}%', f'{lista[1]:.2f}%', f'{lista[2]:.2f}%'], marker_pattern_shape="/", width = 0.45)])

  if(len(lista) == 4):

    fig = go.Figure([go.Bar(x = anos, y = lista, text = [f'{lista[0]:.2f}%', f'{lista[1]:.2f}%', f'{lista[2]:.2f}%', f'{lista[3]:.2f}%'], marker_pattern_shape="/", width = 0.45)])

  if(len(lista) == 5):

    fig = go.Figure([go.Bar(x = anos, y = lista, text = [f'{lista[0]:.2f}%', f'{lista[1]:.2f}%', f'{lista[2]:.2f}%', f'{lista[3]:.2f}%', f'{lista[4]:.2f}%'], marker_pattern_shape="/", width = 0.45)])

  if(len(lista) == 6):

    fig = go.Figure([go.Bar(x = anos, y = lista, text = [f'{lista[0]:.2f}%', f'{lista[1]:.2f}%', f'{lista[2]:.2f}%', f'{lista[3]:.2f}%', f'{lista[4]:.2f}%', f'{lista[5]:.2f}%'], marker_pattern_shape="/", width = 0.45)])
  
  n = grafico_limite(max(lista))
  
  fig.update_xaxes(tickfont_size=11)
  fig.update_yaxes(title_text = '%', range = [0, max(lista)+n], tickfont_size=11, showgrid = False)
  fig.update_traces(textposition = 'outside', textfont_size=11)
  fig.update_layout(title_text = f'Taxa de Evasão dos Estudantes do Curso de {escolha_CURSO}<br>da {escolha_SG_IES}')  

  st.subheader('Gráfico:')
  st.plotly_chart(fig, use_container_width=True)
  button_pagina_incical = st.button('Página Inicial')
  if(button_pagina_incical):
    pagina_inicial()

def grafico_estudantes(escolha_ANOS, escolha_SG_IES, escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados):

  if(escolha_CATEGORIA == 'Concluintes'): 

    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(0, len(escolha_ANOS), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_BRANCA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_PRETA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_PARDA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_AMARELA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_INDIGENA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_CORND'].sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_0_17'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_18_24'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_25_29'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_30_34'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_35_39'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_40_49'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_50_59'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_60_MAIS'].sum())) 

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_MASC'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_FEM'].sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']
    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']
    generos = ['Total', 'Homens', 'Mulheres']

    if(len(escolha_ANOS) == 1):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/")])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))  
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/")])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/", width = 0.45)])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if(len(escolha_ANOS) == 2):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366')])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))  
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366')])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366')])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if(len(escolha_ANOS) == 3):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))  
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = idades, y = lista2[18:27], text = lista2[18:27], marker_pattern_shape="-", marker_color='#179462')])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = generos, y = lista3[6:9], text = lista3[6:9], marker_pattern_shape="-", marker_color='#179462')])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))


    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)

    if(int(dados[(dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RESERVA_VAGA'].sum()) < 1):

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

    else:

      lista4 = []

      for i in range(0, len(escolha_ANOS), 1):

        lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RESERVA_VAGA'].sum()))
        lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RVREDEPUBLICA'].sum()))
        lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RVETNICO'].sum()))
        lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RVPDEF'].sum()))
        lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RVSOCIAL_RF'].sum()))
        lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC_RVOUTROS'].sum()))

      reserva_vagas = ['Total', 'Rede Pública', 'Étnica', 'Deficientes', 'Cunho Social/<br>Renda Familiar', 'Outros']

      if(len(escolha_ANOS) == 1):

        fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista4[0:6], text = lista4[0:6], marker_pattern_shape="/")])
        fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      if(len(escolha_ANOS) == 2):

        fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista4[0:6], text = lista4[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = reserva_vagas, y = lista4[6:12], text = lista4[6:12], marker_pattern_shape="x", marker_color='#f63366')])
        fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      if(len(escolha_ANOS) == 3):

        fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista4[0:6], text = lista4[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = reserva_vagas, y = lista4[6:12], text = lista4[6:12], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = reserva_vagas, y = lista4[12:18], text = lista4[12:18], marker_pattern_shape="-", marker_color='#179462')])
        fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))


      fig4.update_xaxes(tickfont_size=11)
      fig4.update_yaxes(range = [0, max(lista4)+5], tickfont_size=11, showgrid = False)
      fig4.update_traces(textposition = 'outside', textfont_size=11)

      st.subheader('Gráficos:')
      tab1, tab2, tab3, tab4 = st.tabs(["Cor/Raça", "Gêneros", "Idades", "Reserva de Vagas"])
      with tab1:
        st.plotly_chart(fig1, use_container_width=True)
      with tab2:
        st.plotly_chart(fig3, use_container_width=True)
      with tab3:
        st.plotly_chart(fig2, use_container_width=True)   
      with tab4:
        st.plotly_chart(fig4, use_container_width=True)
      button_pagina_incical = st.button('Página Inicial')
      if(button_pagina_incical):
        pagina_inicial()

  if(escolha_CATEGORIA == 'Ingressantes'):
      
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    for i in range(0, len(escolha_ANOS), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_BRANCA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_PRETA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_PARDA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_AMARELA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_INDIGENA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_CORND'].sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_VESTIBULAR'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_ENEM'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_AVALIACAO_SERIADA'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_SELECAO_SIMPLIFICA'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_VG_REMANESC'].sum()))

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_0_17'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_18_24'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_25_29'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_30_34'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_35_39'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_40_49'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_50_59'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_60_MAIS'].sum()))

      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_MASC'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_FEM'].sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']
    formas_ingresso = ['Total', 'Vestibular', 'Enem', 'Avaliação<br>Seriada', 'Seleção<br>Simplificada', 'Vagas<br>Remanescentes']
    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']
    generos = ['Total', 'Homens', 'Mulheres']

    if(len(escolha_ANOS) == 1):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/")])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = formas_ingresso, y = lista2[0:6], text = lista2[0:6], marker_pattern_shape="/")])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Formas de Ingresso do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista3[0:9], text = lista3[0:9], marker_pattern_shape="/")])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista4[0:3], text = lista4[0:3], marker_pattern_shape="/", width = 0.45)])
      fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if(len(escolha_ANOS) == 2):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366')])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = formas_ingresso, y = lista2[0:6], text = lista2[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = formas_ingresso, y = lista2[6:12], text = lista2[6:12], marker_pattern_shape="x", marker_color='#f63366')])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Formas de Ingresso dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista3[0:9], text = lista3[0:9], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = idades, y = lista3[9:18], text = lista3[9:18], marker_pattern_shape="x", marker_color='#f63366')])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista4[0:3], text = lista4[0:3], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = generos, y = lista4[3:6], text = lista4[3:6], marker_pattern_shape="x", marker_color='#f63366')])
      fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))


    if(len(escolha_ANOS) == 3):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = formas_ingresso, y = lista2[0:6], text = lista2[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = formas_ingresso, y = lista2[6:12], text = lista2[6:12], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = formas_ingresso, y = lista2[12:18], text = lista2[12:18], marker_pattern_shape="-", marker_color='#179462')])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Formas de Ingresso dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))      
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista3[0:9], text = lista3[0:9], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = idades, y = lista3[9:18], text = lista3[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = idades, y = lista3[18:27], text = lista3[18:27], marker_pattern_shape="-", marker_color='#179462')])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))      
      fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista4[0:3], text = lista4[0:3], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = generos, y = lista4[3:6], text = lista4[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = generos, y = lista4[6:9], text = lista4[6:9], marker_pattern_shape="-", marker_color='#179462')])
      fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))


    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)

    fig4.update_xaxes(tickfont_size=11)
    fig4.update_yaxes(range = [0, max(lista4)+n], tickfont_size=11, showgrid = False)
    fig4.update_traces(textposition = 'outside', textfont_size=11)

    if(int(dados[(dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RESERVA_VAGA'].sum()) < 1):

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

    else:

      lista5 = []

      for i in range(0, len(escolha_ANOS), 1):

        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RESERVA_VAGA'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RVREDEPUBLICA'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RVETNICO'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RVPDEF'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RVSOCIAL_RF'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_ING_RVOUTROS'].sum()))

      reserva_vagas = ['Total', 'Rede Pública', 'Étnica', 'Deficientes', 'Cunho Social/<br>Renda Familiar', 'Outros']

      if(len(escolha_ANOS) == 1):

        fig5 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista5[0:6], text = lista5[0:6], marker_pattern_shape="/")])
        fig5.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      if(len(escolha_ANOS) == 2):

        fig5 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista5[0:6], text = lista5[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = reserva_vagas, y = lista5[6:12], text = lista5[6:12], marker_pattern_shape="x", marker_color='#f63366')])
        fig5.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      if(len(escolha_ANOS) == 3):

        fig5 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista5[0:6], text = lista5[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = reserva_vagas, y = lista5[6:12], text = lista5[6:12], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = reserva_vagas, y = lista5[12:18], text = lista5[12:18], marker_pattern_shape="-", marker_color='#179462')])
        fig5.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))


      fig5.update_xaxes(tickfont_size=11)
      fig5.update_yaxes(range = [0, max(lista5)+15], tickfont_size=11, showgrid = False)
      fig5.update_traces(textposition = 'outside', textfont_size=11)

      st.subheader('Gráficos:')
      tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cor/Raça", "Formas de Ingresso", "Gêneros", "Idades", "Reserva de Vagas"])
      with tab1:
        st.plotly_chart(fig1, use_container_width=True)
      with tab2:
        st.plotly_chart(fig2, use_container_width=True)
      with tab3:
        st.plotly_chart(fig4, use_container_width=True)
      with tab4:
        st.plotly_chart(fig3, use_container_width=True)
      with tab5:
        st.plotly_chart(fig5, use_container_width=True)
      button_pagina_incical = st.button('Página Inicial')
      if(button_pagina_incical):
        pagina_inicial()

  if(escolha_CATEGORIA == 'Matriculados'):

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    for i in range(0, len(escolha_ANOS), 1):

      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_BRANCA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_PRETA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_PARDA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_AMARELA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_INDIGENA'].sum()))
      lista1.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_CORND'].sum()))

      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_0_17'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_18_24'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_25_29'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_30_34'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_35_39'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_40_49'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_50_59'].sum()))
      lista2.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_60_MAIS'].sum())) 

      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_MASC'].sum()))
      lista3.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_FEM'].sum()))

      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()) + int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()) + int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANCADA'].sum()) + int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_DESVINCULADO'].sum()) - int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()) + int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_FALECIDO'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT'].sum()) - int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANCADA'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_DESVINCULADO'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_TRANSFERIDO'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum()))
      lista4.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_SIT_FALECIDO'].sum()))

    n = grafico_limite(max(lista1))

    cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Declarada']
    idades = ['Total', 'Até 17', '18 até 24', '25 até 29', '30 até 34', '35 até 39', '40 até 49', '50 até 59', '60 ou mais']
    generos = ['Total', 'Homens', 'Mulheres']
    situacoes = ['Total', 'Cursandos', 'Matrículas<br>Trancada', 'Desvinculados', 'Transferidos', 'Formados', 'Falecidos']

    if(len(escolha_ANOS) == 1):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/")])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))   
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/")])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/", width = 0.45)])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = situacoes, y = lista4[0:7], text = lista4[0:7], marker_pattern_shape="/")])
      fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Situações do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))


    if(len(escolha_ANOS) == 2):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366')])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))   
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366')])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366')])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = situacoes, y = lista4[0:7], text = lista4[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = situacoes, y = lista4[7:14], text = lista4[7:14], marker_pattern_shape="x", marker_color='#f63366')])
      fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Situações dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if(len(escolha_ANOS) == 3):

      fig1 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = cor_raca, y = lista1[0:7], text = lista1[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = cor_raca, y = lista1[7:14], text = lista1[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = cor_raca, y = lista1[14:21], text = lista1[14:21], marker_pattern_shape="-", marker_color='#179462')])
      fig1.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Cor/Raça dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))         
      fig2 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = idades, y = lista2[0:9], text = lista2[0:9], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = idades, y = lista2[9:18], text = lista2[9:18], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = idades, y = lista2[18:27], text = lista2[18:27], marker_pattern_shape="-", marker_color='#179462')])
      fig2.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Idades dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig3 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = generos, y = lista3[0:3], text = lista3[0:3], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = generos, y = lista3[3:6], text = lista3[3:6], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = generos, y = lista3[6:9], text = lista3[6:9], marker_pattern_shape="-", marker_color='#179462')])
      fig3.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Gêneros dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      fig4 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = situacoes, y = lista4[0:7], text = lista4[0:7], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = situacoes, y = lista4[7:14], text = lista4[7:14], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = situacoes, y = lista4[14:21], text = lista4[14:21], marker_pattern_shape="-", marker_color='#179462')])
      fig4.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} por Situações dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    fig1.update_xaxes(tickfont_size=11)
    fig1.update_yaxes(range = [0, max(lista1)+n], tickfont_size=11, showgrid = False)
    fig1.update_traces(textposition = 'outside', textfont_size=11)

    fig2.update_xaxes(tickfont_size=11)
    fig2.update_yaxes(range = [0, max(lista2)+n], tickfont_size=11, showgrid = False)
    fig2.update_traces(textposition = 'outside', textfont_size=11)

    fig3.update_xaxes(tickfont_size=11)
    fig3.update_yaxes(range = [0, max(lista3)+n], tickfont_size=11, showgrid = False)
    fig3.update_traces(textposition = 'outside', textfont_size=11)

    fig4.update_xaxes(tickfont_size=11)
    fig4.update_yaxes(range = [0, max(lista4)+n], tickfont_size=11, showgrid = False)
    fig4.update_traces(textposition = 'outside', textfont_size=11)

    if(int(dados[(dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RESERVA_VAGA'].sum()) < 1):

      st.subheader('Gráficos:')
      tab1, tab2, tab3, tab4 = st.tabs(["Cor/Raça", "Gêneros", "Idades", "Situações"])
      with tab1:
        st.plotly_chart(fig1, use_container_width=True)
      with tab2:
        st.plotly_chart(fig3, use_container_width=True)
      with tab3:
        st.plotly_chart(fig2, use_container_width=True)  
      with tab4:
        st.plotly_chart(fig4, use_container_width=True) 
      button_pagina_incical = st.button('Página Inicial')
      if(button_pagina_incical):
        pagina_inicial()   

    else:

      lista5 = []

      for i in range(0, len(escolha_ANOS), 1):

        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RESERVA_VAGA'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RVREDEPUBLICA'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RVETNICO'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RVPDEF'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RVSOCIAL_RF'].sum()))
        lista5.append(int(dados[(dados['NU_ANO_CENSO'] == escolha_ANOS[i]) & (dados['CO_IES'] == escolha_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_MAT_RVOUTROS'].sum()))

      reserva_vagas = ['Total', 'Rede Pública', 'Étnica', 'Deficientes', 'Cunho Social/<br>Renda Familiar', 'Outros']

      if(len(escolha_ANOS) == 1):

        fig5 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista5[0:6], text = lista5[0:6], marker_pattern_shape="/")])
        fig5.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas do Ano de {escolha_ANOS[0]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      if(len(escolha_ANOS) == 2):

        fig5 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista5[0:6], text = lista5[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = reserva_vagas, y = lista5[6:12], text = lista5[6:12], marker_pattern_shape="x", marker_color='#f63366')])
        fig5.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas dos Anos de {escolha_ANOS[0]} e {escolha_ANOS[1]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      if(len(escolha_ANOS) == 3):

        fig5 = go.Figure(data=[go.Bar(name = str(escolha_ANOS[0]), x = reserva_vagas, y = lista5[0:6], text = lista5[0:6], marker_pattern_shape="/"), go.Bar(name = str(escolha_ANOS[1]), x = reserva_vagas, y = lista5[6:12], text = lista5[6:12], marker_pattern_shape="x", marker_color='#f63366'), go.Bar(name = str(escolha_ANOS[2]), x = reserva_vagas, y = lista5[12:18], text = lista5[12:18], marker_pattern_shape="-", marker_color='#179462')])
        fig5.update_layout(title_text = f'Quantidade de Estudantes {escolha_CATEGORIA} do Curso de {escolha_CURSO}<br>da {escolha_SG_IES} que Participam do Programa de Reserva de Vagas dos Anos de {escolha_ANOS[0]}, {escolha_ANOS[1]} e {escolha_ANOS[2]}', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

      fig5.update_xaxes(tickfont_size=11)
      fig5.update_yaxes(range = [0, max(lista5)+20], tickfont_size=11, showgrid = False)
      fig5.update_traces(textposition = 'outside', textfont_size=11)

      st.subheader('Gráficos:')
      tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cor/Raça", "Gêneros", "Idades", "Reserva de Vagas", "Situações"])
      with tab1:
        st.plotly_chart(fig1, use_container_width=True)
      with tab2:
        st.plotly_chart(fig3, use_container_width=True)
      with tab3:
        st.plotly_chart(fig2, use_container_width=True)  
      with tab4:
        st.plotly_chart(fig5, use_container_width=True) 
      with tab5:
        st.plotly_chart(fig4, use_container_width=True) 
      button_pagina_incical = st.button('Página Inicial')
      if(button_pagina_incical):
        pagina_inicial()            

def pagina_inicial(dados):

  titulo = st.header('Analisador Gráfico do Censo da Educação Superior')
  espaco = st.text('')
  sobre = st.subheader('Sobre:')
  descricao1 = st.markdown('O site realiza análises gráficas dos dados do Censo da Educação Superior, providos pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira, comparando a quantidade de estudantes entre concluintes, evadidos, ingressantes e matriculados dos cursos e instituições de ensino superior do Brasil.')
  descricao2 = st.markdown('Desenvolvido por Guilherme Tomaselli Borchardt, junto ao grupo de Iniciação Científica sobre Evasão Escolar, orientado pela professora Isabela Gasparini e pertencente à Universidade do Estado de Santa Catarina (UDESC - CCT).')
  st.sidebar.title('Opções:')
  try:
    escolha_NOME_ESTADO = st.sidebar.selectbox('Escolha um estado:', (dados['NO_UF'].drop_duplicates().sort_values()))
    escolha_ESTADO = int(dados[dados['NO_UF'] == escolha_NOME_ESTADO]['CO_UF'].drop_duplicates())
    escolha_SG_IES = st.sidebar.selectbox('Escolha uma instituição de ensino:', (dados[(dados['NU_ANO_CENSO'] >= 2015) & (dados['CO_UF'] == escolha_ESTADO)]['SG_IES'].drop_duplicates().sort_values().dropna()))
    escolha_IES = int(dados[(dados['NU_ANO_CENSO'] >= 2015) & (dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES)]['CO_IES'].drop_duplicates())
    escolha_CURSO = st.sidebar.selectbox('Escolha um curso:', (dados[(dados['NU_ANO_CENSO'] >= 2015) & (dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES)]['NOME_CURSO'].drop_duplicates().sort_values().dropna()))
    if(int((dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['QT_CONC'].sum())) > 0):
      if(dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['QT_MAT'] > 0)]['NU_ANO_CENSO'].count() >= 4):
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Concluintes', 'Evadidos', 'Ingressantes', 'Matriculados'))
        if(escolha_CATEGORIA == 'Evadidos'):
          button_gerar_grafico = st.sidebar.button('Gerar Gráfico')
          if(button_gerar_grafico):
              titulo.empty()
              espaco.empty()
              sobre.empty()
              descricao1.empty()
              descricao2.empty()
              grafico_estudantes_evadidos(escolha_SG_IES, escolha_IES, escolha_CURSO, dados)
        else:
          escolha_ANOS = st.sidebar.multiselect('Escolha quais anos deseja analisar:', dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna(), default = dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna().min())
          if(len(escolha_ANOS) > 0 and len(escolha_ANOS) < 4):       
            button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
            if(button_gerar_grafico):
                titulo.empty()
                espaco.empty()
                sobre.empty()
                descricao1.empty()
                descricao2.empty()
                grafico_estudantes(sorted(escolha_ANOS), escolha_SG_IES, escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
          else:
            st.sidebar.error('Por favor, selecione entre um e três anos.')               
      else:
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Concluintes', 'Ingressantes', 'Matriculados'))
        escolha_ANOS = st.sidebar.multiselect('Escolha quais anos deseja analisar:', dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna(), default = dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna().min())
        if(len(escolha_ANOS) > 0 and len(escolha_ANOS) < 4):
          button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
          if(button_gerar_grafico):
              titulo.empty()
              espaco.empty()
              sobre.empty()
              descricao1.empty()
              descricao2.empty()
              grafico_estudantes(sorted(escolha_ANOS), escolha_SG_IES, escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
        else:
          st.sidebar.error('Por favor, selecione entre um e três anos.')  
    else:
      if(dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2019)]['QT_ING'].sum() > 0 and dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2020)]['QT_ING'].sum() > 0 and dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO) & (dados['NU_ANO_CENSO'] == 2021)]['QT_ING'].sum() > 0):
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Evadidos', 'Ingressantes', 'Matriculados'))
        if(escolha_CATEGORIA == 'Evadidos'):
          button_gerar_grafico = st.sidebar.button('Gerar Gráfico')
          if(button_gerar_grafico):
            titulo.empty()
            espaco.empty()
            sobre.empty()
            descricao1.empty()
            descricao2.empty()
            grafico_estudantes_evadidos(escolha_SG_IES, escolha_IES, escolha_CURSO, dados)
        else:
          escolha_ANOS = st.sidebar.multiselect('Escolha quais anos deseja analisar:', dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna(), default = dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna().min())
          if(len(escolha_ANOS) > 0 and len(escolha_ANOS) < 4):
            button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
            if(button_gerar_grafico):
              titulo.empty()
              espaco.empty()
              sobre.empty()
              descricao1.empty()
              descricao2.empty()
              grafico_estudantes(sorted(escolha_ANOS), escolha_SG_IES, escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
          else:
            st.sidebar.error('Por favor, selecione entre um e três anos.')          
      else:
        escolha_CATEGORIA = st.sidebar.selectbox('Escolha o que deseja analisar:', ('Ingressantes', 'Matriculados'))
        escolha_ANOS = st.sidebar.multiselect('Escolha quais anos deseja analisar:', dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna(), default = dados[(dados['CO_UF'] == escolha_ESTADO) & (dados['SG_IES'] == escolha_SG_IES) & (dados['NOME_CURSO'] == escolha_CURSO)]['NU_ANO_CENSO'].drop_duplicates().sort_values().dropna().min())
        if(len(escolha_ANOS) > 0 and len(escolha_ANOS) < 4):
          button_gerar_grafico = st.sidebar.button('Gerar Gráficos')
          if(button_gerar_grafico):
            titulo.empty()
            espaco.empty()
            sobre.empty()
            descricao1.empty()
            descricao2.empty()
            grafico_estudantes(sorted(escolha_ANOS), escolha_SG_IES, escolha_IES, escolha_CURSO, escolha_CATEGORIA, dados)
        else:
          st.sidebar.error('Por favor, selecione entre um e três anos.')
  except:
    st.sidebar.error('Desculpa, ocorreu algum problema com os dados selecionados.')
  st.sidebar.write('*Versão 4.5.0*')
  
@st.cache_data(show_spinner=False)
def load_data_alunos():

  dados1 = pd.read_csv('dados1.CSV', encoding='latin-1')
  dados2 = pd.read_csv('dados2.CSV', encoding='latin-1')
  dados3 = pd.read_csv('dados3.CSV', encoding='latin-1')
  dados4 = pd.read_csv('dados4.CSV', encoding='latin-1')

  dados = pd.concat([dados1, dados2, dados3, dados4])

  return dados

if __name__ == '__main__':

  imagem = Image.open('icone.png')
  st.set_page_config(page_title='Analisador Censos', page_icon=imagem)
  dados = load_data_alunos()
  pagina_inicial(dados)
