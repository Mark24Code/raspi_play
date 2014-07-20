#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
使用方法：
  python play.py file.mp4
功能说明：
  自动在视频文件所在的目录下匹配字幕，
  多字幕提供选择。
说明：
  解释器：Python 2.7
  采用 omxplayer

视频格式：
mkv,avi,flv,mp4

字幕格式：
ssa,ass,smi,srt,sub,lrc,sst,txt,xss,psb,ssb

作者：张阳（Mark24）
邮箱：mark.zhangyoung@gmail.com

  2014.7.20

'''
import sys
import os 
#格式常量列表
subtype = ['ssa','ass','smi','srt','sub','lrc','sst',\
            'txt','xss','psb','ssb']

vediotype = ['mkv','avi','flv','mp4']

path = os.getcwd()
#传入视频文件名
files = sys.argv[1]
nikename = files[:-4]
filetypes = files[-3:]
#nikename,filetypes = files.split('.')
#去除格式名
#视频文件绝对路径
workfile = path+files


def search_subtitles(current_path):
    #采用列表储存，当出现多个位置都存在字幕的时候可以放在一个列表中，在后面被挑选使用
    subtitles=[]
    for roots,dirs,files in os.walk(current_path):
        for filespath in files:
            if filespath[:-4] == nikename and filespath[-3:] in subtype:
                subtitles.append(os.path.join(roots,filespath))
            else:
                pass
    #返回 元素是绝对路径的列表
    return subtitles


def ask(subtitles):
    length = len(subtitles)
    print '\n存在多个字幕，您想使用哪个，请选择：\n'
    for num in range(length):
        print '[%d]: %s\n'%(num+1,subtitles[num])
    usenum = raw_input('>')   
    while int(usenum)-1 not in range(length):
        print '\n\n\n[!!!] 错误：输入的不正确，请重新输入！\n'
        print '[!!!] Error: Out of limited num, please try again!\n'
        usenum = raw_input('>')  
    subtitles=subtitles[int(usenum)-1]
    return subtitles #返回的是一个元素，而且应该是个str


def play(filename,subtitles):
    length = len(subtitles)
    print '[!!!] 运行……\n'
    print '[!!!] Starting...\n'
    print '[!!!] 检查格式...\n'
    print '[!!!] Check ...\n'

    if filetypes not in vediotype:
        print '[!!!] 错误：视频格式不正确！\n格式仅支持：mkv,avi,flv,mp4\n'
        print '[!!!] Error: The Vedio Type is not support.\nThe Player is just support:mkv,avi,flv,mp4\n'

    elif length==0:
        print '[!!!] 格式完好...\n'
        print '[!!!] Type OK...\n'
        print '[!!!] 自动匹配字幕 ...\n'
        print '[!!!] Auto matching subtitles ...\n'
        print '没有找到匹配外挂字幕\n'
        print 'No exist subtitles\n'
        print '[!!!] 准备完成！\n'
        print '[!!!] Prepared Complete!\n'
        print '[!!!] 播放...\n'
        print '[!!!] Playing...\n'
        os.system('omxplayer --font /usr/share/fonts/truetype/wqy/wqy-microhei.ttc -r -o hdmi %s'%filename)
        print '[!!!] 完成\n'
        print '[!!!] Finished\n'

    elif length>1:
        print '[!!!] 格式完好...\n'
        print '[!!!] Type OK...\n'
        print '[!!!] 自动匹配字幕 ...\n'
        print '[!!!] Auto matching subtitles ...\n'

        subtitles = ask(subtitles)
        print '[!!!] 准备完成！\n'
        print '[!!!] Prepared Complete!\n'
        print '[!!!] 播放...\n'
        print '[!!!] Playing...\n'
        os.system('omxplayer \
            --font /usr/share/fonts/truetype/wqy/wqy-microhei.ttc \
            --subtitles %s \
            -r -o hdmi %s'%(subtitles,filename))
        print '[!!!] 完成\n'
        print '[!!!] Finished\n'

    else :
        print '[!!!] 格式完好...\n'
        print '[!!!] Type OK...\n'
        print '[!!!] 自动匹配字幕 ...\n'
        print '[!!!] Auto matching subtitles ...\n'
        print '[!!!] 准备完成！\n'
        print '[!!!] Prepared Complete!\n'
        print '[!!!] 播放...\n'
        print '[!!!] Playing...\n'
        os.system('omxplayer \
            --font /usr/share/fonts/truetype/wqy/wqy-microhei.ttc \
            --subtitles %s \
            -r -o hdmi %s'%(subtitles[0],filename))
        print '[!!!] 完成\n'
        print '[!!!] Finished\n'


def main(current_path,filename):
    subtitles = search_subtitles(current_path)
    play(filename, subtitles)

if __name__=='__main__':
    main(path,files)
