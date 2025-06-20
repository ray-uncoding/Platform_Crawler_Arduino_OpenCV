# OpenCV2Arduino/config.py

import json
from pathlib import Path

# 載入 color_config.json
color_config_path = Path(__file__).parent / "color_config.json"

with open(color_config_path, "r", encoding="utf-8") as f:
    color_ranges = json.load(f)

# 顏色 + 形狀 → 對應的控制指令 
#目前選項 "Triangle","Square","Hexagon"
action_map = {
    ('Red', 'Triangle'): 'A',
    ('Red', 'Square'): 'B',
    ('Red', 'Hexagon'): 'C',
    ('Blue', 'Triangle'): 'D',
    ('Blue', 'Square'): 'E',
    ('Blue', 'Hexagon'): 'F',
}
