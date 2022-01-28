
import os, random, shutil
 
firstdir = './dataset/train/'#要复制文件所在路径
tardir = './dataset/test/'#想要复制到的路径
pathdir = os.listdir(firstdir)#获取所在路径下的所有文件
path1 = pathdir[:-1]#这里我不需要最后一个文件夹，把它剔除掉
#把路径和文件夹名字合到一起
path = []
for path2 in path1:
    path.append(firstdir + path2)
 
k = 0#用来作为文件夹名字也就是图像类别的key
for i in path:
    j = 0#因为不能重复命名，所以在文件名后加一个j来区分
    sample = random.sample(os.listdir(i), 2)#随机从每个类别文件夹中选取2张图片
    for name in sample:#对每个选出的文件做复制和重命名操作
        j += 1
        cut = name.split('.')#由于文件后缀不一样，所以在这里用切分来获取文件后缀名
        shutil.move(i+'/'+name, tardir+'/'+name)#复制操作
        os.rename(tardir+'/'+name,tardir+'/'+path1[k]+str(j)+'.'+cut[1])#重命名为类别（path1[k]）的第几张（j）图片.后缀（cut[1]）
    k += 1