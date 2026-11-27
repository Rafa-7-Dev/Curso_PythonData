import turtle # RESPONSÁVEL POR FAZER A TELA, TRABALHA COM FORMAS GEOMÉTRICAS # 
import random
import time

tela = turtle.Screen()
tela.title("Jogo da Cobrinha - Nokia 3310")

pontos = 0

tela.bgcolor("black")
tela.setup(width=600, height =600)

tela.tracer(0)

cobra = turtle.Turtle() # Esse é o jogador (a cobrinha)
cobra.speed(0)
cobra.shape("square")
cobra.color("violet")
cobra.penup() # impede que a cobra desenhe enquanto se movimenta
cobra.goto(0,0)
cobra.direction  = 'stop'

fruta = turtle.Turtle()
fruta.speed(0)
fruta.shape('circle')
fruta.color('green')
fruta.penup()
fruta.goto(0,100)

corpo = []


def cima():
    cobra.direction = 'up'
def baixo():
    cobra.direction = 'down'
def direita():
    cobra.direction = 'right'
def esquerda():
    cobra.direction = 'left'

# Fazer a cobra obedecer aos comandos do teclado
tela.listen()
tela.onkeypress(cima, 'Up')
tela.onkeypress(baixo, 'Down')
tela.onkeypress(direita, 'Right')
tela.onkeypress(esquerda, 'Left')

while True:
    tela.update()
    
    if cobra.distance(fruta) <20:
        x = random.randint (-280, 280)
        y = random.randint (-280, 280)
        fruta.goto (x,y)
        pontos += 10 # Soma os pontos 
        tela .title(f'Pontos: {str(pontos)}')
        
        novo_tamanho = turtle.Turtle() #Criar um novo tamanho do corpo
        novo_tamanho.speed(0)
        novo_tamanho.shape('square')
        novo_tamanho.color('pink')
        novo_tamanho.penup()
        corpo.append(novo_tamanho)
        
    time.sleep(0.1)
    
        
        
    
    # Faz a cobra se movimentar pro lado
    if cobra.direction == 'left':
        x = cobra.xcor()
        cobra.setx(x - 20)
    elif cobra.direction == 'right':
        x = cobra.xcor()
        cobra.setx (x + 20)
    # Faz a cobra se movimentar pra cima e pra baixo
    if cobra.direction == 'up':
        y = cobra.ycor()
        cobra.sety(y + 20)
    elif cobra.direction == 'down':
        y = cobra.ycor()
        cobra.sety (y - 20)
        
    for i in range(len(corpo)-1,0,-1) :
    # iniciamos um laço para percorrer os pedaços do corpo
    # "len" retorna a quantidade de pedaços do corpo
    # Esse - 1 começa pelo ultimo pedaço do corpo
    # Esse 0 define que o laço "for" vai até o primeiro pedaço sem incluir ele.
    # Esse - 1 final faz o contador diminuir de 1 em 1 andando de trás pra frente    
    
        x = corpo[i - 1].xcor()
        y = corpo[i - 1].ycor()
        corpo[i].goto(x, y)
        if len (corpo)>0:
            x = cobra.xcor()
            y = cobra.ycor()
        
    if cobra.xcor() > 280 or cobra.xcor() <-280 or cobra.ycor() >280 or cobra.ycor() <-280:
        tela.title(f'GAME OVER! Pontuação final: {str(pontos)}')
        cobra.goto(0,0)
        cobra.direction = "stop"
        break
    
tela.mainloop()