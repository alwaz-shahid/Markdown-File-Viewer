import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QPushButton, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
import markdown

class MarkdownViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout
        layout = QVBoxLayout()

        # Create the text editor for input
        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.updatePreview)
        layout.addWidget(self.editor)

        # Create the webview for output
        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        # Create the "Open File" button
        self.openButton = QPushButton('Open File', self)
        self.openButton.clicked.connect(self.openFile)
        layout.addWidget(self.openButton)

        # Set the main layout
        self.setLayout(layout)

    def updatePreview(self):
        # Convert Markdown to HTML and display it in the webview
        html = markdown.markdown(self.editor.toPlainText())
        self.webview.setHtml(html)

    def openFile(self):
        # Open a file dialog and let the user select a Markdown file
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Markdown Files (*.md *.markdown)')
        if fileName:
            # Read the contents of the file and display it in the editor
            with open(fileName, 'r', encoding='utf-8') as f:
                self.editor.setPlainText(f.read())

            # Update the preview with the contents of the file
            self.updatePreview()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MarkdownViewer()
    viewer.show()
    sys.exit(app.exec_())
