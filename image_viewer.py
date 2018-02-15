import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QTransform, QResizeEvent
from PyQt5.QtCore import Qt, QSize
from ui.ui_imviewer import Ui_MainWindow
from ui.ui_exifviewer import Ui_Dialog
from utility.Images import ImageListModel
from utility.gpsconverter import get_exif_location

class ExifViewer(QDialog):
    def __init__(self, exif, parent=None):
        super(ExifViewer, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.exif = exif
        self.populate_table()

    def populate_table(self):
        gps = self.exif.pop('GPSInfo') if ('GPSInfo' in self.exif) else None
        self.ui.tableWidget.setRowCount(len(self.exif))
        for r, tag in enumerate(self.exif):
            self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
            self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))
        if (gps is not None):
            lat, lon = get_exif_location(gps)
            url = '<a href="https://www.google.com/maps/search/?api=1&query={0},{1}"> Link to Google Maps </a>'.format(lat, lon)
            print( 'url: {}'.format(url) )
            self.ui.webLabel.setText( url )


class ImViewer(QMainWindow):
    def __init__(self, model: ImageListModel):
        super(ImViewer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model
        self.ui.listView.setModel(self.model)

        self.build_behavior()

    def build_behavior(self):
        self.ui.listView.doubleClicked.connect(self.__show_image)

        self.ui.actionOpen.triggered.connect(lambda: self.model.insertRows(self.__get_file_explorer()))
        self.ui.actionCurrent.triggered.connect(lambda: self.__remove_image(all=False))
        self.ui.actionAll.triggered.connect(lambda: self.__remove_image(all=True))

        self.ui.action90_clockwise.triggered.connect(lambda: self.__rotate_image(90))
        self.ui.action90_counterclockwise.triggered.connect(lambda: self.__rotate_image(-90))

        self.ui.actionExif.triggered.connect(lambda: self.__get_exif() )

    def __get_file_explorer(self):
        files = QFileDialog.getOpenFileNames(None, 'Select one or more images to open', '/home',
                                             "Jpeg images (*.jpg *.jpeg *.JPG);;All files (*.*)")
        return files[0]

    def __show_image(self, e, target=512):
        im = self.model.get_image(e.row())
        w, h = (im.width(), im.height())
        ratio = w/h
        w, h = (target, int(target/ratio)) if (w > h) else (int(ratio*target), target)
        self.ui.labelImg.setPixmap(QPixmap.fromImage(im).scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def __remove_image(self, all=True):
        if all:
            self.model.removeRows(0, self.model.rowCount())
        else:
            item = self.ui.listView.selectionModel().selectedIndexes()
            if (len(item) != 0):
                self.model.removeRows(item[0].row(), 1)

    def __rotate_image(self, angle):
        pixmap = self.ui.labelImg.pixmap()
        if (pixmap is not None):
            pixmap = pixmap.transformed(QTransform().rotate(angle))
            self.ui.labelImg.setPixmap( pixmap )

    def __get_exif(self):
        item = self.ui.listView.selectionModel().selectedIndexes()
        if (len(item) != 0): 
            exif = self.model.get_exif(item[0].row())
            exif_viewer = ExifViewer(exif, self)
            exif_viewer.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    im_viewer = ImViewer(ImageListModel())
    im_viewer.show()
    sys.exit(app.exec_())
