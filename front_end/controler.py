# author: Gustavo A. Ronconi
#########################################
# CIVILTEC TECNOLOGIA EM CONSTRUÇÃO#####
#########################################
# coding: utf-8

from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import StringProperty
import time
import sqlite3
import kivy
kivy.require('1.9.1')

Window.clearcolor = (1, 1, 1, 1)  # FUNDO BRANCO


# CONECTA COM O BANCO DE DADOS
conn = sqlite3.connect('C:\\DEV\\techroad_appmobile\database\\techroadlocal.db', isolation_level=None)



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
        pos_hint: {"x":.1, "y":.5}
        size_hint: (.8, .15)
        font_size: "60sp"
        multiline: False

    InputTechRoad:
        id: senha #coleta o valor de senha
        hint_text: "Senha"
        hint_text_color: C("#87CEEB")
        pos_hint: {"x":.1, "y":.3}
        size_hint: (.8, .15)
        font_size: "50sp"
        password: True
        multiline: False


    ButtonTechRoad:
        pos_hint: {"x":.1, "y":.10}
        size_hint: (.8, .15)
        text: "Login"
        on_press: root.on_press_login()
        font_name: "consola"
        font_size: "30sp"

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
        pos_hint: {"center_x":.765, "y":.05}
        size_hint: (.3, .1)
        text: "Equipamento"
        on_press: root.on_press_selequipamento()
        font_name: "consola"
        font_size: "35sp"
    
    InputTechRoad:
        id: comunicado 
        pos_hint: {"x":.08, "y":.16}
        size_hint: (.835, .23)
        font_size: "24sp"
        multiline: True  
        readonly: True
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
        on_press: root.on_press_voltar();local_origem1.text = ""
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
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
        on_press: root.on_press_voltar();local_origem2.text = ""
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
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
        on_press: root.on_press_voltar();local_destino1.text = ""
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
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
        id: local_destino2 #coleta o local origem digitado
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
        on_press: root.on_press_voltar();local_destino2.text = ""
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
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
        on_press: root.on_press_voltar();cod_material.text = ""
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
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
        id: ton
        pos_hint: {"x":.3749, "y":.635}
        size_hint: (.255, .13)
        text: "TON."
        group: "unidades"
        font_name: "consola"
        font_size: "35sp"
        on_state: root.select_unidade('TON.', self.state)
        
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
        on_press: root.on_press_voltar();qtd_transportada.text = ""; m3.state = 'normal'; ton.state = 'normal'; un.state = 'normal'
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
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
             
        
#TELA SELECIONAR VEICULO - APENAS ADMINISTRADORES      
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
        pos_hint: {"center_x":.5, "y":.35}
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

