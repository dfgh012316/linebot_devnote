import re
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from linebot.models import FlexSendMessage, ButtonsTemplate, TemplateSendMessage

load_dotenv()
ngrok_url = os.getenv('NGROK_URL')

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



def test():
  bubble = FlexSendMessage(
    alt_text = "你的成績",
    contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_5_carousel.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Arm Chair, White",
            "weight": "bold",
            "size": "xl",
            "wrap": True,
            "contents": []
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "$49",
                "weight": "bold",
                "size": "xl",
                "flex": 0,
                "wrap": True,
                "contents": []
              },
              {
                "type": "text",
                "text": ".99",
                "weight": "bold",
                "size": "sm",
                "flex": 0,
                "wrap": True,
                "contents": []
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Add to Cart",
              "uri": "https://linecorp.com"
            },
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Add to wishlist",
              "uri": "https://linecorp.com"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_6_carousel.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Metal Desk Lamp",
            "weight": "bold",
            "size": "xl",
            "wrap": True,
            "contents": []
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "$11",
                "weight": "bold",
                "size": "xl",
                "flex": 0,
                "wrap": True,
                "contents": []
              },
              {
                "type": "text",
                "text": ".99",
                "weight": "bold",
                "size": "sm",
                "flex": 0,
                "wrap": True,
                "contents": []
              }
            ]
          },
          {
            "type": "text",
            "text": "Temporarily out of stock",
            "size": "xxs",
            "color": "#FF5551",
            "flex": 0,
            "margin": "md",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Add to Cart",
              "uri": "https://linecorp.com"
            },
            "flex": 2,
            "color": "#AAAAAA",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Add to wish list",
              "uri": "https://linecorp.com"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "See more",
              "uri": "https://linecorp.com"
            },
            "flex": 1,
            "gravity": "center"
          }
        ]
      }
    }
  ]
})
  return bubble



def flex_homework():  
  bubble = FlexSendMessage(
    alt_text = "作業繳交選單",
    contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
          {
            "type": "text",
            "text": "注意⚠️",
            "weight": "bold",
            "size": "3xl",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          },
          {
            "type": "text",
            "text": "1. 作業資料夾 請勿繳錯位置",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "text",
            "text": " 2. 檔名有統一格式 請勿打錯",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "color": "#FF0000FF"
          },
          {
            "type": "text",
            "text": "TA會在LINE群公告繳交位置及檔名",
            "weight": "regular",
            "size": "md",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          },
          {
            "type": "text",
            "text": "有錯誤者TA都會直接刪除",
            "weight": "regular",
            "size": "md",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          },
          {
            "type": "separator",
            "color": "#FF0000FF"
          },
          {
            "type": "image",
            "url": "https://i.imgur.com/gGSS274.jpg",
            "size": "full",
            "aspectMode": "cover"
          },
          {
            "type": "text",
            "text": "更新時間：6月2號",
            "weight": "bold",
            "size": "sm",
            "align": "start",
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn-icons-png.flaticon.com/512/2113/2113886.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "backgroundColor": "#FAEBFAFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "心理學A",
            "weight": "bold",
            "size": "4xl",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "平時作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/6wCfN49vn"
            },
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期中作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/oHxyLOJGS"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期末作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/J0LcNEo13"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn-icons-png.flaticon.com/512/2113/2113886.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "backgroundColor": "#FAEBFAFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "心理學B",
            "weight": "bold",
            "size": "4xl",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "平時作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/RlrDp6pVG"
            },
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期中作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/KtYm9ifxr"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期末作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/HjCyGwlvJ"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn-icons-png.flaticon.com/512/2113/2113886.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "backgroundColor": "#DCFAF9FF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "心理健康A",
            "weight": "bold",
            "size": "4xl",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "平時作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/nY3AV6CeW"
            },
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期中作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/QNqTqodAQ"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期末作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/1dugyFry9"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn-icons-png.flaticon.com/512/2113/2113886.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "backgroundColor": "#DCFAF9FF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "心理健康B",
            "weight": "bold",
            "size": "4xl",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "平時作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/aakD1utCh"
            },
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期中作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/ipUnLZr7i"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期末作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/V9qTSnQWb"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn-icons-png.flaticon.com/512/2113/2113886.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "backgroundColor": "#F8FEDEFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "社會脈動",
            "weight": "bold",
            "size": "4xl",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "平時作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/xSchvaQj6"
            },
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期中作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/gykHLpH9h"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期末作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/JL6vySref"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn-icons-png.flaticon.com/512/2113/2113886.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "backgroundColor": "#F8FEDEFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "職場人際關係",
            "weight": "bold",
            "size": "3xl",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "平時作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/7D2PCA2A7"
            },
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期中作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/ZB5LZm0sl"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "期末作業",
              "uri": "http://snchangqq.quickconnect.to/sharing/6a6a0VgrC"
            }
          }
        ]
      }
    }
  ]
}
    )
  return bubble



