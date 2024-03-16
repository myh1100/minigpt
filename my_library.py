import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QProcess

def cmdrun(cmmd):
    class CMDRunner(QWidget):
        def __init__(self):
            super().__init__()

            self.initUI()

            self.process = QProcess(self)
            self.process.setProcessChannelMode(QProcess.MergedChannels)
            self.process.readyRead.connect(self.handle_output)

            command = cmmd
            self.process.start('cmd.exe', ['/c', command])

        def initUI(self):
            self.setWindowTitle('Chat GPT')
            self.setGeometry(500, 500, 800, 500)

            layout = QVBoxLayout()

            self.output = QTextEdit()
            self.output.setReadOnly(True)
            layout.addWidget(self.output)

            self.setLayout(layout)

        def handle_output(self):
            data = self.process.readAll().data().decode("utf-8")
            self.output.append(data)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = CMDRunner()
        ex.show()
        sys.exit(app.exec_())

cmdrun('python sample.py --out_dir=out-shakespeare-char --device=cpu --num_samples=1 --start=python')
