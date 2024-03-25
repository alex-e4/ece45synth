from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt5.QtWidgets import QFileDialog
import soundfile as sf
import numpy as np
import sounddevice as sd
import scipy.signal
from scipy.io.wavfile import write

class Ui_MainWindow(object):
    # Create the UI, and connect the buttons to their respective functions
    # UI was created with pyqt5 designer, and then converted to python code
    # Buttons must be connected manually
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.originalplot = QtWidgets.QWidget(self.centralwidget)
        self.originalplot.setGeometry(QtCore.QRect(20, 20, 221, 181))
        self.originalplot.setObjectName("originalplot")
        self.newplot = QtWidgets.QWidget(self.centralwidget)
        self.newplot.setGeometry(QtCore.QRect(330, 30, 221, 171))
        self.newplot.setObjectName("newplot")
        self.originalplot_2 = QtWidgets.QWidget(self.centralwidget)
        self.originalplot_2.setGeometry(QtCore.QRect(30, 210, 531, 190))
        self.originalplot_2.setObjectName("originalplot_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 0, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 47, 13))
        self.label_6.setObjectName("label_6")
        self.FFT1 = QtWidgets.QPushButton(self.centralwidget)
        self.FFT1.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.FFT1.setObjectName("FFT1")
        self.FFT2 = QtWidgets.QPushButton(self.centralwidget)
        self.FFT2.setGeometry(QtCore.QRect(560, 180, 75, 23))
        self.FFT2.setObjectName("FFT2")
        self.FFT3 = QtWidgets.QPushButton(self.centralwidget)
        self.FFT3.setGeometry(QtCore.QRect(570, 360, 75, 23))
        self.FFT3.setObjectName("FFT3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 410, 651, 137))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.cutoff = QtWidgets.QLineEdit(self.widget)
        self.cutoff.setObjectName("cutoff")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cutoff)
        self.lpf = QtWidgets.QPushButton(self.widget)
        self.lpf.setObjectName("lpf")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lpf)
        self.cutofffreq = QtWidgets.QLabel(self.widget)
        self.cutofffreq.setObjectName("cutofffreq")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cutofffreq)
        self.hpf = QtWidgets.QPushButton(self.widget)
        self.hpf.setObjectName("hpf")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hpf)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.volabel = QtWidgets.QLabel(self.widget)
        self.volabel.setObjectName("volabel")
        self.verticalLayout_2.addWidget(self.volabel)
        self.volume = QtWidgets.QSlider(self.widget)
        self.volume.setSliderPosition(50)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.volume.setTickInterval(10)
        self.volume.setObjectName("volume")
        self.verticalLayout_2.addWidget(self.volume)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pitchrange = QtWidgets.QSlider(self.widget)
        self.pitchrange.setSliderPosition(50)
        self.pitchrange.setTracking(False)
        self.pitchrange.setOrientation(QtCore.Qt.Horizontal)
        self.pitchrange.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pitchrange.setTickInterval(10)
        self.pitchrange.setObjectName("pitchrange")
        self.verticalLayout.addWidget(self.pitchrange)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.convolve = QtWidgets.QPushButton(self.widget)
        self.convolve.setObjectName("convolve")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.convolve)
        self.add = QtWidgets.QPushButton(self.widget)
        self.add.setObjectName("add")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.add)
        self.wavedropdown = QtWidgets.QComboBox(self.widget)
        self.wavedropdown.setObjectName("wavedropdown")
        self.wavedropdown.addItem("")
        self.wavedropdown.addItem("")
        self.wavedropdown.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wavedropdown)
        self.add_2 = QtWidgets.QPushButton(self.widget)
        self.add_2.setObjectName("add_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.add_2)
        self.frequency = QtWidgets.QLineEdit(self.widget)
        self.frequency.setObjectName("frequency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.frequency)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.play = QtWidgets.QPushButton(self.widget)
        self.play.setObjectName("play")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.play)
        self.loop = QtWidgets.QRadioButton(self.widget)
        self.loop.setObjectName("loop")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loop)
        self.importbutton = QtWidgets.QPushButton(self.widget)
        self.importbutton.setObjectName("importbutton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.importbutton)
        self.channel1 = QtWidgets.QRadioButton(self.widget)
        self.channel1.setObjectName("channel1")
        self.ChannelGroup = QtWidgets.QButtonGroup(MainWindow)
        self.ChannelGroup.setObjectName("ChannelGroup")
        self.ChannelGroup.addButton(self.channel1)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel1)
        self.recordbutton = QtWidgets.QPushButton(self.widget)
        self.recordbutton.setObjectName("recordbutton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.recordbutton)
        self.channel2 = QtWidgets.QRadioButton(self.widget)
        self.channel2.setObjectName("channel2")
        self.ChannelGroup.addButton(self.channel2)
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.channel2)
        self.save = QtWidgets.QPushButton(self.widget)
        self.save.setObjectName("save")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.save)
        self.filename = QtWidgets.QLineEdit(self.widget)
        self.filename.setObjectName("filename")
        self.clear = QtWidgets.QPushButton(self.widget)
        self.clear.setObjectName("clear")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.clear)
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.filename)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.horizontalLayout.addLayout(self.formLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        """
        Functionality for buttons and sliders
        """
        # Sampling frequency
        self.freq = 44100
        
        # Recording duration
        self.duration = 5

        devices = sd.query_devices()    # get list of devices
        sd.default.device = 2           # set default device to my microphone. Will have to change to record

        # Initizalize signals to zero to prevent errors
        self.channel3sig = np.zeros(self.freq * self.duration)
        self.channel2sig = self.channel3sig
        self.channel1sig = self.channel3sig
        
        # Display empty signals
        self.plotch1()
        self.plotch2()
        self.plotch3()

        # connect buttons to functions
        self.clear.clicked.connect(self.clearoutput)
        self.FFT1.clicked.connect(self.ch1click)
        self.FFT2.clicked.connect(self.ch2click)
        self.FFT3.clicked.connect(self.outputclick)
        self.importbutton.clicked.connect(self.importaudio)
        self.add_2.clicked.connect(self.generate)
        self.add.clicked.connect(self.addtooutput)
        self.play.clicked.connect(self.playaudio)
        self.convolve.clicked.connect(self.convolveaudio)
        self.lpf.clicked.connect(self.lowpass)
        self.hpf.clicked.connect(self.highpass)
        self.recordbutton.clicked.connect(self.recordaudio)
        self.save.clicked.connect(self.saveaudio)

        # add text to ui
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECE45"))
        self.label_2.setText(_translate("MainWindow", "Channel 1"))
        self.label_3.setText(_translate("MainWindow", "Channel 2"))
        self.label_6.setText(_translate("MainWindow", "Output"))
        self.FFT1.setText(_translate("MainWindow", "Frequency"))
        self.FFT2.setText(_translate("MainWindow", "Frequency"))
        self.FFT3.setText(_translate("MainWindow", "Frequency"))
        self.lpf.setText(_translate("MainWindow", "LPF"))
        self.cutofffreq.setText(_translate("MainWindow", "Cutoff Freq"))
        self.hpf.setText(_translate("MainWindow", "HPF"))
        self.volabel.setText(_translate("MainWindow", "Volume"))
        self.label.setText(_translate("MainWindow", "Pitch"))
        self.convolve.setText(_translate("MainWindow", "Convolve"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.wavedropdown.setItemText(0, _translate("MainWindow", "Sine Wave"))
        self.wavedropdown.setItemText(1, _translate("MainWindow", "Sawtooth"))
        self.wavedropdown.setItemText(2, _translate("MainWindow", "Square Wave"))
        self.add_2.setText(_translate("MainWindow", "Generate"))
        self.label_5.setText(_translate("MainWindow", "Frequency"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.loop.setText(_translate("MainWindow", "Loop"))
        self.importbutton.setText(_translate("MainWindow", "Import Audio"))
        self.channel1.setText(_translate("MainWindow", "Channel 1"))
        self.recordbutton.setText(_translate("MainWindow", "Record Audio"))
        self.channel2.setText(_translate("MainWindow", "Channel 2"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Filename"))
        self.clear.setText(_translate("MainWindow", "Clear Output"))

    def plotch1(self):
        # Create a figure and axis for the plot
        self.figure = plt.figure()
        self.axis = self.figure.add_subplot(111)

        if self.FFT1.text() == "Time":
            # Plot your data on the axis
            time_axis = np.arange(len(self.channel1sig)) / self.freq
            self.axis.plot(time_axis, self.channel1sig, label="Channel 1")
        else:
            # Plot the FFT
            fft_data = np.fft.fft(self.channel1sig)
            freq = np.fft.fftfreq(len(self.channel1sig))
            self.axis.plot(freq, np.abs(fft_data))

        # Create a canvas widget for the plot
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.originalplot)

        # matplotlibe figures must be closed maanually
        plt.close(self.figure)

        # Remove existing layout (If possible)
        if self.originalplot.layout():
            QtWidgets.QWidget().setLayout(self.originalplot.layout())


        # Update the layout of the originalplot widget
        self.originalplot.setLayout(QtWidgets.QVBoxLayout())
        self.originalplot.layout().addWidget(self.canvas)

    def plotch2(self):
        # Create a figure and axis for the plot
        self.figure2 = plt.figure()
        self.axis2 = self.figure2.add_subplot(111)

        if self.FFT2.text() == "Time":
            time_axis = np.arange(len(self.channel2sig)) / self.freq
            self.axis2.plot(time_axis, self.channel2sig, label="Channel 2")
        else:
            # Plot the FFT
            fft_data = np.fft.fft(self.channel2sig)
            freq = np.fft.fftfreq(len(self.channel2sig))
            self.axis2.plot(freq, np.abs(fft_data))

        # Create a canvas widget for the plot
        self.canvas = FigureCanvas(self.figure2)
        self.canvas.setParent(self.newplot)

        # matplotlibe figures must be closed maanually
        plt.close(self.figure2)

        # Remove existing layout (If possible)
        if self.newplot.layout():
            QtWidgets.QWidget().setLayout(self.newplot.layout())

        # Update the layout of the newplot widget
        self.newplot.setLayout(QtWidgets.QVBoxLayout())
        self.newplot.layout().addWidget(self.canvas)
    
    def plotch3(self):
        # Create a figure and axis for the plot
        self.figure3 = plt.figure()
        self.axis3 = self.figure3.add_subplot(111)

        if self.FFT3.text() == "Time":
            time_axis = np.arange(len(self.channel3sig)) / self.freq
            self.axis3.plot(time_axis, self.channel3sig, label="Channel 3")
        else:
            # Plot the FFT
            fft_data = np.fft.fft(self.channel3sig)
            freq = np.fft.fftfreq(len(self.channel3sig))
            self.axis3.plot(freq, np.abs(fft_data))

        # Create a canvas widget for the plot
        self.canvas = FigureCanvas(self.figure3)
        self.canvas.setParent(self.originalplot_2)

        # Close the figure
        plt.close(self.figure3)

        # Remove the existing layout if possible
        if self.originalplot_2.layout():
            QtWidgets.QWidget().setLayout(self.originalplot_2.layout())

        # Update the layout 
        self.originalplot_2.setLayout(QtWidgets.QVBoxLayout())
        self.originalplot_2.layout().addWidget(self.canvas)

        #use scroll to zoom into the output
        self.canvas.mpl_connect('scroll_event', self.zoom)

    def zoom(self, event): # check for a scroll to zoom in or out
        if event.button == 'up':
            #zoom in
            self.axis3.set_xlim(self.axis3.get_xlim()[0] * 0.9, self.axis3.get_xlim()[1] * 0.9)
            self.axis3.set_ylim(self.axis3.get_ylim()[0] * 0.9, self.axis3.get_ylim()[1] * 0.9)
        elif event.button == 'down':
            # Zoom out
            self.axis3.set_xlim(self.axis3.get_xlim()[0] * 1.1, self.axis3.get_xlim()[1] * 1.1)
            self.axis3.set_ylim(self.axis3.get_ylim()[0] * 1.1, self.axis3.get_ylim()[1] * 1.1)

        # Redraw the canvas
        self.canvas.draw()

    # Switch between time and frequency domain for ch1, ch2, and ch3 (output)
    def ch1click(self):
        if self.FFT1.text() == "Frequency":
            self.FFT1.setText("Time")
            self.FFT1.clicked.connect(self.plotch1)
        else:
            self.FFT1.setText("Frequency")
            self.FFT1.clicked.connect(self.plotch1)

    def ch2click(self):
        if self.FFT2.text() == "Frequency":
            self.FFT2.setText("Time")
            self.FFT2.clicked.connect(self.plotch2)
        else:
            self.FFT2.setText("Frequency")
            self.FFT2.clicked.connect(self.plotch2)

    def outputclick(self):
        if self.FFT3.text() == "Frequency":
            self.FFT3.setText("Time")
            self.FFT3.clicked.connect(self.plotch3)
        else:
            self.FFT3.setText("Frequency")
            self.FFT3.clicked.connect(self.plotch3)

    # Update the channel with a new audio file or a generated wave
    def updatechannel(self, fileName=0, wave=0):
        if self.channel2.isChecked():
            if fileName != 0:
                self.channel2sig, _ = sf.read(fileName, dtype='float32')
                self.channel2sig = self.channel2sig[:,0]
            else:
                self.channel2sig = wave
            self.plotch2()
        else:
            if fileName != 0:
                self.channel1sig, _ = sf.read(fileName, dtype='float32')
                self.channel1sig = self.channel1sig[:,0]
            else:
                self.channel1sig = wave
            self.plotch1()

    # Open up file dialog to get a .wav file, and then send it to the updatechannel function
    def importaudio(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(filter="WAV Files (*.wav);;All Files (*)")
            self.updatechannel(fileName)
        except:
           return None
    
    # Generate a frequency. defaults to 800 Hz if no frequency is given
    # scipy made this so much easier than manually creating a wave
    def generate(self):
        wave = self.wavedropdown.currentText()
        if self.frequency.text() == "":
            freq = 800
        else:
          freq = float(self.frequency.text())
        if wave == "Sine Wave":
            t = np.linspace(0, self.duration, self.freq*self.duration)
            outputwave = np.sin(2 * np.pi * freq * t)
        elif wave == "Sawtooth":
            t = np.linspace(0, self.duration, self.freq*self.duration)
            outputwave = scipy.signal.sawtooth(2 * np.pi * freq * t)
        else:
            t = np.linspace(0, self.duration, self.freq*self.duration)
            outputwave = scipy.signal.square(2 * np.pi * freq * t)
        self.updatechannel(wave=outputwave*.004)    # reduces the amplitude of the wave as its overpowering with voice recordings
    
    # Clear the output, and stop the audio if it is playing
    def clearoutput(self):
        self.channel3sig = np.zeros(self.freq * self.duration)
        self.plotch3()  # update plot
        sd.stop()
    
    # Add the selected channel to the output
    def addtooutput(self):
        if self.channel2.isChecked():
            self.channel3sig = np.add(self.channel3sig, self.channel2sig)
        else:
            self.channel3sig = np.add(self.channel3sig, self.channel1sig)
        self.plotch3()
    
    # Play the audio, depending on the pitch and vol sliders.
    def playaudio(self):

        pitchrange = pitchrange = .5 + (4 - .5) * (self.pitchrange.value() / 350)

        audio = self.channel3sig * self.volume.value() / 10

        audio = scipy.signal.resample(audio, int(len(audio) / pitchrange))

        sd.play(audio, self.freq, device=4, loop=self.loop.isChecked())
    
    # Use the convolution of the selected channel on the output signal
    def convolveaudio(self):
        if self.channel2.isChecked():
            self.channel3sig = np.convolve(self.channel3sig, self.channel2sig, mode='same')
        else:
            self.channel3sig = np.convolve(self.channel3sig, self.channel1sig, mode='same')
        self.plotch3()
    
    # Create a low pas filter depending on cutoff freq.
    def lowpass(self):
        if not self.cutofffreq.text() or not self.cutofffreq.text().isdigit():
            cutoff_freq = 1000
        else:
            cutoff_freq = float(self.cutofffreq.text())
        
        b, a = scipy.signal.butter(8, cutoff_freq, btype='low', fs=self.freq)

        self.channel3sig = scipy.signal.lfilter(b, a, self.channel3sig)

        self.plotch3()

    # Create a high pass filter depending on cutoff freq.
    def highpass(self):
        if not self.cutofffreq.text() or not self.cutofffreq.text().isdigit():
            cutoff_freq = 500
        else:
            cutoff_freq = float(self.cutofffreq.text())
        
        b, a = scipy.signal.butter(8, cutoff_freq, btype='high', fs=self.freq)

        self.channel3sig = scipy.signal.lfilter(b, a, self.channel3sig)

        self.plotch3()
    
    # Record audio from the selected channel. Might have to change the device to record or an error will occur!
    def recordaudio(self):
        if self.channel2.isChecked():
            self.channel2sig = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=2)
            self.channel2sig = self.channel2sig[:,0]
            sd.wait()
            self.plotch2()
        else:
            self.channel1sig = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=2)
            self.channel1sig = self.channel1sig[:,0]
            sd.wait()
            self.plotch1()
        print("Recording done")

    # Save the output audio to a .wav file
    # I didn't add a lot of checks, so be way with what you name your file
    def saveaudio(self):
        filename = self.filename.text()
        if filename == "" or " " in filename:
            filename = "default"
        write(f"audiofiles/{filename}.wav", self.freq, self.channel3sig)


# Actually display the application and run it
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())