import os
import sys
import time
from time import sleep
import socket
import random
import os.path
os.chdir("tools")

men = """\033[38;2;88;159;240m[###]      The Skid ToolKit (\x1b[1;33mSkidKit\033[38;2;88;159;240m)       [###]
\033[38;2;88;159;240m[###]      Created by KrisIsHere            [###]
\033[38;2;88;159;240m[###]      Version: \x1b[1;33m1.2.2\033[38;2;88;159;240m                   [###]
\033[38;2;88;159;240m[###]      Codename: \x1b[1;33mBender\033[38;2;88;159;240m                 [###]

\033[38;2;88;159;240m[###]      Discord: \033[38;2;0;255;152m@\033[38;2;255;0;211mKrisIsHere#9531\033[38;2;88;159;240m        [###]
\033[38;2;88;159;240m[###]      Follow me on Github: \033[38;2;0;255;152m@\033[38;2;255;0;211mKrisIsHere\033[38;2;88;159;240m [###]
\033[38;2;88;159;240m[###]      Shoutout to: \033[38;2;0;255;152m@\033[38;2;255;0;211mKrisIsHere\033[38;2;88;159;240m         [###]\n"""

try:
    import bane
except:
    xdd = input("You need to install bane\n Would you like to do it automatically? (Y/N) ")
    if xdd == "y":
        os.system("pip3 install bane")
    elif xdd == "Y":
        os.system("pip3 install bane")
    else:
        sys.exit()

try:
    from scapy.all import *
except:
    xdd = input("You need to install scapy\n Would you like to do it automatically? (Y/N) ")
    if xdd == "y":
        os.system("sudo apt install scapy")
    elif xdd == "Y":
        os.system("sudo apt install scapy")
    else:
        sys.exit()

