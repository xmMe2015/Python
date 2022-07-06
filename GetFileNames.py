#coding=utf-8
import os

#获取安装目录文件列表
def GetSetupFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetSetupFileList(newDir, fileList)  
    return fileList

#读取测试文件列表
def GetTestList():
    #获得当前路径
    root = os.getcwd()               
    f = open(root + '\GWDCMisFiles.txt','r')
    testList = []
    for line in f:
        testList.append(line.strip("\n"))
    f.close()
    return testList

#比较测试文件目录和安装目录
def CompareFiles():
    setupPath = input('输入路径：')
    fullPathList = GetSetupFileList(setupPath, [])
    setupList = []
    for fullPath in fullPathList:
        setupList.append(fullPath[len(setupPath)+1:])
        #print(fullPath[len(setupPath)+1:])

    testList = GetTestList()
    #for e in testList:
        #print(e)

    differS2T = set(setupList).difference(set(testList))
    differT2S = set(testList).difference(set(setupList))
    if len(differS2T) ==0 and len(differT2S) ==0:
        print('测试通过！')
    if len(differS2T) > 0:
        print('测试失败,测试文件没有以下文件：')
        print(differS2T)
    if len(differT2S) >0:
        print('测试失败，安装目录没有以下文件：')
        print(differT2S)

#输出安装目录下文件名
def OutputFiles():
    setupPath = input('输入路径：')
    fullPathList = GetSetupFileList(setupPath, [])
    for fullPath in fullPathList:
        print(fullPath[len(setupPath)+1:])
        
CompareFiles()
#OutputFiles()




