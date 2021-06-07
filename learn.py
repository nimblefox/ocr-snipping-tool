# from  https://www.youtube.com/watch?v=rZcdhles6vQ
import PyQt5.QtWidgets as qtw   # Basic
import PyQt5.QtGui as qtg       # for fontsize 

class MainWindow(qtw.QWidget):  # Basic
	def __init__(self):         # Basic
		super(). __init__()	    # Basic

		# Add a title
		self.setWindowTitle("Hello World")

		# Set Vertical layout 
		self.setLayout(qtw.QVBoxLayout())

		# Create a Label
		my_label = qtw.QLabel("Your Name?")
		
		# Set font size
		my_label.setFont(qtg.QFont('Helvetica', 18))
		self.layout().addWidget(my_label)
        
        # text input entry box
		my_entry = qtw.QLineEdit()
		my_entry.setObjectName("name_field")
		my_entry.setText("")
		self.layout().addWidget(my_entry)

		# Create a button
		my_button = qtw.QPushButton("Press", 
			clicked = lambda: press_it())
		self.layout().addWidget(my_button)

		# define button press function
		def press_it():
			# Add name to label
			my_label.setText(f'Hello {my_entry.text()}!')
			# clear the entry box
			my_entry.setText("")


		self.show()


app= qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()
