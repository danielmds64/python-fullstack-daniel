# ex16 - distância entre dois pontos

import math

p1 = (3, 4)
p2 = (7, 1)

d = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print(f"Distância entre os p1 e p2: {d:.4f}")