""")


class TechRoadLogin(Screen):
    def on_press_login(self):
        print(self.ids.usuario.text)
        print(self.ids.senha.text)
        App.get_running_app().root.current = 'telainicial'


class TelaLocalOrigem2(Screen):
    def on_press_avancar(self):
        if self.manager.get_screen('telalocalorigem2').ids.desc_origem2.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
            App.get_running_app().root.current = 'telamaterial2'

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telainicial'

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
        if self.manager.get_screen('telalocalorigem1').ids.desc_origem1.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Local Inexistente...[/color]', '[color=FF0000]Local Desativado...[/color]']:
            App.get_running_app().root.current = 'telalocaldestino1'

    def on_press_voltar(self):
        App.get_running_app().root.current = 'teladeslocamento1'

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
        if self.manager.get_screen('telamaterial2').ids.desc_material.text not in ['[color=FF0000]Digite o código...[/color]', '[color=FF0000]Material Inexistente...[/color]', '[color=FF0000]Material Desativado...[/color]']:
            App.get_running_app().root.current = 'telaquantidade2'

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telalocalorigem2'

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
        self.qtd_material_ton = 0.0

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
        if self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text == '':
            print(self.manager.get_screen('telaquantidade2').ids.qtd_transportada.text)
            App.get_running_app().root.current = 'telalocaldestino2'

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telamaterial2'

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
            if self.unidade == 'TON.':
                self.qtd_material_ton = self.qtd_material.replace('.', ',')
                qtd_material_convertida = float(self.qtd_material)/self.densidade_material[0]
                if self.capacidade_equipamento[0] < qtd_material_convertida:
                    self.manager.get_screen(
                        'telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Qtd. Excede a Cap. Máxima[/color]"
                else:
                    self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material_ton, self.unidade))

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
            if self.unidade == 'TON.':
                self.qtd_material_ton = self.qtd_material.replace('.', ',')
                qtd_material_convertida = float(self.qtd_material)/self.densidade_material[0] #CONVERTE P/ M3
                if self.capacidade_equipamento[0] < qtd_material_convertida:
                    self.manager.get_screen(
                        'telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Qtd. Excede a Cap. Máxima[/color]"
                else:
                    self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material_ton, self.unidade))

            if self.unidade == 'UN.':
                self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = ("[color=00FF00]%s %s[/color]" % (self.qtd_material.replace('.', ','), self.unidade))
        else:
            self.manager.get_screen('telaquantidade2').ids.validador_quantidade.text = "[color=FF0000]Especificar Unid/Qtd.[/color]"


class TelaLocalDestino1(Screen):

    def on_press_avancar(self):
        pass

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telainicial'

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
        pass

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telaquantidade2'

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


class TelaSair(Screen):
    global ultimatela

    def on_press_sim(self):
        App.get_running_app().root.current = 'telalogin'
        self.manager.get_screen('telalogin').ids.usuario.text = ""
        self.manager.get_screen('telalogin').ids.senha.text = ""
        self.manager.get_screen('telalocalorigem1').ids.local_origem1.text = ""
        self.manager.get_screen('telalocalorigem2').ids.local_origem2.text = ""
        self.manager.get_screen('telalocaldestino1').ids.local_destino1.text = ""
        self.manager.get_screen('telamaterial2').ids.cod_material.text = ""
        self.manager.get_screen('telaquantidade2').ids.qtd_transportada.text = ""
        self.manager.get_screen('telaquantidade2').ids.m3.state = "normal"
        self.manager.get_screen('telaquantidade2').ids.ton.state = "normal"
        self.manager.get_screen('telaquantidade2').ids.un.state = "normal"
        self.manager.get_screen('telalocaldestino2').ids.local_destino2.text = ""

    def on_press_nao(self):
        App.get_running_app().root.current = ultimatela


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

    def on_press_op1(self):
        App.get_running_app().root.current = 'teladeslocamento1'

    def on_press_op2(self):
        App.get_running_app().root.current = 'telalocalorigem2'

    def on_press_selequipamento(self):
        App.get_running_app().root.current = 'telaselecionarequipamento'

    crudeclock = RelogioDigital()
    Clock.schedule_interval(crudeclock.update, 1)


gt = ScreenManager()  # GERENCIADOR DE TELAS
gt.add_widget(TechRoadLogin(name='telalogin'))
gt.add_widget(TechRoadMain(name='telainicial'))
gt.add_widget(TelaSair(name='telasair'))
gt.add_widget(TelaLocalOrigem2(name='telalocalorigem2'))
gt.add_widget(TelaLocalDestino1(name='telalocaldestino1'))
gt.add_widget(TelaLocalOrigem1(name='telalocalorigem1'))
gt.add_widget(TelaMaterial2(name='telamaterial2'))
gt.add_widget(TelaQuantidade2(name='telaquantidade2'))
gt.add_widget(TelaLocalDestino2(name='telalocaldestino2'))
gt.add_widget(TelaSelecionarEquipamento(name='telaselecionarequipamento'))
gt.add_widget(TelaDeslocamento1(name='teladeslocamento1'))



class TechRoadApp(App):
    def build(self):
        return gt


if __name__ == '__main__':  # RODA A APLICAÇÃO PRINCIPAL
    TechRoadApp().run()
