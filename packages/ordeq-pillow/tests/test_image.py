from ordeq_pillow import PillowImage
from PIL import Image


def test_pilimage_load_and_save(tmp_path):
    """Tests loading and saving an image using PillowImage."""
    # Create a simple image and save to a bytes buffer
    img = Image.new("RGB", (10, 10), color="red")
    path = tmp_path / "test.png"
    img.save(path, format="PNG")

    # Test loading from buffer
    pil_img = PillowImage(path=path)
    loaded_img = pil_img.load()
    assert loaded_img.size == (10, 10)
    assert loaded_img.mode == "RGB"

    # Test saving to a file
    out_path = tmp_path / "out.png"
    pil_img = PillowImage(out_path)
    pil_img.save(loaded_img)
    assert out_path.exists()
