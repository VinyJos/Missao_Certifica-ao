from cProfile import label
from logging import root
from this import s
from tkinter import *
import tkinter.font as tkFont

from setuptools import Command


root = Tk()


class Application():
    fontStyle = tkFont.Font(family="Lucida Grande", size=7)
    #acão do botão cadastro
    def botao_cadastro(self):
        print('cadastro')
        self.frame_cadastro=Frame(self.root, bd= 4, bg='white', highlightbackground= '#0D0D0D', highlightthickness= 0)
        self.frame_cadastro.place(relx=0.23, rely=0.05, relwidth=0.77, relheight=1)
        self.frame_cadastro
    #ação do botão consulta
    def botao_consulta(self):
        print('consulta')
        self.frame_1=Frame(self.root, bd= 4, bg='#00BBC9', highlightbackground= '#0D0D0D', highlightthickness= 0)
        self.frame_1.place(relx=0.23, rely=0.05, relwidth=0.77, relheight=1)
        self.frame_1

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.widgets_frame1()
        self.botao_cadastro()
        self.botao_consulta()
        root.mainloop()
    
        
    def tela(self):
        self.root.title('Central de Ferramentaria')
        self.root.configure(background= '#463A3E')
        self.root.geometry('900x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=420)


    def frames_de_tela(self):
        self.frame_1=Frame(self.root, bd= 4, bg='#00BBC9', highlightbackground= '#0D0D0D', highlightthickness= 0)
        self.frame_1.place(relx=0.23, rely=0.05, relwidth=0.77, relheight=1)

        self.frame_2=Frame(self.root, bd= 4, bg='#130633', highlightbackground= '#0D0D0D', highlightthickness= 0)
        self.frame_2.place(relx=0, rely=0.05, relwidth=0.23, relheight=1)

        self.frame_3=Frame(self.root, bd= 4, bg='#CACACA', highlightbackground= '#878787', highlightthickness= 0.5)
        self.frame_3.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        #cadastro
        self.frame_cadastro=Frame(self.root, bd= 4, bg='white', highlightbackground= '#0D0D0D', highlightthickness= 0)
        self.frame_cadastro.place(relx=0.23, rely=0.05, relwidth=0.77, relheight=1)

        
    def widgets_frame1(self):
        #Botão cadastar ferramentas
        self.bt_limpar = Button(self.frame_2, text=' Ferramentas', bg='#F2F2F2', command=self.botao_cadastro)
        self.bt_limpar.place(relx=0.01, rely=0.1, relwidth=1, relheight=0.05)
        #Botão consultar ferramentas
        self.bt_limpar = Button(self.frame_2, text='Técnicos', bg='#F2F2F2', command=self.botao_consulta)
        self.bt_limpar.place(relx=0.01, rely=0.152, relwidth=1, relheight=0.05)
        #Botão cadastra Técnico
        self.bt_limpar = Button(self.frame_2, text='Ferramentas', bg='#F2F2F2')
        self.bt_limpar.place(relx=0.01, rely=0.30, relwidth=1, relheight=0.05)
        #Botão consultar Técnico
        self.bt_limpar = Button(self.frame_2, text='Técnicos', bg='#F2F2F2')
        self.bt_limpar.place(relx=0.01, rely=0.353, relwidth=1, relheight=0.05)
        
        
        # texto cadastro
        self.lb_codigo = Label(self.frame_2, text='Cadastro/Consulta', bg='#130633', foreground='white', font='fontStyle')
        self.lb_codigo.place(relx=0.01, rely=0.05, relwidth=1, relheight=0.05)
        # texto consulta
        self.lb_codigo = Label(self.frame_2, text='Consulta', bg='#130633', foreground='white', font='fontStyle')
        self.lb_codigo.place(relx=0.01, rely=0.25, relwidth=1, relheight=0.05)

        
        # Label entrada de código
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_codigo.place(relx=0.060, rely=0.085)

        self.codigo_entry = Entry(self.frame_1, highlightbackground= '#878787', highlightthickness= 1)
        self.codigo_entry.place(relx=0.16, rely=0.085, relwidth=0.60, relheight=0.04)

        # Label entrada descrição
        '''self.lb_descricao = Label(self.frame_1, text='Descrição', bg='#C3C2BF')
        self.lb_descricao.place(relx=0.045, rely=0.35)

        self.descricao_entry = Entry(self.frame_1)
        self.descricao_entry.place(relx=0.045, rely=0.45, relwidth=0.9, relheight=0.10)

        # Label entrada fabricante
        self.lb_fabricante = Label(self.frame_1, text='Fabricante', bg='#C3C2BF')
        self.lb_fabricante.place(relx=0.045, rely=0.55)

        self.fabricante_entry = Entry(self.frame_1)
        self.fabricante_entry.place(relx=0.045, rely=0.65, relwidth=0.4, relheight=0.10)

        # Label entrada voltagem de uso
        self.lb_voltagem = Label(self.frame_1, text='Voltagem', bg='#C3C2BF')
        self.lb_voltagem.place(relx=0.5, rely=0.55)

        self.voltagem_entry = Entry(self.frame_1)
        self.voltagem_entry.place(relx=0.5, rely=0.65, relwidth=0.14, relheight=0.10)

        # Label entrada Part number
        self.lb_part_number = Label(self.frame_1, text='Part Number', bg='#C3C2BF')
        self.lb_part_number.place(relx=0.75, rely=0.55)

        self.part_number_entry = Entry(self.frame_1)
        self.part_number_entry.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.10)

        # Label entrada tamanho
        self.lb_tamanho = Label(self.frame_1, text='Tamanho', bg='#C3C2BF')
        self.lb_tamanho.place(relx=0.75, rely=0.55)

        self.tamanho_entry = Entry(self.frame_1)
        self.tamanho_entry.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.10)

        # Label entrada Unidade de medida
        self.lb_unidade_medida = Label(self.frame_1, text='Unidade de Medida', bg='#C3C2BF')
        self.lb_unidade_medida.place(relx=0.75, rely=0.55)

        self.unidade_medida_entry = Entry(self.frame_1)
        self.unidade_medida_entry.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.10)

        # Label entrada tipo de ferramenta
        self.lb_tipo = Label(self.frame_1, text='Tipo de ferramenta', bg='#C3C2BF')
        self.lb_tipo.place(relx=0.75, rely=0.55)

        self.tipo_entry = Entry(self.frame_1)
        self.tipo_entry.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.10)

        # Label entrada material da ferramenta
        self.lb_material = Label(self.frame_1, text='Material da Ferramenta', bg='#C3C2BF')
        self.lb_material.place(relx=0.75, rely=0.55)

        self.material_entry = Entry(self.frame_1)
        self.material_entry.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.10)

        # Label entrada tempo maximo de reserva
        self.lb_part_number = Label(self.frame_1, text='Part Number', bg='#C3C2BF')
        self.lb_part_number.place(relx=0.75, rely=0.55)

        self.part_number_entry = Entry(self.frame_1)
        self.part_number_entry.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.10)'''



Application()