os.system("clear")
ascii = ["""\x1b[1;33m
   _____ _    _     _ _  ___ _
  / ____| |  (_)   | | |/ (_) |
 | (___ | | ___  __| | ' / _| |_
  \___ \| |/ / |/ _` |  < | | __|
  ____) |   <| | (_| | . \| | |_
 |_____/|_|\_\_|\__,_|_|\_\_|\__|\033[0;37m
""", """\x1b[1;31m
███████ ██   ██ ██ ██████  ██   ██ ██ ████████ 
██      ██  ██  ██ ██   ██ ██  ██  ██    ██    
███████ █████   ██ ██   ██ █████   ██    ██ 
     ██ ██  ██  ██ ██   ██ ██  ██  ██    ██ 
███████ ██   ██ ██ ██████  ██   ██ ██    ██ 
\033[0;37m""", """
\x1b[1;32m.▄▄ · ▄ •▄ ▪  ·▄▄▄▄  ▄ •▄ ▪  ▄▄▄▄▄
▐█ ▀. █▌▄▌▪██ ██▪ ██ █▌▄▌▪██ •██
▄▀▀▀█▄▐▀▀▄·▐█·▐█· ▐█▌▐▀▀▄·▐█· ▐█.▪
▐█▄▪▐█▐█.█▌▐█▌██. ██ ▐█.█▌▐█▌ ▐█▌·
 ▀▀▀▀ ·▀  ▀▀▀▀▀▀▀▀▀• ·▀  ▀▀▀▀ ▀▀▀ \033[0;37m
""", """\033[0;33m
 @@@@@@   @@@  @@@  @@@  @@@@@@@   @@@  @@@  @@@  @@@@@@@
@@@@@@@   @@@  @@@  @@@  @@@@@@@@  @@@  @@@  @@@  @@@@@@@
!@@       @@!  !@@  @@!  @@!  @@@  @@!  !@@  @@!    @@!
!@!       !@!  @!!  !@!  !@!  @!@  !@!  @!!  !@!    !@!
!!@@!!    @!@@!@!   !!@  @!@  !@!  @!@@!@!   !!@    @!!
 !!@!!!   !!@!!!    !!!  !@!  !!!  !!@!!!    !!!    !!!
     !:!  !!: :!!   !!:  !!:  !!!  !!: :!!   !!:    !!:
    !:!   :!:  !:!  :!:  :!:  !:!  :!:  !:!  :!:    :!:
:::: ::    ::  :::   ::   :::: ::   ::  :::   ::     ::
:: : :     :   :::  :    :: :  :    :   :::  :       :
                                                            \033[0;37m
""", """\033[92m   .         . . ... .,~?I777?=,. . ... . .
             .... :+ZO$I?I??I$OOI~.  .  .
          . ..  :7OI~....  .. .~IOZ+. .. .
          ... ,7O+..   .......  ..=O$: .
          ... ,7O+..   .......  ..=O$: .
       ...  .~OI    ......   ....  .?D= . ...
       .....+O~ ....      .     ..   :87......
       ... ?O... .. ... .... ...  ...  O$.....
      ...+O....... ..,,,,:,,,.. .. ....O7.....
   .  .  ~O,  .+...,,,,,,,,,,,,,, ..=, . 8? .. ..
     . ..Z~..=NI..,, ...,.,. ,: ,:. +M?..:8~ .   .
  . ..  I7.=?MZ..:,,..., .. , .,.,,..7MI? IZ.. . .
  . .. :O IZ88, ,...:,.,,=I~.,,:,. :..ZN$$ O+ ...
   ... 7+.D$7I:,, .,..,,?$7D., .,...,,II$N,=O . .
   .  ,Z:ID=OZ.,. ...., ,:$7 ,..,,  ,,I8~87:O~.  .
  . . +II$88Z,.,..,.. ,. ,+ ...  :.,.,.$D8$7?$....
  . . $~O7NZ=.,  ,,,.,:,.::..:,,:,,....~7M78:8  .
    ..$,D$?O?.,  ., .,,:.7O ,,,..... ..+OI7N.O~. .
  .. :$ D7$N., ..,.. ., .::. ..  .,..., 88?M.7? ..
  . .=7=8NM~.,   . . ,,. .. .., ..,. .,.:DN8+7I..
   . .=7=8NM~.,   . . ,,. .. .., ..,. .,.:DN8+7I..
  .. ??O7$$7 ,,..,, .,+D.+7.OI...,:,....?$$I8?$ ..
  . .?+$8=M+.,.  , ?$DMO.=? 7M8I+,,. ., :M+$8+$. .
   . ??~MIM. , ...~MMMMO ~? $MMMMZ.   ..,D7N++Z  .
     =7:8MZ?.,. . ?MMMM8 ?8 ZMMMMD, ..,.=$NN~II .
   . ~$I+MIO:...  ZMMMMM.ID NMMMMN,. .,.O?M?IZ+ .
  . ..7$$I7D~.,..,OMMMMM=ID=MMMMMM:..,.,N7I7$Z~ ..
   . .7+M$=M+ ,,. NMMMMMOZNZMMMMMM~.., =M?IM?O...
  . . ???M7D$+ , ~MMMMMMMNMMMMMMMM? ,.=7NIM$?$ ..
   .  .,Z:OMM7O:..+MMMMMMMMMMMMMMMM?.,.OIMM8:Z= .
    .. .7?7IN$O7 .?MMMMMMMMMMMMMMMM$. ?87MIIIZ....
   . .. ,$IN7+IN:.IMMMMMMMMMMMMMMMM$.,D$+7D7$+ . ..
   .  ...7?7MD?N7?7MMMMMMMMMMMMMMMMZ?7N?OMZ+O.. .
   . . . .O:+NMNNZNMMMMMMMMMMMMMMMMMZ8MNNI,D~ . . .
    .  .. ~Z:7IIZ+$MMMMMMMMMMMMMMMMZ=OI?$:O?. . . .
    . . .. ?Z+D8OZZMMMMMMMMMMMMMMMMZOZON+7$, ..  .
    . .  . .?$,$8OZ?+NMMMMMMMMMMO+?ZZ8$,7Z. ...  .
   .   ..  ..+O,+?+$NMMMMMMMMMMMMNZ?+?:Z$  ..    .
     . ..  . .~8I78NDMMMMMMMMMMMDOMD$ID+ .. .  .
     .   .. ,. ,7$= =MMMMMMMMMMMO .~$O:.... ....
   . ... .  . . .:$ZOMMMMMMMMMMMD?OO+ .. . .    . .
   . . . .O:+NMNNZNMMMMMMMMMMMMMMMMMZ8MNNI,D~ . . .
   . .. . ..   .. .:IZNMMMMMMMMNO$~.. .. .  . .. .. \033[0;37m
   """, """\033[92m             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  \x1b[1;31mSkidKit\033[92m!       |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_\x1b[1;31mKrisIsHere\033[92m|  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,\033[0;37m
""", """\033[92m                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~\033[0;37m
""", """\x1b[1;33m                             o
                    o       /
                     \     /
                      \   /
                       \ /
         +--------------v-------------+
         !  __________________      @ !
         ! /           ,  ooo  \      !
         ! !  ---=====!#O#### !  (\)  !
         ! !          `  \ )  !       !
         ! !   ,;`,      ! !  !  (-)  !
         ! !  // o ',    ! !  !       !
         ! \  ' o \ /,   ! !  / :!!!: !
         !  -ooo--------------  :!!!: !
         +----------------------------+
         []                    []\033[0;37m\n""", """\x1b[1;31m              ----
            -===,=--
          --,-,,,,,,-
        :-;==:========:
      :=---------------::
     :-------------------::
    :----------------------:
   :------------------------:
  :--------------------------:
 :----------=:::==::::-------:
 :------:====--,,,,--====:=---:
:----:===,=++++...++++..--===::
:-===--...+    +.+    +.....,-=/
/==-.....+      +      +......./
;-......+     - / -     +....../
/.......+    -# . #-    +....../
/.......+       +       +....../
/.......+      +.+      +....../
/........+    +...+    +......./
/.........++++.....++++......./
 /..........................-./
 /.-.......................-./
  /.-......M##M$HM###M....-../
   /.-......########$....-../
    /.--......$$$$+-....-.-/
     /..--.....,,,,...--.//
      //..----.....---.//
        ///-..-----.-//
           //////////\033[0;37m\n""", """\x1b[1;31m
     _                      _______                      _
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'
          \033[0;37m""", """\x1b[1;33m
 _________        .------______-------.
:______.-':      :  .--------------.  :
| ______  |      | :                : |
|:______B:|      | |  Little Error: | |
|:______B:|      | |                | |
|:______B:|      | |  OS not        | |
|         |      | |  found.        | |
|:_____:  |      | |                | |
|    ==   |      | :                : |
|       O |      :  '--------------'  :
|       o |      :'---...______...---'
|       o |-._.-i___/'             \._
|'-.____o_|   '-.   '-...______...-'  `-._
:_________:      `.____________________   `-.___.-.
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.
              :____________________________:\033[0;37m\n""", """\033[92m            .       .                   .       .      .     .      .
          .    .         .    .            .     ______
      .           .             .               ////////
                .    .   ________   .  .      /////////     .    .
           .            |.____.  /\        ./////////    .
    .                 .//      \/  |\     /////////
       .       .    .//          \ |  \ /////////       .     .   .
                    ||.    .    .| |  ///////// .     .
     .    .         ||           | |//`,/////                .
             .       \\        ./ //  /  \/   .
  .                    \\.___./ //\` '   ,_\     .     .
          .           .     \ //////\ , /   \                 .    .
                       .    ///////// \|  '  |    .
      .        .          ///////// .   \ _ /          .
                        /////////                              .
                 .   ./////////     .     .
         .           --------   .                  ..             .
  .               .        .         .                       .
                        ________________________
____________------------                        -------------_________\n\033[0;37m""", """\x1b[1;31m XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
\033[0;37m"""]

