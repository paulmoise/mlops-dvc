from compression.train import train
def main() -> None:
    print("Hello from compression!")

    train("dataset-landscape-main/seg_train", (150, 150), 0.0001)

