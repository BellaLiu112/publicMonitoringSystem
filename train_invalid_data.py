from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline


def train(train_path, model_file):
    train_data = load_files(train_path)
    x_train, x_test, y_train, y_test = train_test_split(train_data.data,
                                               train_data.target,
                                               test_size=0.00000001);

    step1 = ('tfidf', TfidfVectorizer(analyzer = 'word', stop_words = 'english'))
    step2 = ('clf', LinearSVC())
    clf = Pipeline(steps = [step1, step2])

    #x_train为文本,y_train为分类(0,1)
    clf = clf.fit(x_train, y_train)
    joblib.dump(clf, model_file)


if __name__ == '__main__':
    train("data/train","train.model")