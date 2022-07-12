
import tkinter
from tkinter import *
from tkinter import ttk
import random

cor_preta = "#444466"  
cor_branca = "#feffff"  
cor_azul = "#6f9fbd"  
cor_valor = "#38576b"  
co_letra = "#403d3d"   
cor_profit = "#e06636"  
cor_profitmais = "#6dd695" 
cor_vermelha = "#ef5350"   
cor_verde = "#00bfa5"   
cor_fundo = "#3b3b3b"
co10 ="#fcfbf7"
cor1='#f58b5d'
cor2='#ff333a'
cor3='#6bd66f'
cor4="#ab8918"

janela=Tk()
janela.title('')
janela.geometry('350x280')
janela.configure(bg=cor_fundo)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=200,ipadx=280)


frame_topo=Frame(janela,width=350,height=30,bg=cor_branca,pady=0,padx=0,relief="flat",)
frame_topo.grid(row=1,column=0,sticky=NW)
frame_corpo=Frame(janela,width=350,height=280,bg=cor_fundo,pady=0,padx=0,relief="flat",)
frame_corpo.grid(row=2,column=0,sticky=NW)

style=ttk.Style(janela)
style.theme_use("clam")

#estilo topo
app_nome=Label(frame_topo,text="ADVINHA O NÚMERO",anchor='center',font=('verdana 14 bold'),bg=cor_branca,fg=cor_azul)
app_nome.place(x=55,y=0)

global tentativas
global pontuacao
#logica
#funcao inicia jogo

tentativas=5
pontuacao=0

def iniciar_jogo():
    l_regra1['text']=''
    l_regra2['text']=''
    l_regra3['text']=''
    
    numeros=random.sample(range(1,10),8)
    resposta= random.choice(numeros)
    
    def estado_do_valor(v):
        
        numeros=random.sample(range(1,10),8)
        resposta= [random.choice(numeros)]
    
        
        global tentativas
        global pontuacao
        
        
        for i in resposta:
            print(i)
            if v ==i:
                
                tentativas +=2
                pontuacao+=10
                l_tentativas['text']=str(tentativas)+'Tentativas'
                l_pontos['text']='Pontuacao: ' + str(pontuacao)
                
            else:
                tentativas -=1
                l_tentativas['text']=str(tentativas)+'Tentativas'
                
                print(tentativas)
                print(numeros)
                
                if tentativas <=0:
                    botao_1['state']='disable'
                    botao_2['state']='disable'
                    botao_3['state']='disable'
                    botao_4['state']='disable'
                    botao_5['state']='disable'
                    botao_6['state']='disable'
                    botao_7['state']='disable'
                    botao_8['state']='disable'
                    
                    
                    
                    botao_1['text']=''
                    botao_2['text']=''
                    botao_3['text']=''
                    botao_4['text']=''
                    botao_5['text']=''
                    botao_6['text']=''
                    botao_7['text']=''
                    botao_8['text']=''
                    
                    #game-over
                    print(pontuacao)
                    game_over()
                    
                else:
                    pass
                
                
                
        
        
        
    
    botao_1=Button(frame_corpo,command=lambda:estado_do_valor(numeros[0]),text=numeros[0],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_1.place(x=40,y=70)
    botao_2=Button(frame_corpo,command=lambda:estado_do_valor(numeros[1]),text=numeros[1],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_2.place(x=108,y=70)
    
    botao_3=Button(frame_corpo,command=lambda:estado_do_valor(numeros[2]),text=numeros[2],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_3.place(x=176,y=70)
    botao_4=Button(frame_corpo,command=lambda:estado_do_valor(numeros[3]),text=numeros[3],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_4.place(x=244,y=70)
    
    botao_5=Button(frame_corpo,command=lambda:estado_do_valor(numeros[4]),text=numeros[4],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_5.place(x=40,y=133)
    botao_6=Button(frame_corpo,command=lambda:estado_do_valor(numeros[5]),text=numeros[5],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_6.place(x=108,y=133)
    
    botao_7=Button(frame_corpo,command=lambda:estado_do_valor(numeros[6]),text=numeros[6],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_7.place(x=176,y=133)
    botao_8=Button(frame_corpo,command=lambda:estado_do_valor(numeros[7]),text=numeros[7],width=5,height=2,relief=RAISED,overrelief=RIDGE,font=('Ivy 15 bold'),bg=co10,fg=cor_preta)
    botao_8.place(x=244,y=133)
    
def game_over():
    
    global tentativas
    global pontuacao
    
   
    
    l_pontuacao=Label(frame_corpo,text="Você pontou :" + str(pontuacao)+'pontos',anchor='center',relief='raised',font=('Ivy 15 bold'),bg=cor_branca,fg=cor_azul)
    l_pontuacao.place(x=52,y=90)
    
    l_jogo=Label(frame_corpo,text="GAME OVER",anchor='center',relief='raised',font=('Ivy 15 bold'),bg=cor_branca,fg=cor_azul)
    l_jogo.place(x=130,y=120)
    
    
    tentativas=5
    pontuacao=0
    
    l_tentativas['text']=str(tentativas)+'Tentativas'
    l_pontos['text']='Pontuacao : '+str(pontuacao)

    
    
    botao_jogar=Button(frame_corpo,command=iniciar_jogo,text="Jogar",width=33,anchor='center',relief=RAISED,overrelief=RIDGE,font=('Ivy 12 bold'),bg=co10,fg=cor_preta)
    botao_jogar.place(x=80,y=145)

    
    


#corpo

l_pontos=Label(frame_corpo,text="Pontuação",anchor='center',font=('Ivy 11 bold'),bg=cor_branca,fg=cor_preta)
l_pontos.place(x=40,y=30)


l_tentativas=Label(frame_corpo,text="Tentativas:",anchor='center',font=('Ivy 11 bold'),bg=cor_branca,fg=cor_preta)
l_tentativas.place(x=205,y=30)

l_linha=Label(frame_corpo,width=90,anchor='center',font=('Ivy 4'),bg=cor_verde,fg=cor_branca)
l_linha.place(x=39,y=59)

l_regra1=Label(frame_corpo,text="Tenta advinhar o número para pontuar",anchor='center',font=('Ivy 8 bold'),bg=cor_fundo,fg=cor_branca)
l_regra1.place(x=40,y=80)

l_regra2=Label(frame_corpo,text="Se você acertar ganhará + 2 chances",anchor='center',font=('Ivy 8 bold'),bg=cor_fundo,fg=cor_branca)
l_regra2.place(x=40,y=110)

l_regra3=Label(frame_corpo,text="Se você errar suas chances irá reduzir",anchor='center',font=('Ivy 8 bold'),bg=cor_fundo,fg=cor_branca)
l_regra3.place(x=40,y=140)


botao_jogar=Button(frame_corpo,command=iniciar_jogo,text="Jogar",width=33,anchor='center',relief=RAISED,overrelief=RIDGE,font=('Ivy 10 bold'),bg=co10,fg=cor_preta)

botao_jogar.place(x=40,y=170)

janela.mainloop
