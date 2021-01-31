import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np

#test data
# data_from_excel=pd.read_excel('測試成績單.xlsx',sheet_name=None,engine='openpyxl')
# print(data_from_excel)
def create_data():
    df = pd.DataFrame()
 
    data = pd.read_excel("測試成績單.xlsx", sheet_name=None,engine='openpyxl')
 
    sheet = pd.ExcelFile("測試成績單.xlsx",engine='openpyxl')
 
    for s_name in sheet.sheet_names:
        df = pd.concat([df, data.get(s_name)], ignore_index=False)
    return df
plt.switch_backend('agg') #不需要圖形介面的的backend
#plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] 顯示中文字

def search_ID_DICT(data,ID):
    try:
        a=data.loc[data['ID']==ID]
        data_dict=a.to_dict('list')
        return data_dict
    except :
        return False

def judge(standar,data,ID):
    df=data.loc[data['ID']==ID].fillna(0)
    grade=[int(df[i]) for i in df.columns[2:8]]      #成績  
    subject=[i for i in df.columns[2:8]]             #科目
    student_dict=dict(zip(subject,grade))
    pass_subject=[]
    for i in subject :
        if standar[i]<=student_dict[i] :
            pass_subject.append(i)
    return pass_subject

def plot_judge(standar,data,ID):
    df=data.loc[data['ID']==ID].fillna(0)
    pass_list=[]
    pass_subject_list=judge(standar,data,ID)

    subjects=[i for i in df.columns[2:8]]

    for subject in subjects :
        if subject not in pass_subject_list :
            pass_list.append((subject,0))
        else :
            pass_list.append((subject,1))

    return pass_list

def return_message(data,input_data):
    if search_ID_DICT(data,input_data) == False :
        return "查無此學號，請重新輸入"
    else :
        content='記憶:'+str(search_ID_DICT(data,input_data)['memory']).replace('[','').replace(']','')+'\n'+\
                '理解:'+str(search_ID_DICT(data,input_data)['understand']).replace('[','').replace(']','')+'\n'+\
                '應用:'+str(search_ID_DICT(data,input_data)['application']).replace('[','').replace(']','')+'\n'+\
                '分析:'+str(search_ID_DICT(data,input_data)['analyse']).replace('[','').replace(']','')+'\n'+\
                '評鑑:'+str(search_ID_DICT(data,input_data)['judge']).replace('[','').replace(']','')+'\n'+\
                '創意:'+str(search_ID_DICT(data,input_data)['cool']).replace('[','').replace(']','')

        return content


def picture(standar,data,ID):
    df=data.loc[data['ID']==ID].fillna(0)            #處理尚未填入成績的空欄位
    grade=[int(df[i]) for i in df.columns[2:8]]      #成績  
    subject=[i for i in df.columns[2:8]]             #科目

    '''
    [2:8]為截取成績單中的第2欄到第7欄中的科目
    '''
    pass_list=plot_judge(standar,data,ID)
    subject,flag=zip(*pass_list)
    x=np.arange(len(subject))                       #取得科目數量
    bars=plt.bar(x,grade,tick_label=subject,color='blue')  
    
    
    for a,b in zip([i for i in range(6)],df.columns[2:8]):
        plt.text(a,int(df[b]),int(df[b]),size=18,horizontalalignment='center')

    for i, bar in enumerate(bars): 
        if flag[i] == 0 : 
            bar.set_color("red")

    plt.xlabel('Subject')
    plt.ylabel('Score')
    plt.title(ID)
    plt.ylim(0,100)
    plt.savefig('static//{}.png'.format(ID))
    plt.close()
    return 'https://32fd4f5f25ee.ngrok.io//static//{}.png'.format(ID)  #mac上改用 /  win上用//

def return_pass_subject(pass_subject):
    content="恭喜"
    for i,j in enumerate(pass_subject):
        if i == len(pass_subject)-1 :
            content+=j
        else :
            content=content+j+','
    return content+'通過'


if __name__ == '__main__':
    plt.switch_backend('agg') #不需要圖形介面的的backend
    #plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] 顯示中文字
    data=create_data()
    standar={'memory':80,'understand':70,'application':60,'analyse':60,'judge':60,'cool':60}
    print(picture(standar,data,'B0742025'))
    print(return_message(data,'B0742025'))






