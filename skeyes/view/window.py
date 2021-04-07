import os
from PyQt5 import QtCore, QtWidgets


# TODO Input callbacks
# TODO Input typechecking, if incorrect input highlight red with modal message?
# TODO Show webcam output from certain port?


class Window:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()

        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(350, 300)
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")

        self.actions = QtWidgets.QWidget()
        self.actions.setObjectName("actions")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.actions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.actions)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 308, 231))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.feature_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.feature_label.setObjectName("feature_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.feature_label)
        self.action_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.action_label.setObjectName("action_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.action_label)
        self.windows_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.windows_label.setObjectName("windows_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.windows_label)
        self.windows_combo = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.windows_combo.setEditable(False)
        self.windows_combo.setObjectName("windows_combo")
        self.windows_combo.addItem("")
        self.windows_combo.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.windows_combo)
        self.gutters_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.gutters_label.setObjectName("gutters_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gutters_label)
        self.gutters_combo = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.gutters_combo.setObjectName("gutters_combo")
        self.gutters_combo.addItem("")
        self.gutters_combo.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gutters_combo)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tab_widget.addTab(self.actions, "")

        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.formLayout_2 = QtWidgets.QFormLayout(self.settings)
        self.formLayout_2.setObjectName("formLayout_2")
        self.stream_enable_checkbox = QtWidgets.QCheckBox(self.settings)
        self.stream_enable_checkbox.setChecked(True)
        self.stream_enable_checkbox.setObjectName("stream_enable_checkbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stream_enable_checkbox)
        self.qgc_label = QtWidgets.QLabel(self.settings)
        self.qgc_label.setObjectName("qgc_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.qgc_label)
        self.gst_ip = QtWidgets.QLineEdit(self.settings)
        self.gst_ip.setMaxLength(16)
        self.gst_ip.setObjectName("gst_ip")

        self.gst_ip.setText("127.0.0.1")

        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gst_ip)
        self.streaming_port_label = QtWidgets.QLabel(self.settings)
        self.streaming_port_label.setObjectName("streaming_port_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.streaming_port_label)
        self.gst_port = QtWidgets.QLineEdit(self.settings)
        self.gst_port.setMaxLength(5)
        self.gst_port.setObjectName("gst_port")

        self.gst_port.setText("5600")

        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gst_port)
        self.file_logging_enable_checkbox = QtWidgets.QCheckBox(self.settings)
        self.file_logging_enable_checkbox.setObjectName("file_logging_enable_checkbox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.file_logging_enable_checkbox)
        self.file_path_label = QtWidgets.QLabel(self.settings)
        self.file_path_label.setObjectName("file_path_label")

        self.file_path_label.setDisabled(True)

        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.file_path_label)
        self.file_path_input = QtWidgets.QLineEdit(self.settings)
        self.file_path_input.setObjectName("file_path_input")

        self.file_path_input.setText("/var/log/skeyes/")
        self.file_path_input.setDisabled(True)

        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.file_path_input)
        self.tab_widget.addTab(self.settings, "")
        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)
        self.main_window.setCentralWidget(self.centralwidget)
        self.actionSettings = QtWidgets.QAction(self.main_window)
        self.actionSettings.setObjectName("actionSettings")

        self.retranslate_ui(self.main_window)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Skeyes"))
        self.feature_label.setText(_translate("MainWindow", "Feature"))
        self.action_label.setText(_translate("MainWindow", "Action"))
        self.windows_label.setText(_translate("MainWindow", "Windows"))
        self.windows_combo.setCurrentText(_translate("MainWindow", "Pause"))
        self.windows_combo.setItemText(0, _translate("MainWindow", "Pause"))
        self.windows_combo.setItemText(1, _translate("MainWindow", "Ignore"))
        self.gutters_label.setText(_translate("MainWindow", "Gutters"))
        self.gutters_combo.setItemText(0, _translate("MainWindow", "Pause"))
        self.gutters_combo.setItemText(1, _translate("MainWindow", "Ignore"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.actions), _translate("MainWindow", "Actions"))
        self.stream_enable_checkbox.setText(_translate("MainWindow", "Enable Video Stream"))
        self.qgc_label.setText(_translate("MainWindow", "QGroundControl IP:"))
        self.streaming_port_label.setText(_translate("MainWindow", "Streaming Port:"))
        self.file_logging_enable_checkbox.setText(_translate("MainWindow", "Enable File Logging"))
        self.file_path_label.setText(_translate("MainWindow", "File Path:"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

    def show(self):
        self.main_window.show()
