from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import numpy as np

# # 特征抽取
#
# # 导入包
# from sklearn.feature_extraction.text import CountVectorizer
#
# # 实例化CountVectorizer
#
# vector = CountVectorizer()
#
# # 调用fit_transform输入并转换数据
#
# res = vector.fit_transform(["life is short,i like python","life is too long,i dislike python"])
#
# # 打印结果
# print(vector.get_feature_names())
#
# print(res.toarray())


def Dictvec():
    """
    字典数据抽取
    :return: None
    """
    dic = DictVectorizer(sparse=False)

    data = dic.fit_transform([{'city': '北京','temperature':100},{'city': '上海','temperature':60},{'city': '深圳','temperature':30}])

    print(dic.get_feature_names())

    print(data)

    return None


def cutword():
    """
    分词处理
    :return: 三篇文章
    """
    c1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")

    c2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")

    c3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系")

    # 构造三个列表
    content1 = []
    content2 = []
    content3 = []

    # 生成器内容放入列表
    for word in c1:
        content1.append(word)

    for word in c2:
        content2.append(word)

    for word in c3:
        content3.append(word)

    con1 = ' '.join(content1)
    con2 = ' '.join(content2)
    con3 = ' '.join(content3)

    return con1, con2, con3





def cv():

    # 获取文章分词结果
    con1, con2, con3 = cutword()

    count = CountVectorizer()

    data = count.fit_transform([con1, con2, con3])

    print(count.get_feature_names())

    print(data.toarray())

    return None


def tfidfvec():

    con1, con2, con3 = cutword()

    # 实例化
    tf = TfidfVectorizer(stop_words=["我们", "所以"])

    data = tf.fit_transform([con1, con2, con3])

    print(tf.get_feature_names())

    print(data.toarray())

    return None


def mm():

    minmax = MinMaxScaler(feature_range=(2, 3))

    data = minmax.fit_transform([[90,2,10,40], [60,4,15,45], [75,3,13,46]])

    print(data)
    return None


def std():

    stdard = StandardScaler()

    data = stdard.fit_transform([[ 1., -1., 3.], [ 2., 4., 2.], [ 4., 6., -1.]])

    print(data)

    return None


def im():

    im = Imputer(missing_values='NaN', strategy='mean', axis=0)

    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])

    print(data)
    return None


# 特征选择删除地方差特征
def var():

    variance = VarianceThreshold()

    data = variance.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

    print(data)
    return None


# PCA
def pca():

    pc = PCA(n_components=1)

    data = pc.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)
    return None


if __name__ == "__main__":
    pca()




