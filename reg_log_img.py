from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def get_mask(img, mask_color=[0, 255, 0, 255]):
    return np.all(img == mask_color, axis=-1)

def main():
    base = np.array(Image.open("images/base.png"))
    mask = np.array(Image.open("images/mask.png"))

    mask = get_mask(mask)

    r_base = base[:, :, 0]
    g_base = base[:, :, 1]
    b_base = base[:, :, 2]

    fig, axs = plt.subplots(3, 3)
    axs[0, 0].imshow(r_base, cmap='hot', interpolation='nearest')
    axs[0, 0].set_title('Red')
    axs[0, 1].imshow(g_base, cmap='hot', interpolation='nearest')
    axs[0, 1].set_title('Green')
    axs[0, 2].imshow(b_base, cmap='hot', interpolation='nearest')
    axs[0, 2].set_title('Blue')

    axs[1, 0].imshow(mask, cmap='hot', interpolation='nearest')
    axs[1, 1].imshow(mask, cmap='hot', interpolation='nearest')
    axs[1, 2].imshow(mask, cmap='hot', interpolation='nearest')

    axs[2, 0].imshow(np.ma.masked_where(mask, r_base), cmap='hot', interpolation='nearest')
    axs[2, 1].imshow(np.ma.masked_where(mask, g_base), cmap='hot', interpolation='nearest')
    axs[2, 2].imshow(np.ma.masked_where(mask, b_base), cmap='hot', interpolation='nearest')

    # plt.imshow(b_base, cmap='hot', interpolation='nearest')
    plt.show()

if __name__ == "__main__":
    main()
