import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import socket
import winrm
import os
import pandas
import ui

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        global EWMain, err
        EWMain = loadUi('./UI/maintitle.ui', self)
        err = loadUi('./UI/err.ui')
        main.con()
    def con():
        f = open(r'.\iplocal.txt','r')
        server_host = f.readlines()[0]
        server_username = f.readlines()[1]
        server_userpassword = f.readlines()[2]
        server_pathp = r'C:\Users\\'
        server_usernamel = r'\\Desktop'
        server_path =server_pathp + server_username + server_usernamel
        
        try:
            s = winrm.Session(server_host, auth=(server_username, server_userpassword), transport='ntlm')  # 远程连接windows
            shell1 = 'cd' + server_path + r'\Exuberant Witness'
            shell2 = 'Exuberant_Witness.py'
            r = s.run_ps(shell1)  # 执行脚本
            if r.status_code == 0:
                r = s.run_ps(shell2)
                err.close()
            #print('已启动服务器')
                return 1
        except Exception:
            err.show()
            return 0
        #global DPStrategy
        #DPStrategy = pandas.DataFrame(columns={"name":"","path":""},index=[0])
        
        #for root, dirs, files in os.walk(server_host +"\\" + server_path + '\\Exuberant Witness' + '\\DeployStrategy'):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
            #for f in files:
                #DS = os.path.join(root, f)
                #DSName = str(f)
                #EWMain.comboBox.additem(DSName)
                #DPStrategy.loc[0]=[DSName, DS]
                
            # 遍历所有的文件夹
            #for d in dirs:
                #print(os.path.join(root, d))
    def order(strwait):
        global s
        s = socket.socket()
        acf = open(r'.\iplocal','r')
        host = acf.readlines()[0]
        port = 8000
        #print(acf.readlines[0])
        s.connect((host, port))
        info = bytes(strwait, encoding='UTF-8')
        s.send(info)

        #DSname = EWMain.comboBox.currentText()
        #DS = DPStrategy.loc[DPStrategy['Name']==DSname,'path']
        #s.send(DS)
        #print(s.recv(1024).decode('UTF-8'))
    def closecon():
        s.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    EWMain.pushButton.clicked.connect(main.order('00100'))
    #EWMain.pushButton.clicked.connect(main.sendserver('79523'))
    #EWMain.pushButton.clicked.connect(main.sendserver('7355608'))
    err.pushButton.clicked.connect(main.con())
    main = main()
    sys.exit(app.exec_())

