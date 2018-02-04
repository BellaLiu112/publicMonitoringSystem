from matplotlib import pyplot as plt
import os
import pylab

def draw_diagram(percentages, labels):

    #调节图形大小，宽，高
    plt.figure(figsize=(6,9))

    if len(labels) == 1:
        colors = ['red']
    elif len(labels)  == 2:
        colors = ['red','yellowgreen']
    elif len(labels) == 3:
        colors = ['red', 'yellowgreen', 'lightskyblue']

    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    patches,l_text,p_text = plt.pie(percentages,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)


    #改变文本的大小
    #方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    #定义饼状图的标签，标签是列表
    #labels = ['pos','neu','neg']
    #每个标签占多大，会自动去算百分比
    #sizes = [60,30,10]
    #draw_diagram(sizes=sizes, labels=labels)
    labels = []
    percentages = []
    result_path = 'result'
    for item in os.listdir(result_path):
        category_dir = result_path + '/' + item
        if os.path.isdir(category_dir):
            category_count = len(os.listdir(category_dir))
            if category_count > 0:
                labels.append(item)
                percentages.append(category_count)


    draw_diagram(percentages=percentages,labels=labels)