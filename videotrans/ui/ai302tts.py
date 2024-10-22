# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets

from videotrans.util import tools


class Ui_ai302ttsform(object):
    def setupUi(self, ai302ttsform):
        self.has_done = False
        ai302ttsform.setObjectName("ai302ttsform")
        ai302ttsform.setWindowModality(QtCore.Qt.NonModal)
        ai302ttsform.resize(600, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ai302ttsform.sizePolicy().hasHeightForWidth())
        ai302ttsform.setSizePolicy(sizePolicy)
        ai302ttsform.setMaximumSize(QtCore.QSize(600, 450))

        v1 = QtWidgets.QVBoxLayout(ai302ttsform)

        h1 = QtWidgets.QHBoxLayout()
        h2 = QtWidgets.QHBoxLayout()
        h3 = QtWidgets.QHBoxLayout()



        self.label_2 = QtWidgets.QLabel(ai302ttsform)
        self.label_2.setObjectName("label_2")
        self.ai302tts_key = QtWidgets.QLineEdit(ai302ttsform)
        self.ai302tts_key.setMinimumSize(QtCore.QSize(0, 35))
        self.ai302tts_key.setObjectName("ai302tts_key")
        h1.addWidget(self.label_2)
        h1.addWidget(self.ai302tts_key)
        v1.addLayout(h1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        self.label_3 = QtWidgets.QLabel(ai302ttsform)
        self.label_3.setObjectName("label_3")
        self.ai302tts_model = QtWidgets.QComboBox(ai302ttsform)
        self.ai302tts_model.setMinimumSize(QtCore.QSize(0, 35))
        self.ai302tts_model.setObjectName("ai302tts_model")
        self.ai302tts_model.setSizePolicy(sizePolicy)
        h2.addWidget(self.label_3)
        h2.addWidget(self.ai302tts_model)
        v1.addLayout(h2)

        self.label_allmodels = QtWidgets.QLabel(ai302ttsform)
        self.label_allmodels.setObjectName("label_allmodels")
        v1.addWidget(self.label_allmodels)
        self.edit_allmodels = QtWidgets.QPlainTextEdit(ai302ttsform)
        self.edit_allmodels.setObjectName("edit_allmodels")
        self.edit_allmodels.setReadOnly(True)
        v1.addWidget(self.edit_allmodels)

        self.set_ai302tts = QtWidgets.QPushButton(ai302ttsform)
        self.set_ai302tts.setMinimumSize(QtCore.QSize(0, 35))
        self.set_ai302tts.setObjectName("set_ai302tts")

        self.test_ai302tts = QtWidgets.QPushButton(ai302ttsform)
        self.test_ai302tts.setMinimumSize(QtCore.QSize(0, 30))
        self.test_ai302tts.setObjectName("test_ai302tts")

        self.label_0 = QtWidgets.QPushButton(ai302ttsform)
        self.label_0.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_0.setStyleSheet("""text-align:left;background-color:transparent""")
        self.label_0.setText('查看填写教程')
        self.label_0.clicked.connect(lambda: tools.open_url("https://pyvideotrans.com/302ai"))
        h3.addWidget(self.set_ai302tts)
        h3.addWidget(self.test_ai302tts)
        h3.addWidget(self.label_0)
        v1.addLayout(h3)

        self.retranslateUi(ai302ttsform)
        QtCore.QMetaObject.connectSlotsByName(ai302ttsform)

    def retranslateUi(self, ai302ttsform):
        ai302ttsform.setWindowTitle("302.ai 接入配音渠道配置")
        self.label_3.setText('选择模型')
        self.label_allmodels.setText('填写所有可用模型，以英文逗号分隔,填写后可在上方选择,目前仅支持tts-1,tts-1-hd')
        self.set_ai302tts.setText('保存')
        self.test_ai302tts.setText('测试..')
        self.ai302tts_key.setPlaceholderText("在api超市-api管理-创建API KEY")
        self.ai302tts_key.setToolTip("如果没有账号，可去 https://302.ai 注册，有7元免费额度")
        self.label_2.setText("API KEY")
