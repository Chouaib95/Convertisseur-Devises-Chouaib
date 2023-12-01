from PySide6 import QtWidgets
import currency_converter
from currency_converter import RateNotFoundError

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() # Remplace QtWidgets.QWidget.__init__()
        self.c = currency_converter.CurrencyConverter() # créer une nouvelle instance de currency_converter
        self.setWindowTitle("Convertisseur de devises")#paramètrer le nom de la fenêtre qui s'ouvre
        self.setup_ui() # fonction qui permet de configurer les composants de la fenêtre (layout)
        self.set_default_values()
        self.setup_connections()
        self.setup_css()

    #fonction qui permet de configurer les composants de la fenêtre:

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self) # créer une nouvelle instance de QtWidgets.QHBoxLayout (Layout horizonatal)
        self.cbb_devisesFrom = QtWidgets.QComboBox() # créer une nouvelle instance de QtWidgets.QComboBox (ComboBox de devises)
        self.spn_montant = QtWidgets.QDoubleSpinBox() # créer une nouvelle instance de QtWidgets.QSpinBox (SpinBox de montant)
        self.cbb_devisesTo = QtWidgets.QComboBox() # créer une nouvelle instance de QtWidgets.QComboBox (ComboBox de devises)
        self.spn_montantConvertisseur = QtWidgets.QDoubleSpinBox() # créer une nouvelle instance de QtWidgets.QSpinBox (SpinBox de montant)
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises") # créer une nouvelle instance de QtWidgets.QPushButton (Boutton d'inversion de devises')

        self.layout.addWidget(self.cbb_devisesFrom) # ajouter les composants dans le layout
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConvertisseur)
        self.layout.addWidget(self.btn_inverser)
        
    def set_default_values(self):
        #self.cbb_devisesFrom.addItem(sorted(list(self.c.currencies))) sauf que PySide6 n'accepte pas une liste comme argument !
        [self.cbb_devisesFrom.addItem(currency.strip()) for currency in sorted(list(self.c.currencies))]
        [self.cbb_devisesTo.addItem(currency.strip()) for currency in sorted(list(self.c.currencies))]

        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("USD")

        self.spn_montant.setRange(0,1000000000)
        self.spn_montantConvertisseur.setRange(0,1000000000)
        self.spn_montant.setValue(100)
        self.spn_montantConvertisseur.setValue(0)
        self.spn_montantConvertisseur.setDecimals(2)
        self.spn_montant.setDecimals(2)

        
    def setup_connections(self):  #connecter les widgets aux méthodes.
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devises)


    def compute(self):
        montant = self.spn_montant.value() # récupérer le montant
        devise_from = self.cbb_devisesFrom.currentText() # récupérer la devise de départ
        devise_to = self.cbb_devisesTo.currentText() # récupérer la devise d'arrivée

        try:
            resultat = self.c.convert(montant, devise_from, devise_to) # convertir le montant en utilisant l'instance de currency_converter
        except RateNotFoundError:
            print("Data non disponible !")
        else:
            self.spn_montantConvertisseur.setValue(round(resultat,2)) # afficher le résultat
       

    def inverser_devises(self):
        devise_from = self.cbb_devisesFrom.currentText() # récupérer la devise de départ
        devise_to = self.cbb_devisesTo.currentText() # récupérer la devise d'arrivée
        self.cbb_devisesFrom.setCurrentText(devise_to) # changer la devise de départ
        self.cbb_devisesTo.setCurrentText(devise_from) # changer la devise d'arrivée
        self.compute() # recalculer les valeurs

    def setup_css(self):
        # Applique une feuille de style CSS pour styliser l'interface graphique
        self.setStyleSheet("""
            background-color: #2E4053;
            color: #FDFEFE;
            font-family: 'Arial', sans-serif;
            """)
        self.btn_inverser.setStyleSheet("""
            background-color: #E74C3C;
            color: #FFF;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            """)
        self.cbb_devisesFrom.setStyleSheet("""
            background-color: #3498DB;
        """)

# Crée une application Qt
app = QtWidgets.QApplication([]) #important de creer l'application app et mettre dedans nos widgets (App) et 
                                 #l'executer par la suite pour avoir un resultat# important de passer une
                                 #  liste vide en argument
# Crée une instance de App et l'affiche
win = App()
win.show()
#execution de l'application Qt
app.exec()