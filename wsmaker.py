import os
import sys

wsid = int(sys.argv[1])

if(wsid>=1000 & wsid<=2000):
    containername = "ws" + str(wsid)
    folder = "ws/" + containername
    command = f"docker run --name {containername} --restart always -v ~/{folder}:/usr/share/nginx/html:ro -d -p {wsid}:80 nginx"

    os.makedirs(folder)
    os.system(command)
    print("sucess")