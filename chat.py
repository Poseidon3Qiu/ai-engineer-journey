# chat.py
# 第一个命令行 AI 助手：问一句，答一句
# 用的是本地 Ollama 跑的 llama3.1:8b 模型

# 第一步：导入 ollama 库（之前用 pip 装的那个）
# 这个库帮我们把话发给本地的 Ollama 服务，再把回答拿回来
import ollama

# 定义我们要用的模型名字
# 注意：必须和 "ollama list" 里看到的名字一模一样，包括冒号后面的 8b
MODEL_NAME = "llama3.1:8b"

# 打印一句欢迎语，让使用者知道程序启动了
print("命令行 AI 助手已启动（输入 quit 退出）")
print("-" * 40)  # 打印一条分隔线，40 个短横线，好看一点

# 用一个 while 循环，让程序可以一直问答，而不是只问一次就结束
# while True 表示「一直循环下去」，直到我们主动 break 跳出
while True:
    # 第二步：接收用户在终端输入的话
    # input() 会暂停程序，等你打字 + 回车
    # 括号里的字是提示语，会显示在终端上
    user_input = input("你：")

    # 如果用户输入 quit，就跳出循环，结束程序
    # .lower() 把输入转成小写，这样 Quit、QUIT 也能识别
    if user_input.lower() == "quit":
        print("再见！")
        break  # break 的作用是「跳出 while 循环」

    # 第三步：把用户的话发给模型
    # ollama.chat() 是这个库的核心函数
    # model 参数：用哪个模型
    # messages 参数：要发的消息，格式是一个列表，里面放字典
    #   role 表示角色，"user" 代表这句话是用户说的
    #   content 就是具体内容，也就是用户输入的话
    response = ollama.chat(
        model=MODEL_NAME, messages=[{"role": "user", "content": user_input}]
    )

    # 第四步：从返回结果里取出模型的回答，并打印
    # response 是一个字典，模型的回答藏在 response["message"]["content"] 里
    ai_reply = response["message"]["content"]
    print("AI：" + ai_reply)
    print("-" * 40)  # 再打一条分隔线，区分每一轮对话
