from src.config.globals import BORDER_RADIUS, SCREEN, WIDTH
import pygame

# Method to draw the life rect


class Rects:
    def __init__(self, rect_type, max_value, height, x, y, color, bar_position):
        self.color = color
        self.height = height
        self.rect_type = rect_type
        self.max_value = max_value
        self.bar_position = bar_position
        self.x = x
        self.y = y
        self.bar_colors = [
            (0, 255, 0), (124, 255, 0), (228, 255, 0),
            (255, 139, 0), (255, 44, 0), (255, 0, 0),
            (158, 0, 0), (0, 255, 255), (25, 25, 25)
        ]
        self.rects_display_sizes = {
            "right": {
                "container": lambda max_value : WIDTH-self.x-max_value,
                "content": lambda width: (WIDTH-self.x)-width
            },
            "left": {
                "container": lambda max_value : self.x,
                "content": lambda width : self.x
            }
        }

    # Method that control the gradient effect
    def draw_bars(self, color_index, current_bar_value, max_value):
        max_value = max_value * 4 if self.rect_type == "life" else max_value * 2.5
        current_bar_value = current_bar_value * 4 if self.rect_type == "life" else current_bar_value * 2.5
        
        pygame.draw.rect(
            surface=SCREEN, 
            color=self.bar_colors[color_index],
            rect=(
                self.rects_display_sizes[self.bar_position]["content"](current_bar_value),
                self.y,
                current_bar_value,
                self.height
            ),
            border_radius=BORDER_RADIUS
        )

        pygame.draw.rect(
            surface=SCREEN, 
            color=self.bar_colors[-1],
            rect=(
                self.rects_display_sizes[self.bar_position]["container"](max_value),
                self.y-1,
                max_value,
                self.height + 2
            ),
            width=3,
            border_radius=BORDER_RADIUS
        )
