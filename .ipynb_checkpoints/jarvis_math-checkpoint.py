import numpy as np
import pandas as pd



def init_set(X):
    if isinstance(X,(list,tuple,np.ndarray,pd.Series)):
        return set(X)
    elif isinstance(X,set):
        return X
    else:
        print("ERROR : Incorrect data type \n")
        return X

def jaccard(A,B):
    '''
    雅卡尔相似度
    '''
    '''
    if isinstance(A,(list,tuple,set,np.ndarray)) and isinstance(B,(list,set,tuple,np.ndarray)):
        init_A,init_B = set(A),set(B)
    elif isinstance(A,set) and isinstance(B,set):
        init_A,init_B = A,B
    else:
        print("ERROR : Incorrect data type")
        return None
    '''
    init_A,init_B = init_set(A),init_set(B)
    intersection = init_A & init_B
    union = init_A | init_B
    return len(intersection) / len(union)

def jaccard_distance(A,B):
    '''
    雅卡尔距离
    '''
    '''
    if isinstance(A,(list,tuple,set,np.ndarray)) and isinstance(B,(list,tuple,set,np.ndarray)):
        init_A,init_B = set(A),set(B)
    elif isinstance(A,set) and isinstance(B,set):
        init_A,init_B = A,B
    else:
        print("ERROR : Incorrect data type")
        return None
    '''
    init_A,init_B = init_set(A),init_set(B)
    intersection = init_A & init_B
    union = init_A | init_B
    return (len(union) - len(intersection)) / len(union)


def cos(A,B):
    '''
    余弦相似度
    '''
    if len(A) != len(B):
        print("ERROR : \n The vectors have different lengths \n",len(A) > len(B) and "A > B" or "B < A")
        return None
    elif isinstance(A,(tuple,set)) and isinstance(B,(tuple,set)):
        init_A,init_B = np.array(list(A)),np.array(list(B))
    elif isinstance(A,(tuple,list)) and isinstance(B,(tuple,list)):
        init_A,init_B = np.array(A),np.array(B)
    elif isinstance(A,np.ndarray) and isinstance(B,np.ndarray):
        init_A,init_B = A,B
    else:
        print("ERROR : Incorrect data type")
        return None
    unit_vector = np.ones_like(init_A)
    return (init_A * init_B).dot(unit_vector)/(np.sqrt((init_A ** 2).dot(unit_vector)) * np.sqrt((init_B ** 2).dot(unit_vector)) )

def feature_dictionary_editor(iter_obj):
    '''
    特征字典编辑器
    '''
    drop_vector = [j for i in iter_obj for j in i ]
    unit_vector = {iter_:0 for iter_ in drop_vector}
    for iter_ in drop_vector:
        unit_vector[iter_] += 1
    return np.array(unit_vector)


def vectors_cos(A,B,return_all = False):
    """
    两个不限长度的可迭代对象的计数余弦相似度
    """
    A,B = list(A),list(B)
    lenght_A,lenght_B = len(A),len(B)
    feature_dictionary = lambda : {iter_:0 for iter_ in (A+B)}
    if lenght_A > lenght_B:
        max_iter = zip(B,A+[None]*(lenght_A-lenght_B)) 
    else :
        max_iter = zip(B+[None]*(lenght_B-lenght_A),A)
    feature_dictionary_A,feature_dictionary_B = feature_dictionary(),feature_dictionary()
    for b,a in max_iter:
        feature_dictionary_B[b]+= 1
        feature_dictionary_A[a]+= 1
    filter_values = lambda x : [v for _,v in x.items()]
    cos_value = cos(filter_values(feature_dictionary_A),filter_values(feature_dictionary_B))
    if return_all:
        return {"cos_value":cos_value,"feature_dictionary":feature_dictionary(),f"eature_dictionary_A":feature_dictionary_A,"feature_dictionary_B":feature_dictionary_B}
    return cos_value

