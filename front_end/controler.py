# author: Gustavo A. Ronconi
#########################################
# CIVILTEC TECNOLOGIA EM CONSTRUÇÃO#####
#########################################
# coding: utf-8
# update: 1

from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.clock import Clock
import time
import sqlite3
import kivy

kivy.require('1.9.1')
Window.clearcolor = (1, 1, 1, 1)  # FUNDO BRANCO


# CONECTA COM O BANCO DE DADOS
conn = sqlite3.connect('techroadlocal.db', isolation_level=None)


Builder.load_string("""
#:include visualclass.kv
#:import C kivy.utils.get_color_from_hex

#TELA DE LOGIN
<TechRoadLogin@FloatLayout>:

    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)


    Image:
        source: 'logo2.png'
        size_hint: .25, .25
        pos_hint: {"x":.375, "y":.77}

    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .78}
        font_size: "60sp"


    InputTechRoad:
        id: usuario #coleta o valor de usuario
        hint_text: "Usuário"
        hint_text_color: C("#87CEEB")
        pos_hint: {"x":.1, "y":.55}
        size_hint: (.8, .15)
        font_size: "60sp"
        multiline: False

    InputTechRoad:
        id: senha #coleta o valor de senha
        hint_text: "Senha"
        hint_text_color: C("#87CEEB")
        pos_hint: {"x":.1, "y":.38}
        size_hint: (.8, .15)
        font_size: "50sp"
        password: True
        multiline: False


    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.21}
        size_hint: (.8, .15)
        text: "Login"
        on_press: root.on_press_login()
        font_name: "consola"
        font_size: "30sp"
        
    TextTechRoad:
        markup: True
        id: validador_login
        pos_hint: {'center_x': .5, 'center_y': .15}
        font_size: "40sp"

    TextTechRoad:
        markup: True
        text: "[color=1874CD]@Desenvolvido por Gustavo A. Ronconi[/color]"
        pos_hint: {'center_x': .76, 'center_y': .05}

#TELA INICIAL
<TechRoadMain@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)

    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .88}
        font_size: "60sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Bem-Vindo[/color]"
        pos_hint: {'center_x': .5, 'center_y': .80}
        font_size: "30sp"

    TextTechRoad:
        markup: True
        text: "[color=1874CD]Selecione a operação:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .74}
        font_size: "30sp"
        
    ButtonTechRoad:
        pos_hint: {"x":.08, "y":.50}
        size_hint: (.4, .2)
        text: "Terraplanagem"
        on_press: root.on_press_op1()
        font_name: "consola"
        font_size: "35sp"
        
    ButtonTechRoad:
        pos_hint: {"x":.52, "y":.50}
        size_hint: (.4, .2)
        text: "Transporte"
        on_press: root.on_press_op2()
        font_name: "consola"
        font_size: "35sp"  
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Comunicados:[/color]"
        pos_hint: {'center_x': .17, 'center_y': .41}
        font_size: "20sp"  
        
    ButtonTechRoad:
        pos_hint: {"center_x":.5, "y":.05}
        size_hint: (.2, .1)
        text: "Sair"
        on_press: root.on_press_logoff()
        font_name: "consola"
        font_size: "35sp"
        
    ButtonTechRoad:
        id: botao_equipamento
        disabled: True
        opacity: 0
        pos_hint: {"center_x":.765, "y":.05}
        size_hint: (.3, .1)
        text: "Equipamento"
        on_press: root.on_press_selequipamento()
        font_name: "consola"
        font_size: "35sp"
    
    ButtonTechRoad:
        id: botao_comunicacao
        pos_hint: {"center_x":.230, "y":.05}
        size_hint: (.3, .1)
        text: "Comunicação"
        on_press: root.on_press_comunicacao()
        font_name: "consola"
        font_size: "35sp"
    
    InputTechRoad:
        id: comunicado 
        pos_hint: {"x":.08, "y":.16}
        size_hint: (.835, .23)
        font_size: "24sp"
        multiline: True  
        readonly: True
        
#TELA CANCELAR        
<TelaCancelar@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)

    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .78}
        font_size: "60sp"
    
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Deseja realmente cancelar?[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .6}
        font_size: "50sp"
    
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Se você cancelar todos os campos preenchidos serão excluídos![/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .53}
        font_size: "18sp" 
         
        
    ButtonTechRoad:
        pos_hint: {"x":.08, "y":.25}
        size_hint: (.4, .2)
        text: "Sim"
        on_press: root.on_press_sim()
        font_name: "consola"
        font_size: "35sp"
        
    ButtonTechRoad:
        pos_hint: {"x":.52, "y":.25}
        size_hint: (.4, .2)
        text: "Não"
        on_press: root.on_press_nao()
        font_name: "consola"
        font_size: "35sp"
                
#TELA SAIR        
<TelaSair@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)

    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .78}
        font_size: "60sp"
    
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Deseja realmente sair?[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .6}
        font_size: "50sp"
    
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Se você sair todas as operações não completadas serão perdidas![/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .53}
        font_size: "18sp" 
         
        
    ButtonTechRoad:
        pos_hint: {"x":.08, "y":.25}
        size_hint: (.4, .2)
        text: "Sim"
        on_press: root.on_press_sim()
        font_name: "consola"
        font_size: "35sp"
        
    ButtonTechRoad:
        pos_hint: {"x":.52, "y":.25}
        size_hint: (.4, .2)
        text: "Não"
        on_press: root.on_press_nao()
        font_name: "consola"
        font_size: "35sp"

#TELA LOCAL ORIGEM 1        
<TelaLocalOrigem1@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .89}
        font_size: "60sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Local Origem:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .75}
        font_size: "50sp"
    
    InputTechRoad:
        id: local_origem1 #coleta o local origem digitado
        hint_text: "Cód. Local"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);
        
    TextTechRoad:
        markup: True
        id: desc_origem1
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "30sp"
        
    ButtonTechRoad:
        id: botao_origem1
        pos_hint: {"x":.51, "y":.21}
        size_hint: (.39, .18)
        text: "Avançar"
        on_press: root.on_press_avancar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.21}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        id: sair_origem1
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"

        
#TELA LOCAL ORIGEM 2        
<TelaLocalOrigem2@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .89}
        font_size: "60sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Local Origem:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .75}
        font_size: "50sp"
    
    InputTechRoad:
        id: local_origem2 #coleta o local origem digitado
        hint_text: "Cód. Local"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);
        
    TextTechRoad:
        markup: True
        id: desc_origem2
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "30sp"
        
    ButtonTechRoad:
        id: botao_origem2
        pos_hint: {"x":.51, "y":.21}
        size_hint: (.39, .18)
        text: "Avançar"
        on_press: root.on_press_avancar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.21}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        id: sair_origem2
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"
        
#TELA LOCAL DESTINO1       
<TelaLocalDestino1@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .89}
        font_size: "60sp"        
        markup: True
        
    TextTechRoad:
        text: "[color=1874CD]Local Destino:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .75}
        font_size: "50sp"
        markup: True
    
    InputTechRoad:
        id: local_destino1 #coleta o local origem digitado
        hint_text: "Cód. Local"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);
        
    TextTechRoad:
        id: desc_destino1
        markup: True
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "30sp"
        
    ButtonTechRoad:
        id: botao_destino1
        pos_hint: {"x":.51, "y":.21}
        size_hint: (.39, .18)
        text: "Avançar"
        on_press: root.on_press_avancar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.21}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        id: sair_destino1
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"
        
#TELA LOCAL DESTINO2       
<TelaLocalDestino2@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .89}
        font_size: "60sp"        
        markup: True
        
    TextTechRoad:
        text: "[color=1874CD]Local Destino:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .75}
        font_size: "50sp"
        markup: True
    
    InputTechRoad:
        id: local_destino2 #coleta o local destino digitado
        hint_text: "Cód. Local"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);
        
    TextTechRoad:
        markup: True
        id: desc_destino2
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "30sp"
        
    ButtonTechRoad:
        id: botao_destino2
        pos_hint: {"x":.51, "y":.21}
        size_hint: (.39, .18)
        text: "Avançar"
        on_press: root.on_press_avancar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.21}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        id: sair_destino2
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"
        
#TELA MATERIAL TRANSPORTADO      
<TelaMaterial2@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .89}
        font_size: "60sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Selecionar Material:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .75}
        font_size: "50sp"
    
    InputTechRoad:
        id: cod_material #coleta o local origem digitado
        hint_text: "Cód. Material"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);
        
    TextTechRoad:
        markup: True
        id: desc_material
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "30sp"
        
    ButtonTechRoad:
        id: botao_material2
        pos_hint: {"x":.51, "y":.21}
        size_hint: (.39, .18)
        text: "Avançar"
        on_press: root.on_press_avancar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.21}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        id: sair_material2
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"
        
        
#TELA QUANTIDADE TRANSPORTADA      
<TelaQuantidade2@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .90}
        font_size: "60sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Quantidade Transportada:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .81}
        font_size: "50sp"
    
    InputTechRoad:
        id: qtd_transportada #coleta o local origem digitado
        hint_text: "Quantidade"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.435}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);
        
    ToggleButtonTechRoad:
        id: m3
        pos_hint: {"x":.1, "y":.635}
        size_hint: (.255, .13)
        text: "M3."
        group: "unidades"
        font_name: "consola"
        font_size: "35sp"
        on_state: root.select_unidade('M3.', self.state)
        
    
    ToggleButtonTechRoad:
        id: kg
        pos_hint: {"x":.3749, "y":.635}
        size_hint: (.255, .13)
        text: "KG."
        group: "unidades"
        font_name: "consola"
        font_size: "35sp"
        on_state: root.select_unidade('KG.', self.state)
        
    ToggleButtonTechRoad:
        id: un
        pos_hint: {"x":.6449, "y":.635}
        size_hint: (.255, .13)
        text: "UN."
        group: "unidades"
        font_name: "consola"
        font_size: "35sp"
        on_state: root.select_unidade('UN.', self.state)         
       
    TextTechRoad:
        markup: True
        id: validador_quantidade
        pos_hint: {'center_x': .5, 'center_y': .38}
        font_size: "50sp"
        
    ButtonTechRoad:
        id: botao_quantidade2
        pos_hint: {"x":.51, "y":.15}
        size_hint: (.39, .18)
        text: "Avançar"
        on_press: root.on_press_avancar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.15}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        id: sair_quantidade2
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"
        
#TELA SELECIONAR OPCAO DESLOCAMENTO      
<TelaDeslocamento1@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)

    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .85}
        font_size: "60sp"
    
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Deslocando-se vazio?[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .67}
        font_size: "50sp"
    
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Caso sim, as informações de trajeto até a obra serão coletadas![/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .60}
        font_size: "18sp" 
         
        
    ButtonTechRoad:
        pos_hint: {"x":.08, "y":.32}
        size_hint: (.4, .2)
        text: "Sim"
        on_press: root.on_press_sim()
        font_name: "consola"
        font_size: "35sp"
        
    ButtonTechRoad:
        pos_hint: {"x":.52, "y":.32}
        size_hint: (.4, .2)
        text: "Não"
        on_press: root.on_press_nao()
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        pos_hint: {"x":.30, "y":.109}
        size_hint: (.18, .1)
        text: "Voltar"
        on_press: root.on_press_voltar()
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        pos_hint: {"x":.52, "y":.109}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"             
             
        
#TELA SELECIONAR EQUIPAMENTO - APENAS ADMINISTRADORES      
<TelaSelecionarEquipamento@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]@TechRoad[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .87}
        font_size: "60sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Equipamento atual:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .76}
        font_size: "50sp"
    
    TextTechRoad:
        id: equipamento_atual
        markup: True
        pos_hint: {'center_x': .5, 'center_y': .67}
        font_size: "50sp"
   
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Novo equipamento:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .57}
        font_size: "50sp" 
        
    InputTechRoad:
        id: novo_equipamento #coleta o novo veiculo do sistema
        hint_text: "Cod. Equip."
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.34}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        on_text: root.ao_teclar(self.text);    
        
    TextTechRoad:        
        markup: True
        id: desc_equipamento
        pos_hint: {'center_x': .5, 'center_y': .30}
        font_size: "30sp"     
       
    ButtonTechRoad:
        pos_hint: {"x":.51, "y":.055}
        size_hint: (.39, .18)
        text: "Alterar"
        on_press: root.on_press_alterar()
        font_name: "consola"
        font_size: "35sp" 
             
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.055}
        size_hint: (.39, .18)
        text: "Voltar"
        on_press: root.on_press_voltar();novo_equipamento.text = ""
        font_name: "consola"
        font_size: "35sp"

#RESUMO DE INFORMAÇÕES PRE-ROTA 1(TERRAPLENAGEM BOTA FORA)      
<ResumoInfo1@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Resumo pré-rota[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .90}
        font_size: "50sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Conferir e corrigir, se necessário![/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .83}
        font_size: "18sp" 
        
    TextTechRoad:
        id: local_origem1_text
        markup: True
        text: "[color=1874CD]-Local Origem:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .70}
        font_size: "40sp"
        
    ButtonTechRoad:
        id: local_origem_op1
        pos_hint: {"x": .48, "y": .695}
        size_hint: (.45, .09)
        font_name: "consola"
        font_size: "35sp"
        on_press: root.ao_focar1();
                
        
    TextTechRoad:
        id: local_destino1_text
        markup: True
        text: "[color=1874CD]-Local Destino:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .60}
        font_size: "40sp"
     
    ButtonTechRoad:
        id: local_destino_op1
        pos_hint: {"x": .48, "y": .595}
        size_hint: (.45, .09)
        font_name: "consola"
        font_size: "35sp"
        on_press: root.ao_focar2();        
    
    TextTechRoad:
        id: hora1_text
        markup: True
        text: "[color=1874CD]-Início(h:min):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .50}
        font_size: "40sp" 
        
    InputTechRoad:
        markup: True
        id: hora_op1        
        pos_hint: {"x": .48, "y": .495}
        size_hint: (.45, .09)
        font_size: "40sp" 
        padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached))/2
        disabled: True
        
    TextTechRoad:
        id: km1_text
        markup: True
        text: "[color=1874CD]-Início(km):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .40}
        font_size: "40sp"
    
    InputTechRoad:
        markup: True
        id: km_op1        
        pos_hint: {"x": .48, "y": .395}
        size_hint: (.45, .09)
        font_size: "40sp" 
        padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached))/2
        disabled: True  
        
       
    TextTechRoad:
        id: nivel1_text
        markup: True
        text: "[color=1874CD]-Início(l):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .30}
        font_size: "40sp"
    
    InputTechRoad:
        markup: True
        id: nivel_op1        
        pos_hint: {"x": .48, "y": .295}
        size_hint: (.45, .09)
        font_size: "40sp" 
        padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached))/2
        disabled: True 
        
    ButtonTechRoad:
        pos_hint: {"x":.51, "y":.055}
        size_hint: (.39, .18)
        text: "Iniciar"
        on_press: root.on_press_iniciar()
        font_name: "consola"
        font_size: "35sp"
    
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.055}
        size_hint: (.39, .18)
        text: "Cancelar"
        on_press: root.on_press_cancelar()
        font_name: "consola"
        font_size: "35sp"
        
#RESUMO DE INFORMAÇÕES PRE-ROTA 2(TRANSPORTE)      
<ResumoInfo2@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Resumo pré-rota[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .925}
        font_size: "50sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Conferir e corrigir, se necessário![/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .865}
        font_size: "18sp" 
        
    TextTechRoad:
        id: local_origem2_text
        markup: True
        text: "[color=1874CD]-Local Origem:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .76}
        font_size: "35sp"
        
    ButtonTechRoad:
        id: local_origem_op2
        pos_hint: {"x": .48, "y": .755}
        size_hint: (.45, .08)
        font_name: "consola"
        font_size: "35sp"
        on_press: root.ao_focar1();              
        
    TextTechRoad:
        id: local_destino2_text
        markup: True
        text: "[color=1874CD]-Local Destino:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .67}
        font_size: "35sp"
     
    ButtonTechRoad:
        id: local_destino_op2
        pos_hint: {"x": .48, "y": .665}
        size_hint: (.45, .08)
        font_name: "consola"
        font_size: "35sp"
        on_press: root.ao_focar2();        

    TextTechRoad:
        id: material2_text
        markup: True
        text: "[color=1874CD]-Cód. Material:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .58}
        font_size: "35sp"   

    ButtonTechRoad:
        id: material_op2
        pos_hint: {"x": .48, "y": .575}
        size_hint: (.45, .08)
        font_name: "consola"
        font_size: "35sp"
        on_press: root.ao_focar3();
            
        
    TextTechRoad:
        id: quantidade2_text
        markup: True
        text: "[color=1874CD]-Quantidade:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .49}
        font_size: "35sp"   

    ButtonTechRoad:
        id: quantidade_op2
        pos_hint: {"x": .48, "y": .485}
        size_hint: (.45, .08)
        font_name: "consola"
        font_size: "35sp"
        on_press: root.ao_focar4();           
    
    
    TextTechRoad:
        id: hora1_text
        markup: True
        text: "[color=1874CD]-Início(h:min):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .40}
        font_size: "35sp" 
        
    InputTechRoad:
        markup: True
        id: hora_op2        
        pos_hint: {"x": .48, "y": .395}
        size_hint: (.45, .08)
        font_size: "35sp" 
        padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached))/2
        disabled: True
        
    TextTechRoad:
        id: km2_text
        markup: True
        text: "[color=1874CD]-Início(km):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .31}
        font_size: "35sp"
    
    InputTechRoad:
        markup: True
        id: km_op2        
        pos_hint: {"x": .48, "y": .305}
        size_hint: (.45, .08)
        font_size: "35sp" 
        padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached))/2
        disabled: True  
        
       
    TextTechRoad:
        id: nivel2_text
        markup: True
        text: "[color=1874CD]-Início(l):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .22}
        font_size: "35sp"
    
    InputTechRoad:
        markup: True
        id: nivel_op2        
        pos_hint: {"x": .48, "y": .215}
        size_hint: (.45, .08)
        font_size: "35sp" 
        padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached))/2
        disabled: True 
        
    ButtonTechRoad:
        pos_hint: {"x":.51, "y":.045}
        size_hint: (.39, .15)
        text: "Iniciar"
        on_press: root.on_press_iniciar()
        font_name: "consola"
        font_size: "35sp"
    
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.045}
        size_hint: (.39, .15)
        text: "Cancelar"
        on_press: root.on_press_cancelar()
        font_name: "consola"
        font_size: "35sp"
        
#TELA COMUNICACAO  
<TelaComunicacao@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Status de Comunicação[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .825}
        font_size: "50sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Comunicação obrigatória (OBD-II, GPS)[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .765}
        font_size: "18sp" 
        
    TextTechRoad:
        id: comunicacaoobd_text
        markup: True
        text: "[color=1874CD]-Comunicação OBD-II:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .60}
        font_size: "35sp" 
        
    TextTechRoad:
        id: gps_text
        markup: True
        text: "[color=1874CD]-GPS (Localização):[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .50}
        font_size: "35sp"
        
    TextTechRoad:
        id: internet_text
        markup: True
        text: "[color=1874CD]-Conexão à Internet:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .40}
        font_size: "35sp"
        
    TextTechRoad:
        id: sincroniza_text
        markup: True
        text: "[color=1874CD]-Última Sincronização:[/color]"
        text_size: self.size
        pos_hint: {"x": .06, "y": .30}
        font_size: "35sp" 
         
    ButtonTechRoad:
        pos_hint: {"x":.25, "y":.0555}
        size_hint: (.50, .15)
        text: "Voltar"
        on_press: root.on_press_voltar()
        font_name: "consola"
        font_size: "35sp"        
         
#ACOMPANHAMENTO DE ROTA
<ResumoRota@FloatLayout>:
    orientation: "horizontal"
    canvas.before:
        Color:
            rgba: C("#1874CD")
        Line:
            width: 1.5
            rectangle: (0.05*self.width, 0.03*self.height, 0.9*self.width, 0.94*self.height)
            
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Acompanhamento de Rota[/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .880}
        font_size: "55sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]Concentre-se em dirigir neste momento![/b][/color]"
        pos_hint: {'center_x': .5, 'center_y': .790}
        font_size: "18sp"
 
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]-Velocímetro(km/h):[/b][/color]"
        pos_hint: {'center_x': .38, 'center_y': .68}
        font_size: "50sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]-Distância(km):[/b][/color]"
        pos_hint: {'center_x': .312, 'center_y': .59}
        font_size: "50sp"
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD][b]-Tempo em Rota:[/b][/color]"
        pos_hint: {'center_x': .3135, 'center_y': .50}
        font_size: "50sp"
        
    TextTechRoad:
        markup: True
        id: cronid
        text: "PARADO"
        pos_hint: {"center_x": .70, "center_y": .50}
        font_name: "consola"
        font_size: "50sp"        
        
    ButtonTechRoad:
        pos_hint: {"x":.51, "y":.045}
        size_hint: (.39, .15)
        text: "Finalizar"
        on_press: root.on_press_finalizar()
        font_name: "consola"
        font_size: "35sp"
        
    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.045}
        size_hint: (.39, .15)
        text: "Cancelar"
        on_press: root.on_press_cancelar()
        font_name: "consola"
        font_size: "35sp"
   
""")


