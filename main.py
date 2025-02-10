def draw_mirrored_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * i)

# Example usage
height = 5
draw_mirrored_triangle(height)