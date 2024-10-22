# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets

from videotrans.configure import config
from videotrans.util import tools


class Ui_zijiehuoshanform(object):
    def setupUi(self, zijiehuoshanform):
        self.has_done = False
        zijiehuoshanform.setObjectName("zijiehuoshanform")
        zijiehuoshanform.setWindowModality(QtCore.Qt.NonModal)
        zijiehuoshanform.resize(600, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(zijiehuoshanform.sizePolicy().hasHeightForWidth())
        zijiehuoshanform.setSizePolicy(sizePolicy)
        zijiehuoshanform.setMaximumSize(QtCore.QSize(600, 570))

        v1=QtWidgets.QVBoxLayout(zijiehuoshanform)
        h1=QtWidgets.QHBoxLayout()
        h2=QtWidgets.QHBoxLayout()
        h3=QtWidgets.QHBoxLayout()
        h4=QtWidgets.QHBoxLayout()


        self.label_2 = QtWidgets.QLabel(zijiehuoshanform)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.zijiehuoshan_key = QtWidgets.QLineEdit(zijiehuoshanform)
        self.zijiehuoshan_key.setMinimumSize(QtCore.QSize(0, 35))
        self.zijiehuoshan_key.setObjectName("zijiehuoshan_key")
        h1.addWidget(self.label_2)
        h1.addWidget(self.zijiehuoshan_key)
        v1.addLayout(h1)

        self.label_3 = QtWidgets.QLabel(zijiehuoshanform)
        self.label_3.setObjectName("label_3")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.zijiehuoshan_model = QtWidgets.QComboBox(zijiehuoshanform)
        self.zijiehuoshan_model.setMinimumSize(QtCore.QSize(0, 35))
        self.zijiehuoshan_model.setObjectName("zijiehuoshan_model")
        self.zijiehuoshan_model.setSizePolicy(sizePolicy)
        h2.addWidget(self.label_3)
        h2.addWidget(self.zijiehuoshan_model)
        v1.addLayout(h2)

        self.label_allmodels = QtWidgets.QLabel(zijiehuoshanform)
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText('填写所有推理接入点，填写后可在上方选择')
        v1.addWidget(self.label_allmodels)

        self.edit_allmodels = QtWidgets.QPlainTextEdit(zijiehuoshanform)
        self.edit_allmodels.setObjectName("edit_allmodels")
        v1.addWidget(self.edit_allmodels)

        self.label_4 = QtWidgets.QLabel(zijiehuoshanform)
        self.label_4.setGeometry(QtCore.QRect(10, 285, 571, 21))
        self.label_4.setObjectName("label_4")
        v1.addWidget(self.label_4)

        self.zijiehuoshan_template = QtWidgets.QPlainTextEdit(zijiehuoshanform)
        self.zijiehuoshan_template.setGeometry(QtCore.QRect(10, 310, 571, 151))
        self.zijiehuoshan_template.setObjectName("zijiehuoshan_template")
        v1.addWidget(self.zijiehuoshan_template)


        self.set_zijiehuoshan = QtWidgets.QPushButton(zijiehuoshanform)
        self.set_zijiehuoshan.setMinimumSize(QtCore.QSize(0, 35))
        self.set_zijiehuoshan.setObjectName("set_zijiehuoshan")

        self.test_zijiehuoshan = QtWidgets.QPushButton(zijiehuoshanform)
        self.test_zijiehuoshan.setMinimumSize(QtCore.QSize(0, 30))
        self.test_zijiehuoshan.setObjectName("test_zijiehuoshan")

        self.label_0 = QtWidgets.QPushButton(zijiehuoshanform)
        self.label_0.setText('点击打开使用教程')
        self.label_0.setStyleSheet("background-color: rgba(255, 255, 255,0);text-align:left")
        self.label_0.clicked.connect(lambda: tools.open_url('https://pyvideotrans.com/zijiehuoshan'))
        self.label_0.setCursor(QtCore.Qt.PointingHandCursor)
        h3.addWidget(self.set_zijiehuoshan)
        h3.addWidget(self.test_zijiehuoshan)
        h3.addWidget(self.label_0)
        v1.addLayout(h3)

        self.retranslateUi(zijiehuoshanform)
        QtCore.QMetaObject.connectSlotsByName(zijiehuoshanform)

    def retranslateUi(self, zijiehuoshanform):
        zijiehuoshanform.setWindowTitle("字节火山引擎接入翻译" if config.defaulelang == 'zh' else 'ByteDance Ark')
        self.label_3.setText('选择推理接入点')
        self.zijiehuoshan_template.setPlaceholderText("prompt")
        self.label_4.setText("{lang}代表目标语言名称，不要删除。")
        self.set_zijiehuoshan.setText('保存')
        self.test_zijiehuoshan.setText('测试..')
        self.zijiehuoshan_key.setPlaceholderText("填写API key")
        self.label_2.setText("API key")
