import random
import string
import hashlib

def generate_password(length=8):
    # 定义密码可能包含的字符集
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # 确保密码包含至少一个大写字母、一个小写字母、一个数字和一个特殊字符
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # 剩余的字符随机选择
    password += random.sample(all_characters, length - 4)
    
    # 打乱密码字符的顺序
    random.shuffle(password)
    
    # 将列表转换为字符串
    return ''.join(password)


def hash_string_sha256(input_string):
    # 创建一个sha256哈希对象
    hash_object = hashlib.sha256()
    
    # 将输入字符串编码为字节，然后更新哈希对象
    hash_object.update(input_string.encode('utf-8'))
    
    # 获取哈希值的十六进制表示
    hex_dig = hash_object.hexdigest()
    
    return hex_dig

internal_password = []
for i in range(100):
    strong_password = generate_password(8)
    hashed_string = hash_string_sha256(strong_password)
    internal_password.append(hashed_string)

print(str(internal_password))