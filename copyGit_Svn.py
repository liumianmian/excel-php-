#coding:utf-8
import os
import sys
import re
import os.path
import shutil
import json

def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    if not os.path.isdir(dst):
        os.makedirs(dst)
        
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        print srcname
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                # if re.search(r'configs\\facebook', srcname) or re.search(r'configs\\armorGame', srcname) or re.search(r'configs\\friendSter', srcname) or re.search(r'configs\\kongregate', srcname) or re.search(r'configs\\y8', srcname) or re.search(r'configs\\lookol', srcname):
                if re.search(r'configs\\weibo', srcname) or re.search(r'configs\\friendSter', srcname) or re.search(r'configs\\kongregate', srcname) or re.search(r'configs\\Y8', srcname) or re.search(r'configs\\lookol', srcname) or re.search(r'configs\\newGround', srcname) or re.search(r'configs\\addicting', srcname) or re.search(r'configs\\armorGame', srcname)  or re.search(r'configs\\facebook', srcname)  or re.search(r'view', srcname) or re.search(r'js', srcname):
                    print srcname
                    continue
                copytree(srcname, dstname, symlinks)
            else:
                if os.path.isdir(dstname):
                    os.rmdir(dstname)
                elif os.path.isfile(dstname):
                    os.remove(dstname)
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except OSError as err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)

if __name__ == '__main__':
    fileConfig = json.load((file('c:\excelConfig.json')))    

    #�����ļ�����
    configName = fileConfig['configName']
    #����·��
    sourcePath = fileConfig['sourcePath']
    copyPath = fileConfig['copyPath']

    #����svn
    print "�Ե�>>>>>>>>>>>>>>> crossPlatformVersionĿ¼������..."
    # os.system("svn update " + copyPath)

    print "�Ե�>>>>>>>>>>>>>>> dev_main2Ŀ¼������..."
    # os.system("svn update " + fileConfig['main2Path'] + "/v20130228")

    print "�Ե�>>>>>>>>>>>>>>> ��ʼͬ���汾..."
    copytree(sourcePath + 'v20130228', copyPath + 'v20130228')
    # copytree(sourcePath + 'images', copyPath + 'images')

    print sourcePath + 'v20130228'
    print ">>>>>>>>>>>>ͬ���汾��ɣ�"

    #�ύsvn
    svncomand = 'TortoiseProc /command:commit /path:"' + copyPath + '"'
    os.system(svncomand)