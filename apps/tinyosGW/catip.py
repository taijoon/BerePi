# -*- coding: utf-8 -*-
# Author : jeonghoonkang, https://github.com/jeonghoonkang

from __future__ import print_function
import subprocess
import os
import sys

if __name__ == '__main__':

    print ("usage : python %s {IP_ADD} {PORT} {id}, {} : user should input" %__file__)
    exit()

    if len(sys.argv) < 2:
        exit("[bye] you need to input args, ip / port / id")

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    ip = arg1
    port = arg2
    id = arg3
    print ("... start running", " inputs are ", ip, port, id)

    print ("... key generating")
    os.system('ssh-keygen')

    print ("... entering copying security file")
    run_cmd = "cat ~/.ssh/id_rsa.pub"
    run_cmd += " | ssh -p %s %s@%s" %(port, id, ip)
    run_cmd += " 'cat>>/home/%s/.ssh/authorized_keys'" %id
    print (run_cmd)
    os.system(run_cmd)

    ''' 아래 코드는 동작을 안함. 확인 필요 '''
    #ret = subprocess.check_output(run_cmd)
    #print (ret)

    
    if __name__ == '__main__':
    dirs = "./out"
    p_ip = getip()
    i_ip = getiip()
    info = i_ip + p_ip
    hostn = hostname()
    fname = '/home/%s/devel/BerePi/apps/tinyosGW/out/%s.txt' %(id, hostn[:-1])

    writefile (info, fname)
    checkifexist(fname)

    cmd = "scp" + " %s " %fname + '%s@%s:'%(id,ip) + '/var/www/html/server/'
    ret = run_cmd(cmd)
    print (" ")
    print (ret)