def feature_value_filter(A,B,return_all = False):
    """
    两个可迭代对象的计数余弦相似度
    """
    A,B = list(A),list(B)
    lenght_A,lenght_B = len(A),len(B)
    feature_dictionary = lambda : {iter_:0 for iter_ in (A+B)}
    if lenght_A > lenght_B:
        max_iter = zip(B,A+[None]*(lenght_A-lenght_B)) 
    else :
        max_iter = zip(B+[None]*(lenght_B-lenght_A),A)
    feature_dictionary_A,feature_dictionary_B = feature_dictionary(),feature_dictionary()
    for b,a in max_iter:
        feature_dictionary_B[b]+= 1
        feature_dictionary_A[a]+= 1
    # 过滤计数值
    filter_values = lambda x : [v for _,v in x.items()]
    

    cos_value = cos(filter_values(feature_dictionary_A),filter_values(feature_dictionary_B))
    if return_all == True : 
        return {"cos_value":cos_value,"feature_dictionary":feature_dictionary(),"eature_dictionary_A":feature_dictionary_A,"feature_dictionary_B":feature_dictionary_B,"jaccard":jaccard(A,B)}
    elif return_all == "cos":
        return cos_value
    elif return_all == "jaccard":
        return jaccard(A,B)
    else:
        return {"cos":cos_value,"jaccard":jaccard(A,B),"lenght_A":lenght_A,"lenght_B":lenght_B,"feature_dictionary_A":feature_dictionary_A,"feature_dictionary_B":feature_dictionary_B}

def counter(X,return_type="dict"):
    '''
    计数
    '''
    if isinstance(X,(tuple,list,set)):
        init_X = np.array(X)
    elif isinstance(X,(np.ndarray,pd.Series)):
        init_X = X
    elif isinstance(X, dict):
        init_X = np.array([x for x,v in X.items()])
    unique,counter_values = np.unique(init_X,return_counts=True)
    #print(unique,counter)
    if return_type == "dict":
        return dict(zip(unique,counter_values))
    elif return_type == "ndarray":
        return unique,counter_values


def probability(X,return_type="dict"):
    '''
    概率
    '''
    length = len(X)
    unique,counter_values = counter(X,return_type = "ndarray")
    if return_type == "ndarray":
        return unique,counter_values/length
    elif return_type == "dict":
        return dict(zip(unique,counter_values/length))


def shannon_entropy(X):
    '''
    香农熵
    '''
    unique,probability_values = probability(X,return_type="ndarray")
    amount_of_information = -(probability_values*np.log(probability_values))
    return {"entropy":amount_of_information.dot(np.ones_like(amount_of_information)),"uniqu":unique,"amount_of_information":-np.log(probability_values)}
 

def KL_divergence(A,B):
    '''
    KL散度
    '''
    if len(A)== len(B):
        probA,probB = probability(A),probability(B)
        return probA/np.log(probA/probB)
    else:
        print(("ERROR : \n The vectors have different lengths \n",len(A) > len(B) and "A > B" or "B < A"))
        return None
'''
def cross_entropy(p,q):
    """
    交叉熵
    """
    step = np.nan_to_num(p*np.log(q)+(1-p)*np.log(1-q))
    return step.dot(np.ones_like(step))

def cross_entropy_(a, y):
    return np.sum(np.nan_to_num(-y*np.log(a)-(1-y)*np.log(1-a)))

def cross_entropy(y, y_hat):
    # n = 1e-6
    # return -np.sum(y * np.log(y_hat + n) + (1 - y) * np.log(1 - y_hat + n), axis=1)
    assert y.shape == y_hat.shape
    res = -np.sum(np.nan_to_num(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)))
    return round(res, 3)
'''

def softmax(x):
    '''
    '''
    exp_x = np.exp(x-np.max(x))
    return exp_x/exp_x.dot(exp_x)

if __name__ == "__main__":
    A,B = {1,1,2,1,1,1,0,0,0},[1,1,1,0,1,1,1,1,1]
    print(cos(A,B))
    print(jaccard(A,B))
    print(jaccard_distance(A,B))
    print(feature_value_filter(A,B))#,return_all = "jaccard"))
    print(counter(list("sjdljsakjdjasasdsa"),return_type="dict"))
    print(probability(B,return_type="dict"))
    print(shannon_entropy(list("190jmknjbjhbhjghvhvgjg")))
    print(KL_divergence(list("KMsaksjhs"),list("jksjkajskdnak")))
    x = np.random.normal(0,1,10)
    y = np.random.normal(0,1,10)
    print("softmax:",softmax(x))
    #print(cross_entropy(x,y))
    #print(cross_entropy_(x,y))