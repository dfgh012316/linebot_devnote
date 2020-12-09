import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np

data=pd.read_csv('測試成績單.csv')
plt.switch_backend('agg') #不需要圖形介面的的backend
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] #顯示中文字

def search_ID_DICT(ID):
    a=data.loc[data['ID']==ID]
    data_dict=a.to_dict('list')
    return data_dict

def return_message(data,input_data):
    content='學號:'+str(search_ID_DICT(input_data)['ID']).replace('[','').replace(']','')+'\n'+\
            '姓名:'+str(search_ID_DICT(input_data)['姓名']).replace('[','').replace(']','')+'\n'+\
            '記憶:'+str(search_ID_DICT(input_data)['記憶']).replace('[','').replace(']','')+'\n'+\
            '理解:'+str(search_ID_DICT(input_data)['理解']).replace('[','').replace(']','')+'\n'+\
            '應用:'+str(search_ID_DICT(input_data)['應用']).replace('[','').replace(']','')+'\n'+\
            '分析:'+str(search_ID_DICT(input_data)['分析']).replace('[','').replace(']','')+'\n'+\
            '評鑑:'+str(search_ID_DICT(input_data)['評鑑']).replace('[','').replace(']','')+'\n'+\
            '創意:'+str(search_ID_DICT(input_data)['創意']).replace('[','').replace(']','')

    return content


def picture(data,ID):
    df=data.loc[data['ID']==ID].fillna(0)
    
    grade=[int(df[i]) for i in df.columns[2:8]]
    subject=[i for i in df.columns[2:8]]

    x=np.arange(len(subject))
    plt.bar(x,grade,tick_label=subject,color='blue')  
    for a,b in zip([i for i in range(6)],df.columns[2:8]):
        plt.text(a,int(df[b]),int(df[b]),size=18,horizontalalignment='center')
    plt.xlabel('科目')
    plt.ylabel('成績')
    plt.title(ID)
    plt.ylim(0,100)
    plt.savefig('static\\{}.png'.format(ID))
    plt.close()
    return 'https://8fc4a9d93111.ngrok.io//static//{}.png'.format(ID)


if __name__ == '__main__':
    picture(data,'b0742024')






