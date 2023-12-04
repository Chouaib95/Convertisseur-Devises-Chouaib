from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()  # Remplace QtWidgets.QWidget.__init__()
        self.setObjectName("Form")
        self.resize(773, 585)
        self.setupUi()
        self.setup_connections()

    def setupUi(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setGeometry(QtCore.QRect(60, 80, 71, 31))
        self.label_name.setTextFormat(QtCore.Qt.RichText)
        self.label_name.setObjectName("label_name")
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setGeometry(QtCore.QRect(60, 140, 61, 41))
        self.label_email.setObjectName("label_email")
        self.lineEdit_name_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_name_2.setGeometry(QtCore.QRect(130, 90, 113, 22))
        self.lineEdit_name_2.setObjectName("lineEdit_name_2")
        self.lineEdit_email = QtWidgets.QLineEdit(self)
        self.lineEdit_email.setGeometry(QtCore.QRect(130, 160, 113, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(300, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")

#########################################################################
        """la partie du code suivante correspond à  la traduction (localisation) des textes dans votre interface utilisateur. 
        Cela permet à votre application d'être présentée dans différentes langues en modifiant dynamiquement le texte des
          éléments de l'interface utilisateur en fonction de la langue sélectionnée.

    Le code utilise la méthode retranslateUi pour mettre à jour les textes des éléments de l'interface
    utilisateur. Cette méthode est généralement générée automatiquement lors de la conception de l'interface graphique
    à l'aide de l'outil de conception de PyQt (Qt Designer). Le but principal est de séparer le code lié à la conception de
    l'interface graphique du code lié à la logique de l'application.

    Voici comment cela fonctionne :

    self.retranslateUi() : Cette méthode est appelée initialement pour définir les textes des éléments de l'interface utilisateur.

    QtCore.QMetaObject.connectSlotsByName(self) : Cette ligne connecte les signaux (comme le signal clicked d'un bouton) aux emplacements
    correspondants dans le code de l'application. Cela permet d'automatiser certaines connexions entre les éléments 
    de l'interface utilisateur et les fonctions associées.

    def retranslateUi(self) : Cette méthode contient les appels à _translate pour chaque élément de l'interface utilisateur, 
    définissant ainsi les textes à afficher. Le texte est généralement stocké dans des fichiers de traduction (.ts), qui peuvent
    être générés et modifiés à l'aide de l'outil pylupdate de PyQt.

    En résumé, cette partie du code est une partie standard lors de l'utilisation de l'outil de conception de PyQt, et elle facilite
    la gestion de plusieurs langues pour votre application en séparant les textes de l'interface utilisateur du code de logique métier. 
    Si vous n'avez pas l'intention de localiser votre application pour différentes langues, vous pourriez ne pas avoir besoin de cette partie du code.
        """
#############################################################################

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Formulaire"))
        self.label_name.setText(_translate("Form", "Name : "))
        self.label_email.setText(_translate("Form", "Email : "))
        self.pushButton.setText(_translate("Form", "Submit"))

    def setup_connections(self):
        self.pushButton.clicked.connect(self.compute)

    def compute(self):
        import sys
        nom = self.lineEdit_name_2.text()
        email = self.lineEdit_email.text()
        chemin = (Path(sys.argv[0]).parent / "Formulaire.txt")
        print(chemin)
        sys.exit(chemin.write_text(f"Nom : {nom}\nEmail : {email}"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = Ui_Form()
    win.show()
    app.exec_()
