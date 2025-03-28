import os
import shutil
import random

def split_dataset(image_dir, output_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')
    
    for d in [train_dir, val_dir, test_dir]:
        os.makedirs(d, exist_ok=True)
    
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random.shuffle(images)
    
    total_images = len(images)
    train_count = int(total_images * train_ratio)
    val_count = int(total_images * val_ratio)
    
    train_images = images[:train_count]
    val_images = images[train_count:train_count + val_count]
    test_images = images[train_count + val_count:]
    
    for img in train_images:
        shutil.copy(os.path.join(image_dir, img), os.path.join(train_dir, img))
    for img in val_images:
        shutil.copy(os.path.join(image_dir, img), os.path.join(val_dir, img))
    for img in test_images:
        shutil.copy(os.path.join(image_dir, img), os.path.join(test_dir, img))
    
    print(f"Dataset split complete: {train_count} train, {val_count} val, {len(test_images)} test.")

split_dataset('images','images')