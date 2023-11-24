import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import random

# cores
co0 = "#FFFFFF"   # branco
co1 = "#333333"   # preto
co11 = "#555555"  # cinza
co2 = "#fcc058"   # laranja
co3 = "#fff873"   # amarelo
co4 = "#34eb3d"   # verde
co5 = "#e85151"   # vermelho
fundo = "#3b3b3b" # cinza escuro

# configuração da janela
janela = Tk()
janela.title("")
janela.geometry("260x280")
janela.configure(bg=fundo)

# divisão da janela
headframe = Frame(janela, width=260, height=100, bg=co1, relief='raised')
headframe.grid(row = 0, column = 0, sticky = NW)

bodyframe = Frame(janela, width=260, height=300, bg=co11, relief='flat')
bodyframe.grid(row = 1, column = 0, sticky = NW)

style = ttk.Style(janela)
style.theme_use('clam')

# configuração do headframe - jogador
app_1 = Label(headframe, text="Jogador", height=1, anchor="center", font=("Ivy 9 bold"), bg=co1, fg=co0)
app_1.place(x=10, y=75)

app_1_line = Label(headframe, height=10, anchor="center", bg='#444444', fg=co0)
app_1_line.place(x=0, y=0)

app_1_point = Label(headframe, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_1_point.place(x=50, y=20)

# divisor de pontos
division = Label(headframe, text="VS", height=1, anchor="center", font=("Ivy 20 bold"), bg=co1, fg=co0)
division.place(x=111, y=27)

# configuração do headframe - computer
app_2_point = Label(headframe, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_2_point.place(x=181, y=20)

app_2 = Label(headframe, text="Computador", height=1, anchor="center", font=("Ivy 9 bold"), bg=co1, fg=co0)
app_2.place(x=175, y=75)

app_2_line = Label(headframe, height=10, anchor="center", bg='#444444', fg=co0)
app_2_line.place(x=255, y=0)

# linha de empate
app_tie = Label(headframe, width=255, anchor="center", bg='#444444', fg=co0)
app_tie.place(x=0, y=95)

# jogada
app_player = Label(bodyframe, text="", height=1, anchor="center", font=("Ivy 10 bold"), bg=co11, fg=co0)
app_player.place(x=15, y=10)
app_pc = Label(bodyframe, text="", height=1, anchor="center", font=("Ivy 10 bold"), bg=co11, fg=co0)
app_pc.place(x=190, y=10)



# ----- variaveis globais -----
global player, pc, rondas, player_points, pc_points
player_points = pc_points = 0
rondas = 10



# ----- func logica -----
def jogar(i):
    global rondas, player_points, pc_points
    
    if rondas > 0:
        print(rondas)
        opcoes = ['pedra', 'papel', 'tesoura']
        pc = random.choice(opcoes)
        player = i
        
        app_player['text'] = player
        app_player['fg'] = co0
        app_pc['text'] = pc
        app_pc['fg'] = co0
        
        #empates
        if player == 'pedra' and pc == 'pedra':
            print('empate')
            app_tie['bg'] = co3
            app_1_line['bg'] = co1
            app_2_line['bg'] = co1
        elif player == 'papel' and pc == 'papel':
            print('empate')
            app_tie['bg'] = co3
            app_1_line['bg'] = co1
            app_2_line['bg'] = co1
        elif player == 'tesoura' and pc == 'tesoura':
            print('empate')
            app_tie['bg'] = co3
            app_1_line['bg'] = co1
            app_2_line['bg'] = co1
            
            
        #perdas e ganhos
        elif player == 'pedra' and pc == 'papel':
            print('perdeu')
            app_tie['bg'] = co1
            app_1_line['bg'] = co1
            app_2_line['bg'] = co5
            pc_points += 1
            
        elif player == 'pedra' and pc == 'tesoura':
            print('ganhou')
            app_tie['bg'] = co1
            app_1_line['bg'] = co4
            app_2_line['bg'] = co1
            player_points += 1
        
        elif player == 'papel' and pc == 'tesoura':
            print('perdeu')
            app_tie['bg'] = co1
            app_1_line['bg'] = co1
            app_2_line['bg'] = co5
            pc_points += 1
            
        elif player == 'papel' and pc == 'pedra':
            print('ganhou')
            app_tie['bg'] = co1
            app_1_line['bg'] = co4
            app_2_line['bg'] = co1
            player_points += 1
            
        elif player == 'tesoura' and pc == 'pedra':
            print('perdeu')
            app_tie['bg'] = co1
            app_1_line['bg'] = co1
            app_2_line['bg'] = co5
            pc_points += 1
            
        elif player == 'tesoura' and pc == 'papel':
            print('ganhou')
            app_tie['bg'] = co1
            app_1_line['bg'] = co4
            app_2_line['bg'] = co1
            player_points += 1
        
        #atualização de pontos
        app_1_point['text'] = player_points
        app_2_point['text'] = pc_points
        
        #decrementar rondas
        rondas -= 1
        
    else:
        app_1_point['text'] = player_points
        app_2_point['text'] = pc_points
        finish()
        

        
# ----- func play -----
def play():
    global icon_pedra, icon_papel, icon_tesoura, b_icon_pedra, b_icon_papel, b_icon_tesoura
    
    b_play.destroy()
    
    # configuração do bodyframe
    icon_pedra = Image.open("images/pedra.png")
    icon_pedra = icon_pedra.resize((50,50))
    icon_pedra = ImageTk.PhotoImage(icon_pedra)
    b_icon_pedra = Button(bodyframe, command = lambda: jogar('pedra'), width=50, image=icon_pedra, compound=CENTER, bg=co11, fg=co1, font=("Ivy 9 bold"), anchor=CENTER, relief=FLAT)
    b_icon_pedra.place(x=15, y=60)

    icon_papel = Image.open("images/papel.png")
    icon_papel = icon_papel.resize((50,50))
    icon_papel = ImageTk.PhotoImage(icon_papel)
    b_icon_papel = Button(bodyframe, command = lambda: jogar('papel'), width=50, image=icon_papel, compound=CENTER, bg=co11, fg=co1, font=("Ivy 9 bold"), anchor=CENTER, relief=FLAT)
    b_icon_papel.place(x=101, y=60)

    icon_tesoura = Image.open("images/tesoura.png")
    icon_tesoura = icon_tesoura.resize((50,50))
    icon_tesoura = ImageTk.PhotoImage(icon_tesoura)
    b_icon_tesoura = Button(bodyframe, command = lambda: jogar('tesoura'), width=50, image=icon_tesoura, compound=CENTER, bg=co11, fg=co1, font=("Ivy 9 bold"), anchor=CENTER, relief=FLAT)
    b_icon_tesoura.place(x=190, y=60)


    
# ----- func finish -----
def finish():
    global rondas, player_points, pc_points
    player_points = pc_points = 0
    rondas = 10
    
    b_icon_pedra.destroy()
    b_icon_papel.destroy()
    b_icon_tesoura.destroy()
    
    playerpoints = int(app_1_point['text'])
    pcpoints = int(app_2_point['text'])
    
    #resultado
    if playerpoints == pcpoints:
        app_win = Label(bodyframe, text="empate!", height=1, anchor="center", font=("Ivy 10 bold"), bg=co11, fg=co0)
        app_win.place(x=100, y=80)
    
    elif playerpoints > pcpoints:
        app_win = Label(bodyframe, text="jogador venceu!", height=1, anchor="center", font=("Ivy 10 bold"), bg=co11, fg=co0)
        app_win.place(x=80, y=80)
    
    elif playerpoints < pcpoints:
        app_win = Label(bodyframe, text="PC venceu!", height=1, anchor="center", font=("Ivy 10 bold"), bg=co11, fg=co0)
        app_win.place(x=90, y=80)
    
    # ----- func jogar de novo -----
    def again():
        app_1_point['text'] = app_2_point['text'] = '0'
        app_win.destroy()
        play()
        b_play_again.destroy()
        
        
    b_play_again = Button(bodyframe, command = again, text='JOGAR', width=34, bg=fundo, fg=co0, font=("Ivy 9 bold"), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_play_again.place(x=6, y=150)
        
        
        
# botão jogar
b_play = Button(bodyframe, command = play, text='JOGAR', width=34, bg=fundo, fg=co0, font=("Ivy 9 bold"), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_play.place(x=6, y=150)

janela.mainloop()
