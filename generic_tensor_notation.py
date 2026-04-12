import torch

print("=== Generic Tensor Notation ===")

# create tensor
images_pt = torch.zeros([32, 28, 28, 3])

print("shape of images_pt =", images_pt.shape)

print("\nExplanation:")
print("32  -> number of images (batch size)")
print("28  -> height of image")
print("28  -> width of image")
print("3   -> color channels (RGB)")
