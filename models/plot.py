import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np
from linebot.models import FlexSendMessage

def flex_grade(url, values):
    bubble = FlexSendMessage(
      alt_text = "你的成績",
      contents =
      {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": url,
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": "https://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "成績",
        "size": "3xl",
        "align": "center",
        "gravity": "center",
        "wrap": True,
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "margin": "lg",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "知識",
                "size": "xl",
                "color": "#AAAAAA",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": str(values[0]),
                "size": "xl",
                "color": "#666666",
                "flex": 4,
                "wrap": True,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "能力",
                "size": "xl",
                "color": "#AAAAAA",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": str(values[1]),
                "size": "xl",
                "color": "#666666",
                "flex": 4,
                "wrap": True,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "態度",
                "size": "xl",
                "color": "#AAAAAA",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": str(values[2]),
                "size": "xl",
                "color": "#666666",
                "flex": 4,
                "wrap": True,
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  }
}
    )
    return bubble



def flex_simple():
  flex_message = FlexSendMessage(
            alt_text="stock_name",
            contents=
            {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": "https://linecorp.com"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "Brown's Burger",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "$10.5",
                "weight": "bold",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "400kcl",
                "size": "sm",
                "color": "#AAAAAA",
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"
              },
              {
                "type": "text",
                "text": "$15.5",
                "weight": "bold",
                "flex": 0,
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "550kcl",
                "size": "sm",
                "color": "#AAAAAA",
                "align": "end",
                "contents": []
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "Sauce, Onions, Pickles, Lettuce & Cheese",
        "size": "xxs",
        "color": "#AAAAAA",
        "wrap": True,
        "contents": []
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "spacer",
        "size": "xxl"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "Add to Cart",
          "uri": "https://linecorp.com"
        },
        "color": "#905C44",
        "style": "primary"
      }
    ]
  }
}
        )
  return flex_message



def create_data():
    df = pd.DataFrame()
    data = pd.read_excel("張松年計分冊.xlsx", sheet_name=None, engine='openpyxl')
    sheet = pd.ExcelFile("張松年計分冊.xlsx", engine='openpyxl')
    for s_name in sheet.sheet_names:
        df = pd.concat([df, data.get(s_name)], ignore_index=False)

    return df


def search_ID_DICT(data, ID):
    try:
        a = data.loc[data['ID'] == ID]
        data_dict = a.to_dict('list')
        return data_dict
    except:
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
        ax.set_ylim([0,115])
        def autolabel(rects):
    
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
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
                bar.set_color("#FF7575")      #不及格的顏色

        fig.savefig('static//{}.png'.format(ID))
        plt.close()
        return  'https://aec1-2401-e180-8883-2fc0-8181-800e-eee4-1a82.ngrok.io//static//{}.png'.format(ID)  

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
    
    print(picture(standar,data,'B0742024'))
    print(flex_grade(data,'B0742024',picture(standar,data,'B0742024')))






