#       __        __      ________      ________  __      ________  ___________  _______  ___      ___       __        ________ 
#      /""\      |" \    /"       )    /"       )|" \    /"       )("     _   ")/"     "||"  \    /"  |     /""\      /"       )
#     /    \     ||  |  (:   \___/    (:   \___/ ||  |  (:   \___/  )__/  \\__/(: ______) \   \  //   |    /    \    (:   \___/ 
#    /' /\  \    |:  |   \___  \       \___  \   |:  |   \___  \       \\_ /    \/    |   /\\  \/.    |   /' /\  \    \___  \   
#   //  __'  \   |.  |    __/  \\       __/  \\  |.  |    __/  \\      |.  |    // ___)_ |: \.        |  //  __'  \    __/  \\  
#  /   /  \\  \  /\  |\  /" \   :)     /" \   :) /\  |\  /" \   :)     \:  |   (:      "||.  \    /:  | /   /  \\  \  /" \   :) 
# (___/    \___)(__\_|_)(_______/     (_______/ (__\_|_)(_______/       \__|    \_______)|___|\__/|___|(___/    \___)(_______/  

# Autor: Rafael A. Lima
# Versão: 0.1.0

from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import sqlite3
import os
import config
import numpy as np
import dash
from dash import Dash, html, dcc
import plotly.graph_objs as go

app = Flask (__name__)
db_path = config.DB_PATH

#função para inicializar o banco de dados
def init_db():
    with sqlite3.connect ('db_path') as conn:
        cursor = conn.cursor()
        cursor.execute('''
             CREATE TABLE IF NOT EXISTS inadimplencia (
                 mes TEXT PRIMARY KEY,
                 inadimplencia REAL
                 )          
              ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS selic (
                 mes TEXT PRIMARY KEY,
                 selic_diaria REAL
                 )          
            ''')
        conn.commit()
    
