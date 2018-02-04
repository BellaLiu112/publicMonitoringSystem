from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline


# 第一个参数为测试数据路径
# 第二个参数为保存模型名称
def train_sentiment(train_path, model_file):
    train_data = load_files(train_path)
    x_train, x_test, y_train, y_test = train_test_split(train_data.data,
                                               train_data.target,
                                               test_size=0.00000001);

    step1 = ('tfidf', TfidfVectorizer(analyzer = 'word', stop_words = 'english'))
    step2 = ('clf', LinearSVC())
    #step2 = ('clf', MultinomialNB())

    clf = Pipeline(steps = [step1, step2])

    #x_train为文本,y_train为分类(0,1)
    clf = clf.fit(x_train, y_train)
    joblib.dump(clf, model_file)

    names_file = open(model_file + '.names','w')
    for name in train_data.target_names:
        names_file.write(name + '\n')
    names_file.close()


if __name__ == '__main__':
    train_sentiment("test_facebook","sentiment.model")