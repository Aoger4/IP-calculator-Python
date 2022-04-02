from calc import *
from PyQt5.QtWidgets import * #sirve para QLabel, QLineEdit, QSpinbox, etc.
from PyQt5.QtCore import *  #sirve para usar Qt.
from PyQt5.QtGui import *


class MainApp(QMainWindow,C): #(QMainWindow) viene de QtWidgets y sirve para trabajar con UIs

    def __init__(self, parent=None, *args):

        super(MainApp, self).__init__(parent=parent)

        self.setFixedSize(701, 502)
        self.setWindowTitle('SubnetCalc')
        self.setStyleSheet("background-color: rgb(164, 167, 169);")
        
        #Entrada de texto
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(294, 20, 41, 21)
        self.input1.setMaxLength(3)
        self.input1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input1.setAlignment(Qt.AlignCenter)
        self.input1.setValidator(QRegExpValidator(QRegExp('[0-9]+[0-9]+[0-9]')))
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(345, 20, 42, 21)
        self.input2.setMaxLength(3)
        self.input2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input2.setAlignment(Qt.AlignCenter)
        self.input2.setValidator(QRegExpValidator(QRegExp('[0-9]+[0-9]+[0-9]')))
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(397, 20, 43, 21)
        self.input3.setMaxLength(3)
        self.input3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input3.setAlignment(Qt.AlignCenter)
        self.input3.setValidator(QRegExpValidator(QRegExp('[0-9]+[0-9]+[0-9]')))
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(450, 20, 42, 21)
        self.input4.setMaxLength(3)
        self.input4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input4.setAlignment(Qt.AlignCenter)
        self.input4.setValidator(QRegExpValidator(QRegExp('[0-9]+[0-9]+[0-9]')))
        #Silder
        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setGeometry(299, 60, 141, 22)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setRange(0,32)
        #SpinBox
        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(450, 58, 48, 24)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setRange(0,32)
        #Botón calcular
        self.btnC = QPushButton('Calculate',self)
        self.btnC.setGeometry(QRect(190, 100, 311, 31))
        self.btnC.clicked.connect(self.calculate)
        #Labels
        self.label1 = QLabel('IP Address',self)
        self.label1.setGeometry(190, 20, 81, 21)
        self.label2 = QLabel('Subnet',self)
        self.label2.setGeometry(190, 60, 61, 21)

        self.label_ip = QLabel('IP',self)
        self.label_ip.setGeometry(50, 160, 60, 16)
        self.label_ip.setContentsMargins(5,0,0,0)
        self.label_ipD = QLabel(self)
        self.label_ipD.setGeometry(50, 180, 141, 21)
        self.label_ipD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_ipD.setAlignment(Qt.AlignCenter)
        self.label_ipH = QLabel(self)
        self.label_ipH.setGeometry(190, 180, 141, 21)
        self.label_ipH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_ipH.setAlignment(Qt.AlignCenter)
        self.label_ipB = QLabel(self)
        self.label_ipB.setGeometry(50, 200, 281, 21)
        self.label_ipB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_ipB.setAlignment(Qt.AlignCenter)
        self.label_ipB.setFont(QFont('Arial',14))

        self.label_broad = QLabel('Broadcast',self)
        self.label_broad.setGeometry(370, 160, 71, 16)
        self.label_broad.setContentsMargins(5,0,0,0)
        self.label_broadD = QLabel(self)
        self.label_broadD.setGeometry(370, 180, 141, 21)
        self.label_broadD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_broadD.setAlignment(Qt.AlignCenter)
        self.label_broadH = QLabel(self)
        self.label_broadH.setGeometry(510, 180, 141, 21)
        self.label_broadH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_broadH.setAlignment(Qt.AlignCenter)
        self.label_broadB = QLabel(self)
        self.label_broadB.setGeometry(370, 200, 281, 21)
        self.label_broadB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_broadB.setAlignment(Qt.AlignCenter)
        self.label_broadB.setFont(QFont('Arial',14))

        self.label_netm = QLabel('Netmask',self)
        self.label_netm.setGeometry(50, 240, 60, 16)
        self.label_netm.setContentsMargins(5,0,0,0)
        self.label_netmD = QLabel(self)
        self.label_netmD.setGeometry(50, 260, 141, 21)
        self.label_netmD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_netmD.setAlignment(Qt.AlignCenter)
        self.label_netmH = QLabel(self)
        self.label_netmH.setGeometry(190, 260, 141, 21)
        self.label_netmH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_netmH.setAlignment(Qt.AlignCenter)
        self.label_netmB = QLabel(self)
        self.label_netmB.setGeometry(50, 280, 281, 21)
        self.label_netmB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_netmB.setAlignment(Qt.AlignCenter)
        self.label_netmB.setFont(QFont('Arial',14))

        self.label_minh= QLabel('Minimum Host',self)
        self.label_minh.setGeometry(370, 240, 91, 16)
        self.label_minh.setContentsMargins(5,0,0,0)
        self.label_minhD = QLabel(self)
        self.label_minhD.setGeometry(370, 260, 141, 21)
        self.label_minhD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_minhD.setAlignment(Qt.AlignCenter)
        self.label_minhH = QLabel(self)
        self.label_minhH.setGeometry(510, 260, 141, 21)
        self.label_minhH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_minhH.setAlignment(Qt.AlignCenter)
        self.label_minhB = QLabel(self)
        self.label_minhB.setGeometry(370, 280, 281, 21)
        self.label_minhB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_minhB.setAlignment(Qt.AlignCenter)
        self.label_minhB.setFont(QFont('Arial',14))

        self.label_wild= QLabel('Wildcard',self)
        self.label_wild.setGeometry(50, 320, 60, 16)
        self.label_wild.setContentsMargins(5,0,0,0)
        self.label_wildD = QLabel(self)
        self.label_wildD.setGeometry(50, 340, 141, 21)
        self.label_wildD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_wildD.setAlignment(Qt.AlignCenter)
        self.label_wildH = QLabel(self)
        self.label_wildH.setGeometry(190, 340, 141, 21)
        self.label_wildH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_wildH.setAlignment(Qt.AlignCenter)
        self.label_wildB = QLabel(self)
        self.label_wildB.setGeometry(50, 360, 281, 21)
        self.label_wildB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_wildB.setAlignment(Qt.AlignCenter)
        self.label_wildB.setFont(QFont('Arial',14))

        self.label_maxh= QLabel('Maximum Host',self)
        self.label_maxh.setGeometry(370, 320, 101, 16)
        self.label_maxh.setContentsMargins(5,0,0,0)
        self.label_maxhD = QLabel(self)
        self.label_maxhD.setGeometry(370, 340, 141, 21)
        self.label_maxhD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_maxhD.setAlignment(Qt.AlignCenter)
        self.label_maxhH = QLabel(self)
        self.label_maxhH.setGeometry(510, 340, 141, 21)
        self.label_maxhH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_maxhH.setAlignment(Qt.AlignCenter)
        self.label_maxhB = QLabel(self)
        self.label_maxhB.setGeometry(370, 360, 281, 21)
        self.label_maxhB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_maxhB.setAlignment(Qt.AlignCenter)
        self.label_maxhB.setFont(QFont('Arial',14))

        self.label_net= QLabel('Network',self)
        self.label_net.setGeometry(50, 400, 60, 16)
        self.label_net.setContentsMargins(5,0,0,0)
        self.label_netD = QLabel(self)
        self.label_netD.setGeometry(50, 420, 141, 21)
        self.label_netD.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_netD.setAlignment(Qt.AlignCenter)
        self.label_netH = QLabel(self)
        self.label_netH.setGeometry(190, 420, 141, 21)
        self.label_netH.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_netH.setAlignment(Qt.AlignCenter)
        self.label_netB = QLabel(self)
        self.label_netB.setGeometry(50, 440, 281, 21)
        self.label_netB.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_netB.setAlignment(Qt.AlignCenter)
        self.label_netB.setFont(QFont('Arial',14))

        self.label_det= QLabel('Details',self)
        self.label_det.setGeometry(370, 400, 60, 16)
        self.label_det.setContentsMargins(5,0,0,0)
        self.label_detMh = QLabel('Max Hosts',self)
        self.label_detMh.setGeometry(370, 420, 141, 21)
        self.label_detMh.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_detMh.setAlignment(Qt.AlignCenter)
        self.label_detclass = QLabel('Class',self)
        self.label_detclass.setGeometry(510, 420, 141, 21)
        self.label_detclass.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_detclass.setAlignment(Qt.AlignCenter)
        self.label_detnumMaxHosts = QLabel(self)
        self.label_detnumMaxHosts.setGeometry(370, 440, 141, 21)
        self.label_detnumMaxHosts.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_detnumMaxHosts.setAlignment(Qt.AlignCenter)
        self.label_detipC = QLabel(self)
        self.label_detipC.setGeometry(510, 440, 141, 21)
        self.label_detipC.setStyleSheet("background-color: rgb(202, 205, 205);")
        self.label_detipC.setAlignment(Qt.AlignCenter)

        self.horizontalSlider.sliderMoved['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.btnC.setShortcut("Return")
        QMetaObject.connectSlotsByName(self)


    def calculate(self): #Se llama cuando se activa botón calculate
        try:
            print("Se ha hecho click o se dio enter")
            #Se obtiene valores del spinBox y de las entradas de texto.
            subnet = self.spinBox.value()

            #A continuación se obtienen los datos de las casillas de entrada
            dir = [self.input1.text(),self.input2.text(),self.input3.text(),self.input4.text()]

            for dato in dir:        #verifica datos entre 0 y 255
                if int(dato) < 0 or int(dato) > 255:
                    self.label_ipB.setText('Error. Values must be between [0 - 255]')
                    self.label_ipD.setText('!')
                    self.label_ipH.setText('!')
                    self.label_broadB.setText('!')
                    self.label_netmB.setText('!')
                    self.label_wildB.setText('!')
                    self.label_netB.setText('!')
                    self.label_maxhB.setText('!')
                    self.label_minhB.setText('!')
                    return None

            dir = C.concat(dir)
            dirBin = C.dec_a_bin(dir)
            exp = 32-subnet
            nums_hosts = 2**exp - 2
            if nums_hosts<2:
                nums_hosts = 1
            #Mostrar resultados. Actualizando los labels
            self.label_ipD.setText(dir)
            self.label_ipH.setText(C.dec_a_hexad(dir))
            self.label_ipB.setText(dirBin)
            broad_binario = C.broadcast(dirBin,subnet)
            broad_dec = C.bin_a_dec(broad_binario)
            self.label_broadB.setText(broad_binario)
            self.label_broadD.setText(broad_dec)
            self.label_broadH.setText(C.dec_a_hexad(broad_dec))
            netm_binario = C.netmask(dirBin,subnet)
            netm_dec = C.bin_a_dec(netm_binario)
            self.label_netmB.setText(netm_binario)
            self.label_netmD.setText(netm_dec)
            self.label_netmH.setText(C.dec_a_hexad(netm_dec))
            wild_bin = C.wildcard(netm_binario,subnet)
            wild_dec = C.bin_a_dec(wild_bin)
            self.label_wildB.setText(wild_bin)
            self.label_wildD.setText(wild_dec)
            self.label_wildH.setText(C.dec_a_hexad(wild_dec))
            netw_bin = C.network(dirBin,subnet)
            netw_dec = C.bin_a_dec(netw_bin)
            self.label_netB.setText(netw_bin)
            self.label_netD.setText(netw_dec)
            self.label_netH.setText(C.dec_a_hexad(netw_dec))
            maxh_bin = C.max_minHost(netw_bin,subnet,False)
            maxh_dec = C.bin_a_dec(maxh_bin)
            self.label_maxhB.setText(maxh_bin)
            self.label_maxhD.setText(maxh_dec)
            self.label_maxhH.setText(C.dec_a_hexad(maxh_dec))
            min_hostB = C.max_minHost(netw_bin,subnet,True)
            min_hostD = C.bin_a_dec(min_hostB)
            self.label_minhB.setText(min_hostB)
            self.label_minhD.setText(min_hostD)
            self.label_minhH.setText(C.dec_a_hexad(min_hostD))
            self.label_detnumMaxHosts.setText(str(nums_hosts))
            self.label_detipC.setText(C.clasifica(self.input1.text(),self.input2.text()))
        
        except ValueError:
            self.label_ipB.setText('Error. Missing input values.')
            self.label_ipD.setText('!')
            self.label_ipH.setText('!')
            self.label_broadB.setText('!')
            self.label_netmB.setText('!')
            self.label_wildB.setText('!')
            self.label_netB.setText('!')
            self.label_maxhB.setText('!')
            self.label_minhB.setText('!')


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()