@app.route('/')
def index():
    return render_template_string('''
    <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { margin: 0; min-height: 100vh; display: grid; place-items: center; font: 16px/1.5 system-ui, sans-serif; color: #10202e; background: linear-gradient(#d9e0e8 1px, transparent 1px) 0 0 / 28px 28px, linear-gradient(90deg, #d9e0e8 1px, transparent 1px) 0 0 / 28px 28px, #f4f6f8; }
  main { --x: 50%; --y: 0; width: min(520px, 92vw); margin: 2rem 0; padding: 2.2rem; box-sizing: border-box; border: 1px solid #d9e0e8; border-radius: 18px; background: radial-gradient(280px circle at var(--x) var(--y), rgba(242, 177, 52, .24), transparent 70%), #fff; box-shadow: 0 24px 48px -16px rgba(16, 32, 46, .3); }
  h1 { margin: .2rem 0 0; font: 700 1.9rem/1.15 ui-serif, Georgia, serif; letter-spacing: -.02em; }
  svg path { fill: none; stroke: #0e5a6b; stroke-width: 2.5; stroke-linejoin: round; stroke-dasharray: 400; stroke-dashoffset: 400; animation: d 2.4s .3s ease-out forwards; }
  svg path:last-child { stroke: #f2b134; animation-delay: .9s; }
  @keyframes d { to { stroke-dashoffset: 0 } }
  @media (prefers-reduced-motion: reduce) { svg path { animation: none; stroke-dashoffset: 0 } }
  label { display: block; margin-top: 1.1rem; font-size: .9rem; font-weight: 600; }
  input[type=file] { width: 100%; box-sizing: border-box; margin-top: .4rem; padding: .9rem; border: 2px dashed #b7c3d0; border-radius: 12px; background: #f8fafc; font: inherit; color: #5b6b7b; cursor: pointer; transition: .25s; }
  input[type=file]:hover, input[type=file]:focus-visible { border-color: #0e5a6b; background: #eef6f8; transform: translateY(-2px); }
  ::file-selector-button { margin-right: 1rem; padding: .5rem .9rem; border: 0; border-radius: 8px; background: #0e5a6b; color: #fff; font-weight: 600; cursor: pointer; }
  input[type=submit] { width: 100%; margin-top: 1.6rem; padding: .95rem; border: 0; border-radius: 12px; color: #fff; font: inherit; font-weight: 600; cursor: pointer; background: linear-gradient(110deg, #10202e 40%, #0e5a6b 50%, #10202e 60%) 100% 0 / 250% 100%; transition: background-position .7s, transform .15s; }
  input[type=submit]:hover { background-position: 0 0; }
  input[type=submit]:active { transform: scale(.98); }
  hr { margin: 2rem 0 1rem; border: 0; border-top: 1px solid #d9e0e8; }
  a { display: block; padding: .7rem .9rem; border-radius: 10px; color: #10202e; font-weight: 500; text-decoration: none; box-shadow: inset 3px 0 0 #f2b134; transition: .25s; }
  a:hover { padding-left: 1.5rem; background: #fdf5e1; box-shadow: inset 8px 0 0 #f2b134; }
</style>
<main onmousemove="r=this.getBoundingClientRect();this.style.setProperty('--x',event.clientX-r.left+'px');this.style.setProperty('--y',event.clientY-r.top+'px')">
    <svg viewBox="0 0 200 40" width="100%" height="40"><path d="M0 34 L25 28 L50 31 L75 18 L100 22 L125 10 L150 15 L175 5 L200 8"/><path d="M0 12 L40 12 L80 20 L120 30 L160 26 L200 36"/></svg>
    <h1> Upload de dados Econômicos </h1>
    <form action='/upload' method='POST' enctype='multipart/form-data'>
        <label for='campo_inadimplencia'> Aquivo de Inadimplência (CSV): </label>
        <input id='campo_inadimplencia' name='campo_inadimplencia' type='file' required>

        <label for='campo_selic'> Arquivo da Taxa Selic (CSV) </label>
        <input id='campo_selic' name='campo_selic' type='file' required>
        <input type='submit' value='Fazer Upload'>
    </form>
    <hr>
    <a href='/consultar'> Consultar dados Armazenados </a>
    <a href='/graficos'> Visualizar Graficos </a>
    <a href='/editar_inadimplencia'> Editar dados de Inadimplencia </a>
    <a href='/editar_selic'> Editar dados da Selic </a>
    <a href='/correlacao'> Analisar Correlação </a>
</main>
''')
    
    
@app.route('/upload', methods =['POST','GET'])
def upload():
    inad_file = request.files.get('campo_inadimplencia')
    selic_file = request.files.get('campo_selic')
    
    # Vamos verificar se os arquivos foram devidamente enviados
    if not inad_file or not selic_file:
        return jsonify({"Erro":"Ambos os arquivos precisam ser enviados!"})
    inad_df = pd.read_csv(
        inad_file, 
        sep = ';',
        names = ['data', 'inadimplencia'],
        header = 0
    )
    selic_df = pd.read_csv(
        selic_file, 
        sep = ';',
        names = ['data', 'selic_diaria'],
        header = 0
    )
    
    inad_df['data'] = pd.to_datetime(inad_df['data'], format="%d/%m/%Y")
    selic_df['data'] = pd.to_datetime(selic_df['data'], format="%d/%m/%Y")
    
    inad_df['mes'] = inad_df['data'].dt.to_period('M').astype(str)
    selic_df['mes'] = selic_df['data'].dt.to_period('M').astype(str)
    
    inad_mensal = inad_df[['mes','inadimplencia']].drop_duplicates()
    selic_mensal = selic_df.groupby('mes')['selic_diaria'].mean().reset_index()
    
    with sqlite3.connect(db_path) as conn :
        inad_mensal.to_sql('inadimplencia', conn, if_exists = 'replace', index = False)
        selic_mensal.to_sql('selic', conn, if_exists = 'replace', index = False)
    return jsonify({'Mensagem':'dados armazenados com sucesso!'})

