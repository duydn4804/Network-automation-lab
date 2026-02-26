from netmiko import ConnectHandler
from datetime import datetime
import os

# 1. Khai báo thông tin 2 Router
devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.99.1",
        "username": "admin",
        "password": "admin123",
        "name": "R1"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.99.2",
        "username": "admin",
        "password": "admin123",
        "name": "R2"
    }
]

# 2. Tạo thư mục lưu file backup
backup_dir = "backup_configs"
os.makedirs(backup_dir, exist_ok=True)

# 3. Lấy thời gian thực để gắn vào tên file
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print("=== BẮT ĐẦU TỰ ĐỘNG SAO LƯU CẤU HÌNH ===")

# 4. Vòng lặp kết nối và lấy cấu hình từng thiết bị
for dev in devices:
    # Lấy biến 'name' ra khỏi dictionary để Netmiko không bị lỗi
    device_name = dev.pop("name") 
    
    print(f"Đang kết nối tới {device_name} ({dev['host']})...")
    try:
        # Mở phiên SSH với các thông số Netmiko hợp lệ
        net_connect = ConnectHandler(**dev)
        
        # Gửi lệnh lấy cấu hình đang chạy
        output = net_connect.send_command("show run")
        
        # Lưu ra file text
        filepath = f"{backup_dir}/{device_name}_{now}.txt"
        with open(filepath, "w") as f:
            f.write(output)
            
        print(f" -> Đã lưu thành công: {filepath}")
        net_connect.disconnect()
        
    except Exception as e:
        print(f" -> Lỗi khi kết nối {device_name}: {e}")

print("=== HOÀN TẤT ===")
