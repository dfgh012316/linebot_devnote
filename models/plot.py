import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from linebot.models import FlexSendMessage, ButtonsTemplate, TemplateSendMessage

ngrok_url = 'https://61d9-61-56-180-227.ngrok.io'

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



def flex_PSY_A():
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
        "text": "您選擇了心理學A",
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
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSd06M587hWgJwuJBPYrUh6wUckCBWQNGtrnwlvcEqXZBwkXeA/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期中報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSeE6R4Bo8DzBXS1gTmJ4QvA62SUIawtIIh6QXFymv_JD4o_2g/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期末報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSfw67-G1_T-m_jmOnFIAeArCZ4wY__w_mEsGhM7i_le4ZDXZg/viewform?usp=sf_link"
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



def flex_PSY_B():
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
        "text": "您選擇了心理學B",
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
          "uri": "https://www.dropbox.com/request/lQ3fvTZ5OMcbaWvE5fRH"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期中報告",
          "uri": "https://www.dropbox.com/request/IEdYEAaiFpM2YfjQQPtF"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期末報告",
          "uri": "https://www.dropbox.com/request/4pkl5kG3B5q7o4XrnjgI"
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



def flex_MHD_A():
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
        "text": "您選擇了心理健康A",
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
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSc6JWL4G2V5rwISYLb6YJywJfd5p3ZcgEmqv5NzSzaERuF50Q/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期中報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSehfQaIVCF13q-hwsJyqhtKvrx0_bP2i0r44AWyf7Lay1fyXw/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期末報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLScNFko8jEiUsjtsgGT5t2ZUHTDR5Z6rkOKIXV25zqujdRs9GA/viewform?usp=sf_link"
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



def flex_MHD_B():
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
        "text": "您選擇了心理健康B",
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
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSeGaujit1YH4QUR12iau88dcagn7AK3zUfhlhIS_dJYLIiB0Q/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期中報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSezD5MFqK2nFeO1wxyZ9qdJpefIgZRqX-HGkU6S01y4d7HIFA/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期末報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSd9X47JWKVBAe8kP4VtJwEOJT0yv4B6FsLUgVexM2sRlI5eNA/viewform?usp=sf_link"
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



def flex_IRW():
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
        "text": "您選擇了職場/蘭陽采風",
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
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSd5dPzG6TJsAiDLGb1Pc11jIzBqL9HaDeKqepqEsPgEyMrsBA/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期中報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdh2CvxXnEATWvhZ8nY18T9Xcn0cSHSl-6uNzWDrDqe--ARWQ/viewform?usp=sf_link"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "期末報告",
          "uri": "https://docs.google.com/forms/d/e/1FAIpQLSfEKaMiSCetvyDs3kbYmbFkJnz_XJBtWWWoaOLfdIGzOaUBew/viewform?usp=sf_link"
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



def flex_Social():
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



def flex_account(stu_id, user_id):  
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
  


def flex_PPT():
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "size": "mega",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://0cb4-61-56-180-227.ngrok.io//static//pog.png",
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
        "text": "課程簡報",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "text",
        "text": "請選擇課程",
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
          "label": "心理學",
          "uri": "https://drive.google.com/drive/folders/1eNZvfEYThdsacEro9AlQt-0rHtpjK3l9?usp=sharing"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "心理健康",
          "uri": "https://drive.google.com/drive/folders/1eT6IwpapjPj1nbJwIsyvQShZRNOlzFlM?usp=sharing"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "職場與人際關係",
          "uri": "https://drive.google.com/drive/folders/1ruXW77yG_V0jCBhQkB6WXlobP67donCn?usp=sharing"
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
  


def flex_Addition():
  bubble = FlexSendMessage(
      alt_text = "課程按鈕",
      contents ={
  "type": "bubble",
  "size": "mega",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://0cb4-61-56-180-227.ngrok.io//static//pog.png",
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
        "text": "補充教材",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "text",
        "text": "請選擇課程",
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
          "label": "心理學",
          "uri": "https://drive.google.com/drive/folders/0B5xUZ5W4szenYXhYb21Ua2t3NE0?resourcekey=0-hPkpJYZfmmRkpft3DKx35w&usp=sharing"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "心理健康",
          "uri": "https://drive.google.com/drive/folders/0B5xUZ5W4szenZGo3RXlaa3ZzWWs?resourcekey=0-h97IDu1MRrfkEseIWBLklA&usp=sharing"
        },
        "color": "#905C44",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "職場與人際關係",
          "uri": "https://drive.google.com/drive/folders/0B5xUZ5W4szenLThOSFNlS0QwNTA?resourcekey=0-r5tN3Oha4rcmkfxkMEGnFg&usp=sharing"
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