'''
         ,
       _=|_
     _[_## ]_
_  +[_[_+_]P/    _    |_       ____      _=--|-~
 ~---\_I_I_[=\--~ ~~--[o]--==-|##==]-=-~~  o]H
-~ /[_[_|_]_]\\  -_  [[=]]    |====]  __  !j]H
  /    "|"    \      ^U-U^  - |    - ~ .~  U/~
 ~~--__~~~--__~~-__   H_H_    |_     --   _H_
-. _  ~~~#######~~~     ~~~-    ~~--  ._ - ~~-=
           ~~~=~~  -~~--  _     . -      _ _ -

       ----------------------------------
      |        June, 20th, 1969          |
      |  Here Men from the Planet Earth  |
      |   First set Foot upon the Moon   |
      | We came in Peace for all Mankind |
       ----------------------------------

'''


def update2():
    os.system("mkdir .notgithubtools")
    os.system("cp -r DoS/fasthttp.py .notgithubtools")
    os.system("cp -r DoS/PyDDOS.py .notgithubtools")
    os.system("cp -r DoS/tcp.py .notgithubtools")
    os.system("cp -r Doxxing/ip.py .notgithubtools")
    os.system("cp -r Other/cloudcheck.py .notgithubtools")
    os.system("cp -r Other/pscan.py .notgithubtools")
    os.system("cp -r Other/dir.py .notgithubtools")
    os.system("cp -r Other/directory-list-big.txt .notgithubtools")
    os.system("cp -r Other/siteip.py .notgithubtools")
    os.system("cp -r Other/sniff.py .notgithubtools")
    os.system("rm -rf Other Phising Doxxing DoS")
    os.system("mkdir Doxxing Other Phising DoS")
    os.system("cp -r .notgithubtools/cloudcheck.py Other")
    os.system("cp -r .notgithubtools/sniff.py Other")
    os.system("cp -r .notgithubtools/dir.py Other")
    os.system("cp -r .notgithubtools/directory-list-big.txt Other")
    os.system("cp -r .notgithubtools/siteip.py Other")
    os.system("cp -r .notgithubtools/fasthttp.py DoS")
    os.system("cp -r .notgithubtools/PyDDOS.py DoS")
    os.system("cp -r .notgithubtools/tcp.py DoS")
    os.system("cp -r .notgithubtools/ip.py Doxxing")
    os.system("cp -r .notgithubtools/pscan.py Other")
    os.chdir("DoS")
    os.system("git clone https://github.com/Karlheinzniebuhr/torshammer ; git clone https://github.com/JackzGamez/Saphyra.py ; git clone https://github.com/KrisIsHere/BDoS ; ")
    os.chdir("..")
    os.chdir("Phising")
    os.system("git clone https://github.com/htr-tech/zphisher ; git clone https://github.com/An0nUD4Y/blackeye ")
    os.chdir("..")
    os.chdir("Doxxing")
    os.system("git clone https://github.com/hangetzzu/saycheese")
    os.chdir("..")
    os.system("touch .info/tools.py")


