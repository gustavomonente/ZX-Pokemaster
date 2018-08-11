# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SorterLauncher.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(500, 550))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setBaseSize(QtCore.QSize(0, 0))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pokemaster.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        Dialog.setSizeGripEnabled(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoadSettings = QtWidgets.QPushButton(Dialog)
        self.btnLoadSettings.setObjectName("btnLoadSettings")
        self.horizontalLayout.addWidget(self.btnLoadSettings)
        self.btnSaveSettings = QtWidgets.QPushButton(Dialog)
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.horizontalLayout.addWidget(self.btnSaveSettings)
        spacerItem = QtWidgets.QSpacerItem(158, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSortFiles = QtWidgets.QPushButton(Dialog)
        self.btnSortFiles.setObjectName("btnSortFiles")
        self.horizontalLayout.addWidget(self.btnSortFiles)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabMainOptions = QtWidgets.QWidget()
        self.tabMainOptions.setAccessibleName("")
        self.tabMainOptions.setObjectName("tabMainOptions")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabMainOptions)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tabMainOptions)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnAddPath = QtWidgets.QPushButton(self.groupBox)
        self.btnAddPath.setObjectName("btnAddPath")
        self.gridLayout_2.addWidget(self.btnAddPath, 0, 1, 1, 1)
        self.chkTraverseSubdirectories = QtWidgets.QCheckBox(self.groupBox)
        self.chkTraverseSubdirectories.setChecked(True)
        self.chkTraverseSubdirectories.setObjectName("chkTraverseSubdirectories")
        self.gridLayout_2.addWidget(self.chkTraverseSubdirectories, 3, 0, 1, 1)
        self.lstInputPaths = QtWidgets.QListWidget(self.groupBox)
        self.lstInputPaths.setObjectName("lstInputPaths")
        self.gridLayout_2.addWidget(self.lstInputPaths, 0, 0, 3, 1)
        self.btnRemovePaths = QtWidgets.QPushButton(self.groupBox)
        self.btnRemovePaths.setObjectName("btnRemovePaths")
        self.gridLayout_2.addWidget(self.btnRemovePaths, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tabMainOptions)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.txtOutputPath = QtWidgets.QLineEdit(self.tabMainOptions)
        self.txtOutputPath.setObjectName("txtOutputPath")
        self.horizontalLayout_2.addWidget(self.txtOutputPath)
        self.btnBrowseOutputPath = QtWidgets.QToolButton(self.tabMainOptions)
        self.btnBrowseOutputPath.setObjectName("btnBrowseOutputPath")
        self.horizontalLayout_2.addWidget(self.btnBrowseOutputPath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabMainOptions)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cmbOutputPathStructure = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbOutputPathStructure.setEditable(False)
        self.cmbOutputPathStructure.setCurrentText("")
        self.cmbOutputPathStructure.setObjectName("cmbOutputPathStructure")
        self.gridLayout.addWidget(self.cmbOutputPathStructure, 0, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.btnRemovePattern = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRemovePattern.setObjectName("btnRemovePattern")
        self.gridLayout.addWidget(self.btnRemovePattern, 1, 2, 1, 1)
        self.btnAddPattern = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddPattern.setObjectName("btnAddPattern")
        self.gridLayout.addWidget(self.btnAddPattern, 1, 0, 1, 1)
        self.btnEditPattern = QtWidgets.QPushButton(self.groupBox_2)
        self.btnEditPattern.setObjectName("btnEditPattern")
        self.gridLayout.addWidget(self.btnEditPattern, 1, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chkMaxFilesPerFolder = QtWidgets.QCheckBox(self.tabMainOptions)
        self.chkMaxFilesPerFolder.setObjectName("chkMaxFilesPerFolder")
        self.horizontalLayout_6.addWidget(self.chkMaxFilesPerFolder)
        self.txtMaxFilesPerFolder = QtWidgets.QSpinBox(self.tabMainOptions)
        self.txtMaxFilesPerFolder.setEnabled(False)
        self.txtMaxFilesPerFolder.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtMaxFilesPerFolder.setMaximum(999999999)
        self.txtMaxFilesPerFolder.setProperty("value", 255)
        self.txtMaxFilesPerFolder.setObjectName("txtMaxFilesPerFolder")
        self.horizontalLayout_6.addWidget(self.txtMaxFilesPerFolder)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.chkCamelCase = QtWidgets.QCheckBox(self.tabMainOptions)
        self.chkCamelCase.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.chkCamelCase.setObjectName("chkCamelCase")
        self.verticalLayout_2.addWidget(self.chkCamelCase)
        self.chkShortFilenames = QtWidgets.QCheckBox(self.tabMainOptions)
        self.chkShortFilenames.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.chkShortFilenames.setObjectName("chkShortFilenames")
        self.verticalLayout_2.addWidget(self.chkShortFilenames)
        self.chkPlacePokFilesIntoPOKESSubfolders = QtWidgets.QCheckBox(self.tabMainOptions)
        self.chkPlacePokFilesIntoPOKESSubfolders.setChecked(True)
        self.chkPlacePokFilesIntoPOKESSubfolders.setObjectName("chkPlacePokFilesIntoPOKESSubfolders")
        self.verticalLayout_2.addWidget(self.chkPlacePokFilesIntoPOKESSubfolders)
        self.verticalLayout_2.setStretch(0, 2)
        self.tabWidget.addTab(self.tabMainOptions, "")
        self.tabFileFiltering = QtWidgets.QWidget()
        self.tabFileFiltering.setObjectName("tabFileFiltering")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabFileFiltering)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tabFileFiltering)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txtFormatPreference = QtWidgets.QLineEdit(self.tabFileFiltering)
        self.txtFormatPreference.setInputMask("")
        self.txtFormatPreference.setObjectName("txtFormatPreference")
        self.horizontalLayout_3.addWidget(self.txtFormatPreference)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tabFileFiltering)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.txtLanguages = QtWidgets.QLineEdit(self.tabFileFiltering)
        self.txtLanguages.setInputMask("")
        self.txtLanguages.setObjectName("txtLanguages")
        self.horizontalLayout_4.addWidget(self.txtLanguages)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.tabFileFiltering)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.txtMaxArchiveSize = QtWidgets.QSpinBox(self.tabFileFiltering)
        self.txtMaxArchiveSize.setMinimum(1)
        self.txtMaxArchiveSize.setMaximum(10000)
        self.txtMaxArchiveSize.setObjectName("txtMaxArchiveSize")
        self.horizontalLayout_8.addWidget(self.txtMaxArchiveSize)
        self.label_5 = QtWidgets.QLabel(self.tabFileFiltering)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.chkIncludeAlternate = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeAlternate.setObjectName("chkIncludeAlternate")
        self.verticalLayout.addWidget(self.chkIncludeAlternate)
        self.chkIncludeDemos = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeDemos.setChecked(True)
        self.chkIncludeDemos.setObjectName("chkIncludeDemos")
        self.verticalLayout.addWidget(self.chkIncludeDemos)
        self.chkIncludeRereleases = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeRereleases.setChecked(True)
        self.chkIncludeRereleases.setObjectName("chkIncludeRereleases")
        self.verticalLayout.addWidget(self.chkIncludeRereleases)
        self.chkIncludeAlternateFileFormats = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeAlternateFileFormats.setChecked(True)
        self.chkIncludeAlternateFileFormats.setObjectName("chkIncludeAlternateFileFormats")
        self.verticalLayout.addWidget(self.chkIncludeAlternateFileFormats)
        self.chkIncludeHacked = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeHacked.setChecked(True)
        self.chkIncludeHacked.setObjectName("chkIncludeHacked")
        self.verticalLayout.addWidget(self.chkIncludeHacked)
        self.chkIncludeXRated = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeXRated.setChecked(True)
        self.chkIncludeXRated.setObjectName("chkIncludeXRated")
        self.verticalLayout.addWidget(self.chkIncludeXRated)
        self.chkIncludeSupplementaryFiles = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeSupplementaryFiles.setChecked(True)
        self.chkIncludeSupplementaryFiles.setObjectName("chkIncludeSupplementaryFiles")
        self.verticalLayout.addWidget(self.chkIncludeSupplementaryFiles)
        self.chkIncludeUnknownFiles = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkIncludeUnknownFiles.setChecked(True)
        self.chkIncludeUnknownFiles.setTristate(False)
        self.chkIncludeUnknownFiles.setObjectName("chkIncludeUnknownFiles")
        self.verticalLayout.addWidget(self.chkIncludeUnknownFiles)
        self.chkSeparateUnknownFiles = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkSeparateUnknownFiles.setChecked(True)
        self.chkSeparateUnknownFiles.setTristate(False)
        self.chkSeparateUnknownFiles.setObjectName("chkSeparateUnknownFiles")
        self.verticalLayout.addWidget(self.chkSeparateUnknownFiles)
        self.chkRetainFoldersForUnknownFiles = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkRetainFoldersForUnknownFiles.setChecked(False)
        self.chkRetainFoldersForUnknownFiles.setTristate(False)
        self.chkRetainFoldersForUnknownFiles.setObjectName("chkRetainFoldersForUnknownFiles")
        self.verticalLayout.addWidget(self.chkRetainFoldersForUnknownFiles)
        self.chkDeleteSourceFiles = QtWidgets.QCheckBox(self.tabFileFiltering)
        self.chkDeleteSourceFiles.setChecked(False)
        self.chkDeleteSourceFiles.setTristate(False)
        self.chkDeleteSourceFiles.setObjectName("chkDeleteSourceFiles")
        self.verticalLayout.addWidget(self.chkDeleteSourceFiles)
        self.label_6 = QtWidgets.QLabel(self.tabFileFiltering)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.chkIncludeAlternate.raise_()
        self.chkIncludeDemos.raise_()
        self.chkIncludeAlternateFileFormats.raise_()
        self.chkIncludeHacked.raise_()
        self.chkIncludeRereleases.raise_()
        self.chkIncludeXRated.raise_()
        self.chkIncludeSupplementaryFiles.raise_()
        self.chkIncludeUnknownFiles.raise_()
        self.chkSeparateUnknownFiles.raise_()
        self.chkRetainFoldersForUnknownFiles.raise_()
        self.chkDeleteSourceFiles.raise_()
        self.label_6.raise_()
        self.tabWidget.addTab(self.tabFileFiltering, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.textBrowser = QtWidgets.QTextBrowser(self.tabAbout)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 441, 331))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.btnReadme = QtWidgets.QPushButton(self.tabAbout)
        self.btnReadme.setGeometry(QtCore.QRect(20, 350, 241, 28))
        self.btnReadme.setObjectName("btnReadme")
        self.btnFacebook = QtWidgets.QPushButton(self.tabAbout)
        self.btnFacebook.setGeometry(QtCore.QRect(20, 390, 241, 28))
        self.btnFacebook.setObjectName("btnFacebook")
        self.btnSourceForge = QtWidgets.QPushButton(self.tabAbout)
        self.btnSourceForge.setGeometry(QtCore.QRect(20, 430, 241, 28))
        self.btnSourceForge.setObjectName("btnSourceForge")
        self.tabWidget.addTab(self.tabAbout, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.lstInputPaths)
        Dialog.setTabOrder(self.lstInputPaths, self.btnAddPath)
        Dialog.setTabOrder(self.btnAddPath, self.btnRemovePaths)
        Dialog.setTabOrder(self.btnRemovePaths, self.chkTraverseSubdirectories)
        Dialog.setTabOrder(self.chkTraverseSubdirectories, self.txtOutputPath)
        Dialog.setTabOrder(self.txtOutputPath, self.btnBrowseOutputPath)
        Dialog.setTabOrder(self.btnBrowseOutputPath, self.cmbOutputPathStructure)
        Dialog.setTabOrder(self.cmbOutputPathStructure, self.btnAddPattern)
        Dialog.setTabOrder(self.btnAddPattern, self.btnEditPattern)
        Dialog.setTabOrder(self.btnEditPattern, self.btnRemovePattern)
        Dialog.setTabOrder(self.btnRemovePattern, self.chkMaxFilesPerFolder)
        Dialog.setTabOrder(self.chkMaxFilesPerFolder, self.txtMaxFilesPerFolder)
        Dialog.setTabOrder(self.txtMaxFilesPerFolder, self.chkCamelCase)
        Dialog.setTabOrder(self.chkCamelCase, self.chkShortFilenames)
        Dialog.setTabOrder(self.chkShortFilenames, self.chkPlacePokFilesIntoPOKESSubfolders)
        Dialog.setTabOrder(self.chkPlacePokFilesIntoPOKESSubfolders, self.btnLoadSettings)
        Dialog.setTabOrder(self.btnLoadSettings, self.btnSaveSettings)
        Dialog.setTabOrder(self.btnSaveSettings, self.btnSortFiles)
        Dialog.setTabOrder(self.btnSortFiles, self.txtFormatPreference)
        Dialog.setTabOrder(self.txtFormatPreference, self.txtLanguages)
        Dialog.setTabOrder(self.txtLanguages, self.chkIncludeAlternate)
        Dialog.setTabOrder(self.chkIncludeAlternate, self.chkIncludeDemos)
        Dialog.setTabOrder(self.chkIncludeDemos, self.chkIncludeRereleases)
        Dialog.setTabOrder(self.chkIncludeRereleases, self.chkIncludeAlternateFileFormats)
        Dialog.setTabOrder(self.chkIncludeAlternateFileFormats, self.chkIncludeHacked)
        Dialog.setTabOrder(self.chkIncludeHacked, self.chkIncludeXRated)
        Dialog.setTabOrder(self.chkIncludeXRated, self.chkIncludeSupplementaryFiles)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ZX Pokemaster"))
        self.btnLoadSettings.setText(_translate("Dialog", "Load Settings..."))
        self.btnSaveSettings.setText(_translate("Dialog", "Save Settings..."))
        self.btnSortFiles.setText(_translate("Dialog", "Sort files"))
        self.groupBox.setTitle(_translate("Dialog", "Input paths"))
        self.btnAddPath.setText(_translate("Dialog", "Add path..."))
        self.chkTraverseSubdirectories.setText(_translate("Dialog", "Traverse subdirectories"))
        self.btnRemovePaths.setText(_translate("Dialog", "Remove path"))
        self.label.setText(_translate("Dialog", "Output path:"))
        self.btnBrowseOutputPath.setText(_translate("Dialog", "..."))
        self.groupBox_2.setTitle(_translate("Dialog", "Output path structure pattern"))
        self.btnRemovePattern.setText(_translate("Dialog", "Remove pattern"))
        self.btnAddPattern.setText(_translate("Dialog", "Add pattern..."))
        self.btnEditPattern.setText(_translate("Dialog", "Edit pattern..."))
        self.chkMaxFilesPerFolder.setText(_translate("Dialog", "Max files per folder:"))
        self.chkCamelCase.setText(_translate("Dialog", "CamelCaseInsteadOfSpaces"))
        self.chkShortFilenames.setText(_translate("Dialog", "Use 8.3 naming scheme"))
        self.chkPlacePokFilesIntoPOKESSubfolders.setText(_translate("Dialog", "Place .POK files into POKES subfolders"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMainOptions), _translate("Dialog", "Main options"))
        self.label_2.setText(_translate("Dialog", "Formats preference:"))
        self.txtFormatPreference.setPlaceholderText(_translate("Dialog", "tap,z80,sna,dsk,trd,tzx,img,mgt,rom,scl,slt,szx"))
        self.label_3.setText(_translate("Dialog", "Languages:"))
        self.txtLanguages.setPlaceholderText(_translate("Dialog", "en,es,ru,pl,cz,fr,de,nl,hu,cr,pl,sr,sl,sv,no"))
        self.label_4.setText(_translate("Dialog", "Max archive size to look into:"))
        self.label_5.setText(_translate("Dialog", "MB"))
        self.chkIncludeAlternate.setText(_translate("Dialog", "Include alternate files (marked [a] in TOSEC)"))
        self.chkIncludeDemos.setText(_translate("Dialog", "Include demos (non-full versions of games)"))
        self.chkIncludeRereleases.setText(_translate("Dialog", "Include re-releases"))
        self.chkIncludeAlternateFileFormats.setText(_translate("Dialog", "Include alternate file formats (see formats preference order)"))
        self.chkIncludeHacked.setText(_translate("Dialog", "Include files marked as cracked, hacked or modded"))
        self.chkIncludeXRated.setToolTip(_translate("Dialog", "18+ games: may contain nudity, pornographic images, extremely obscene language or hate speech"))
        self.chkIncludeXRated.setText(_translate("Dialog", "Include x-rated games"))
        self.chkIncludeSupplementaryFiles.setToolTip(_translate("Dialog", "If a ZX Spectrum file has got other files with the same name in the same folder or in a subfolder, include those as well. May be handy tor maps, manuals etc."))
        self.chkIncludeSupplementaryFiles.setText(_translate("Dialog", "Include supplementary files (Warning: may be slow!)"))
        self.chkIncludeUnknownFiles.setText(_translate("Dialog", "Include unknown files"))
        self.chkSeparateUnknownFiles.setText(_translate("Dialog", "Put unknown files into \"Unknown\" folder"))
        self.chkRetainFoldersForUnknownFiles.setText(_translate("Dialog", "Retain relative folder structure for unknown files"))
        self.chkDeleteSourceFiles.setText(_translate("Dialog", "Delete source files after sorting (USE AT YOUR OWN RISK!)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFileFiltering), _translate("Dialog", "File filtering"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Brought to you by Helga Iliashenko aka Lady Eklipse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">with the sencere feelings to the ZX Spectrum community.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">For those willing to support ZX Pokemaster, please consider donating:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">BitCoin: </span><a href=\"bitcoin:1KLBSzFYBpmwwkiG9VhXV6Hfd6YVsnF9D9\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">1KLBSzFYBpmwwkiG9VhXV6Hfd6YVsnF9D9</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">LiteCoin: </span><a href=\"litecoin:LPuLp1dfdZXVdcFdL3ahQCaQwmghxkFuJh\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">LPuLp1dfdZXVdcFdL3ahQCaQwmghxkFuJh</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Etherium: 0xF60Dc0c3d32b12Ae02A68723Af9133AD1938a178</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Special thanks to:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Anna Soloviova for Facebook group logo and moral support;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Gerard Sweeney for </span><a href=\"http://www.the-tipshop.co.uk\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">www.the-tipshop.co.uk</span></a><span style=\" font-size:8pt;\">;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Einar Saukas for ZXDB;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Peter Jones for </span><a href=\"https://spectrumcomputing.co.uk\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">spectrumcomputing.co.uk</span></a><span style=\" font-size:8pt;\">;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">D. Kampschulte aka Der Eratosthenes for beta testing;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">blinkydoos for beta testing;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The </span><a href=\"https://www.tosecdev.org\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">TOSEC</span></a><span style=\" font-size:8pt;\"> team, especially:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">gorski, maddog, dziuber, duncantwain, mictlantecuhtle, panda and others.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.btnReadme.setText(_translate("Dialog", "View README"))
        self.btnFacebook.setText(_translate("Dialog", "Visit Facebook tech support group"))
        self.btnSourceForge.setText(_translate("Dialog", "Check for new version on SourceForge"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("Dialog", "Help"))

import res_rc
