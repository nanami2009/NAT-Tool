import requests  # 导入requests库，用于发送HTTP请求
import socket  # 导入socket库，用于网络通信
import stun  # 导入stun库，用于获取NAT类型和外部IP地址

# 获取公网IP地址
def get_public_ip():
    try:
        # 通过访问api.ipify.org获取公网IP地址
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException:
        # 如果请求失败，返回None
        return None

# 获取私网IP地址
def get_private_ip():
    try:
        # 创建一个UDP socket连接到Google的DNS服务器
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        # 获取本地IP地址
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error:
        # 如果获取失败，返回None
        return None

# 获取NAT类型
def get_nat_type():
    try:
        # 使用STUN协议获取NAT类型、外部IP地址和外部端口
        nat_type, external_ip, external_port = stun.get_ip_info()
        return nat_type, external_ip, external_port
    except Exception as e:
        # 如果获取失败，返回错误信息
        return str(e), None, None

if __name__ == '__main__':
    # 让用户选择输出语言
    language = input("请选择输出语言 (zh-cn/en-us): ").strip().lower()

    # 获取并打印公网IP地址
    public_ip = get_public_ip()
    private_ip = get_private_ip()
    nat_type, external_ip, external_port = get_nat_type()

    if language == 'zh-cn':
        # 输出中文结果
        print(f"公网IP地址: {public_ip}")
        print(f"私网IP地址: {private_ip}")
        print(f"NAT类型: {nat_type}")
        print(f"外部IP地址: {external_ip}")
        print(f"外部端口: {external_port}")
    elif language == 'en-us':
        # 输出英文结果
        print(f"Public IP Address: {public_ip}")
        print(f"Private IP Address: {private_ip}")
        print(f"NAT Type: {nat_type}")
        print(f"External IP Address: {external_ip}")
        print(f"External Port: {external_port}")
    else:
        # 无效的语言选择
        print("Invalid language selection. Please choose 'zh-cn' or 'en-us'.")