class TechRoadLogin(Screen):
    def on_press_login(self):
        login_user = ''
        #VERIFICA SE O USUARIO EXISTE NO SISTEMA
        u = conn.cursor()
        for row in u.execute("SELECT EMAIL FROM auth_user WHERE USER_ID > 0"):
            for usuario in row:
                if usuario[:usuario.find('@')] == self.ids.usuario.text:
                    login_user = usuario
        s = conn.cursor()
        s.execute("SELECT PASSWORD FROM auth_user WHERE EMAIL = '%s'" % login_user)
        senha = s.fetchone()

        if login_user == '':
            self.manager.get_screen('telalogin').ids.validador_login.text = "[color=FF0000]Usuário Inexistente[/color]"

        elif senha[0] != self.ids.senha.text:
            self.manager.get_screen('telalogin').ids.validador_login.text = "[color=FF0000]Senha Incorreta[/color]"

        else:
            # VERIFICA SE O USUARIO E ADMINISTRADOR
            a = conn.cursor()
            a.execute("SELECT GROUP_ID FROM auth_user WHERE EMAIL = '%s'" % login_user)
            grupo = a.fetchone()
            if grupo[0] == 1:
                self.manager.get_screen('telainicial').ids.botao_equipamento.disabled = False
                self.manager.get_screen('telainicial').ids.botao_equipamento.opacity = 1
            App.get_running_app().root.current = 'telainicial'
            self.manager.get_screen('telalogin').ids.validador_login.text = ""





