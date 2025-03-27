#@title Data preparation code
import pathlib

import cv2
import numpy
import sklearn.metrics
import sklearn.utils

CLASS_NAMES = ["buildings", "forest", "glacier", "mountain", "sea", "street"]
CLASS_INDICES = {l: i for i, l in enumerate(CLASS_NAMES)}


def get_images(
    dir_path: pathlib.Path, image_size: tuple[int, int], shuffle: bool = True
) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    images = []
    labels = []
    file_paths = []

    for subdir_path in dir_path.iterdir():

        label = CLASS_INDICES.get(subdir_path.name)

        for image_path in subdir_path.iterdir():
            image = cv2.imread(str(image_path))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, image_size)
            image = image.astype("float32")
            images.append(image)
            labels.append(label)
            file_paths.append(image_path)
    images_array = numpy.array(images)
    labels_array = numpy.array(labels)
    file_paths_array = numpy.array(file_paths)

    if shuffle:
        images_array, labels_array, file_paths_array = sklearn.utils.shuffle(
            images_array, labels_array, file_paths_array
        )
    return images_array, labels_array, file_paths_array
