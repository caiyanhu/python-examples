import os


def check_file_details(file_path):
    """
    检查文件内容，打印出包含中文或非ASCII字符的具体行号和列号。
    """
    if not os.path.exists(file_path):
        print(f"错误: 文件 '{file_path}' 不存在。")
        return

    print(f"正在检查文件: {file_path}")
    print(f"{'行号':<8} | {'列号':<8} | {'字符':<6} | {'类型'}")
    print("-" * 50)

    found_count = 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # enumerate(f, 1) 获取行号，从1开始
            for line_num, line in enumerate(f, 1):
                # enumerate(line, 1) 获取列号，从1开始
                for col_num, char in enumerate(line, 1):
                    char_type = None

                    # 1. 优先检查中文 (范围: 4E00-9FFF)
                    if "\u4e00" <= char <= "\u9fff":
                        char_type = "中文字符"

                    # 2. 如果不是中文，再检查是否为其他非ASCII (如Emoji, 日文, 特殊符号)
                    # 中文肯定也是非ASCII，所以用 elif 避免重复
                    elif ord(char) > 127:
                        char_type = "非ASCII字符"

                    # 如果发现了特殊字符，打印出来
                    if char_type:
                        # 对于换行符等不可见字符，做特殊处理显示，防止打印乱版
                        display_char = char
                        if char == "\n":
                            display_char = "\\n"
                        elif char == "\r":
                            display_char = "\\r"

                        print(
                            f"{line_num:<10} | {col_num:<10} | {display_char:<8} | {char_type}"
                        )
                        found_count += 1

    except UnicodeDecodeError:
        print("错误: 文件无法用 UTF-8 解码。请尝试检查文件编码是否为 GBK 或其他。")
        return
    except Exception as e:
        print(f"发生未知错误: {e}")
        return

    print("-" * 50)
    if found_count == 0:
        print("结果: 文件是纯 ASCII 格式 (未发现中文或特殊字符)。")
    else:
        print(f"结果: 共发现 {found_count} 处非 ASCII 字符。")


# ================= 测试代码 =================
if __name__ == "__main__":
    target_file = "code_check.txt"

    # 生成一个包含各种情况的测试文件
    if not os.path.exists(target_file):
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("def hello():\n")  # 第1行：纯英文
            f.write("    print('你好')\n")  # 第2行：包含中文
            f.write("    x = 10 # € value\n")  # 第3行：包含欧元符号(非ASCII)
            f.write("    return 'End' 😊")  # 第4行：包含 Emoji
        print(f"已生成测试文件: {target_file}\n")

    check_file_details(target_file)
