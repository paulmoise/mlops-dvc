#@title Model training code
from pathlib import Path


# # 1st method
# from compression.data import get_images

# get_images(...)

# # 2nd method
# from .data import get_images

# get_images(...)

# # 3rd method
# import compression.data

# compression.data.get_images(...)

from compression.data import get_images  # To edit depending on your code organization
from compression.model import get_lenet  # To edit depending on your code organization


def train(
    train_dir: str,
    image_size: tuple[int, int],
    learning_rate: float,
    batch_size: int,
    epochs: int,
    model_path: str
) -> None:
    images, labels, paths = get_images(Path(train_dir), image_size)
    model = get_lenet(image_size, learning_rate)
    model.fit(images, labels, batch_size, epochs=epochs)
    model.save(model_path)
