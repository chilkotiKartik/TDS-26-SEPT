from PIL import Image

# (scrambled_row, scrambled_col) -> (original_row, original_col)
MAPPING = {
    (0, 0): (2, 1), (0, 1): (1, 1), (0, 2): (4, 1), (0, 3): (0, 3), (0, 4): (0, 1),
    (1, 0): (1, 4), (1, 1): (2, 0), (1, 2): (2, 4), (1, 3): (4, 2), (1, 4): (2, 2),
    (2, 0): (0, 0), (2, 1): (3, 2), (2, 2): (4, 3), (2, 3): (3, 0), (2, 4): (3, 4),
    (3, 0): (1, 0), (3, 1): (2, 3), (3, 2): (3, 3), (3, 3): (4, 4), (3, 4): (0, 2),
    (4, 0): (3, 1), (4, 1): (1, 2), (4, 2): (1, 3), (4, 3): (0, 4), (4, 4): (4, 0),
}
GRID = 5

src = Image.open("jigsaw.webp").convert("RGB")
W, H = src.size
tw, th = W // GRID, H // GRID

# 1) put every tile back where it belongs
out = Image.new("RGB", (W, H))
for (sr, sc), (orow, ocol) in MAPPING.items():
    tile = src.crop((sc * tw, sr * th, (sc + 1) * tw, (sr + 1) * th))
    out.paste(tile, (ocol * tw, orow * th))

# 2) luminance grayscale, rounded like JavaScript Math.round
px = out.load()
gray = Image.new("L", (W, H))
gp = gray.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        gp[x, y] = int(0.2126 * r + 0.7152 * g + 0.0722 * b + 0.5)

gray.save("reconstructed_grayscale.png")
print("saved reconstructed_grayscale.png", gray.size)
