#!/usr/bin/env python3
import re

with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'r', encoding='utf-8') as f:
    content = f.read()

# 定義舊函式的具體模式 (多行)
old_pattern = r'def can_move_down\(r, c, im\): # 向下移動判斷 \(r 需要在 0 到 6 之間\).*?return False'

# 定義新函式
new_func = '''def can_move_down(r, c, im): # 向下移動判斷 (r 需要在 0 到 6 之間)
    # 僅檢查垂直向下移動 (r, c) -> (r+1, c)
    # 明確排除對角線移動
    if not (0 <= r < 7 and 0 <= c < 8):
    # 行必須在 0-6（能向下），欄在 0-7
        return False

    top_color = get_gem_color(r, c, im)
    bottom_color = get_gem_color(r+1, c, im)

    # 檢查以 (r+1, c) 為起點的垂直三連
    if top_color == bottom_color:
    # 情況: (r, c), (r+1, c), (r+2, c) 全相同
        if r <= 5:  # 確保 r+2 在 8x8 板內
            bottom1 = get_gem_color(r+1, c, im)
            if top_color == bottom_color == bottom1:
                # 再檢查 r+2
                if r <= 4:
                    bottom2 = get_gem_color(r+2, c, im)
                    if top_color == bottom_color == bottom1 == bottom2:
                        return True
                else:
                    return True  # 三格足夠
        else:
            return True  # 三格足夠

    # 檢查以 (r, c) 為起點的垂直三連 (向上)
    # 情況: (r-1, c), (r, c), (r+1, c) 全相同
    # 已在 can_move_up 中檢查過

    return False # 無法形成三消'''

# 使用 DOTALL 參數讓 . 匹配換行符
if re.search(old_pattern, content, re.DOTALL):
    content = re.sub(old_pattern, new_func, content, flags=re.DOTALL)
    with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully replaced can_move_down function')
else:
    print('Old pattern not found, trying alternative...')
    # 嘗試更簡單的字串替換
    old_func2 = """def can_move_down(r, c, im): # 向下移動判斷 (r 需要在 0 到 6 之間)
    if not (0 <= r < 7 and 0 <= c < 8):
        return False

    top_color = get_gem_color(r, c, im)
    bottom_color = get_gem_color(r+1, c, im)"""

    new_func2 = """def can_move_down(r, c, im): # 向下移動判斷 (r 需要在 0 到 6 之間)
    # 僅檢查垂直向下移動 (r, c) -> (r+1, c)
    # 明確排除對角線移動
    if not (0 <= r < 7 and 0 <= c < 8):
    # 行必須在 0-6（能向下），欄在 0-7
        return False

    top_color = get_gem_color(r, c, im)
    bottom_color = get_gem_color(r+1, c, im)"""

    if old_func2 in content:
        content = content.replace(old_func2, new_func2)
        with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Successfully replaced using simple string replace')
    else:
        print('Simple string replace also failed')