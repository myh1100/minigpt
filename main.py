import easygui
import os
import tkinter as tk
import sys
import shutil
import torch
import datetime

def get_filename_from_absolute_path(path):
    return os.path.basename(path)


def rf(dir,oldn,newn):
    file = (oldn, newn)
    old_path = os.path.join(dir, file[0])
    new_path = os.path.join(dir, file[1])
    if os.path.exists(old_path):
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)

def model():
    m=list(os.listdir("data\\model\\pt"))
    m.append('null')
    m.append('null')
    k = easygui.choicebox(msg = "请选择模型：",title = "",choices = m )
    return k

def generate_file(path,thing):
    try:
        with open(path, 'w') as file:
            file.write(thing)
        print(f'文件已成功生成：{path}')
    except Exception as e:
        print(f'生成文件时发生错误：{str(e)}')

# 检查文件夹路径是否存在，如果不存在则创建文件夹
def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'文件夹已成功创建：{path}')

# 检查文件路径所在的文件夹是否存在，如果不存在则创建文件夹
def create_folder_for_file(file_path):
    folder_path = os.path.dirname(file_path)
    create_folder_if_not_exists(folder_path)

# 在指定文件夹生成文件
def cfi(folder_path,filename,thing):
    create_folder_if_not_exists(folder_path)
    generate_file(os.path.join(folder_path, filename),thing)

#cfi('data/test/ta','nwe.py','hello')

def stf(source_folder,target_folder,foname):
    # 获取当前时间，并格式化为字符串
    now = datetime.datetime.now()
    time_str = now.strftime(foname)
    # 在目标文件夹中创建一个以当前时间为名的子文件夹
    sub_folder = os.path.join(target_folder, time_str)
    os.makedirs(sub_folder)

    # 遍历源文件夹中的所有文件，并复制到子文件夹中
    for file in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file)
        target_file = os.path.join(sub_folder, file)
        shutil.copy(source_file, target_file)

    # 删除源文件夹中的所有文件
    for file in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file)
        os.remove(source_file)
#stf('data/test/ta','data/test/tb')

class FileCopyDelete:
    # 定义一个初始化方法，接受源文件路径和目标文件路径作为参数
    def __init__(self, src_path, target_path):
        # 检查参数是否是字符串类型
        if not isinstance(src_path, str) or not isinstance(target_path, str):
            raise TypeError("src_path and target_path must be strings")
        # 检查源文件路径是否存在
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"src_path {src_path} does not exist")
        # 检查目标文件路径是否是一个目录
        if not os.path.isdir(target_path):
            raise ValueError(f"target_path {target_path} is not a directory")
        # 将参数赋值给实例属性
        self.src_path = src_path
        self.target_path = target_path

    # 定义一个方法，用于复制或删除文件
    def copy_or_delete(self,des):
        # 如果源文件路径是一个文件
        if os.path.isfile(self.src_path):
            # 如果源文件路径是特殊值，表示要删除目标文件路径下的同名文件
            if des== 'del':
                # 获取目标文件路径下的同名文件
                target_file = os.path.join(self.target_path, os.path.basename(self.src_path))
                # 如果目标文件存在，删除它
                if os.path.exists(target_file):
                    os.remove(target_file)
                # 否则，打印提示信息
                else:
                    print(f"No such file {target_file} to delete")
            # 否则，表示要复制源文件到目标文件路径下
            else:
                # 复制源文件到目标文件路径下，如果目标文件已存在，覆盖它
                shutil.copy(self.src_path, self.target_path)
        # 如果源文件路径是一个目录
        elif os.path.isdir(self.src_path):
            # 遍历源文件路径下的所有文件和子目录
            for file in os.listdir(self.src_path):
                # 获取源文件或子目录的完整路径
                src_file = os.path.join(self.src_path, file)
                # 创建一个新的实例，传入源文件或子目录的路径和目标文件路径作为参数
                fcd = FileCopyDelete(src_file, self.target_path)
                # 调用该实例的copy_or_delete方法，递归地复制或删除文件或子目录
                fcd.copy_or_delete(des)
        # 否则，打印提示信息
        else:
            print(f"Invalid src_path {self.src_path}")


