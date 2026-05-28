from flask import Flask, render_template, request
import random

app = Flask(__name__)

tarot_cards = [
    "愚者", "魔術師", "女祭司", "皇后", "皇帝", "教皇", "戀人", "戰車",
    "力量", "隱士", "命運之輪", "正義", "吊人", "死神", "節制", "惡魔",
    "高塔", "星星", "月亮", "太陽", "審判", "世界"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    cards_drawn = None
    user_question = ""
    copy_text = ""
    
    if request.method == 'POST':
        user_question = request.form.get('question')
        selected_cards = random.sample(tarot_cards, 3)
        positions = ["過去", "現在", "未來"]
        
        cards_drawn = []
        text_lines = [f"問題：{user_question}", "【塔羅三牌陣占卜結果】"]
        
        for i in range(3):
            status = random.choice(["正位", "逆位"])
            cards_drawn.append({
                "pos": positions[i],
                "name": selected_cards[i],
                "status": status
            })
            text_lines.append(f"- {positions[i]}：{selected_cards[i]} ({status})")
            
        text_lines.append("請幫我詳細解讀這個牌陣，謝謝！")
        copy_text = "\n".join(text_lines)
        
    return render_template('index.html', cards=cards_drawn, question=user_question, copy_text=copy_text)

if __name__ == '__main__':
    app.run(debug=True)
