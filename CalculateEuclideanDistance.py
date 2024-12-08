import math

# Noktaları tanımlama
points = [(2, 3), (5, 7), (1, 9), (8, 2), (3, 6)]

# Öklid mesafesi hesaplayan fonksiyon
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclidean_distance(points[i], points[j]))

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçları yazdırma
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)
