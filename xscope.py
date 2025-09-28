import numpy as np
import matplotlib
matplotlib.use('WxAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count


class InfiniteSineWave:
    def __init__(self, window_size=10, update_interval=50, line_color='b'):
        """
        初始化无限正弦波动画

        参数:
            window_size: x轴显示的窗口大小(单位:弧度)
            update_interval: 更新间隔(毫秒)
            line_color: 线条颜色
        """
        self.window_size = window_size
        self.update_interval = update_interval
        self.line_color = line_color

        # 初始化图形
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        self.fig, (self.ax, self.ax1, self.ax2) = plt.subplots(3, 1, figsize=(10, 5))
        self.fig.canvas.manager.set_window_title("动态数据曲线")
        self.ax.set_xlim(0, window_size)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)
        self.ax.set_title("左支臂")
        # self.ax.set_xlabel("时间")
        self.ax.set_ylabel("功率R/转速Bx1000")

        self.ax1.set_xlim(0, window_size)
        self.ax1.set_ylim(0, 10)
        self.ax1.grid(True)
        self.ax1.set_title("右支臂")
        # self.ax1.set_xlabel("时间")
        self.ax1.set_ylabel("功率R/转速Bx1000")

        self.ax2.set_xlim(0, window_size*2)
        self.ax2.set_ylim(0, 20)
        self.ax2.grid(True)
        self.ax2.set_title("卷筒")
        # self.ax2.set_xlabel("时间")
        self.ax2.set_ylabel("功率R/转速Bx1000")


        # 初始化数据
        self.x_data = []
        self.y_power_left = []
        self.y_power_right = []
        self.y_power_roll = []
        # self.line, = self.ax.plot([], [], f'{self.line_color}-', linewidth=2)
        self.y_line_power_left, = self.ax.plot([], [], color='r', linestyle='-', linewidth=0.5)
        self.y_line_speed_left, = self.ax.plot([], [], color='b', linestyle='-', linewidth=0.5)

        self.y_line_power_right, = self.ax1.plot([], [], color='r', linestyle='-', linewidth=0.5)
        self.y_line_speed_right, = self.ax1.plot([], [], color='b', linestyle='-', linewidth=0.5)

        self.y_line_power_roll, = self.ax2.plot([], [], color='r', linestyle='-', linewidth=0.5)
        self.y_line_speed_roll, = self.ax2.plot([], [], color='b', linestyle='-', linewidth=0.5)
        # 初始化计数器
        self.counter = count(start=0, step=0.1)

        # 动画对象
        self.animation = None

    def _update(self, _):
        """动画更新函数"""
        return self.y_line_power_left,

    def start(self):
        """启动动画"""
        if self.animation is None:
            self.animation = FuncAnimation(
                fig=self.fig,
                func=self._update,
                frames=None,
                interval=self.update_interval,
                blit=True,
                cache_frame_data=False
            )
        plt.show(block=False)

    def stop(self):
        """停止动画"""
        if self.animation is not None:
            self.animation.event_source.stop()

    def save(self, filename, fps=20):
        """保存动画为GIF"""
        if self.animation is not None:
            self.animation.save(filename, writer='pillow', fps=fps)


class RollingSineWave(InfiniteSineWave):
    """固定长度滚动窗口版本"""

    def __init__(self, data_points=100, **kwargs):
        super().__init__(**kwargs)
        self.data_points = data_points

        # 重新初始化数据为固定长度数组
        self.x_data = np.linspace(0, self.window_size, data_points)

        self.y_power_left = np.zeros(data_points)
        self.y_line_power_left.set_data(self.x_data, self.y_power_left)

        self.y_speed_left = np.zeros(data_points)
        self.y_line_speed_left.set_data(self.x_data, self.y_speed_left)


        self.y_power_right = np.zeros(data_points)
        self.y_line_power_right.set_data(self.x_data, self.y_power_right)

        self.y_speed_right = np.zeros(data_points)
        self.y_line_speed_right.set_data(self.x_data, self.y_speed_right)

        self.y_power_roll = np.zeros(data_points)
        self.y_line_power_roll.set_data(self.x_data, self.y_power_roll)

        self.y_speed_roll = np.zeros(data_points)
        self.y_line_speed_roll.set_data(self.x_data, self.y_speed_roll)

        # 重置坐标轴
        self.ax.set_xlim(0, self.window_size)
        self.ax1.set_xlim(0, self.window_size)
        self.ax2.set_xlim(0, self.window_size)

    def _update_data(self, power_list):
        # self.current_x = next(self.counter)
        # 滚动更新数据
        # self.y_data[:-1] = self.y_data[1:]
        # self.y_data[-1] = np.sin(self.current_x)
        self.y_power_left[:-1] = self.y_power_left[1:]
        self.y_power_left[-1] = power_list[0]
        self.y_speed_left[:-1] = self.y_speed_left[1:]
        self.y_speed_left[-1] = power_list[3]


        self.y_power_right[:-1] = self.y_power_right[1:]
        self.y_power_right[-1] = power_list[1]
        self.y_speed_right[:-1] = self.y_speed_right[1:]
        self.y_speed_right[-1] = power_list[4]


        self.y_power_roll[:-1] = self.y_power_roll[1:]
        self.y_power_roll[-1] = power_list[2]
        self.y_speed_roll[:-1] = self.y_speed_roll[1:]
        self.y_speed_roll[-1] = power_list[5]

    def _update(self, _):
        # 更新线条
        self.y_line_power_left.set_ydata(self.y_power_left)
        self.y_line_speed_left.set_ydata(self.y_speed_left)

        self.y_line_power_right.set_ydata(self.y_power_right)
        self.y_line_speed_right.set_ydata(self.y_speed_right)

        self.y_line_power_roll.set_ydata(self.y_power_roll)
        self.y_line_speed_roll.set_ydata(self.y_speed_roll)
        # 更新x轴标签
        # self.ax.set_xlabel(f"时间: {self.current_x:.1f}弧度")

        return self.y_line_power_left, self.y_line_power_right, self.y_line_power_roll, \
               self.y_line_speed_left, self.y_line_speed_right, self.y_line_speed_roll,


# # 创建并启动动画
# # sine_wave = InfiniteSineWave(window_size=8)
# # sine_wave.start()
# rolling_wave = RollingSineWave(
#     data_points=200,
#     window_size=10,
#     update_interval=20,
#     line_color='r'
# )
# rolling_wave.start()