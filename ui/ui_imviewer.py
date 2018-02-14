# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/imageviewer.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Custom QLabel and QListView
class cQLabel(QtWidgets.QLabel):
    def __init__(self, arg):
        super(cQLabel, self).__init__(arg)
        self.stored_pixmap = None

    def resizeEvent(self, a0: QtGui.QResizeEvent, min_size=512):
        super(cQLabel, self).resizeEvent(a0)
        stored_pixmap = self.stored_pixmap
        if stored_pixmap is not None:
            # avoiding image degradation
            stored_pixmap = stored_pixmap.copy()
            # defining increase dimension
            dw = a0.size().width() - a0.oldSize().width()
            dh = a0.size().height() - a0.oldSize().height()
            # choosing AspectRatio behaviour
            AspectRatioMode = QtCore.Qt.KeepAspectRatio
            if (dw > 0) or (dh > 0):
                AspectRatioMode = QtCore.Qt.KeepAspectRatioByExpanding
            # behaviour in case of image maximum extension
            if ((self.pixmap().width()+dw) >= self.width()-15) or ((self.pixmap().height()+dh) >= self.height()-15):
                dw = -1
                dh = -1
            # defining new width (nw) and new height (nh)
            nw = self.pixmap().width() + dw
            nh = self.pixmap().height() + dh
            # drawing image
            self.setPixmap(stored_pixmap.scaled(nw, nh, AspectRatioMode, QtCore.Qt.SmoothTransformation), False)
            # avoiding image smaller that min_size (according to orientation)
            if (self.pixmap().width() > self.pixmap().height()):
                if (self.pixmap().width() < min_size):
                    AspectRatioMode = QtCore.Qt.KeepAspectRatioByExpanding
                    self.setPixmap(stored_pixmap.scaled(min_size, nh, AspectRatioMode, QtCore.Qt.SmoothTransformation), False)
            else:
                if (self.pixmap().height() < min_size):
                    AspectRatioMode = QtCore.Qt.KeepAspectRatioByExpanding
                    self.setPixmap(stored_pixmap.scaled(nw, min_size, AspectRatioMode, QtCore.Qt.SmoothTransformation), False)

    def setPixmap(self, a0: QtGui.QPixmap, save=True):
        super(cQLabel, self).setPixmap(a0)
        if save:
            self.stored_pixmap = a0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMinimumSize(QtCore.QSize(256, 0))
        self.listView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listView.setSizeIncrement(QtCore.QSize(0, 0))
        self.listView.setIconSize(QtCore.QSize(75, 75))
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 742, 538))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        # self.labelImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg = cQLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImg.sizePolicy().hasHeightForWidth())
        self.labelImg.setSizePolicy(sizePolicy)
        self.labelImg.setMouseTracking(True)
        self.labelImg.setAutoFillBackground(False)
        self.labelImg.setText("")
        self.labelImg.setScaledContents(False)
        self.labelImg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImg.setObjectName("labelImg")
        self.gridLayout.addWidget(self.labelImg, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuClose = QtWidgets.QMenu(self.menuFile)
        self.menuClose.setObjectName("menuClose")
        self.menuModify = QtWidgets.QMenu(self.menubar)
        self.menuModify.setEnabled(True)
        self.menuModify.setObjectName("menuModify")
        self.menuRotate = QtWidgets.QMenu(self.menuModify)
        self.menuRotate.setEnabled(True)
        self.menuRotate.setObjectName("menuRotate")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCurrent = QtWidgets.QAction(MainWindow)
        self.actionCurrent.setObjectName("actionCurrent")
        self.actionAll = QtWidgets.QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.action90_clockwise = QtWidgets.QAction(MainWindow)
        self.action90_clockwise.setObjectName("action90_clockwise")
        self.action90_counterclockwise = QtWidgets.QAction(MainWindow)
        self.action90_counterclockwise.setObjectName("action90_counterclockwise")
        self.actionCustom_angle = QtWidgets.QAction(MainWindow)
        self.actionCustom_angle.setObjectName("actionCustom_angle")
        self.actionShow_images = QtWidgets.QAction(MainWindow)
        self.actionShow_images.setCheckable(True)
        self.actionShow_images.setChecked(True)
        self.actionShow_images.setObjectName("actionShow_images")
        self.actionIn = QtWidgets.QAction(MainWindow)
        self.actionIn.setObjectName("actionIn")
        self.actionOut = QtWidgets.QAction(MainWindow)
        self.actionOut.setObjectName("actionOut")
        self.actionFit_to_Window = QtWidgets.QAction(MainWindow)
        self.actionFit_to_Window.setObjectName("actionFit_to_Window")
        self.actionOriginal_size = QtWidgets.QAction(MainWindow)
        self.actionOriginal_size.setObjectName("actionOriginal_size")
        self.actionImage_proprieties = QtWidgets.QAction(MainWindow)
        self.actionImage_proprieties.setObjectName("actionImage_proprieties")
        self.actionExif = QtWidgets.QAction(MainWindow)
        self.actionExif.setObjectName("actionExif")
        self.menuClose.addAction(self.actionCurrent)
        self.menuClose.addAction(self.actionAll)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuClose.menuAction())
        self.menuRotate.addAction(self.action90_clockwise)
        self.menuRotate.addAction(self.action90_counterclockwise)
        self.menuModify.addAction(self.menuRotate.menuAction())
        self.menuView.addAction(self.actionExif)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuModify.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuClose.setTitle(_translate("MainWindow", "Close image(s)"))
        self.menuModify.setTitle(_translate("MainWindow", "Modify"))
        self.menuRotate.setTitle(_translate("MainWindow", "Rotate"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCurrent.setText(_translate("MainWindow", "Current"))
        self.actionAll.setText(_translate("MainWindow", "All"))
        self.action90_clockwise.setText(_translate("MainWindow", "90° clockwise"))
        self.action90_clockwise.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action90_counterclockwise.setText(_translate("MainWindow", "90° counterclockwise"))
        self.action90_counterclockwise.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionCustom_angle.setText(_translate("MainWindow", "Custom angle"))
        self.actionShow_images.setText(_translate("MainWindow", "Show images"))
        self.actionShow_images.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionIn.setText(_translate("MainWindow", "In"))
        self.actionOut.setText(_translate("MainWindow", "Out"))
        self.actionFit_to_Window.setText(_translate("MainWindow", "Fit to Window"))
        self.actionFit_to_Window.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionOriginal_size.setText(_translate("MainWindow", "Original size"))
        self.actionImage_proprieties.setText(_translate("MainWindow", "Image exif"))
        self.actionExif.setText(_translate("MainWindow", "Exif"))
        self.actionExif.setShortcut(_translate("MainWindow", "Ctrl+E"))

