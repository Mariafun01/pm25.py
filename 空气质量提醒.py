# pm25.py
# 空气质量提醒
def main():
    pm = eval(input("What is today's PM2.5?"))

    # 打印相关提醒
    if pm > 75:
        print("Unhealthy. Be careful!")
    if pm < 35:
        print("Good. Go running!")
main()