@app.route('/consultar', methods=['POST','GET'])
def consultar():
    # Resultado se a pagina for carregada recebendo um POST
    if request.method == 'POST' :
        tabela = request.form.get('campo_tabela')
        if tabela not in ['inadimplencia','selic'] :
            return jsonify ({'Erro':'Tabela inválida'}),400
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query(f'SELECT * FROM {tabela}',conn)
        return df.to_html(index=False)
    
    
    # Resultado sem receber um POST, ou seja, primeiro carregamento da pagina
    return render_template_string('''
        <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { margin: 0; min-height: 100vh; display: grid; place-items: center; font: 16px/1.5 system-ui, sans-serif; color: #10202e; background: linear-gradient(#d9e0e8 1px, transparent 1px) 0 0 / 28px 28px, linear-gradient(90deg, #d9e0e8 1px, transparent 1px) 0 0 / 28px 28px, #f4f6f8; }
  main { --x: 50%; --y: 0; width: min(520px, 92vw); margin: 2rem 0; padding: 2.2rem; box-sizing: border-box; border: 1px solid #d9e0e8; border-radius: 18px; background: radial-gradient(280px circle at var(--x) var(--y), rgba(242, 177, 52, .24), transparent 70%), #fff; box-shadow: 0 24px 48px -16px rgba(16, 32, 46, .3); }
  h1 { margin: .2rem 0 0; font: 700 1.9rem/1.15 ui-serif, Georgia, serif; letter-spacing: -.02em; }
  svg path { fill: none; stroke: #0e5a6b; stroke-width: 2.5; stroke-linejoin: round; stroke-dasharray: 400; stroke-dashoffset: 400; animation: d 2.4s .3s ease-out forwards; }
  svg path:last-child { stroke: #f2b134; animation-delay: .9s; }
  @keyframes d { to { stroke-dashoffset: 0 } }
  @media (prefers-reduced-motion: reduce) { svg path { animation: none; stroke-dashoffset: 0 } }
  label { display: block; margin-top: 1.1rem; font-size: .9rem; font-weight: 600; }
  select { width: 100%; box-sizing: border-box; margin-top: .4rem; padding: .9rem 2.6rem .9rem .9rem; border: 2px solid #b7c3d0; border-radius: 12px; font: inherit; color: #10202e; cursor: pointer; appearance: none; transition: .25s; background: linear-gradient(45deg, transparent 50%, #0e5a6b 50%) calc(100% - 22px) 52% / 6px 6px no-repeat, linear-gradient(135deg, #0e5a6b 50%, transparent 50%) calc(100% - 16px) 52% / 6px 6px no-repeat, #f8fafc; }
  select:hover, select:focus-visible { border-color: #0e5a6b; transform: translateY(-2px); outline: 0; box-shadow: 0 8px 20px -10px rgba(14, 90, 107, .6); }
  input[type=submit] { width: 100%; margin-top: 1.6rem; padding: .95rem; border: 0; border-radius: 12px; color: #fff; font: inherit; font-weight: 600; cursor: pointer; background: linear-gradient(110deg, #10202e 40%, #0e5a6b 50%, #10202e 60%) 100% 0 / 250% 100%; transition: background-position .7s, transform .15s; }
  input[type=submit]:hover { background-position: 0 0; }
  input[type=submit]:active { transform: scale(.98); }
  a { display: block; margin-top: 1.4rem; padding: .7rem .9rem; border-radius: 10px; color: #10202e; font-weight: 500; text-decoration: none; box-shadow: inset 3px 0 0 #f2b134; transition: .25s; }
  a:hover { padding-left: 1.5rem; background: #fdf5e1; box-shadow: inset 8px 0 0 #f2b134; }
</style>
<main onmousemove="r=this.getBoundingClientRect();this.style.setProperty('--x',event.clientX-r.left+'px');this.style.setProperty('--y',event.clientY-r.top+'px')">
    <svg viewBox="0 0 200 40" width="100%" height="40"><path d="M0 34 L25 28 L50 31 L75 18 L100 22 L125 10 L150 15 L175 5 L200 8"/><path d="M0 12 L40 12 L80 20 L120 30 L160 26 L200 36"/></svg>
    <h1>Consulta de Tabelas</h1>
    <form method='POST'>
        <label for='campo_tabela'> Escolha uma Tabela </label>
        <select id='campo_tabela' name='campo_tabela'>
            <option value='inadimplencia'> Inadimplencia </option>
            <option value='selic'> Taxa Selic </option>
        </select>
        <input type='submit' value='consultar'>
    </form>
    <a href="/"> Voltar </a>
</main>
''')
       
