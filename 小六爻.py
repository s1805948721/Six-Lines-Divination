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

    # 从"大安"开始，获取对应的元素
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

def main_menu():
    print("\n=== 小六爻算卦系统 ===")
    print("1. 传统六爻预测")
    print("2. 八卦预测")
    print("3. 简易四象预测")
    print("4. 综合预测（显示所有结果）")
    print("0. 退出程序")
    return input("请选择预测方式（0-4）：")

def get_numbers():
    while True:
        try:
            n1 = int(input("请输入第一个数字（1-9）："))
            n2 = int(input("请输入第二个数字（1-9）："))
            n3 = int(input("请输入第三个数字（1-9）："))
            
            if all(1 <= n <= 9 for n in [n1, n2, n3]):
                return n1, n2, n3
            else:
                print("错误：所有数字必须在1到9之间")
        except ValueError:
            print("错误：请输入有效的数字")

def main():
    while True:
        choice = main_menu()
        
        if choice == '0':
            print("感谢使用，再见！")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("无效选择，请重试")
            continue
            
        n1, n2, n3 = get_numbers()
        
        print("\n=== 预测结果 ===")
        if choice in ['1', '4']:
            result = get_elements(n1, n2, n3)
            print("\n六爻预测结果：")
            for element in result:
                print(element)
                
        if choice in ['2', '4']:
            bagua_result = get_bagua(n1, n2, n3)
            print("\n八卦预测结果：")
            print(bagua_result)
            
        if choice in ['3', '4']:
            yijing_result = get_yijing(n1, n2, n3)
            print("\n四象预测结果：")
            print(yijing_result)
        
        if input("\n是否继续？(y/n): ").lower() != 'y':
            print("感谢使用，再见！")
            break

if __name__ == "__main__":
    main()