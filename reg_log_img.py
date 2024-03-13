from PIL import Image
import numpy as np

def main():
    base = np.array(Image.open("images/base.png"))
    mask = np.array(Image.open("images/mask.png"))

    mask = np.all(mask == [0, 255, 0, 255], axis=-1)

    print(mask)

if __name__ == "__main__":
    main()