@app.route('/graficos')
def graficos ():
    with sqlite3.connect(db_path) as conn :
        inad_df     = pd.read_sql_query ('SELECT * FROM inadimplencia', conn)
        selic_df    = pd.read_sql_query ('SELECT * FROM selic', conn)
        
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x = inad_df ['mes'],
        y = inad_df ['inadimplencia'],
        mode = 'lines+markers',
        name = 'Inadimplência'        
        )           
    ) 
    #'ggplot2', 'seaborn', 'simple_white', 'plotly','plotly_white', 'plotly_dark', 'presentation', 'xgridoff','ygridoff', 'gridon', 'none'
    fig1.update_layout(
        title = "Evolução da Inadimplência",
        xaxis_title = "Mês",
        yaxis_title = '%',
        template = 'plotly_dark'   
                        )
    
    fig2 = go.Figure ()
    fig2.add_trace (go.Scatter(
        x = selic_df['mes'],
        y = selic_df ['selic_diaria'],
        mode = 'lines+markers',
        name= 'Selic'
        )
    )
    fig2.update_layout(
        title       = 'Média Mensal da Selic',
        xaxis_title = 'Mês',
        yaxis_title = 'Taxa',
        template    = 'plotly_dark'
    )
    
    graph_html_1 = fig1.to_html(full_html = False, include_plotlyjs='cdn')
    graph_html_2 = fig2.to_html(full_html = False, include_plotlyjs = False)
    return render_template_string('''
                                  <html>
            <head>
                <title> Graficos Esconomicos </title>
                <style>
                        .container{
                            display:flex;
                            justify-content:space-around;
                        }
                        .graph{ 
                            width: 48%;
                        }         
                </style>
            </head>
            <body>
                   <h1><marquee> Graficos Economicos </marquee></h1>   
                    <div class="container">                      
                        <div class="graph">{{ grafico1 |safe }}</div>
                        <div class="graph">{{grafico2 |safe }}</div>
                    </div>            
            </body>
        </html>
                                  
                                  ''', grafico1 = graph_html_1, grafico2= graph_html_2)

@app.route('/editar_inadimplencia', methods=['POST','GET'])
def editar_inadimplencia():
    # Recebe os dados e realiza a edição
    if request.method == 'POST':
        mes = request.form.get('campo_mes')
        novo_valor = request.form.get('campo_valor')
        try:
            novo_valor = float(novo_valor)
        except:
            return jsonify({"ERRO":"Valor inválido"}),400
        
        with sqlite3.connect(db_path) as conn :
            cursor = conn.cursor()
            cursor.execute("UPDATE inadimplencia SET inadimplencia = ? WHERE mes = ?",(novo_valor, mes))
        return jsonify ({"Mensagem":f"O valor atualizado para a data {mes} com sucesso"})
        
    # exibe 0 painel de edição (primeira carga sem dados editados)
    return render_template_string('''
        <h1> Editar Inadimplencia </h1>
        <form method="POST" action="/editar_inadimplencia">
            <label for="campo_mes">Mês (AAAA-MM):</label>
            <input type="text" name="campo_mes"><br>
                                  
            <label for="campo_valor">Novo valor de Inadimplência:</label>
            <input type="text" name="campo_valor"><br>
                                  
            <input type="submit" value="Atualizar Dados">
        </form>
        <br>
        <a href="/"> Voltar </a>
    ''') 

@app.route('/editar_selic', methods = ['POST','GET'])
def editar_selic():
     # Recebe os dados e realiza a edição
    if request.method == 'POST':
        mes = request.form.get('campo_mes')
        novo_valor = request.form.get('campo_valor')
        try:
             novo_valor = float(novo_valor)
        except:
            return jsonify({"ERRO":"Valor inválido"}),400
        
        with sqlite3.connect(db_path) as conn :
            cursor = conn.cursor()
            cursor.execute("UPDATE selic SET selic_diaria = ? WHERE mes = ?",(novo_valor, mes))
            
            if cursor.rowcount == 0:
                return jsonify ({'Erro': f'Não foi possível encontrar o registro para o mês {mes}'}),404
        return jsonify ({'Mensagem':f'Taxa sekic atualizada para o mes {mes} com sucesso'})
    
    return render_template_string('''
        <h1>Editar Taxa SELIC</h1>

        <form method="POST" action="/editar_selic">

            <label for="campo_mes">Mês (AAAA-MM):</label>
            <input name="campo_mes" required>
            <br><br>

            <label for="campo_valor">Nova Taxa SELIC:</label>
            <input name="campo_valor">
            <br><br>

            <input type="submit" value="Atualizar Dados">

        </form>

        <br>
        <a href="/">Voltar</a>
        ''')
    
    # exibe 0 painel de edição (primeira carga sem dados editados)
    return render_template_string('''
        <h1> Editar Selic </h1>
        <form method="POST" action="/editar_selic">
            <label for="campo_mes">Mês (AAAA-MM):</label>
            <input type="text" name="campo_mes"><br>
                                  
            <label for="campo_valor">Novo valor de Selic:</label>
            <input type="text" name="campo_valor"><br>
                                  
            <input type="submit" value="Atualizar Dados">
        </form>
        <br>
        <a href="/"> Voltar </a>
    ''') 
    
