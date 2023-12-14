import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

font_path = 'enkacard\\src\\assets\\total\\font\\Genshin_Impact.ttf'

custom_font = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = custom_font.get_name()

def create_normalized_radial_chart(data, data_rect):
    params = [item['name'] for item in data]
    values = [item['value'] for item in data]

    # Создаем словарь с максимальными значениями для каждой категории из data_rect
    max_values = {item['name']: item['value'] for item in data_rect}

    # Получаем максимальные значения для каждой категории из data_rect
    max_data_rect_values = [item['value'] for item in data_rect]

    # Количество параметров для графика
    num_vars = len(params)

    # Нормализуем значения в соответствии с максимальными значениями из data_rect
    normalized_values = [values[i] / max_values[params[i]] for i in range(num_vars)]
    normalized_values += [normalized_values[0]]  # Для замыкания графика добавляем первое значение в конец

    # Разделение круга на секции для параметров
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Для замыкания графика добавляем первый угол в конец

    # Настройка графика
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    
    ax.grid(False)

    # Добавление значений из data_rect на график
    normalized_values_rect = [max_data_rect_values[i] / max_values[params[i]] for i in range(num_vars)]
    normalized_values_rect += [normalized_values_rect[0]]  # Для замыкания графика добавляем первое значение в конец
    
    num_background_lines = 6

    # Находим максимальное значение из data_rect
    max_data_rect_value = max(normalized_values_rect)

    # Рассчитываем шаг для линий фона
    step = max_data_rect_value / num_background_lines

    # Добавление прямых линий фона в зависимости от максимального значения
    for i in range(1, num_background_lines + 2):
        radii = [step * i] * len(angles)
        radii.append(radii[0])  # Добавляем первый элемент в конец списка, чтобы замкнуть график
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
            
        ax.annotate(val, (angle, value), textcoords="offset points", xytext=(0, 5), color = "white", fontsize=7, ha='left', alpha = 0.5)
    # Построение радиальной диаграммы с нормализованными значениями
    normalized_values_v = []
    for key in normalized_values:
        if key > 1.0:
            key = 1.2
        normalized_values_v.append(key)
        
    ax.plot(angles, normalized_values_v, linewidth=1, color = (170/255,55/255,199/255), marker='o', zorder=1)
    ax.fill(angles, normalized_values_v, color= (170/255,55/255,199/255), alpha=0.3)

    ax.xaxis.grid(linewidth=0) 
    ax.set_yticklabels([])
    ax.set_xticks(angles)
    ax.set_xticklabels(params + params[:1], color='white', fontproperties=custom_font,fontsize=10)
    ax.spines['polar'].set_visible(False)
            
    plt.savefig('test_grafic.png', transparent=True)
    plt.close(fig)  # Закрываем рисунок после сохранения