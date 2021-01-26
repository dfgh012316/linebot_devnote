import pandas as pd 

standar={'記憶':80,'理解':70,'應用':60,'分析':60,'評鑑':60,'創意':60}

data=pd.read_csv('測試成績單.csv')
ID='b0742024'
def search_ID_DICT(ID):
    a=data.loc[data['ID']==ID]
    data_dict=a.to_dict('list')
    return data_dict


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

def return_pass_subject(pass_subject):
    content="恭喜"
    for i,j in enumerate(pass_subject):
        if i == len(pass_subject)-1 :
            content+=j
        else :
            content=content+j+','
    return content+'通過'



if __name__ == '__main__' :
    print(search_ID_DICT(ID))
    print(standar)
    print(judge(standar,data,ID))
    pass_subject=judge(standar,data,ID)
    print(pass_subject)
    print(return_pass_subject(pass_subject))