@app.route('/correlacao')
def correlacao():
    with sqlite3.connect(db_path) as conn:
         inad_df = pd.read_sql_query('SELECT * FROM inadimplencia', conn)
         selic_df = pd.read_sql_query('SELECT * FROM selic', conn)
    merged = pd.merge(inad_df, selic_df, on = 'mes')
    
    # Correlação de pearson
    correl = merged ['inadimplencia'].corr(merged['selic_diaria'])
    
    # Regressão Linear para visualização 
    
    x = merged ['selic_diaria']
    y = merged ['inadimplencia']
    m, b = np.polyfit (x,y,1)
    
    # O terceiro argumento indica que queremos ajustar uma reta, ou seja, um polinomio de primeiro grau
    # M -> Coeficiente angular (inclinação da reta)
    # B -> Coeficiente linear (ponto onde a reta cruza o eixo y)
 
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode = 'markers',
        name = 'Inadimplencia x Selic',
        hovertemplate = 'SELIC: %{X:.2f}<br>Inadimplencia: %{Y:.2f}<extra></extra>',
        marker=dict(
            color = 'rgba(0,123,255,0.8)',
            size = 12,
            line = dict(width=2, color='white'),
            symbol='circle'
            )
        ))
    fig.add_trace(go.Scatter(
       x=x,
       y= m * x + b,
       mode = 'lines',
       name = 'Linha de Tendencia',
       line = dict(color = 'rgba(220,53, 69,1)', width=4, dash='dot')
    ))
    fig.update_layout(
        title ={
            'text':f'<b>Correlação entre Selic e Inadiplência</b><br><span style="font-size:16px">Coeficiente de Correlação: {correl}</span>',
            'y':0.95,
            'x':0.5,
            'xanchor':'center',
            'yanchor':'top'  
        },
        xaxis_title=dict(
            text         = 'Selic Media Mensal (%)',
            font         = dict(size=18,family = 'Arial', color = 'gray')
            ),
        yaxis_title=dict(
            text         = 'Inadimplencia (%)',
            font         = dict(size=18,family = 'Arial', color = 'gray')
            ),
        xaxis=dict(
            gridcolor    = 'light gray',
            tickfont     = dict(size=14,family = 'Arial', color = 'gray')
            ),
        yaxis=dict(
            gridcolor    = 'light gray',
            tickfont     = dict(size=14,family = 'Arial', color = 'gray')
            ),
        plot_bgcolor     = "#f8f9fa",
        paper_bgcolor    = "white",
        font             = dict(size=14,family = 'Arial', color = 'black'),
        margin           = dict(l=60, r=60, t=120, b=60),
        legend           = dict(
            orientation  = 'h',
            yanchor      = 'bottom',
            y            = 1.05,
            xanchor      = 'center',
            x            = 0.5,
            bgcolor      = 'rgba(0,0,0,0)',
            borderwidth  = 0
        )
    )
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return render_template_string('''
            <html>
        <head>
            <title>Correlação SELIC vs Inadimplência</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #ffffff; color: #333; }
                .container { width: 90%; margin: auto; text-align: center; }
                h1 { margin-top: 40px; }
                a { text-decoration: none; color: #007bff; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Correlação entre SELIC e Inadimplência</h1>
                <div>{{graph|safe}}</div>
                <br><div><a href="/">Voltar</a></div>
            </div>
        </body>
        </html>                      
    ''',graph = graph_html)
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    