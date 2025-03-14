import os

# 图片所在的目录
image_dir = r'C:\Users\Admin\Desktop\task1\docs-d\docs\source\_static\参考手册\EcuM2'

# 获取目录下所有以 image 开头且后面跟数字的图片文件
image_files = []
for filename in os.listdir(image_dir):
    if filename.startswith('image'):
        try:
            number = int(''.join(filter(str.isdigit, filename)))
            # 假设图片扩展名常见为 .png、.jpg、.jpeg
            if any(filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                image_files.append((filename, number))
        except ValueError:
            continue

# 按数字编号从大到小排序
image_files.sort(key=lambda x: x[1], reverse=True)

# 新的起始编号
new_start_num = 27

# 进行重命名操作
for old_filename, _ in image_files:
    file_ext = os.path.splitext(old_filename)[1]
    new_filename = f'image{new_start_num}{file_ext}'
    old_path = os.path.join(image_dir, old_filename)
    new_path = os.path.join(image_dir, new_filename)

    try:
        os.rename(old_path, new_path)
        print(f"成功将 {old_filename} 重命名为 {new_filename}")
    except FileExistsError:
        print(f"错误：新文件名 {new_filename} 已存在，跳过 {old_filename} 的重命名。")
    except Exception as e:
        print(f"重命名 {old_filename} 时出现未知错误: {e}")

    new_start_num -= 1

    # 确保新编号不小于 3
    if new_start_num < 3:
        break