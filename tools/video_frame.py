"""Grade a YouTube video frame to match the Scent Pilot dark email look.

Usage: python3 -I tools/video_frame.py <input.jpg> <output.jpg> [--crop x0,y0,x1,y1] [--size 1200x800]

Pull clean frames (no thumbnail text) from https://i.ytimg.com/vi/<VIDEO_ID>/maxres1.jpg, maxres2.jpg, maxres3.jpg.
The script darkens, warms and lightly desaturates the frame and adds a soft vignette, so it sits in a
black/amber email and can be faded into the sections around it in Figma (keep the fades as Figma layers).
"""
import sys
from PIL import Image, ImageEnhance, ImageDraw, ImageFilter, ImageChops

def grade(im, size=(1200, 800), crop=None):
    im = im.convert('RGB')
    if crop:
        im = im.crop(crop)
    tw, th = size
    r = max(tw / im.width, th / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x, y = (im.width - tw) // 2, (im.height - th) // 2
    im = im.crop((x, y, x + tw, y + th))
    im = ImageEnhance.Color(im).enhance(0.72)
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Brightness(im).enhance(0.62)
    warm = Image.new('RGB', im.size, (255, 226, 190))
    im = ImageChops.multiply(im, warm)
    mask = Image.new('L', im.size, 0)
    ImageDraw.Draw(mask).ellipse((-tw * 0.15, -th * 0.2, tw * 1.15, th * 1.2), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(tw * 0.12))
    return Image.composite(im, Image.new('RGB', im.size, (0, 0, 0)), mask)

if __name__ == '__main__':
    a = sys.argv[1:]
    crop = size = None
    if '--crop' in a:
        crop = tuple(int(v) for v in a[a.index('--crop') + 1].split(','))
    if '--size' in a:
        size = tuple(int(v) for v in a[a.index('--size') + 1].split('x'))
    grade(Image.open(a[0]), size or (1200, 800), crop).save(a[1], quality=90)