class TelaLocalOrigem2(Screen):
    def on_press_avancar(self):
        if self.manager.get_screen('telalocalorigem2').ids.botao_origem2.text == "Avançar":
            if self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                App.get_running_app().root.current = 'telamaterial2'
        else:
            if self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                self.manager.get_screen('telaprerota2').ids.local_origem_op2.text = self.manager.get_screen('telalocalorigem2').ids.local_origem2.text
                App.get_running_app().root.current = 'telaprerota2'

    def on_press_voltar(self):
        if self.manager.get_screen('telalocalorigem2').ids.botao_origem2.text == "Avançar":
            self.manager.get_screen('telalocalorigem2').ids.local_origem2.text = ""
            App.get_running_app().root.current = 'telainicial'

        else:
            self.manager.get_screen('telalocalorigem2').ids.local_origem2.text = self.manager.get_screen('telaprerota2').ids.local_origem_op2.text
            App.get_running_app().root.current = 'telaprerota2'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telalocalorigem2'
        App.get_running_app().root.current = 'telasair'
        
    def ao_teclar(self, text):
        c = conn.cursor()
        d = conn.cursor()
        c.execute("SELECT DESCRICAO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        descricao_local = c.fetchone()
        d.execute("SELECT ESTADO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        estado_local = d.fetchone()

        if descricao_local == None and text == '':
            self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text = "[color=FF0000]Digite o código...[/color]"
        elif descricao_local == None and text != '':
            self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text = "[color=FF0000]Local Inexistente...[/color]"

        elif descricao_local != None and estado_local == (1,):
            self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text = ("[color=00FF00]%s[/color]" % descricao_local)

        elif descricao_local != None and estado_local != (1,):
            self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text = "[color=FF0000]Local Desativado...[/color]"

class TelaLocalOrigem1(Screen):
    def on_press_avancar(self):
        if self.manager.get_screen('telalocalorigem1').ids.botao_origem1.text == "Avançar":
            if self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                App.get_running_app().root.current = 'telalocaldestino1'
        else:
            if self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                self.manager.get_screen('telaprerota1').ids.local_origem_op1.text = self.manager.get_screen('telalocalorigem1').ids.local_origem1.text
                App.get_running_app().root.current = 'telaprerota1'


    def on_press_voltar(self):
        if self.manager.get_screen('telalocalorigem1').ids.botao_origem1.text == "Avançar":
            self.manager.get_screen('telalocalorigem1').ids.local_origem1.text = ""
            App.get_running_app().root.current = 'teladeslocamento1'

        else:
            self.manager.get_screen('telalocalorigem1').ids.local_origem1.text = self.manager.get_screen('telaprerota1').ids.local_origem_op1.text
            App.get_running_app().root.current = 'telaprerota1'


    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telalocaldestino1'
        App.get_running_app().root.current = 'telasair'

    def ao_teclar(self, text):
        c = conn.cursor()
        d = conn.cursor()
        c.execute("SELECT DESCRICAO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        descricao_local = c.fetchone()
        d.execute("SELECT ESTADO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        estado_local = d.fetchone()

        if descricao_local == None and text == '':
            self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text = "[color=FF0000]Digite o código...[/color]"
        elif descricao_local == None and text != '':
            self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text = "[color=FF0000]Local Inexistente...[/color]"

        elif descricao_local != None and estado_local == (1,):
            self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text = ("[color=00FF00]%s[/color]" % descricao_local)

        elif descricao_local != None and estado_local != (1,):
            self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text = "[color=FF0000]Local Desativado...[/color]"


class TelaMaterial2(Screen):
    def on_press_avancar(self):
        if self.manager.get_screen('telamaterial2').ids.botao_material2.text == "Avançar":
            if self.manager.get_screen('telamaterial2').ids.desc_material.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Material Inexistente...[/color]', '[color=FF0000]Material Desativado...[/color]']:
                App.get_running_app().root.current = 'telaquantidade2'
        else:
            if self.manager.get_screen('telamaterial2').ids.desc_material.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Material Inexistente...[/color]','[color=FF0000]Material Desativado...[/color]']:
                self.manager.get_screen('telaprerota2').ids.material_op2.text = self.manager.get_screen('telamaterial2').ids.cod_material.text
                App.get_running_app().root.current = 'telaprerota2'

    def on_press_voltar(self):
        if self.manager.get_screen('telamaterial2').ids.botao_material2.text == "Avançar":
            self.manager.get_screen('telamaterial2').ids.cod_material.text = ""
            App.get_running_app().root.current = 'telalocalorigem2'
        else:
            self.manager.get_screen('telamaterial2').ids.cod_material.text = self.manager.get_screen('telaprerota2').ids.material_op2.text
            App.get_running_app().root.current = 'telaprerota2'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telamaterial2'
        App.get_running_app().root.current = 'telasair'
        
    def ao_teclar(self, text):
        c = conn.cursor()
        d = conn.cursor()
        c.execute("SELECT DESCRICAO_MATERIAL FROM tb_material WHERE CHAVE_MATERIAL = '%s'" % text)
        descricao_material = c.fetchone()
        d.execute("SELECT ESTADO_MATERIAL FROM tb_material WHERE CHAVE_MATERIAL = '%s'" % text)
        estado_material = d.fetchone()

        if descricao_material == None and text == '':
            self.manager.get_screen('telamaterial2').ids.desc_material.text = "[color=FF0000]Digite o código...[/color]"
        elif descricao_material == None and text != '':
            self.manager.get_screen('telamaterial2').ids.desc_material.text = "[color=FF0000]Material Inexistente...[/color]"

        elif descricao_material != None and estado_material == (1,):
            self.manager.get_screen('telamaterial2').ids.desc_material.text = ("[color=00FF00]%s[/color]" % descricao_material)

        elif descricao_material != None and estado_material != (1,):
            self.manager.get_screen('telamaterial2').ids.desc_material.text = "[color=FF0000]Material Desativado...[/color]"



class TelaQuantidade2(Screen):
    def __init__(self, **kwargs):
        super(TelaQuantidade2, self).__init__(**kwargs)
        self.unidade = ''
        self.qtd_material = ''
        self.equipamento_atual = ()
        self.capacidade_equipamento = ()
        self.qtd_material_kg = 0.0

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def no_zero(self, string):
        try:
            string = float(string)
            if string == 0.0:
                return False
            else:
                return True
        except ValueError:
            return False


    def on_press_avancar(self):
        if self.manager.get_screen('telaquantidade2').ids.botao_quantidade2.text == "Avançar":
            if self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text not in ['[color=FF0000]Qtd. Excede a Cap. Máxima[/color]', '[color=FF0000]Especificar Unid/Qtd.[/color]']:
                App.get_running_app().root.current = 'telalocaldestino2'
        else:
            if self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text not in ['[color=FF0000]Qtd. Excede a Cap. Máxima[/color]', '[color=FF0000]Especificar Unid/Qtd.[/color]']:
                self.manager.get_screen('telaprerota2').ids.quantidade_op2.text = self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text[(self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text.find('0]')+2):(self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text.find('[/'))]
                App.get_running_app().root.current = 'telaprerota2'


    def on_press_voltar(self):
        if self.manager.get_screen('telaquantidade2').ids.botao_quantidade2.text == "Avançar":
            self.manager.get_screen('telaquantidade2').ids.qtd_transportada.text = ""
            self.manager.get_screen('telaquantidade2').ids.m3.state = 'normal'
            self.manager.get_screen('telaquantidade2').ids.kg.state = 'normal'
            self.manager.get_screen('telaquantidade2').ids.un.state = 'normal'
            App.get_running_app().root.current = 'telamaterial2'
        else:
            self.manager.get_screen('telaquantidade2').ids.qtd_transportada.text = self.manager.get_screen('telaprerota2').ids.quantidade_op2.text[:self.manager.get_screen('telaprerota2').ids.quantidade_op2.text.find(' M' or ' K' or ' U')]
            if self.manager.get_screen('telaprerota2').ids.quantidade_op2.text.find(' M') != -1:
                self.manager.get_screen('telaquantidade2').ids.m3.state = 'down'
                self.manager.get_screen('telaquantidade2').ids.kg.state = 'normal'
                self.manager.get_screen('telaquantidade2').ids.un.state = 'normal'
            if self.manager.get_screen('telaprerota2').ids.quantidade_op2.text.find(' K') != -1:
                self.manager.get_screen('telaquantidade2').ids.m3.state = 'normal'
                self.manager.get_screen('telaquantidade2').ids.kg.state = 'down'
                self.manager.get_screen('telaquantidade2').ids.un.state = 'normal'
            if self.manager.get_screen('telaprerota2').ids.quantidade_op2.text.find(' U') != -1:
                self.manager.get_screen('telaquantidade2').ids.m3.state = 'normal'
                self.manager.get_screen('telaquantidade2').ids.kg.state = 'normal'
                self.manager.get_screen('telaquantidade2').ids.un.state = 'down'
            App.get_running_app().root.current = 'telaprerota2'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telaquantidade2'
        App.get_running_app().root.current = 'telasair'

    def select_unidade(self, uni, estado):
        if estado == 'down':
            self.unidade = uni
        else:
            self.unidade = ''

        if self.unidade != '' and self.qtd_material != '' and self.is_float(self.qtd_material) and self.no_zero(self.qtd_material):
            if self.unidade == 'M3.':
                if self.capacidade_equipamento[0] < float(self.qtd_material):
                    self.manager.get_screen(
                        'telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Qtd. Excede a Cap. Máxima[/color]"
                else:
                    self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material.replace('.', ','), self.unidade))
            if self.unidade == 'KG.':
                self.qtd_material_kg = self.qtd_material.replace('.', ',')
                qtd_material_convertida = float(self.qtd_material)/self.densidade_material[0]
                if self.capacidade_equipamento[0] < qtd_material_convertida:
                    self.manager.get_screen(
                        'telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Qtd. Excede a Cap. Máxima[/color]"
                else:
                    self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material_kg, self.unidade))

            if self.unidade == 'UN.':
                self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material.replace('.', ','), self.unidade))
        else:
            self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Especificar Unid/Qtd.[/color]"


    def ao_teclar(self, text):
        #IDENTIFICAR EQUIPAMENTO
        e = conn.cursor()
        e.execute("SELECT EQUIPAMENTO_SEL FROM tb_config WHERE ID_CONFIG = 1")
        self.equipamento_atual = e.fetchone()
        #IDENTIFICAR CAPACIDADE DO EQUIPAMENTO
        c = conn.cursor()
        c.execute("SELECT CAPACIDADE_MAXIMA FROM tb_equipamento WHERE CHAVE_EQUIPAMENTO = '%s'" % self.equipamento_atual)
        self.capacidade_equipamento = c.fetchone()
        #IDENTIFICAR DENSIDADE DO MATERIAL
        cod_material = self.manager.get_screen('telamaterial2').ids.cod_material.text
        d = conn.cursor()
        d.execute("SELECT DENSIDADE_ESPECIFICA FROM tb_material WHERE CHAVE_MATERIAL = '%s'" % cod_material)
        self.densidade_material = d.fetchone()

        if ',' in text:
            text = text.replace(',','.')
            if text[0] == '.':
                text = '0.' + text[1:]
            if text[-1] == ',':
                text = text + '00'
        if '.' in text:
            if text[0] == '.':
                text = '0.' + text[1:]
            if text[-1] == '.':
                text = text + '00'
        self.qtd_material = text



        if self.unidade != '' and text != '' and self.is_float(self.qtd_material) and self.no_zero(self.qtd_material):
            if self.unidade == 'M3.':
                if self.capacidade_equipamento[0] < float(self.qtd_material):
                    self.manager.get_screen(
                            'telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Qtd. Excede a Cap. Máxima[/color]"
                else:
                    self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material.replace('.', ','), self.unidade))
            if self.unidade == 'KG.':
                self.qtd_material_kg = self.qtd_material.replace('.', ',')
                qtd_material_convertida = float(self.qtd_material)/self.densidade_material[0] #CONVERTE P/ M3
                if self.capacidade_equipamento[0] < qtd_material_convertida:
                    self.manager.get_screen(
                        'telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Qtd. Excede a Cap. Máxima[/color]"
                else:
                    self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material_kg, self.unidade))

            if self.unidade == 'UN.':
                self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material.replace('.', ','), self.unidade))
        else:
            self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Especificar Unid/Qtd.[/color]"


