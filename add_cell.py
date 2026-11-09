import json

with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Create new cell
new_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'id': 'new_cell_131',
    'metadata': {},
    'source': [
        'import time\n',
        'start_time = time.time()\n',
        'im = pyg.screenshot()\n',
        '\n',
        '# 先存下目前的時間\n',
        'start_time = time.time()\n',
        '# 螢幕截圖\n',
        'im = pyg.screenshot()\n',
        '\n',
        '# 進入無窮迴圈\n',
        'while True:\n',
        '    elapsed = time.time() - start_time\n',
        '    if elapsed > 60:\n',
        '        print("超過一分鐘，離開迴圈")\n',
        '        break\n',
        '    \n',
        '    # 對於畫面中的每顆寶石(r,c)，判斷是否可以移動\n',
        '    for r in range(8):\n',
        '        for c in range(8):\n',
        '            moved = False\n',
        '            \n',
        '            if can_move_left(r,c,im):\n',
        '                # 移動寶石到左邊\n',
        '                x,y = get_gem_position(r,c-1)\n',
        '                pyg.click(x,y,duration=0.5)\n',
        '                moved = True\n',
        '            elif can_move_right(r,c,im):\n',
        '                # 移動寶石到右邊\n',
        '                x,y = get_gem_position(r,c+1)\n',
        '                pyg.click(x,y,duration=0.5)\n',
        '                moved = True\n',
        '            elif can_move_up(r,c,im):\n',
        '                # 移動寶石到上方\n',
        '                x,y = get_gem_position(r-1,c)\n',
        '                pyg.click(x,y,duration=0.5)\n',
        '                moved = True\n',
        '            elif can_move_down(r,c,im):\n',
        '                # 移動寶石到下方\n',
        '                x,y = get_gem_position(r+1,c)\n',
        '                pyg.click(x,y,duration=0.5)\n',
        '                moved = True\n',
        '    \n',
        '    if moved:\n',
        '        im = pyg.screenshot()\n',
        '    \n',
        '    print(f"迴圈執行中，已過時間: {elapsed:.1f} 秒")'
    ]
}

# Append the new cell
nb['cells'].append(new_cell)

# Write back
with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Done! New cell added.')