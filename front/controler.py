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
import time

import kivy
kivy.require('1.9.1')

Window.clearcolor = (1, 1, 1, 1)  # FUNDO BRANCO

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
        
#TELA LOCAL ORIGEM        
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
        id: local_origem #coleta o local origem digitado
        hint_text: "Cód. Local"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        
    TextTechRoad:
        markup: True
        text: "[color=FF0000]Desc. Obra...[/color]"
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "50sp"
        
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
        on_press: root.on_press_voltar();local_origem.text = ""
        font_name: "consola"
        font_size: "35sp"   
        
    ButtonTechRoad:
        pos_hint: {"center_x":.5, "y":.039}
        size_hint: (.18, .1)
        text: "Sair"
        on_press: root.on_press_sair();
        font_name: "consola"
        font_size: "35sp"
        
#TELA LOCAL DESTINO       
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
        
    TextTechRoad:
        markup: True
        text: "[color=1874CD]Local Destino:[/color]"
        pos_hint: {'center_x': .5, 'center_y': .75}
        font_size: "50sp"
    
    InputTechRoad:
        id: local_destino #coleta o local origem digitado
        hint_text: "Cód. Local"
        hint_text_color: C("#87CEEB")
        pos_hint: {"center_x":.5, "y":.50}
        size_hint: (.8, .18)
        font_size: "80sp"
        multiline: False
        input_type: "number"
        
    TextTechRoad:
        markup: True
        text: "[color=FF0000]Desc. Obra...[/color]"
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "50sp"
        
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
        on_press: root.on_press_voltar();local_destino.text = ""
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
        
    TextTechRoad:
        markup: True
        text: "[color=FF0000]Desc. Material...[/color]"
        pos_hint: {'center_x': .5, 'center_y': .445}
        font_size: "50sp"
        
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
""")


class TechRoadLogin(Screen):
    def on_press_login(self):
        print(self.ids.usuario.text)
        print(self.ids.senha.text)
        App.get_running_app().root.current = 'telainicial'


class TelaLocalOrigem2(Screen):
    def on_press_avancar(self):
        print(self.ids.local_origem.text)
        App.get_running_app().root.current = 'telamaterial2'

    def on_press_voltar(self):
        print(self.ids.local_origem.text)
        App.get_running_app().root.current = 'telainicial'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telalocalorigem2'
        App.get_running_app().root.current = 'telasair'


class TelaMaterial2(Screen):
    def on_press_avancar(self):
        print(self.ids.cod_material.text)

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telalocalorigem2'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telamaterial2'
        App.get_running_app().root.current = 'telasair'


class TelaLocalDestino1(Screen):
    def on_press_avancar(self):
        pass

    def on_press_voltar(self):
        App.get_running_app().root.current = 'telainicial'

    def on_press_sair(self):
        global ultimatela
        ultimatela = 'telalocaldestino1'
        App.get_running_app().root.current = 'telasair'


class DataAtual(Label):
    def update(self, *args):
        self.markup = True
        self.text = "[b][color=1874CD]" + time.strftime('%d/%m/%y') + "," + "[/color][/b]"
        self.pos_hint = {"center_x":.42, "center_y":.45}
        self.font_name = "consola"
        self.font_size = "25sp"


class RelogioDigital(Label):
    def update(self, *args):
        self.markup =  True
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
        self.manager.get_screen('telalocalorigem2').ids.local_origem.text = ""
        self.manager.get_screen('telalocaldestino1').ids.local_destino.text = ""
        self.manager.get_screen('telamaterial2').ids.cod_material.text = ""

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
        App.get_running_app().root.current = 'telalocaldestino1'

    def on_press_op2(self):
        App.get_running_app().root.current = 'telalocalorigem2'

    crudeclock = RelogioDigital()
    Clock.schedule_interval(crudeclock.update, 1)


gt = ScreenManager()  # GERENCIADOR DE TELAS
gt.add_widget(TechRoadLogin(name='telalogin'))
gt.add_widget(TechRoadMain(name='telainicial'))
gt.add_widget(TelaSair(name='telasair'))
gt.add_widget(TelaLocalOrigem2(name='telalocalorigem2'))
gt.add_widget(TelaLocalDestino1(name='telalocaldestino1'))
gt.add_widget(TelaMaterial2(name='telamaterial2'))


class TechRoadApp(App):
    def build(self):
        return gt


if __name__ == '__main__':  # RODA A APLICAÇÃO PRINCIPALLL
    TechRoadApp().run()
