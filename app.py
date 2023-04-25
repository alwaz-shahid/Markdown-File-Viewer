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

        # Create the "Open File" button
        self.openButton = QPushButton('Open File', self)
        self.openButton.clicked.connect(self.openFile)
        layout.addWidget(self.openButton)

        # Create the "Preview" button
        self.previewButton = QPushButton('Preview', self)
        self.previewButton.clicked.connect(self.preview)
        layout.addWidget(self.previewButton)

        # Set the main layout
        self.setLayout(layout)

    def updatePreview(self):
        # Convert Markdown to HTML and display it in the webview
        markdown_text = self.editor.toPlainText()
        html = markdown.markdown(markdown_text)
        self.preview_html = html

    def openFile(self):
        # Open a file dialog and let the user select a Markdown file
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Markdown Files (*.md *.markdown)')
        if fileName:
            # Read the contents of the file and display it in the editor
            with open(fileName, 'r', encoding='utf-8') as f:
                self.editor.setPlainText(f.read())

            # Update the preview with the contents of the file
            self.updatePreview()

    def preview(self):
        # Create a new window for the preview
        self.previewWindow = QWidget()
        self.previewWindow.setWindowTitle('Preview')

        # Create a layout for the preview window
        layout = QVBoxLayout()

        # Create a webview for displaying the HTML
        self.preview_webview = QWebEngineView()
        self.preview_webview.setHtml(self.preview_html)
        layout.addWidget(self.preview_webview)

        # Set the layout for the preview window
        self.previewWindow.setLayout(layout)

        # Show the preview window
        self.previewWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MarkdownViewer()
    viewer.show()
    sys.exit(app.exec_())
