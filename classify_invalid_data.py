
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib

is_clf_loaded = 0
model_file = ''

def load_model(model_file):
    global clf
    clf = joblib.load(model_file)

def collect_valid_data(text):
    global is_clf_loaded
    if is_clf_loaded == 0:
        global clf
        clf = joblib.load(model_file)

def collect_valid_data(model_file, preditct_file):
    file = open(preditct_file, "r")
    indices = []
    texts = []

    while 1:
        line = file.readline()
        if line:
            lines = line.split('\t')
            indices.append(lines[0])
            #texts.append(clean_data(lines[1]))
            texts.append(lines[1])
        else:
            break;
    file.close()


    #载入的数据中没有去除超链接，标点等符号，这里直接拿来用来，需要注意是否需要预处理一下?
    ret = clf.predict(texts)
    index = 0
    save_file = open(preditct_file + ".predict.csv", "wt+")
    save_file.write("Id,Category\n")
    for r in ret:
        line = indices[index] + "," + str(r)
        save_file.write(line + "\n")
        print(line + " : " + texts[index])
        index += 1
    save_file.close()

if __name__ == '__main__':
    predict("train.model", "test.tsv")
    #print(clean_data("hello world, 124 ppp http://www.baidu.com a HURB enable enabled"))