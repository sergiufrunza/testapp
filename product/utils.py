from PIL import Image

def crop_center(pil_img ,crop):
    img_width ,img_height = pil_img.size
    return pil_img.crop(((img_width - crop) // 2 ,
                         (img_height - crop) // 2 ,
                         (img_width + crop) // 2 ,
                         (img_height + crop) // 2))