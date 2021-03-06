import os

import cv2


class Preprocessing:

    def __init__(self):
        pass

    def create_directory(self, str_directory_name):
        """
        Creates a new directory if it doesn't exist.

        :param str_directory_name: name of new directory
        :return: None
        """
        if os.path.exists("../" + str_directory_name):
            print("Directory " + str_directory_name + " exists")
            return None
        else:
            print("Creating Directory: " + str_directory_name)
            os.mkdir("../" + str_directory_name)
        return None

    def resize_images(self, original_directory, new_directory, img_height, img_width):
        """
        Imports each image, and resizes to a given size

        :param original_directory: directory containing original images
        :param new_directory: directory to place new images
        :param img_height: new image height
        :param img_width: new image height
        :return: New image in specified folder
        """

        for item in os.listdir(original_directory):
            img = cv2.imread(original_directory + item, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (img_height, img_width))
            cv2.imwrite(new_directory + item, img)
        return None

    def mirror_images(self, image_directory):
        """
        Mirrors all images in the specified directory
        :param image_directory: current directory with all images
        :return: mirrored images, saved to image_directory
        """

        lst = [l for l in os.listdir(image_directory)]
        lst = [img.split(".jpg")[0] for img in lst]

        # for item in os.listdir("../data-faces/"):
        #     for i in os.path.splitext(item):
        #         if i != ".jpg":
        #             print(i)

        for item in lst:
            img = cv2.imread(image_directory + item + ".jpg")
            img = cv2.flip(img, 1)  # Mirrors image passed to cv2
            cv2.imwrite(image_directory + item + "_mirrored.jpg", img)
        return None

    def get_faces(self, filename):
        """
        Imports an image, and returns all faces within the image
        :param filename: image file, JPG or PNG
        :return: Images of cropped faces
        """
        face_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_eye.xml')
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)  # Originally 1.1

        face_images = []

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) >= 1:
                face_images.append(roi_color)

        return face_images

    def scan_images(self, root_dir, output_dir):
        """
        Locates all faces in a given directory, and outputs cropped faces to new directory.
        :param root_dir: original image directory
        :param output_dir: new directory where facial images are exported
        :return: cropped images of only faces, stored in output_dir
        """
        image_extensions = ["jpg", "png"]

        for dir_name, subdir_list, file_list in os.walk(root_dir):
            print('Scanning directory: %s' % dir_name)
            for filename in file_list:
                extension = os.path.splitext(filename)[1][1:]
                if extension in image_extensions:
                    faces = self.get_faces(os.path.join(dir_name, filename))

                    for face in faces:
                        face_filename = os.path.join(output_dir, "{}".format(filename))
                        cv2.imwrite(face_filename, face)


if __name__ == "__main__":
    preprocessing = Preprocessing()
    preprocessing.create_directory(str_directory_name="data-grayscale")
    preprocessing.create_directory(str_directory_name="data-faces")
    preprocessing.resize_images(original_directory="../data-color/", new_directory="../data-grayscale/",
                                img_height=1024, img_width=1024)
    preprocessing.scan_images(root_dir="../data-grayscale/", output_dir="../data-faces/")
    preprocessing.resize_images(original_directory="../data-faces/", new_directory="../data-faces/", img_height=512,
                                img_width=512)
    preprocessing.mirror_images(image_directory="../data-faces/")
