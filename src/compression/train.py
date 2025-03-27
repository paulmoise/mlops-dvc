#@title Model training code
from pathlib import Path

from compression.data import get_images  # To edit depending on your code organization
from compression.model import get_lenet  # To edit depending on your code organization


def train(
    data_dir: str,
    image_size: tuple[int, int],
    learning_rate: float,
) -> None:
    print(f"File Path is {Path(data_dir)}")
    images, labels, paths = get_images(Path(data_dir), image_size)
    model = get_lenet(image_size, learning_rate)
    model.fit(images, labels, 128, epochs=4)
    model.save("landscape_classifier.keras")
