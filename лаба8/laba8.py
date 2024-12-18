from PIL import Image

def rotate_image_90(image_path):

  # открытие изображения
  image = Image.open(image_path)
  print(f"Исходное изображение: формат={image.format}, размер={image.size}, режим={image.mode}")
  
  #поворот изображения на 90 градусов
  rotated_image = image.rotate(90, expand=True)
  print(f"Изображение успешно повернуто на 90 градусов.")
  
  # сохранение изображения по тому же пути
  rotated_image.save(image_path)
  print(f"Изображение сохранено по пути: {image_path}")
    


# пример
if __name__ == "__main__":
    img_path = "C:/Users/artur/Desktop/Артур/python лабы/лаба8/imgs/walle.jpg"
    rotate_image_90(img_path)
