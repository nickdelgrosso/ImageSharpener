import utils
from dataclasses import dataclass
import numpy as np
from typing import Optional

@dataclass
class App:
    sharpen_radius: int = 1
    sharpen_amount: int = 3
    image: Optional[np.ndarray] = None


    def load_image(self, im_bytes):
        self.image = utils.bytes_to_array(image_bytes=im_bytes)

    @property
    def sharpened_image(self) -> Optional[np.ndarray]:
        if self.image is None:
            return None
        return utils.sharpen(self.image, self.sharpen_radius, self.sharpen_amount)