class TelaLocalDestino1(Screen):

    def on_press_avancar(self):
        if self.manager.get_screen('telalocaldestino1').ids.botao_destino1.text == "Avançar":
            if self.manager.get_screen('telalocaldestino1').ids.desc_destino1.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                if self.manager.get_screen('telalocalorigem1').ids.local_origem1.text != "": #CHECA A OPCAO DE TERRAPLENAGEM SELECIONADA
                    self.manager.get_screen('telaprerota1').ids.local_origem_op1.text = self.manager.get_screen('telalocalorigem1').ids.local_origem1.text
                    self.manager.get_screen('telaprerota1').ids.local_destino_op1.text = self.manager.get_screen('telalocaldestino1').ids.local_destino1.text
                    self.manager.get_screen('telaprerota1').ids.hora_op1.text = time.strftime('%H:%M')
                    App.get_running_app().root.current = 'telaprerota1'
                elif self.manager.get_screen('telalocalorigem1').ids.local_origem1.text == "":
                    self.manager.get_screen('telaprerota1').ids.local_destino_op1.text = self.manager.get_screen('telalocaldestino1').ids.local_destino1.text
                    self.manager.get_screen('telaprerota1').ids.hora_op1.text = time.strftime('%H:%M')
                    self.manager.get_screen('telaprerota1').ids.local_origem1_text.disabled = True
                    self.manager.get_screen('telaprerota1').ids.local_origem1_text.opacity = 0
                    self.manager.get_screen('telaprerota1').ids.local_origem_op1.disabled = True
                    self.manager.get_screen('telaprerota1').ids.local_origem_op1.opacity = 0
                    self.manager.get_screen('telaprerota1').ids.local_destino1_text.pos_hint = {"x": .06, "y": .70}
                    self.manager.get_screen('telaprerota1').ids.local_destino_op1.pos_hint = {"x": .48, "y": .695}
                    self.manager.get_screen('telaprerota1').ids.hora1_text.pos_hint = {"x": .06, "y": .60}
                    self.manager.get_screen('telaprerota1').ids.hora_op1.pos_hint = {"x": .48, "y": .595}
                    self.manager.get_screen('telaprerota1').ids.km1_text.pos_hint = {"x": .06, "y": .50}
                    self.manager.get_screen('telaprerota1').ids.km_op1.pos_hint = {"x": .48, "y": .495}
                    self.manager.get_screen('telaprerota1').ids.nivel1_text.pos_hint = {"x": .06, "y": .40}
                    self.manager.get_screen('telaprerota1').ids.nivel_op1.pos_hint = {"x": .48, "y": .395}
                    App.get_running_app().root.current = 'telaprerota1'


        elif self.manager.get_screen('telalocaldestino1').ids.botao_destino1.text == "Alterar":
            if self.manager.get_screen('telalocaldestino1').ids.desc_destino1.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                self.manager.get_screen('telaprerota1').ids.local_destino_op1.text = self.manager.get_screen('telalocaldestino1').ids.local_destino1.text
                App.get_running_app().root.current = 'telaprerota1'


    def on_press_voltar(self):
        if self.manager.get_screen('telalocaldestino1').ids.botao_destino1.text == "Avançar":
            self.manager.get_screen('telalocaldestino1').ids.local_destino1.text = ""
            if self.manager.get_screen('telalocalorigem1').ids.local_origem1.text == "":
                App.get_running_app().root.current = 'teladeslocamento1'
            else:
                App.get_running_app().root.current = 'telalocalorigem1'

        else:
            self.manager.get_screen('telalocaldestino1').ids.local_destino1.text = self.manager.get_screen('telaprerota1').ids.local_destino_op1.text
            App.get_running_app().root.current = 'telaprerota1'



    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telalocaldestino1'
        App.get_running_app().root.current = 'telasair'

    def ao_teclar(self, text):
        c = conn.cursor()
        d = conn.cursor()
        c.execute("SELECT DESCRICAO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        descricao_local = c.fetchone()
        d.execute("SELECT ESTADO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        estado_local = d.fetchone()

        if descricao_local == None and text == '':
            self.manager.get_screen('telalocaldestino1').ids.desc_destino1.text = "[color=FF0000]Digite o código...[/color]"
        elif descricao_local == None and text != '':
            self.manager.get_screen('telalocaldestino1').ids.desc_destino1.text = "[color=FF0000]Local Inexistente...[/color]"

        elif descricao_local != None and estado_local == (1,):
            self.manager.get_screen('telalocaldestino1').ids.desc_destino1.text = ("[color=00FF00]%s[/color]" % descricao_local)

        elif descricao_local != None and estado_local != (1,):
            self.manager.get_screen('telalocaldestino1').ids.desc_destino1.text = "[color=FF0000]Local Desativado...[/color]"

class TelaLocalDestino2(Screen):
    def on_press_avancar(self):
        if self.manager.get_screen('telalocaldestino2').ids.botao_destino2.text == "Avançar":
            if self.manager.get_screen('telalocaldestino2').ids.desc_destino2.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                if self.manager.get_screen('telalocalorigem2').ids.local_origem2.text != "":
                    self.manager.get_screen('telaprerota2').ids.local_origem_op2.text = self.manager.get_screen('telalocalorigem2').ids.local_origem2.text
                    self.manager.get_screen('telaprerota2').ids.local_destino_op2.text = self.manager.get_screen('telalocaldestino2').ids.local_destino2.text
                    self.manager.get_screen('telaprerota2').ids.material_op2.text = self.manager.get_screen('telamaterial2').ids.cod_material.text
                    self.manager.get_screen('telaprerota2').ids.quantidade_op2.text = self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text[(self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text.find('0]')+2):(self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text.find('[/'))]
                    self.manager.get_screen('telaprerota2').ids.hora_op2.text = time.strftime('%H:%M')
                    App.get_running_app().root.current = 'telaprerota2'

        elif self.manager.get_screen('telalocaldestino2').ids.botao_destino2.text == "Alterar":
            if self.manager.get_screen('telalocaldestino2').ids.desc_destino2.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
                self.manager.get_screen('telaprerota2').ids.local_destino_op2.text = self.manager.get_screen('telalocaldestino2').ids.local_destino2.text
                App.get_running_app().root.current = 'telaprerota2'

    def on_press_voltar(self):
        if self.manager.get_screen('telalocaldestino2').ids.botao_destino2.text == "Avançar":
            self.manager.get_screen('telalocaldestino2').ids.local_destino2.text = ""
            App.get_running_app().root.current = 'telaquantidade2'
        else:
            self.manager.get_screen('telalocaldestino2').ids.local_destino2.text = self.manager.get_screen('telaprerota2').ids.local_destino_op2.text
            App.get_running_app().root.current = 'telaprerota2'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telalocaldestino2'
        App.get_running_app().root.current = 'telasair'

    def ao_teclar(self, text):
        c = conn.cursor()
        d = conn.cursor()
        c.execute("SELECT DESCRICAO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        descricao_local = c.fetchone()
        d.execute("SELECT ESTADO_LOCAL FROM tb_local WHERE CHAVE_LOCAL = '%s'" % text)
        estado_local = d.fetchone()

        if descricao_local == None and text == '':
            self.manager.get_screen('telalocaldestino2').ids.desc_destino2.text = "[color=FF0000]Digite o código...[/color]"
        elif descricao_local == None and text != '':
            self.manager.get_screen('telalocaldestino2').ids.desc_destino2.text = "[color=FF0000]Local Inexistente...[/color]"

        elif descricao_local != None and estado_local == (1,):
            self.manager.get_screen('telalocaldestino2').ids.desc_destino2.text = ("[color=00FF00]%s[/color]" % descricao_local)

        elif descricao_local != None and estado_local != (1,):
            self.manager.get_screen('telalocaldestino2').ids.desc_destino2.text = "[color=FF0000]Local Desativado...[/color]"


class TelaDeslocamento1(Screen):
    def on_press_sim(self):
        App.get_running_app().root.current = 'telalocalorigem1'

    def on_press_nao(self):
        App.get_running_app().root.current = 'telalocaldestino1'

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telainicial'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'teladeslocamento1'
        App.get_running_app().root.current = 'telasair'

class TelaSelecionarEquipamento(Screen):
    def on_press_alterar(self):
        if self.manager.get_screen('telaselecionarequipamento').ids.desc_equipamento.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Equipamento Inexistente...[/color]','[color=FF0000]Equipamento Desativado...[/color]']:
            novo_equipamento = self.manager.get_screen('telaselecionarequipamento').ids.novo_equipamento.text
            i = conn.cursor()
            i.execute("""UPDATE tb_config SET EQUIPAMENTO_SEL = ? WHERE ID_CONFIG = 1""", (novo_equipamento,))
            i.close()
            self.manager.get_screen('telaselecionarequipamento').ids.equipamento_atual.text = ("[color=00FF00]%s[/color]" % novo_equipamento)
    def on_press_voltar(self):
        App.get_running_app().root.current = 'telainicial'

    def ao_teclar(self, text):
        c = conn.cursor()
        d = conn.cursor()
        e = conn.cursor()
        e.execute("SELECT EQUIPAMENTO_SEL FROM tb_config WHERE ID_CONFIG = 1")
        equipamento_atual = e.fetchone()
        c.execute("SELECT DESCRICAO_EQUIPAMENTO FROM tb_equipamento WHERE CHAVE_EQUIPAMENTO = '%s'" % text)
        descricao_equipamento = c.fetchone()
        d.execute("SELECT ESTADO_EQUIPAMENTO FROM tb_equipamento WHERE CHAVE_EQUIPAMENTO = '%s'" % text)
        estado_equipamento = d.fetchone()

        self.manager.get_screen('telaselecionarequipamento').ids.equipamento_atual.text = ("[color=00FF00]%s[/color]" % equipamento_atual)

        if descricao_equipamento == None and text == '':
            self.manager.get_screen('telaselecionarequipamento').ids.desc_equipamento.text = "[color=FF0000]Digite o código...[/color]"
        elif descricao_equipamento == None and text != '':
            self.manager.get_screen('telaselecionarequipamento').ids.desc_equipamento.text = "[color=FF0000]Equipamento Inexistente...[/color]"

        elif descricao_equipamento != None and estado_equipamento == (1,):
            self.manager.get_screen('telaselecionarequipamento').ids.desc_equipamento.text = ("[color=00FF00]%s[/color]" % descricao_equipamento)

        elif descricao_equipamento != None and estado_equipamento != (1,):
            self.manager.get_screen('telaselecionarequipamento').ids.desc_equipamento.text = "[color=FF0000]Equipamento Desativado...[/color]"


class ResumoInfo1(Screen):

    def on_press_iniciar(self):
        self.manager.get_screen('telaresumorota').ids.cronid.text = "[b][color=1874CD]" + "00:00:00" + "[/color][/b]"
        App.get_running_app().root.current = 'telaresumorota'


    def on_press_cancelar(self):
        global ultimatela_cancela
        ultimatela_cancela = 'telaprerota1'
        App.get_running_app().root.current = 'telacancelar'

    def ao_focar1(self):
        self.manager.get_screen('telalocalorigem1').ids.botao_origem1.text = "Alterar"
        self.manager.get_screen('telalocalorigem1').ids.sair_origem1.disabled = True
        self.manager.get_screen('telalocalorigem1').ids.sair_origem1.opacity = 0
        App.get_running_app().root.current = 'telalocalorigem1'

    def ao_focar2(self):
        self.manager.get_screen('telalocaldestino1').ids.botao_destino1.text = "Alterar"
        self.manager.get_screen('telalocaldestino1').ids.sair_destino1.disabled = True
        self.manager.get_screen('telalocaldestino1').ids.sair_destino1.opacity = 0
        App.get_running_app().root.current = 'telalocaldestino1'

class ResumoInfo2(Screen):

    def on_press_iniciar(self):
        self.manager.get_screen('telaresumorota').ids.cronid.text = "[b][color=1874CD]" + "00:00:00" + "[/color][/b]"
        App.get_running_app().root.current = 'telaresumorota'


    def on_press_cancelar(self):
        global ultimatela_cancela
        ultimatela_cancela = 'telaprerota2'
        App.get_running_app().root.current = 'telacancelar'

    def ao_focar1(self):
        self.manager.get_screen('telalocalorigem2').ids.botao_origem2.text = "Alterar"
        self.manager.get_screen('telalocalorigem2').ids.sair_origem2.disabled = True
        self.manager.get_screen('telalocalorigem2').ids.sair_origem2.opacity = 0
        App.get_running_app().root.current = 'telalocalorigem2'

    def ao_focar2(self):
        self.manager.get_screen('telalocaldestino2').ids.botao_destino2.text = "Alterar"
        self.manager.get_screen('telalocaldestino2').ids.sair_destino2.disabled = True
        self.manager.get_screen('telalocaldestino2').ids.sair_destino2.opacity = 0
        App.get_running_app().root.current = 'telalocaldestino2'

    def ao_focar3(self):
        self.manager.get_screen('telamaterial2').ids.botao_material2.text = "Alterar"
        self.manager.get_screen('telamaterial2').ids.sair_material2.disabled = True
        self.manager.get_screen('telamaterial2').ids.sair_material2.opacity = 0
        App.get_running_app().root.current = 'telamaterial2'

    def ao_focar4(self):
        self.manager.get_screen('telaquantidade2').ids.botao_quantidade2.text = "Alterar"
        self.manager.get_screen('telaquantidade2').ids.sair_quantidade2.disabled = True
        self.manager.get_screen('telaquantidade2').ids.sair_quantidade2.opacity = 0
        App.get_running_app().root.current = 'telaquantidade2'


class TelaComunicacao(Screen):
    def on_press_voltar(self):
        App.get_running_app().root.current = 'telainicial'


class ResumoRota(Screen):
    def __init__(self, **kwargs):
        super(ResumoRota, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        if self.manager.get_screen('telaresumorota').ids.cronid.text != 'PARADO':
            segundos = int(self.manager.get_screen('telaresumorota').ids.cronid.text[23:25])
            minutos = int(self.manager.get_screen('telaresumorota').ids.cronid.text[20:22])
            horas = int(self.manager.get_screen('telaresumorota').ids.cronid.text[17:19])
            if segundos == 60:
                minutos += 1
                segundos = 0
            if minutos == 60:
                horas += 1
                minutos = 0
            segundos += 1
            self.manager.get_screen('telaresumorota').ids.cronid.text = "[b][color=1874CD]" + "{:02}".format(horas)+":"+"{:02}".format(minutos)+":"+"{:02}".format(segundos) + "[/color][/b]"

    def on_press_finalizar(self):
        pass

    def on_press_cancelar(self):
        global ultimatela_cancela
        ultimatela_cancela = 'telaresumorota'
        App.get_running_app().root.current = 'telacancelar'


class ResumoRotaFinal(Screen):
    def on_press_salvar(self):
        pass

    def on_press_cancelar(self):
        global ultimatela_cancela
        ultimatela_cancela = 'telaresumorotafinal'
        App.get_running_app().root.current = 'telacancelar'

class TelaCancelar(Screen):
    global ultimatela_cancela

    def on_press_sim(self):
        self.manager.get_screen('telaresumorota').ids.cronid.text = "PARADO"
        self.manager.get_screen('telaprerota1').ids.local_origem1_text.disabled = False
        self.manager.get_screen('telaprerota1').ids.local_origem1_text.opacity = 1
        self.manager.get_screen('telaprerota1').ids.local_origem_op1.disabled = False
        self.manager.get_screen('telaprerota1').ids.local_origem_op1.opacity = 1
        self.manager.get_screen('telaprerota1').ids.local_origem1_text.pos_hint = {"x": .06, "y": .70}
        self.manager.get_screen('telaprerota1').ids.local_origem_op1.pos_hint = {"x": .48, "y": .695}
        self.manager.get_screen('telaprerota1').ids.local_destino1_text.pos_hint = {"x": .06, "y": .60}
        self.manager.get_screen('telaprerota1').ids.local_destino_op1.pos_hint = {"x": .48, "y": .595}
        self.manager.get_screen('telaprerota1').ids.hora1_text.pos_hint = {"x": .06, "y": .50}
        self.manager.get_screen('telaprerota1').ids.hora_op1.pos_hint = {"x": .48, "y": .495}
        self.manager.get_screen('telaprerota1').ids.km1_text.pos_hint = {"x": .06, "y": .40}
        self.manager.get_screen('telaprerota1').ids.km_op1.pos_hint = {"x": .48, "y": .395}
        self.manager.get_screen('telaprerota1').ids.nivel1_text.pos_hint = {"x": .06, "y": .30}
        self.manager.get_screen('telaprerota1').ids.nivel_op1.pos_hint = {"x": .48, "y": .295}
        self.manager.get_screen('telalocaldestino1').ids.botao_destino1.text = "Avançar"
        self.manager.get_screen('telalocaldestino1').ids.sair_destino1.disabled = False
        self.manager.get_screen('telalocaldestino1').ids.sair_destino1.opacity = 1
        self.manager.get_screen('telalocalorigem1').ids.sair_origem1.disabled = False
        self.manager.get_screen('telalocalorigem1').ids.sair_origem1.opacity = 1
        self.manager.get_screen('telalocalorigem1').ids.local_origem1.text = ""
        self.manager.get_screen('telalocalorigem2').ids.local_origem2.text = ""
        self.manager.get_screen('telalocalorigem2').ids.botao_origem2.text = "Avançar"
        self.manager.get_screen('telalocalorigem2').ids.sair_origem2.disabled = False
        self.manager.get_screen('telalocalorigem2').ids.sair_origem2.opacity = 1
        self.manager.get_screen('telalocaldestino2').ids.botao_destino2.text = "Avançar"
        self.manager.get_screen('telalocaldestino2').ids.sair_destino2.disabled = False
        self.manager.get_screen('telalocaldestino2').ids.sair_destino2.opacity = 1
        self.manager.get_screen('telamaterial2').ids.botao_material2.text = "Avançar"
        self.manager.get_screen('telamaterial2').ids.sair_material2.disabled = False
        self.manager.get_screen('telamaterial2').ids.sair_material2.opacity = 1
        self.manager.get_screen('telaquantidade2').ids.botao_quantidade2.text = "Avançar"
        self.manager.get_screen('telaquantidade2').ids.sair_quantidade2.disabled = False
        self.manager.get_screen('telaquantidade2').ids.sair_quantidade2.opacity = 1
        self.manager.get_screen('telalocaldestino1').ids.local_destino1.text = ""
        self.manager.get_screen('telamaterial2').ids.cod_material.text = ""
        self.manager.get_screen('telaquantidade2').ids.qtd_transportada.text = ""
        self.manager.get_screen('telaquantidade2').ids.m3.state = "normal"
        self.manager.get_screen('telaquantidade2').ids.kg.state = "normal"
        self.manager.get_screen('telaquantidade2').ids.un.state = "normal"
        self.manager.get_screen('telalocaldestino2').ids.local_destino2.text = ""
        self.manager.get_screen('telainicial').ids.botao_equipamento.disabled = True
        self.manager.get_screen('telainicial').ids.botao_equipamento.opacity = 0
        self.manager.get_screen('telalocalorigem1').ids.botao_origem1.text = "Avançar"
        App.get_running_app().root.current = 'telainicial'

    def on_press_nao(self):
        App.get_running_app().root.current = ultimatela_cancela


class TelaSair(Screen):
    global ultimatela

    def on_press_sim(self):
        self.manager.get_screen('telalogin').ids.usuario.text = ""
        self.manager.get_screen('telalogin').ids.senha.text = ""
        self.manager.get_screen('telalocalorigem1').ids.local_origem1.text = ""
        self.manager.get_screen('telalocalorigem2').ids.local_origem2.text = ""
        self.manager.get_screen('telalocaldestino1').ids.local_destino1.text = ""
        self.manager.get_screen('telalocaldestino2').ids.local_destino2.text = ""
        self.manager.get_screen('telamaterial2').ids.cod_material.text = ""
        self.manager.get_screen('telaquantidade2').ids.qtd_transportada.text = ""
        self.manager.get_screen('telaquantidade2').ids.m3.state = "normal"
        self.manager.get_screen('telaquantidade2').ids.kg.state = "normal"
        self.manager.get_screen('telaquantidade2').ids.un.state = "normal"
        self.manager.get_screen('telalocaldestino2').ids.local_destino2.text = ""
        self.manager.get_screen('telainicial').ids.botao_equipamento.disabled = True
        self.manager.get_screen('telainicial').ids.botao_equipamento.opacity = 0
        App.get_running_app().root.current = 'telalogin'

    def on_press_nao(self):
        App.get_running_app().root.current = ultimatela


class DataAtual(Label):
    def update(self, *args):
        self.markup = True
        self.text = "[b][color=1874CD]" + time.strftime('%d/%m/%y') + "," + "[/color][/b]"
        self.pos_hint = {"center_x":.42, "center_y":.45}
        self.font_name = "consola"
        self.font_size = "25sp"


class RelogioDigital(Label):
    def update(self, *args):
        self.markup = True
        self.text = "[b][color=1874CD]" + time.strftime('%H:%M:%S') + "[/color][/b]"
        self.pos_hint = {"center_x": .58, "center_y": .45}
        self.font_name = "consola"
        self.font_size = "25sp"


class TechRoadMain(Screen):
    def __init__(self, **kwargs):
        super(TechRoadMain, self).__init__(**kwargs)
        self.relogio = RelogioDigital()
        self.dataatual = DataAtual()
        self.add_widget(self.relogio)
        self.add_widget(self.dataatual)
        Clock.schedule_interval(self.relogio.update, 1)
        Clock.schedule_interval(self.dataatual.update, 1)

    def on_press_logoff(self):
        App.get_running_app().root.current = 'telalogin'
        self.manager.get_screen('telalogin').ids.usuario.text = ""
        self.manager.get_screen('telalogin').ids.senha.text = ""
        self.manager.get_screen('telainicial').ids.botao_equipamento.disabled = True
        self.manager.get_screen('telainicial').ids.botao_equipamento.opacity = 0

    def on_press_op1(self):
        App.get_running_app().root.current = 'teladeslocamento1'

    def on_press_op2(self):
        App.get_running_app().root.current = 'telalocalorigem2'

    def on_press_selequipamento(self):
        App.get_running_app().root.current = 'telaselecionarequipamento'

    def on_press_comunicacao(self):
        App.get_running_app().root.current = 'telacomunicacao'

    crudeclock = RelogioDigital()
    Clock.schedule_interval(crudeclock.update, 1)


gt = ScreenManager()  # GERENCIADOR DE TELAS
gt.add_widget(TechRoadLogin(name='telalogin'))
gt.add_widget(ResumoInfo1(name='telaprerota1'))
gt.add_widget(ResumoInfo2(name='telaprerota2'))
gt.add_widget(TechRoadMain(name='telainicial'))
gt.add_widget(TelaSair(name='telasair'))
gt.add_widget(TelaCancelar(name='telacancelar'))
gt.add_widget(TelaLocalOrigem2(name='telalocalorigem2'))
gt.add_widget(TelaLocalDestino1(name='telalocaldestino1'))
gt.add_widget(TelaLocalOrigem1(name='telalocalorigem1'))
gt.add_widget(TelaMaterial2(name='telamaterial2'))
gt.add_widget(TelaQuantidade2(name='telaquantidade2'))
gt.add_widget(TelaLocalDestino2(name='telalocaldestino2'))
gt.add_widget(TelaSelecionarEquipamento(name='telaselecionarequipamento'))
gt.add_widget(TelaDeslocamento1(name='teladeslocamento1'))
gt.add_widget(TelaComunicacao(name='telacomunicacao'))
gt.add_widget(ResumoRota(name='telaresumorota'))
gt.add_widget(ResumoRotaFinal(name='telaresumorotafinal'))


class TechRoadApp(App):
    def build(self):
        return gt


if __name__ == '__main__':  # RODA A APLICAÇÃO PRINCIPAL
    TechRoadApp().run()
