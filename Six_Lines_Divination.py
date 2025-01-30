import maliang

# 预测逻辑函数
def get_elements(n1, n2, n3):
    elements = [
        "大安（震）（木）（阳）：平安吉祥，诸事顺遂。长期、缓慢、稳定",
        "留连（坎）（水）（阴）：事情拖延，难以决断。停止、反复、复杂",
        "速喜（离）（火）（阳）：喜事临门，好消息快来。惊喜、快速、突然",
        "赤口（兑）（金）（阳）：口舌是非，易生争执。争斗、凶恶、伤害",
        "小吉（巽）（木）（阴）：小有收获，平稳略好。起步、不多、尚可",
        "空亡（震）（木）（阳）：虚无缥缈，难有结果。失去、虚伪、空想",
        "病符（坤）（土）（阴）：不适不顺，多有不便。病态、异常、治疗",
        "桃花（艮）（土）（阴）：姻缘桃花，人际和谐。欲望、牵绊、异性",
        "天德（乾）（金）（阳）：吉祥如意，贵人相助。贵人、上司、高远"
    ]
    return (
        elements[(n1 - 1) % len(elements)],
        elements[(n1 + n2 - 2) % len(elements)],
        elements[(n1 + n2 + n3 - 3) % len(elements)]
    )


def get_bagua(n1, n2, n3):
    bagua = [
        "乾卦：天行健，君子以自强不息。主动、创造、领导力",
        "坤卦：地势坤，君子以厚德载物。包容、顺从、守成",
        "震卦：雷雨动，君子以恐惧修省。行动、变革、惊醒",
        "巽卦：随风动，君子以立教治民。谦逊、入世、循序",
        "坎卦：水势险，君子以德行险中。智慧、危机、机遇",
        "离卦：火光明，君子以继明照于四方。光明、文明、觉悟",
        "艮卦：山不动，君子以思不出其位。稳重、停止、内省",
        "兑卦：泽气悦，君子以朋友讲习。喜悦、和谐、交流"
    ]
    return bagua[(n1 + n2 + n3) % 8]


def get_yijing(n1, n2, n3):
    yijing = [
        "吉：大吉大利，诸事顺遂",
        "凶：诸事不宜，需要谨慎",
        "平：平平常常，无喜无忧",
        "悔：有所悔恨，需要反省"
    ]
    return yijing[(n1 * n2 * n3) % 4]


# 创建主窗口
root = maliang.Tk(title="卜卦")
root.center()

# 创建画布并设置渐变背景
cv = maliang.Canvas(auto_zoom=True, keep_ratio="min", free_anchor=True)
cv.place(width=1280, height=720, x=640, y=360, anchor="center")

# 标题（使用更大字号和居中对齐）
maliang.Text(cv, (640, 80), text="卜 卦", fontsize=48, anchor="center")

# 预测方式选择 + 输入提示文本（调整间距和字号）
maliang.Text(cv, (400, 150), text="选择预测方式并输入三个数字：", fontsize=20, anchor="w")
mode_select = maliang.OptionButton(cv, (720, 130), text=("传统六爻预测", "八卦预测", "简易四象预测", "综合预测"), default=0)
maliang.Tooltip(mode_select, text="选择不同的预测方式将得到不同的解读结果")

# 数字输入框（水平方向排列）
n1_input = maliang.InputBox(cv, (500, 200), (80, 40), placeholder="第一个数", fontsize=16, align="center")
maliang.Tooltip(n1_input, text="请输入1-9之间的数字")

n2_input = maliang.InputBox(cv, (600, 200), (80, 40), placeholder="第二个数", fontsize=16, align="center")
maliang.Tooltip(n2_input, text="请输入1-9之间的数字")

n3_input = maliang.InputBox(cv, (700, 200), (80, 40), placeholder="第三个数", fontsize=16, align="center")
maliang.Tooltip(n3_input, text="请输入1-9之间的数字")

# 结果显示区域（使用Text组件，并设置合适的字体和对齐方式）
result_box = maliang.Text(cv, (370, 390), text="预测结果将在此显示", fontsize=16, anchor="nw")

# 预测按钮功能
def predict():
    try:
        n1, n2, n3 = int(n1_input.get()), int(n2_input.get()), int(n3_input.get())
        if not all(1 <= n <= 9 for n in [n1, n2, n3]):
            result_box.set("错误：所有数字必须在 1 到 9 之间。")
            return

        try:
            mode_idx = mode_select.get()  # 获取选中项的索引
        except:
            result_box.set("请先选择预测方式！")
            return
            
        modes = ["传统六爻预测", "八卦预测", "简易四象预测", "综合预测"]
        mode = modes[mode_idx]
        
        elements_result = get_elements(n1, n2, n3)
        bagua_result = get_bagua(n1, n2, n3)
        yijing_result = get_yijing(n1, n2, n3)
        
        if mode_idx == 0:  # 传统六爻预测
            result = f"预测方式：{mode}\n数字：{n1}, {n2}, {n3}\n\n结果：\n初爻：{elements_result[0]}\n二爻：{elements_result[1]}\n三爻：{elements_result[2]}"
        elif mode_idx == 1:  # 八卦预测
            result = f"预测方式：{mode}\n数字：{n1}, {n2}, {n3}\n\n结果：\n{bagua_result}"
        elif mode_idx == 2:  # 简易四象预测
            result = f"预测方式：{mode}\n数字：{n1}, {n2}, {n3}\n\n结果：\n{yijing_result}"
        else:  # 综合预测
            result = f"预测方式：{mode}\n数字：{n1}, {n2}, {n3}\n\n六爻结果：\n初爻：{elements_result[0]}\n二爻：{elements_result[1]}\n三爻：{elements_result[2]}\n\n八卦：\n{bagua_result}\n\n四象：\n{yijing_result}"
        
        result_box.set(result)
    except ValueError:
        result_box.set("错误：请输入有效的数字！")

# 绑定预测按钮功能（调整大小和字号）
predict_btn = maliang.Button(cv, (520, 290), (240, 60), text="开始预测", command=predict, fontsize=20)
maliang.Tooltip(predict_btn, text="点击开始进行卜卦预测")

# 启动主循环
root.mainloop()