# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
from . import pill
import io
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from pathlib import Path

assets = assets = Path(__file__).parent.parent / 'assets'

font_path = str(assets / 'font' / 'Genshin_Impact.ttf')

custom_font = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = custom_font.get_name()

async def create_normalized_radial_chart(data, data_rect, rgb):
    rgb = pill.element_color_text.get(rgb, (149,107,5,255))
    params = [item['name'] for item in data]
    values = [item['value'] for item in data]

    max_values = {item['name']: item['value'] for item in data_rect}

    max_data_rect_values = [item['value'] for item in data_rect]

    num_vars = len(params)
   
    normalized_values = [values[i] / max_values[params[i]] if  max_values[params[i]] != 0 else 0 for i in range(num_vars)]
    normalized_values += [normalized_values[0]]


    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1] 

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    
    ax.grid(False)

    normalized_values_rect = [max_data_rect_values[i] / max_values[params[i]] if max_values[params[i]] != 0 else 0 for i in range(num_vars)]
    normalized_values_rect += [normalized_values_rect[0]]
    
    num_background_lines = 6

    max_data_rect_value = max(normalized_values_rect)


    step = max_data_rect_value / num_background_lines

    for i in range(1, num_background_lines + 2):
        radii = [step * i] * len(angles)
        radii.append(radii[0]) 
        ax.plot(np.append(angles, angles[0]), radii, color='white', linestyle='-', linewidth=0.5, zorder=0, alpha=0.3)
    
    for i in range(1, len(data_rect)+1):
        radii = [step * i for step in range(len(data_rect))]
        ax.plot([angles[i], angles[i]], [0.16, 1.16], color='white', linestyle='-', linewidth=0.5, zorder=1, alpha=0.3)

    valuess = [item['value'] for item in data_rect]
    valuess += [valuess[0]]
    ax.plot(angles, normalized_values_rect, linewidth=2, color='white', marker='o', linestyle='solid', zorder=0, alpha=0.5)
    for i, (angle, value) in enumerate(zip(angles, normalized_values_rect)):
        if valuess[i] % 1 == 0:
            val = str(valuess[i])
        else:
            val = '{:.1f}%'.format(valuess[i])
            
        ax.annotate(val, (angle, value), textcoords="offset points", xytext=(-10, -10), color = "white", fontsize=7, ha='left', alpha = 1)

    normalized_values_v = []
    for key in normalized_values:
        if key > 1.0:
            key = 1.2
        normalized_values_v.append(key)
        
    ax.plot(angles, normalized_values_v, linewidth=1, color = (rgb[0]/255,rgb[1]/255,rgb[2]/255), marker='o', zorder=1)
    ax.fill(angles, normalized_values_v, color= (rgb[0]/255,rgb[1]/255,rgb[2]/255), alpha=0.3)

    ax.xaxis.grid(linewidth=0) 
    ax.set_yticklabels([])
    ax.set_xticks(angles)
    ax.set_xticklabels(params + params[:1], color='white', fontproperties=custom_font,fontsize=10)
    ax.spines['polar'].set_visible(False)
            
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)

    img = Image.open(buffer)

    plt.close(fig)
    
    return img