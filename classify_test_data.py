
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
from util import mkdirs
import os


#model_file:上一步训练的模型名称
#test_data_dir:待测试数据存放路径
#test_result_dir:测试结果存放路径
def classify_test_data(model_file, test_data_dir, test_result_dir):

    texts = []
    old_files = []

    mkdirs(test_result_dir + '/pos')
    mkdirs(test_result_dir + '/neu')
    mkdirs(test_result_dir + '/neg')

    clf = joblib.load(model_file)

    for item in os.listdir(test_data_dir):
        if item[0] =='.': #.Ds_store
            continue
        file = open(test_data_dir + '/' + item)
        content = file.read()
        file.close()
        texts.append(content)
        old_files.append(item)

    ret = clf.predict(texts)
    names_file = open(model_file + '.names','rt')
    target_names = []
    for line in names_file.readlines():
        target_names.append(line.strip('\n'))
    names_file.close()

    index = 0
    for category in ret:
        new_file_path = test_result_dir + '/' + target_names[category] + '/' + old_files[index]
        new_file = open(new_file_path, 'w')
        new_file.write(texts[index])
        new_file.close()
        index = index + 1

if __name__ == '__main__':
    classify_test_data("sentiment.model", "test_facebook1", "result")