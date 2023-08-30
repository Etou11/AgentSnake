class Snake:
    def __init__(self, list_snake_fields, head_position, facing_direction, speed):
        self.list_snake_fields = list_snake_fields
        self.head_position = head_position
        self.facing_direction = facing_direction
        self.speed = speed

    def length(self):
        return len(self.list_snake_fields)
