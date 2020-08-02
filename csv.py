
import csv    #加载csv包便于读取csv文件
csv_file=open('D:\python\实习\lip_train_set.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
date=[]    #创建列表准备接收csv各行数据
renshu = 0
for one_line in csv_reader_lines:
    date.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中
    renshu = renshu + 1    #统计行数（这里是学生人数）
i=0
while i < renshu:
    print (date[i][3])    #访问列表date中的数据验证读取成功（这里是打印所有学生的姓名）
    i = i+1
