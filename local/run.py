import os
import re
import paramiko
import win32com.client
from dfa import Sensitive_word, cDfa
from Qa import Qa

# Construct a dataset to save the sensitive word
cdfa = cDfa(Sensitive_word)

# get the ip of the service
hostip = '123.127.237.185'
user = 'stu'
passwd = 'stu'


def connect(input1):
    try:
        # connect the service and sent the input to the service
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostip, 22, user, passwd)

        path1 = "D://pic5_fin//1_start.txt"
        with open(path1, 'w', encoding="utf-8") as f2:
            f2.write(input1)

        ftp = ssh.open_sftp()
        ftp.put(path1, "/home/stu/pkq/gpt-2/samples/story_start/1_start.txt")

        stdout = ssh.exec_command('source anaconda3/bin/activate story_generation;cd pkq/gpt-2/src;'
                                  'python run.py', get_pty=True)[1]

        result = stdout.readlines()
        print(result)
        for i in result:
            print(i)

        for i in range(1, 6):
            path2 = "/home/stu/pkq/gpt-2/samples/story_final_return/" + str(i) + ".txt"
            path3 = "D://pic5_fin//data//" + str(i) + ".txt"
            ftp.get(path2, path3)

        # result = stdout.readlines()
        # print(result)
        # for i in result:
        #     print(i)
        ssh.close()
    except Exception as e:
        print("\tError %s\n" % e)


def detect(path1):
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，]+'
    i = 0
    for root, dirs, files in os.walk(path1):
        for file in files:
            path2 = path1 + "\\" + file
            i += 1

            with open(path2, 'r') as f1:
                for line in f1.readlines():
                    line = line.lower()
                    ls = re.sub(r, ' ', line).split()

                    if cdfa.isContain(ls):
                        break

            return i

        return None


def speak(path2):
    spk = win32com.client.Dispatch("SAPI.SpVoice")
    spk.rate = 0
    f = open(path2, "r")
    str1 = f.read()
    str1.replace("\n", "")
    f.close()
    spk.Speak(str1)


def run1():
    input1 = 'A cat'
    connect(input1)
    path1 = "D://pic5_fin//data"
    n = detect(path1)
    print(n)
    #
    path2 = "D://pic5_fin//data//" + str(n) + ".txt"
    speak(path2)

    qa = Qa()
    animalMessage = qa.reader("D:\\pic5_fin\\base.xlsx")
    question = input("your question: ")
    worlds = qa.analyseQuestion(question)
    # print(animalMessage[0].__len__())
    answeranimal = []
    for i in worlds:
        for index in range(animalMessage[0].__len__()):
            if str(animalMessage[0].__getitem__(index)).lower() == str(i).lower():
                if i not in answeranimal:
                    answeranimal.append(i)
                    str1 = "The" + i + " is a " + animalMessage[3].__getitem__(index) + " animal. " + animalMessage[
                        2].__getitem__(index) + " and " + animalMessage[4].__getitem__(
                        index) + "And, his favorite food is " + animalMessage[1].__getitem__(index) + "."

                    with open('D://pic5_fin//2.txt', 'w', encoding='utf-8') as f2:
                        f2.write(str1)

                    path3 = 'D://pic5_fin//2.txt'
                    speak(path3)

    if len(answeranimal) == 0:
        str2 = "Sorry, this question is too difficult, I can't answer your question"
        with open('D://pic5_fin//2.txt', 'w', encoding='utf-8') as f2:
            f2.write(str2)

        path3 = 'D://pic5_fin//2.txt'
        speak(path3)

run1()
