from PIL import Image
import numpy as np
import face_recognition

def load_rgb_image(image_path):
    with Image.open(image_path) as img:
        print(f"\nConstruct of image '{image_path}'")
        print("Og", img.mode)
        img = img.convert('RGB')
        img_np = np.array(img)
        print("dtype", img_np.dtype)
        print("shape", img_np.shape)
        return img_np

def is_same_person(image_path1, image_path2, tolerance=0.6):
    # Load images
    image1 = load_rgb_image(image_path1)
    image2 = load_rgb_image(image_path2)

    # Find face encodings
    encodings1 = face_recognition.face_encodings(image1)
    encodings2 = face_recognition.face_encodings(image2)

    # Ensure each image has at least one face
    if len(encodings1) == 0 or len(encodings2) == 0:
        raise ValueError("One of the images has no detectable faces.")

    # Compare first face found in each image
    result = face_recognition.compare_faces([encodings1[0]], encodings2[0], tolerance=tolerance)

    return result[0]

print("\nis same person?" , is_same_person('hamid.jpg', 'hamid2.jpg'))