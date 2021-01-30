import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np

data=pd.read_csv('測試成績單.csv')
plt.switch_backend('agg') #不需要圖形介面的的backend
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] #顯示中文字

def search_ID_DICT(ID):
    try:
        a=data.loc[data['ID']==ID]
        data_dict=a.to_dict('list')
        return data_dict
    except :
        return False

def return_message(data,input_data):
    if search_ID_DICT(input_data) == False :
        return "查無此學號"
    else :
        content='記憶:'+str(search_ID_DICT(input_data)['記憶']).replace('[','').replace(']','')+'\n'+\
                '理解:'+str(search_ID_DICT(input_data)['理解']).replace('[','').replace(']','')+'\n'+\
                '應用:'+str(search_ID_DICT(input_data)['應用']).replace('[','').replace(']','')+'\n'+\
                '分析:'+str(search_ID_DICT(input_data)['分析']).replace('[','').replace(']','')+'\n'+\
                '評鑑:'+str(search_ID_DICT(input_data)['評鑑']).replace('[','').replace(']','')+'\n'+\
                '創意:'+str(search_ID_DICT(input_data)['創意']).replace('[','').replace(']','')

        return content


def picture(data,ID):
    df=data.loc[data['ID']==ID].fillna(0)            #處理尚未填入成績的空欄位
    
    grade=[int(df[i]) for i in df.columns[2:8]]      #成績  
    subject=[i for i in df.columns[2:8]]             #科目

    '''
    [2:8]為截取成績單中的第2欄到第7欄中的科目
    '''

    x=np.arange(len(subject))                       #取得科目數量
    plt.bar(x,grade,tick_label=subject,color='blue')  
    for a,b in zip([i for i in range(6)],df.columns[2:8]):
        plt.text(a,int(df[b]),int(df[b]),size=18,horizontalalignment='center')
    plt.xlabel('科目')
    plt.ylabel('成績')
    plt.title(ID)
    plt.ylim(0,100)
    plt.savefig('static//{}.png'.format(ID))
    plt.close()
    return 'https://32fd4f5f25ee.ngrok.io//static//{}.png'.format(ID)  #mac上改用 /  win上用//


if __name__ == '__main__':
    print(picture(data,'b0742024'))
    print(return_message(data,'b0742024'))






