# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
from . import pill
import io
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from pathlib import Path
import warnings
import random

warnings.filterwarnings("ignore")

assets = assets = Path(__file__).parent.parent / 'assets'

font_path = str(assets / 'font' / 'Genshin_Impact.ttf')

custom_font = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = custom_font.get_name()

indices =  [2, 1, 0, 7, 6, 5, 4, 3, 9, 10, 11, 12]

class RadialChart:
    def __init__(self, data, data_rect, rgb):
        self.data = data
        self.data_rect = data_rect
        self.rgb = rgb

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = self._reorder_data_by_indices(value)

    @property
    def data_rect(self):
        return self._data_rect

    @data_rect.setter
    def data_rect(self, value):
        self._data_rect = self._reorder_data_by_indices(value)

    @staticmethod
    def _reorder_data_by_indices(lst):
        normalized_indices = [i % len(lst) for i in indices if i < len(lst)]
        return [lst[i] for i in normalized_indices]

    async def create_normalized_radial_chart(self):

        rgb = pill.element_color_text.get(self.rgb, (149, 107, 5, 255))
        params = [item['name'] for item in self.data]
        values = [item['value'] for item in self.data]

        max_values = {item['name']: item['value'] for item in self.data_rect}

        num_vars = len(params)
        normalized_values = []
        for i in range(num_vars):
            if max_values[params[i]] != 0:
                if max_values[params[i]] < values[i]:
                    normalized_values.append(7)
                else:
                    normalized_values.append(values[i] / max_values[params[i]])

            else:
                normalized_values.append(0)

        normalized_values += [normalized_values[0]]

        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]

        fig, ax = plt.subplots(subplot_kw=dict(polar=True))

        ax.grid(False)

        normalized_values_rect = [6.0 if max_values[params[i]] != 0 else 0 for i in range(num_vars)]
        normalized_values_rect += [normalized_values_rect[0]]

        num_background_lines = 7

        max_data_rect_value = max(normalized_values_rect)
        min_data_rect_value = min(normalized_values_rect)

        step = (max_data_rect_value - min_data_rect_value) / (num_background_lines - 1) if max_data_rect_value != min_data_rect_value else 1

        radii_rect = [6] * len(normalized_values_rect)

        radii_values = [self._get_value(item, max_values) for item in self.data]
        radii_values.append(radii_values[0])

        for i in range(1, num_background_lines + 1):
            radii = [step * (i - 1) + 1] * len(angles)
            radii.append(radii[0])
            ax.plot(np.append(angles, angles[0]), radii, color='white', linestyle='-', linewidth=0.5, zorder=0,
                    alpha=0.3)

        for i in range(1, len(self.data_rect) + 1):
            radii = [i + 0.16] * len(self.data_rect)
            ax.plot([angles[i], angles[i]], [0.16, num_background_lines + 0.16], color='white', linestyle='-',
                    linewidth=0.5, zorder=1, alpha=0.3)

        valuess = [item['value'] for item in self.data_rect]
        valuess += [valuess[0]]

        ax.plot(angles, radii_rect, linewidth=2, color='white', marker='o', linestyle='solid', zorder=0, alpha=0.5)
        for i, (angle, radius) in enumerate(zip(angles, radii_rect)):
            if valuess[i] % 1 == 0:
                val = str(valuess[i])
            else:
                val = '{:.1f}%'.format(valuess[i])

            ax.annotate(val, (angle, radius), textcoords="offset points", xytext=(-10, -10), color="white",
                        fontsize=9, ha='left', alpha=1)

        ax.plot(angles, radii_values, linewidth=1, color=(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255), marker='o',
                zorder=1)
        ax.fill(angles, radii_values, color=(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255), alpha=0.3)

        ax.xaxis.grid(linewidth=0)
        ax.set_yticklabels([])
        ax.set_xticks(np.linspace(0, 2 * np.pi, len(params), endpoint=False))
        ax.set_xticklabels(params, color='white', fontproperties=custom_font, fontsize=10)

        ax.spines['polar'].set_visible(False)

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', transparent=True)
        buffer.seek(0)

        img = Image.open(buffer)

        plt.close(fig)

        return img

    @staticmethod
    def _get_value(value_info, max_value_dict):
        max_value = max_value_dict.get(value_info['name'], None)
        if max_value is None or max_value == 0:
            return 1
        if value_info['value'] > max_value:
            normalized_value = 7 + (value_info['value'] - max_value) / (max_value * 0.3)
            return min(7.5, normalized_value)
        else:
            return int(1 + 5 * ((value_info['value'] / max_value) ** 2.5))

