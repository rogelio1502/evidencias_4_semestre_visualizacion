#importamos la clase Ui_Formulario que contiene la interfaz del formulario
from formulario import Ui_Formulario
#importamos sys para salir del programa
import sys
#importamos los modulos uic y Qtwidgets de la libreria PyQt5
from PyQt5 import uic,QtWidgets


#nombre del archivo ui principal a importar
qtCreatorFile = "main.ui"
#lo cargamos
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


#definimos la clase principal del programa
#heredamos de la clase Qtwidgets y Ui_MainWindow
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        # inicializamos las clases
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # cargamos un objeto a la interfaz
        self.setupUi(self)
        # definimos el titulo de la ventana
        self.setWindowTitle("Inicio")
        # definimos los tamaño
        self.setMaximumSize(850,400)
        self.setMinimumSize(850,400)
        # añadimos funcionalidad para que al presionar el boton se abra la otra ventana
        self.btn_abrir.clicked.connect(self.abrir_ventana_captura)
        # mostramos la pantalla
        self.show()

    # metodo para abrir la otra ventana
    def abrir_ventana_captura(self):
        #instanciamos un objeto de la clase QtWidgets.QMainWindow()
        self.ventana_capura = QtWidgets.QMainWindow()
        # definimos los tamaño maximos
        self.ventana_capura.setMaximumSize(900,800)
        self.ventana_capura.setMinimumSize(900, 800)
        # instanciamos un objeto de la clase Ui_Formulario
        self.ui = Ui_Formulario()
        # cargamos un objeto a la interfaz
        self.ui.setupUi(self.ventana_capura)
        #metodo de la clase Ui_formulario para llenar la tabla
        self.ui.fillTable()
        # añadimos funcionalidad para que al presionar el boton se validen los datos para despues grabarlos en la tabla
        self.ui.btn_grabar.clicked.connect(self.ui.grabar)
        # añadimos funcionalidad para que al presionar el boton se limpien los campos
        self.ui.btn_limpiar.clicked.connect(self.ui.clean)
        # añadimos funcionalidad para que al presionar el boton se escriban los datos de la tabla en un archivo csv
        self.ui.btn_escribir.clicked.connect(self.ui.escribir)
        # mostramos la pantalla
        self.ventana_capura.show()


#if para correr el programa
if __name__=="__main__":
    #instanciamos un objeto de la clase QApplication
    app = QtWidgets.QApplication(sys.argv)
    #le damos un estilo
    app.setStyle("Fusion")
    #instanciamos un objeto de la clase MyApp
    ventana = MyApp()

    sys.exit(app.exec_())