def flex_choose():
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents =
          {
  "type": "bubble",
  "size": "mega",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": ngrok_url + "//static//homework.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "backgroundColor": "#F9BFEAFF",
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
        "text": "要繳交作業到哪個課程呢?",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "text",
        "text": "請選擇課程按鈕",
        "weight": "regular",
        "size": "lg",
        "color": "#726C6CFF",
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
        "size": "xs"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "1.心理學a",
          "text": " ",
          "data": 'action=心理學a&answer=NA'
        },
        "color": "#905C44",
        "style": "primary",
        "position": "relative"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "2.心理學b",
          "text": " ",
          "data": 'action=心理學b&answer=NA'
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "3.心理健康a",
          "text": " ",
          "data": 'action=心理健康a&answer=NA'
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "3.心理健康b",
          "text": " ",
          "data": 'action=心理健康b&answer=NA'
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "5.職場/蘭陽采風",
          "text": " ",
          "data": 'action=職場/蘭陽采風&answer=NA'
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "6.社會脈動",
          "text": " ",
          "data": 'action=社會脈動&answer=NA'
        },
        "color": "#905C44",
        "style": "primary"
      }
    ]
  },
  "styles": {
    "footer": {
      "backgroundColor": "#E6E1ABFF",
      "separator": False,
      "separatorColor": "#FFFFFFFF"
    }
  }
}
  )
  return bubble



  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "size": "mega",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": ngrok_url+"//static//link.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "backgroundColor": "#F9BFEAFF",
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
        "text": "要繳交哪一份作業呢?",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "text",
        "text": "您選擇了社會脈動",
        "weight": "regular",
        "size": "lg",
        "color": "#726C6CFF",
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
        "size": "xs"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "平時作業",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdg7Dwou5aHQxdc810cLO11EBd9dCqPlOfp0IgYGOzpK--Qhg/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期中報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSevfGLB1c4P_oXXjPATZMSJHKvDjDiBt0VuanxXFnsActelJg/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期末報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSc5cfYUDHrnMa0yUKU1UVi6QgU1hTCVcdkI9-TDpd_1Oeyuxw/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      }
    ]
  },
  "styles": {
    "footer": {
      "backgroundColor": "#E6E1ABFF",
      "separator": False,
      "separatorColor": "#FFFFFFFF"
    }
  }
}
  )
  
  return bubble



def flex_account(stu_id, user_id):  # Not in json
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "size": "mega",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": ngrok_url + "//static//bind.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "backgroundColor": "#F9BFEAFF",
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
        "text": "是否確定要綁定此學號?",
        "weight": "bold",
        "size": "xl",
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
        "size": "xs"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "確定綁定",
          "text": " ",
          "data": 'action=NA&answer=yes&stu_id='+stu_id+'&user_id='+user_id
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "取消綁定",
          "text": " ",
          "data": 'action=NA&answer=no'
        },
        "color": "#905C44",
        "style": "primary"
      }
    ]
  },
  "styles": {
    "footer": {
      "backgroundColor": "#E6E1ABFF",
      "separator": False,
      "separatorColor": "#FFFFFFFF"
    }
  }
}
  )
  return bubble
  


def flex_ppt():
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "filler"
      },
      {
        "type": "text",
        "text": "課程簡報",
        "weight": "bold",
        "size": "3xl",
        "align": "center",
        "gravity": "top",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://www.iconpacks.net/icons/2/free-ppt-icon-1517-thumb.png",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "lg",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "心理學與現代社會",
              "uri": "https://gofile.me/6ZkPp/s4twVTo0x"
            },
            "height": "md",
            "style": "primary",
            "gravity": "center"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "心理健康與發展",
              "uri": "https://gofile.me/6ZkPp/m14DuhC2q"
            },
            "style": "primary"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "職場人際關係",
              "uri": "https://gofile.me/6ZkPp/w1FH05Oow"
            },
            "style": "primary"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "社會脈動與關懷",
              "text": "尚未開放！"
            },
            "style": "secondary"
          },
          {
            "type": "separator"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "separator"
      }
    ]
  }
}
  )
  return bubble
  


def flex_addition():
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "filler"
      },
      {
        "type": "text",
        "text": "補充教材",
        "weight": "bold",
        "size": "3xl",
        "align": "center",
        "gravity": "top",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://cdn-icons-png.flaticon.com/512/4151/4151213.png",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "lg",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "心理學與現代社會",
              "uri": "https://gofile.me/6ZkPp/RNmCjQhFK"
            },
            "height": "md",
            "style": "primary",
            "gravity": "center"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "心理健康與發展",
              "uri": "https://gofile.me/6ZkPp/W39IGE0pw"
            },
            "style": "primary"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "職場人際關係",
              "uri": "https://gofile.me/6ZkPp/HsG5kqIbQ"
            },
            "style": "primary"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "社會脈動與關懷",
              "text": "尚未開放！"
            },
            "style": "secondary"
          },
          {
            "type": "separator"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "separator"
      }
    ]
  }
}
  )
  return bubble



