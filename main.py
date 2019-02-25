# coding=utf-8
from cmd import Cmd
from code.add_shell import *
count = 0
class YmlConsole(Cmd):
    prompt = "yml-> "
    Object = None
    def __init__(self):
        Cmd.__init__(self)
    def preloop(self):
        string = """
        *          .,:,,,                                        .::,,,::.          
 *        .::::,,;;,                                  .,;;:,,....:i:         
 *        :i,.::::,;i:.      ....,,:::::::::,....   .;i:,.  ......;i.        
 *        :;..:::;::::i;,,:::;:,,,,,,,,,,..,.,,:::iri:. .,:irsr:,.;i.        
 *        ;;..,::::;;;;ri,,,.                    ..,,:;s1s1ssrr;,.;r,        
 *        :;. ,::;ii;:,     . ...................     .;iirri;;;,,;i,        
 *        ,i. .;ri:.   ... ............................  .,,:;:,,,;i:        
 *        :s,.;r:... ....................................... .::;::s;        
 *        ,1r::. .............,,,.,,:,,........................,;iir;        
 *        ,s;...........     ..::.,;:,,.          ...............,;1s        
 *       :i,..,.              .,:,,::,.          .......... .......;1,       
 *      ir,....:rrssr;:,       ,,.,::.     .r5S9989398G95hr;. ....,.:s,      
 *     ;r,..,s9855513XHAG3i   .,,,,,,,.  ,S931,.,,.;s;s&BHHA8s.,..,..:r:     
 *    :r;..rGGh,  :SAG;;G@BS:.,,,,,,,,,.r83:      hHH1sXMBHHHM3..,,,,.ir.    
 *   ,si,.1GS,   sBMAAX&MBMB5,,,,,,:,,.:&8       3@HXHBMBHBBH#X,.,,,,,,rr    
 *   ;1:,,SH:   .A@&&B#&8H#BS,,,,,,,,,.,5XS,     3@MHABM&59M#As..,,,,:,is,   
 *  .rr,,,;9&1   hBHHBB&8AMGr,,,,,,,,,,,:h&&9s;   r9&BMHBHMB9:  . .,,,,;ri.  
 *  :1:....:5&XSi;r8BMBHHA9r:,......,,,,:ii19GG88899XHHH&GSr.      ...,:rs.  
 *  ;s.     .:sS8G8GG889hi.        ....,,:;:,.:irssrriii:,.        ...,,i1,  
 *  ;1,         ..,....,,isssi;,        .,,.                      ....,.i1,  
 *  ;h:               i9HHBMBBHAX9:         .                     ...,,,rs,  
 *  ,1i..            :A#MBBBBMHB##s                             ....,,,;si.  
 *  .r1,..        ,..;3BMBBBHBB#Bh.     ..                    ....,,,,,i1;   
 *   :h;..       .,..;,1XBMMMMBXs,.,, .. :: ,.               ....,,,,,,ss.   
 *    ih: ..    .;;;, ;;:s58A3i,..    ,. ,.:,,.             ...,,,,,:,s1,    
 *    .s1,....   .,;sh,  ,iSAXs;.    ,.  ,,.i85            ...,,,,,,:i1;     
 *     .rh: ...     rXG9XBBM#M#MHAX3hss13&&HHXr         .....,,,,,,,ih;      
 *      .s5: .....    i598X&&A&AAAAAA&XG851r:       ........,,,,:,,sh;       
 *      . ihr, ...  .         ..                    ........,,,,,;11:.       
 *         ,s1i. ...  ..,,,..,,,.,,.,,.,..       ........,,.,,.;s5i.         
 *          .:s1r,......................       ..............;shs,           
 *          . .:shr:.  ....                 ..............,ishs.             
 *              .,issr;,... ...........................,is1s;.               
 *                 .,is1si;:,....................,:;ir1sr;,                  
 *                    ..:isssssrrii;::::::;;iirsssssr;:..                    
 *                         .,::iiirsssssssssrri;;:.                                              
           """
        self.commandHelp = """
        Command Tips
        =============

        Command          Tips
        -------       -----------
        addip         添加shell ip和端口
        addshell      添加shell路径
        saveshell     保存shell到文件
        showip        查看ip列表
        removeip      移除某个ip
        clearip       清除ip列表
        saveip        将ip保存到文件
        updead        上传bash不死马文件(.crons.php)
        loadip        加载储存的IP列表
        loadwebshell  加载储存的shell列表
        liuliang      进行流量混淆(请先添加ip或loadip)
        addflagshell  添加获取flag的shell
        saveflagshell 将获取flag的shell储存到文件
        loadflagshell 加载储存的flagshell列表
        getflag       获取flag(demo: getflag-cat /flag  注意分隔符是"-")
        exit          退出
                        """
        print(string)
        print(self.commandHelp)
    def help_addip(self):#添加shell的ip地址和端口
        print("例如输入:addip 10.10.11-22.10 80-90")
        print("addip [ip段] [端口段]")
    def do_addip(self,argv):
        global count
        ip = argv.split(' ')
        if len(ip)!=2:
            print("输入有误!!!")
            self.help_addip()
        else:
            #print("success")
            ip_list(ip[0])
            get_port(ip[1])
            print("ip and port add ok!!!")
        count = 1
    def help_addshell(self,argv):
        print("/shell.php pass(shell路径 密码) post/get")
    def do_addshell(self,argv):
        if count!=0:
            shell = argv.split(' ')
            if len(shell)!=3:
                print("shell环境输入错误")
                print("/shell.php pass(shell路径 密码) post/get")
            else:
                add_shell(shell[0],shell[1],shell[2])
                print(shell[0])
                print(shell[1])
                print(shell[2])
                print("add shell ok!!!")
                print("若想保存请输入:saveshell")
                print(webshell)
        else:
            print("请先设置ip和端口")
    def do_showip(self,argv):#查看ip
            print_ip()
    def do_removeip(self,argv):
        delip = argv.split(' ')
        if ipList == []:
            print("您还没有添加ip")
        else:
            count = remove_ip(delip[0])
            if count == 1:
                print("删除成功")
            else:
                print("删除失败，ip不存在")
    def do_clearip(self,argv):
        clear_ip()
        print("IP列表已清空")
    def do_saveshell(self,argv):
        save_shell()
        print("saveshell ok!!!")
    def do_updead(self,argv):
        undead_shell()
    def do_saveip(self,argv):
        save_ip()
        print("保存成功")
    def do_loadip(self,argv):
        global count
        load_ip()
        count=1
        print("成功加载ip列表")
    def do_loadwebshell(self,argv):
        load_webshell()
        print("成功加载webshell列表")
    def do_loadflagshell(self,argv):
        load_flagshell()
        print("load flagshell ok")
    def do_liuliang(self,argv):
        print("获取攻击地址:")
        attack_ll()
        ll_hunxiao()
        print("开始发送:")
        send_ll()
    def do_addflagshell(self,argv):
        if count!=0:
            shell = argv.split(' ')
            if len(shell)!=3:
                print("flagshell环境输入错误")
                print("/shell.php pass(shell路径 密码) post/get")
            else:
                add_flag_shell(shell[0],shell[1],shell[2])
                #print(shell[0])
                #print(shell[1])
                #print(shell[2])
                print("add shell ok!!!")
                print("若想保存请输入:saveflagshell")
                print(webshell)
        else:
            print("请先设置ip和端口")
    def do_saveflagshell(self,argv):
        save_flag_shell()
        print("成功保存flagshell到文件")
    def do_getflag(self,argv):
        cmd = argv.split('-')
        if len(cmd) != 2:
            print("请输入获取flag的命令")
        else:
            get_flag(cmd[1])
    def do_exit(self, argv):
        print("Bye Bye!!!!")
        return True

    def Error(self, info):
        print(info)
        return
if __name__ == '__main__':
    yml = YmlConsole()
    yml.cmdloop()