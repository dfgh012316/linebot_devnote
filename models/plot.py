import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np
from linebot.models import FlexSendMessage


def flex_grade(data, input_data, url):
    bubble = FlexSendMessage(
        alt_text="你的成績",
        contents={
              "type": "bubble",
              "size": "mega",
              "direction": "ltr",
              "hero": {
                  "type": "image",
                  "url": url,
                  "size": "full",
                  "aspectMode": "fit",
                  "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": url
                  }
                },
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
              {
                "type": "text",
                "text": "成績",
                "weight": "bold",
                "size": "xl"
              },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "知識",
                #"color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": str(search_ID_DICT(data, input_data)['知識_40%']).replace('[', '').replace(']', '').replace(".0", ""),
                "wrap": True,
                #"color": "#666666",
                "size": "sm",
                "flex": 1
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
                #"color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": str(search_ID_DICT(data,input_data)['能力_40%']).replace('[','').replace(']','').replace(".0",""),
                "wrap": True,
                #"color": "#666666",
                "size": "sm",
                "flex": 1
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "態度",
                "size": "sm",
                #"color": "#aaaaaa",
                "flex": 1
              },
              {
                "type": "text",
                "text": str(search_ID_DICT(data, input_data)['態度_20%']).replace('[', '').replace(']', '').replace(".0", ""),
                "flex": 5,
                "wrap": True,
                "size": "sm",
                "flex": 1
              }
            ],
            "spacing": "sm"
          }
        ]
      },
      {
        "type": "separator",
        #"color": "#aaaaaa",
        "margin": "xxl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "baseline",
    "contents": [
      {
        "type": "text",
        "text": "總排名",
        "size": "md"
      },
      {
        "type": "text",
        "text": str(search_ID_DICT(data,input_data)['總排名']).replace('[','').replace(']','').replace(".0",""),
        "margin": "none",
        "size": "sm",
        #"color": "#aaaaaa"
      }
    ]
  },
  "styles": {
    "header": {
      "separator": True
    }
  }
}
    )
    return bubble
  

def flex_grade1(url):
    bubble=FlexSendMessage(
      alt_text="你的成績",
      contents=
      {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": 'https://aec1-2401-e180-8883-2fc0-8181-800e-eee4-1a82.ngrok.io//static//B0742024.png',
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": "http://linecorp.com/"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
          {
            "type": "text",
            "text": "BROWN'S ADVENTURE\nIN MOVIE",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Date",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "Monday 25, 9:00PM",
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 4
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
                    "text": "Place",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "7 Floor, No.3",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 4
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
                    "text": "Seats",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "C Row, 18 Seat",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 4
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
  bubble=FlexSendMessage(
    alt_text="你的成績",
      contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "sm"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "sm"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "sm"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "sm"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
            "size": "sm"
          },
          {
            "type": "text",
            "text": "4.0",
            "size": "sm",
            "color": "#999999",
            "flex": 0,
            "margin": "md",
            "contents": []
          }
        ]
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
                "text": "Place",
                "size": "sm",
                "color": "#AAAAAA",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                "size": "sm",
                "color": "#666666",
                "flex": 5,
                "wrap": true,
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
                "text": "Time",
                "size": "sm",
                "color": "#AAAAAA",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "10:00 - 23:00",
                "size": "sm",
                "color": "#666666",
                "flex": 5,
                "wrap": true,
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "CALL",
          "uri": "https://linecorp.com"
        },
        "height": "sm",
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "WEBSITE",
          "uri": "https://linecorp.com"
        },
        "height": "sm",
        "style": "link"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
  )



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






