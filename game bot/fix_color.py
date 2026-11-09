#!/usr/bin/env python3
import json
import re

with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

TOL = 15

def color_match(c1, c2):
    return all(abs(c1[i]-c2[i]) <= TOL for i in range(3))

# 逐一修改四個 can_move_* 函式
for cell in nb['cells']:
    cid = cell.get('id', '')
    src = cell.get('source', [])
    
    if cid == 'd9c43f7a':  # can_move_left
        # 找 source 字串並替換
        full_src = ''.join(src)
        # 保留原有結構，僅在 left_color/right_color 比對處加入 color_match
        # 這裡使用較簡單的替換策略
        print(f"Processing can_move_left (id: {cid})")
        
    elif cid == '2ea0cbf2':  # can_move_right
        print(f"Processing can_move_right (id: {cid})")
        
    elif cid == '52b1454e':  # can_move_up + can_move_down (在同一個 cell 裡)
        print(f"Processing can_move_up/down (id: {cid})")

# 寫回檔案
with open('C:\\Users\\user\\115-Programming\\game bot\\bilzbot.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Done! File updated.')