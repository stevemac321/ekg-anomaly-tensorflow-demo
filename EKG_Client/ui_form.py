# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.sendNormal = QPushButton(Widget)
        self.sendNormal.setObjectName(u"sendNormal")
        self.sendNormal.setGeometry(QRect(110, 480, 131, 24))
        self.sendAnom = QPushButton(Widget)
        self.sendAnom.setObjectName(u"sendAnom")
        self.sendAnom.setGeometry(QRect(420, 480, 151, 24))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.sendNormal.setText(QCoreApplication.translate("Widget", u"Submit Normal", None))
        self.sendAnom.setText(QCoreApplication.translate("Widget", u"Send Anomaly", None))
    # retranslateUi

