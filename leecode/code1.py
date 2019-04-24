import os
import jieba
import numpy as np
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

def dict_vector():
    dic = DictVectorizer(sparse=False)
    data = dic.fit_transform([
            {'city': '北京','temperature':100},
            {'city': '上海','temperature':60},
            {'city': '深圳','temperature':30}
        ])
    print(dic.get_feature_names())
    print(data)


def cutword():
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


def count_vector():
    con1, con2, con3 = cutword()
    cv = CountVectorizer()
    data = cv.fit_transform([con1, con2, con3])
    k = cv.get_feature_names()
    print(k)
    arr = data.toarray()
    print(arr)
    for a in arr:
        for i, key in enumerate(a):
            if key:
                print(k[i])
    
        print("part stop \n")

def tfi_vector():
    con1, con2, con3 = cutword()
    tfi = TfidfVectorizer()
    data = tfi.fit_transform([con1, con2, con3])
    k = tfi.get_feature_names()
    print(k)
    print(data.toarray())


def mm_scaler():
    mm = MinMaxScaler(feature_range=(2, 3))
    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)
   

def std_scaler():
    mm = MinMaxScaler()
    data = mm.fit_transform([[ 1., -1., 3.], [ 2., 4., 2.], [ 4., 6., -1.]])
    print(data)


def im():

    im = Imputer(missing_values='NaN', strategy='mean', axis=0)

    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])

    print(data) 


def var():

    variance = VarianceThreshold()

    data = variance.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

    print(data)


def pca():

    pc = PCA(n_components=1)

    data = pc.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)
 

def practice():
    pwd = os.getcwd()
    org = 'G:/机器学习/第一天/资料/instacart/order_products__prior.csv'
    os.chdir(os.path.dirname(org))

    prior = pd.read_csv(os.path.basename(org))
    org = 'G:/机器学习/第一天/资料/instacart/products.csv'
    products = pd.read_csv(os.path.basename(org))
    org = 'G:/机器学习/第一天/资料/instacart/orders.csv'
    orders = pd.read_csv(os.path.basename(org))
    org = 'G:/机器学习/第一天/资料/instacart/aisles.csv'
    aisles = pd.read_csv(os.path.basename(org))    
    os.chdir(pwd)
    #合并四张表到一张表(用户-物品类别)
    _mg = pd.merge(prior,products,on=['product_id','product_id'])
    _mg = pd.merge(_mg,orders,on=['order_id','order_id'])
    _mg = pd.merge(_mg,aisles,on=['aisle_id','aisle_id'])
    _mg.head(10)
    cross = pd.crosstab(_mg['user_id'],_mg['aisle'])
    corss.head(10)
    pca = PCA(n_components=0.9)
    data = pca.fit_transform(cross)
    print(data)


def main():
    # dict_vector()
    # print(cutword())
    # count_vector()
    tfi_vector()
    # mm_scaler()
    # std_scaler()
    # im()
    # var()
    # pca()
    # practice()

if __name__ == '__main__':
    main()