def update():
        os.system("rm -rf .info/tools.py")
        os.chdir('..')
        path = os.getcwd()
        parent = os.path.abspath(os.path.join(path, os.pardir))
        os.system("cp -r tools/.info " + parent)
        os.system("cp -r tools/update.py " + parent)
        os.system("python3 " + parent + "/update.py")
        sys.exit()

def other():
        os.system("clear")
        print(random.choice(ascii))

        print(men)

        print("""Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) CloudFlare checker
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) Port Scanner
        \033[38;2;0;255;152m3\033[38;2;88;159;240m) HTTPSniff
        \033[38;2;0;255;152m4\033[38;2;88;159;240m) Vuln. Scan
        \033[38;2;0;255;152m5\033[38;2;88;159;240m) Site IP Finder
        \033[38;2;0;255;152m6\033[38;2;88;159;240m) Site Dir. Scanner

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
        try:
            menu1 = input("""\x1b[1;33mSkidKitOther\033[38;2;88;159;240m: """)
            if menu1 == "1":
                xd = input("Site: ")
                os.system("python2 Other/cloudcheck.py " + xd)
            if menu1 == "2":
                ho = input("Host: ")
                os.system("python2 Other/pscan.py -m 1 -M 99999 " + ho)
            if menu1 == "3":
                os.system("python2 Other/sniff.py")
            if menu1 == "4":
                url = input("Enter target URL: ")
                print("Doing XSS scan :")
                bane.xss(url)
                print("Doing RCE scan :")
                bane.rce(url)
            if menu1 == "5":
                os.system("python3 Other/siteip.py")
            if menu1 == "6":
                url = input("Site (https://example.com): ")
                word = input("Wordlist (1 for default): ")
                if word == "1":
                    word = "Other/directory-list-big.txt"
                os.system("python3 Other/dir.py " + url + " " + word)
            if menu1 == "0":
                menu()
        except:
            menu()

def dox():
        os.system("clear")
        print(random.choice(ascii))

        print(men)

        print("""Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) IP Tracker
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) SayCheese

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
        try:
            menu1 = input("""\x1b[1;33mSkidKitDox\033[38;2;88;159;240m: """)
            if menu1 == "1":
                os.system("python2 Doxxing/ip.py")
            if menu1 == "2":
                os.chdir("dox/saycheese")
                os.system("bash Doxxing/saycheese/saycheese.sh")
                os.chdir("..")
                os.chdir("..")
            if menu1 == "0":
                menu()
        except:
            menu()

def phish():
    os.system("clear")
    print(random.choice(ascii))

    print(men)

    print("""Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) Zphisher
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) BlackEye

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
    try:
        menu1 = input("""\x1b[1;33mSkidKitPhish\033[38;2;88;159;240m: """)
        if menu1 == "1":
            os.chdir("Phising/zphisher")
            os.system("bash zphisher.sh")
            os.chdir("..")
            os.chdir("..")
        if menu1 == "2":
            os.chdir("Phising/blackeye")
            os.system("bash blackeye.sh")
            os.chdir("..")
            os.chdir("..")
        if menu1 == "0":
            menu()
    except:
        menu()

def dos():
    os.system("clear")
    print(random.choice(ascii))

    print(men)

    print("""Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) Torshammer
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) Saphyra
        \033[38;2;0;255;152m3\033[38;2;88;159;240m) BDoS
        \033[38;2;0;255;152m4\033[38;2;88;159;240m) FastHTTP
        \033[38;2;0;255;152m5\033[38;2;88;159;240m) UDP Flood
        \033[38;2;0;255;152m6\033[38;2;88;159;240m) IP Pinger
        \033[38;2;0;255;152m7\033[38;2;88;159;240m) TCP Pinger

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
    try:
        menu1 = input("""\x1b[1;33mSkidKitDoS\033[38;2;88;159;240m: """)
        if menu1 == "1":
        		targ = input("Target (www.example.com): ")
        		tar = input("Threads: ")
        		port = input("Port: ")
        		os.system("python2 DoS/torshammer/torshammer.py -t " + targ + " -r " + tar + " -p " + port)
        if menu1 == "3":
        		targ = input("Target (www.example.com): ")
        		tar = input("Threads: ")
        		connections = input("Amount of connections per thread: ")
        		port = input("Port: ")
        		os.system("python2 DoS/BDoS/BDoS/BDoS_en.py " + targ + " -t " + tar + " -c " + connections + " -p " + port)
        if menu1 == "2":
            targ = input("Target (www.example.com): ")
            os.system("python2 DoS/Saphyra.py/saphyra " + targ)
        if menu1 == "7":
            ho = input("Host: ")
            po = input("Port: ")
            os.system("python2 DoS/tcp.py " + ho + " " + po + " 99999" )
        if menu1 == "6":
            ho = input("Host: ")
            os.system("ping " + ho)
        if menu1 == "5":
            os.system("python2 DoS/PyDDOS.py")
        if menu1 == "4":
            try:
                os.system("python2 DoS/fasthttp.py")
            except:
                print("Error: Script not starting")
        if menu1 == "0":
            menu()
    except:
        menu()

def menu():
    os.system("clear")
    print(random.choice(ascii))

    tools = """Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) DoS
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) Phising
        \033[38;2;0;255;152m3\033[38;2;88;159;240m) Doxxing
        \033[38;2;0;255;152m4\033[38;2;88;159;240m) Other
        \033[38;2;0;255;152m5\033[38;2;88;159;240m) Update
        \033[38;2;0;255;152m6\033[38;2;88;159;240m) Update tools
        \033[38;2;0;255;152m7\033[38;2;88;159;240m) About/Credit

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Exit"""

    print(men)
    print(tools)
    loop = True
    while loop == True:
        try:
            menu = input("""\x1b[1;33mSkidKit\033[38;2;88;159;240m: """)
            if menu == "1":
                dos()
            if menu == "2":
                phish()
            if menu == "3":
                dox()
            if menu == "4":
                other()
            if menu == "5":
                update()
            if menu == "6":
                update2()
            if menu == "7":
                print("\n")
                print("About: ")
                os.system("cat ../info/about.txt")
                print("\n")
                print("Credit: ")
                os.system("cat ../info/credit.txt")
                print("\n")
            if menu == "0":
                loop = False
                exit()
            if menu == "clear":
                os.system("clear")
                print(random.choice(ascii))
                print(men)
                print(tools)

        except:
            print("You mistyped, try again.")
if os.path.isfile(".info/tools.py"):
    menu()
else:
    xd = input("Press '1' to download tools: ")
    if xd == "1":
        os.chdir("DoS")
        os.system("git clone https://github.com/Karlheinzniebuhr/torshammer ; git clone https://github.com/JackzGamez/Saphyra.py ; git clone https://github.com/KrisIsHere/BDoS ; ")
        os.chdir("..")
        os.chdir("Phising")
        os.system("git clone https://github.com/htr-tech/zphisher ; git clone https://github.com/An0nUD4Y/blackeye ")
        os.chdir("..")
        os.chdir("Doxxing")
        os.system("git clone https://github.com/hangetzzu/saycheese")
        os.chdir("..")
        os.system("touch .info/tools.py")
        menu()
