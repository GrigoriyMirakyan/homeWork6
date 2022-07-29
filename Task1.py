import copy

values = [2, 3, 5, 7, 11, 13, 17, 29, 41, 55]
transformation = lambda a: copy.deepcopy(a)
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('Ok')
else:
    print('Fail')

# Замучился с VSCode, почему то при сохранении автоматически меняет строку с лямбда на функцию def