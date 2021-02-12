import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np

def create_data():
    df = pd.DataFrame()
    data = pd.read_excel("測試成績單.xlsx", sheet_name=None,engine='openpyxl')
    sheet = pd.ExcelFile("測試成績單.xlsx",engine='openpyxl')
    for s_name in sheet.sheet_names:
        df = pd.concat([df, data.get(s_name)], ignore_index=False)

    return df

def search_ID_DICT(data,ID):
    try:
        a=data.loc[data['ID']==ID]
        data_dict=a.to_dict('list')
        return data_dict
    except :
        return False

def judge(standar,data,ID):
    df=data.loc[data['ID']==ID].fillna(0)
    grade=[int(df[i]) for i in df.columns[2:5]]      #成績  
    subject=[i for i in df.columns[2:5]]             #科目
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

    subjects=[i for i in df.columns[2:5]]

    for subject in subjects :
        if subject not in pass_subject_list :
            pass_list.append((subject,0))
        else :
            pass_list.append((subject,1))

    return pass_list

def return_message(data,input_data):
    if len(search_ID_DICT(data,input_data)['ID']) == 0 :
        return 
    else :
        content='知識:'+str(search_ID_DICT(data,input_data)['知識_40%'])+"--排名"+str(search_ID_DICT(data,input_data)['知識排名'])+'\n'+\
                '能力:'+str(search_ID_DICT(data,input_data)['能力_40%'])+"--排名"+str(search_ID_DICT(data,input_data)['能力排名'])+'\n'+\
                '態度:'+str(search_ID_DICT(data,input_data)['態度_20%'])+"--排名"+str(search_ID_DICT(data,input_data)['態度排名'])+'\n'+\
                "----------------"+'\n'+\
                '總排名:'+str(search_ID_DICT(data,input_data)['總排名'])+'\n'+\
                '總人數:'+str(search_ID_DICT(data,input_data)['人數'])

        return content.replace('[','').replace(']','').replace(".0","")+""


def picture(standar,data,ID):
    if len(search_ID_DICT(data,ID)['ID']) == 0 :
        return "查無此學號，請重新輸入。"
    else :
        df=data.loc[data['ID']==ID].fillna(0)            #處理尚未填入成績的空欄位
        grade=[int(df[i]) for i in df.columns[2:5]]      #成績  
        grade2=[int(df[i]) for i in df.columns[11:14]]
        subject=[i for i in df.columns[2:5]]
        x=np.arange(len(subject)) #取得科目數量
        
        width=0.35
        fig,ax=plt.subplots()
        rects1 = ax.bar(x +width/2, grade, width,color='#84C1FF')   #學生目前成績
        rects2 = ax.bar(x - width/2, grade2, width,color='#BE77FF')  #學生自評

        ax.set_ylabel('成績')
        ax.set_title(ID)
        ax.set_xticks(x)
        ax.set_xticklabels(subject) 
        def autolabel(rects):
    
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height-3),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    size=20)
        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        pass_list=plot_judge(standar,data,ID)
        subject,flag=zip(*pass_list)

        for i, bar in enumerate(rects1): 
            if flag[i] == 0 : 
                bar.set_color("#FF7575")      #不及格的成績

        fig.savefig('static//{}.png'.format(ID))
        plt.close()
        return 'https://902e8626c1ba.ngrok.io//static//{}.png'.format(ID)  #mac上改用 /  win上用//

def return_pass_subject(pass_subject):
    content="恭喜"
    for i,j in enumerate(pass_subject):
        if i == len(pass_subject)-1 :
            content+=j
        else :
            content=content+j+','
    return (content+'通過').replace("_40%","").replace("_20%","")

if __name__ == '__main__':
    plt.switch_backend('agg') #不需要圖形介面的的backend
    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] #顯示中文字
    data=create_data()
    standar={'知識_40%':80,'能力_40%':70,'態度_20%':60}
    
    print(picture(standar,data,'B0924031'))
    print(return_message(data,'B0924031'))