def flex_rule():
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "filler"
      },
      {
        "type": "text",
        "text": "課程規定",
        "weight": "bold",
        "size": "3xl",
        "align": "center",
        "gravity": "top",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://cdn-icons-png.flaticon.com/512/2534/2534888.png",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "lg",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "心理學與現代社會",
              "uri": "https://gofile.me/6ZkPp/bX7j5JP0q"
            },
            "height": "md",
            "style": "primary",
            "gravity": "center"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "心理健康與發展",
              "uri": "https://gofile.me/6ZkPp/zQTHi3wVJ"
            },
            "style": "primary"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "職場人際關係",
              "uri": "https://gofile.me/6ZkPp/GZWChWzyk"
            },
            "style": "primary"
          },
          {
            "type": "separator"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "社會脈動與關懷",
              "text": "尚未開放！"
            },
            "style": "secondary"
          },
          {
            "type": "separator"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "separator"
      }
    ]
  }
})
  return bubble


def true_or_false(stu_id):
  bubble = FlexSendMessage(
    alt_text = "身分確認...",
    contents ={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "身分確認...",
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "gravity": "center",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://cdn-icons-png.flaticon.com/512/947/947496.png",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "您是否是"+str(stu_id),
        "weight": "bold",
        "size": "xl",
        "align": "center",
        "contents": []
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "是",
          "text": str(stu_id)
        },
        "style": "primary",
        "gravity": "center"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "否",
          "text": "請詢問助教帳號綁定問題，並提供截圖。"
        },
        "style": "secondary",
        "gravity": "center"
      }
    ]
  }
})
  return bubble  

def create_data():
    df = pd.DataFrame()
    data = pd.read_excel("張松年計分冊.xlsx", sheet_name=None, engine='openpyxl')
    excel_sheet = pd.ExcelFile("張松年計分冊.xlsx", engine='openpyxl')
    for s_name in excel_sheet.sheet_names:
        df = pd.concat([df, data.get(s_name)], ignore_index=False)
    
    return df

def search_ID_DICT(data, ID):
    try:
        a = data.loc[data[2] == ID]
        data_dict = a.to_dict('list')
        print(data_dict)
        return data_dict
    except:
        return False

def judge(standar,data,ID):
    df=data.loc[data[2]==ID].fillna(0)
    #grade=[int(df[i]) for i in df.columns[6:9]]      #知識_40%	能力_40%	態度_20% 成績欄位  
    grade = df.values[:,-3:].tolist()
    #subject=[i for i in df.columns[6:9]]             #科目
    grade = [float(i) for i in grade[0]]
    
    subject=['知識_40%', '能力_40%', '態度_20%']
    student_dict=dict(zip(subject,grade))            #這裡list內的資料形態要注意
    pass_subject=[]   
    for i in subject :
        if standar[i]<=student_dict[i] :
            pass_subject.append(i)
    return pass_subject

def plot_judge(standar,data,ID):
    df=data.loc[data[2]==ID].fillna(0)
    pass_list=[]
    pass_subject_list=judge(standar,df,ID)

    #subjects=[i for i in df.columns[6:9]]
    subjects=['知識_40%', '能力_40%', '態度_20%']

    for subject in subjects :
        if subject not in pass_subject_list :
            pass_list.append((subject,0))
        else :
            pass_list.append((subject,1))

    return pass_list

def picture(standar, data, ID):
    if (len(search_ID_DICT(data, ID)[2])==False) :
        return "查無此學號，請重新輸入。"
    else :
        df = data.loc[data[2]==ID].fillna(0)            #處理尚未填入成績的空欄位
        print(df)
        #grade = [i for i in df.iloc[-3:]]      #知識_40%	能力_40%	態度_20% 成績欄位
        grade = df.values[:,-3:].tolist() #這裡list內的資料形態要注意
        grade = [float(i) for i in grade[0]]

        print(type(grade))
        print(str(grade)+' gradeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        #grade2=[int(df[i]) for i in df.columns[12:14]]    #自評知識	自評能力	自評態度 給學生選用的欄位 學期末才會自評
        #subject = [i for i in df.columns[6:9]]
        subject = ['知識_40%', '能力_40%', '態度_20%']
        x=np.arange(len(subject)) #取得科目數量
        width=0.35
        fig,ax=plt.subplots()
        
        rects1 = ax.bar(x + width/2, grade, width, color='#84C1FF')   #學生目前成績
        #rects2 = ax.bar(x - width/2, grade2, width, color='#BE77FF')  #學生自評
        
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
        #autolabel(rects2)
        fig.tight_layout()

        pass_list = plot_judge(standar, data, ID)
        subject, flag=zip(*pass_list)

        for i, bar in enumerate(rects1): 
            if flag[i] == 0 : 
                bar.set_color("#FF7575")      #不及格的顏色

        fig.savefig('static//{}.png'.format(ID))
        plt.close()        
        return ngrok_url + '//static//{}.png'.format(ID)  

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
    plt.rcParams['font.sans-serif'] = ['TaipeiSansTCBeta-Regular.ttf'] #顯示中文字
    #data=create_data()
    #data = create_sheet()
    standar = {'知識_40%':80,'能力_40%':70,'態度_20%':60}
    #print(data)
    #print(picture(standar,data,'B0742024'))
    #print(flex_grade(data,'B0742024',picture(standar,data,'B0742024')))