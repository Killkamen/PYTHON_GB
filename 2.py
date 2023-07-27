def triangle_type(a, b, c):

    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"

    if a != b and b != c and a != c:
        return "Треугольник разносторонний"
    elif a == b and b == c:
        return "Треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"