#    src_path = "files/ndvi.tif"
#    target_path = "files/backup"
#    fcd = FileCopyDelete(src_path, target_path)
#    fcd.copy_or_delete("del" / null)
def cod(sp,fm,to,delss):
    fcd = FileCopyDelete('data/model/'+sp+'/'+fm, to)
    if(delss == "del"):
        fcd.copy_or_delete("del")
    else:
        fcd.copy_or_delete("hhhh")
def check_cuda():
    # 如果torch模块可以使用CUDA，打印提示信息
    if torch.cuda.is_available():
        return 1
    else:
        return 0

def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def cmdrunn (cmmd):
    s = os.popen(cmmd)
    print(s.read())

###############################################################

def bx():
    s=model()
    if(s=='null' or s==None):
        pass
    else:    
        cod('sc',s,'data/shakespeare_char/','dle')
        cod('pt',s,'out-shakespeare-char/','dle')
        inl = easygui.enterbox(msg="输入的内容",title = "ChatGPT")
        if inl == None:
            pass
        else:
            cil = "python sample.py --out_dir=out-shakespeare-char --device=cpu --num_samples=1 --start="+inl
            cmdrunn(cil)
        cod('sc',s,'data/shakespeare_char/','del')
        cod('pt',s,'out-shakespeare-char/','del')
        shutil.copy('data/prepare.py', 'data/shakespeare_char/')
def tr():
    fin = easygui.fileopenbox()
    shutil.copy(fin, "data/shakespeare_char")
    path = fin
    filename = get_filename_from_absolute_path(path) 
    directory = "data/shakespeare_char"
    old_name = filename
    new_name = "input.txt"
    rf(directory, old_name, new_name)
    cil = "python data/shakespeare_char/prepare.py "
    cmdrunn(cil)

def cm(cuda):
    easygui.msgbox("此操作需要较长时间，请耐心等待","ChatGPT")
    if cuda == True:
        cil = "python train.py config/train_shakespeare_char.py --compile=False --block_size=64 "
    elif cuda == False:
        cil = "python train.py config/train_shakespeare_char.py --compile=False --block_size=64 --device=cpu "
    cmdrunn(cil)


shutil.copy('data/prepare.py', 'data/shakespeare_char/')
while True:
    out = easygui.buttonbox(msg='ChatGPT', title='ChatGPT' ,choices =('生成模型','补写文档','退出'))
    if out == "补写文档":
        bx()
    elif out == "生成模型":
        name = easygui.enterbox(msg="模型名称",title="ChatGPT")
        a = easygui.ccbox(msg = "GPT-2 模型训练",title = "ChatGPT",choices = ("选择训练文本文件","关闭"))
        if a==1:
            tr()
            easygui.msgbox("模型文件已生成","ChatGPT")
            easygui.msgbox("即将开始编译","ChatGPT")
            a = easygui.choicebox(msg = "请选择：",title = "",choices = ['使用显卡(支持CUDA)','使用CPU'] )
            print(a)
            if a=='使用显卡(支持CUDA)':
                a = check_cuda()
                if a==0:
                    easygui.msgbox("未检测到CUDA核心，编译失败","ChatGPT")
                else:
                    cm(True)
                    easygui.msgbox("编译完成","ChatGPT")
                    stf('data/shakespeare_char/','data/model/sc',name)
                    stf('out-shakespeare-char/','data/model/pt',name)
                    shutil.copy('data/prepare.py', 'data/shakespeare_char/')
                    easygui.msgbox("复制完成","ChatGPT")
            elif a=='使用CPU':
                cm(False)
                easygui.msgbox("编译完成","ChatGPT")
                stf('data/shakespeare_char/','data/model/sc',name)
                stf('out-shakespeare-char/','data/model/pt',name)
                shutil.copy('data/prepare.py', 'data/shakespeare_char/')
            else:
                easygui.msgbox('已取消','ChatGPT')
    else:
        quit()