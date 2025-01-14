import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 定义数据
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
    first_index = (n1 - 1) % len(elements)
    second_index = (n1 + n2 - 2) % len(elements)
    third_index = (n1 + n2 + n3 - 3) % len(elements)
    return elements[first_index], elements[second_index], elements[third_index]

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
    index = (n1 + n2 + n3) % 8
    return bagua[index]

def get_yijing(n1, n2, n3):
    yijing = [
        "吉：大吉大利，诸事顺遂",
        "凶：诸事不宜，需要谨慎",
        "平：平平常常，无喜无忧",
        "悔：有所悔恨，需要反省"
    ]
    index = (n1 * n2 * n3) % 4
    return yijing[index]

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="morph")  # 使用 ttkbootstrap 的 "morph" 主题
        self.title("卜卦")
        self.geometry("800x600")
        self.minsize(600, 400)  # 设置窗口最小大小
        self.resizable(True, True)  # 允许调整窗口大小

        # 设置窗口图标（可选）
        try:
            self.iconbitmap("icon.ico")  # 替换为你的图标文件路径
        except:
            pass

        self.create_widgets()

    def create_widgets(self):
        # 主容器
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 标题
        self.title_label = ttk.Label(
            self.main_frame,
            text="卜卦",
            font=("Helvetica", 24, "bold"),
            bootstyle=PRIMARY
        )
        self.title_label.pack(pady=20)

        # 选择预测方式
        self.mode_frame = ttk.Frame(self.main_frame)
        self.mode_frame.pack(pady=10)

        self.mode_label = ttk.Label(
            self.mode_frame,
            text="选择预测方式并输入三个数字：",
            font=("Helvetica", 12),
            bootstyle=SECONDARY
        )
        self.mode_label.pack(side=tk.LEFT, padx=5)

        self.mode_var = tk.StringVar()
        self.mode_combobox = ttk.Combobox(
            self.mode_frame,
            textvariable=self.mode_var,
            values=["传统六爻预测", "八卦预测", "简易四象预测", "综合预测"],
            state="readonly",
            width=20,
            bootstyle=INFO
        )
        self.mode_combobox.current(0)  # 默认选择第一个
        self.mode_combobox.pack(side=tk.LEFT, padx=5)

        # 输入数字
        self.number_frame = ttk.Frame(self.main_frame)
        self.number_frame.pack(pady=20)

        self.n1_entry = ttk.Entry(
            self.number_frame,
            width=5,
            font=("Helvetica", 12),
            bootstyle=INFO
        )
        self.n1_entry.pack(side=tk.LEFT, padx=10)
        self.n2_entry = ttk.Entry(
            self.number_frame,
            width=5,
            font=("Helvetica", 12),
            bootstyle=INFO
        )
        self.n2_entry.pack(side=tk.LEFT, padx=10)
        self.n3_entry = ttk.Entry(
            self.number_frame,
            width=5,
            font=("Helvetica", 12),
            bootstyle=INFO
        )
        self.n3_entry.pack(side=tk.LEFT, padx=10)

        # 预测按钮
        self.predict_button = ttk.Button(
            self.main_frame,
            text="开始预测",
            command=self.predict,
            bootstyle=SUCCESS,
            width=15
        )
        self.predict_button.pack(pady=20)

        # 结果显示区域
        self.result_canvas = tk.Canvas(
            self.main_frame,
            bg="#f0f0f0",
            bd=0,
            highlightthickness=0,
            relief=tk.FLAT
        )
        self.result_canvas.pack(fill=tk.BOTH, expand=True, pady=10)

        # 结果显示文本
        self.result_text = tk.Text(
            self.result_canvas,
            bg="#f0f0f0",
            font=("Helvetica", 12),
            wrap=tk.WORD,
            bd=0,
            highlightthickness=0
        )
        self.result_text_window = self.result_canvas.create_window(
            10, 10,
            window=self.result_text,
            anchor=tk.NW,
            width=760,  # 初始宽度
            height=300  # 初始高度
        )

        # 绑定窗口大小调整事件
        self.result_canvas.bind("<Configure>", self.on_canvas_resize)

    def on_canvas_resize(self, event):
        """当 Canvas 大小调整时，动态调整 Text 组件的大小"""
        self.result_canvas.itemconfig(
            self.result_text_window,
            width=event.width - 20,  # 减去边距
            height=event.height - 20  # 减去边距
        )

    def predict(self):
        try:
            n1 = int(self.n1_entry.get())
            n2 = int(self.n2_entry.get())
            n3 = int(self.n3_entry.get())

            if not all(1 <= n <= 9 for n in [n1, n2, n3]):
                messagebox.showerror("错误", "所有数字必须在1到9之间")
                return

            mode = self.mode_combobox.current()
            self.result_text.delete(1.0, tk.END)

            if mode in [0, 3]:  # 传统六爻预测或综合预测
                result = get_elements(n1, n2, n3)
                self.result_text.insert(tk.END, "六爻预测结果：\n")
                for element in result:
                    self.result_text.insert(tk.END, element + "\n")

            if mode in [1, 3]:  # 八卦预测或综合预测
                bagua_result = get_bagua(n1, n2, n3)
                self.result_text.insert(tk.END, "\n八卦预测结果：\n")
                self.result_text.insert(tk.END, bagua_result + "\n")

            if mode in [2, 3]:  # 简易四象预测或综合预测
                yijing_result = get_yijing(n1, n2, n3)
                self.result_text.insert(tk.END, "\n四象预测结果：\n")
                self.result_text.insert(tk.END, yijing_result + "\n")

            # 添加动画效果
            self.animate_result()

        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")

    def animate_result(self):
        """简单的动画效果：逐渐改变背景颜色"""
        colors = ["#f0f0f0", "#e0e0e0", "#d0d0d0", "#c0c0c0", "#b0b0b0", "#a0a0a0"]
        self.animate_colors(colors, 0)

    def animate_colors(self, colors, index):
        """递归实现颜色动画"""
        if index < len(colors):
            self.result_canvas.configure(bg=colors[index])
            self.result_text.configure(bg=colors[index])
            self.after(100, self.animate_colors, colors, index + 1)
        else:
            # 动画结束后恢复原色
            self.result_canvas.configure(bg="#f0f0f0")
            self.result_text.configure(bg="#f0f0f0")

if __name__ == "__main__":
    app = App()
    app.mainloop()