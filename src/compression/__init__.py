from dvc.api import params_show

from compression.train import train

def main() -> None:
    args = params_show(stages=["train"])
    print(args)
    train(**args)

