# justpy 用javascript编写，能够直接完成网页app的构建
# 此处调用了Quasar框架设计网页 https://quasar.dev/introduction-to-quasar
import justpy as jp

def app():
    wp = jp.QuasarPage()         # 'wp' is just a variable name and 'wp'stands for web page
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    return wp

jp.justpy(app)

