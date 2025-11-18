from pathlib import Path

import pytest
from ordeq import IOException
from ordeq_pillow import PDF2Image
from PIL import Image


def create_sample_pdf(pdf_path: Path) -> None:
    """Create a simple PDF file for testing purposes."""
    # Create a minimal PDF manually - this should work with pdf2image
    minimal_pdf_content = b"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R 4 0 R]
/Count 2
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 5 0 R
>>
endobj

4 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 6 0 R
>>
endobj

5 0 obj
<<
/Length 44
>>
stream
BT
/F1 12 Tf
100 750 Td
(Test PDF - Page 1) Tj
ET
endstream
endobj

6 0 obj
<<
/Length 44
>>
stream
BT
/F1 12 Tf
100 750 Td
(Test PDF - Page 2) Tj
ET
endstream
endobj

xref
0 7
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000115 00000 n
0000000192 00000 n
0000000269 00000 n
0000000363 00000 n
trailer
<<
/Size 7
/Root 1 0 R
>>
startxref
457
%%EOF"""
    pdf_path.write_bytes(minimal_pdf_content)


@pytest.fixture
def sample_pdf(tmp_path):
    """Create a sample PDF file for testing."""
    pdf_path = tmp_path / "sample.pdf"
    create_sample_pdf(pdf_path)
    return pdf_path


def test_pdf2image_with_existing_pdf(sample_pdf):
    """Test PDF2Image with an actual PDF file."""
    pdf_input = PDF2Image(sample_pdf)
    images = pdf_input.load()

    # Verify return value
    assert isinstance(images, list)
    assert len(images) >= 1  # Should have at least one page

    # Verify each image is a PIL Image
    for img in images:
        assert isinstance(img, Image.Image)
        assert img.size[0] > 0  # Width should be positive
        assert img.size[1] > 0  # Height should be positive


def test_pdf2image_with_nonexistent_pdf():
    """Test PDF2Image with a non-existent PDF file."""
    nonexistent_path = Path("nonexistent.pdf")
    pdf_input = PDF2Image(nonexistent_path)

    # pdf2image will raise an exception for non-existent files
    with pytest.raises(IOException):
        pdf_input.load()


def test_pdf2image_load_with_options(sample_pdf):
    """Test PDF2Image load method with additional options."""
    pdf_input = PDF2Image(sample_pdf)

    # Test with various load options
    load_options = {
        "dpi": 200  # Use reasonable DPI for testing
    }

    images = pdf_input.load(**load_options)

    # Verify return value
    assert isinstance(images, list)
    assert len(images) >= 1

    # Verify images are PIL Images with expected higher resolution
    for img in images:
        assert isinstance(img, Image.Image)
        assert img.size[0] > 0
        assert img.size[1] > 0
        # With DPI=200, images should be reasonably sized
        assert img.size[0] > 100  # Minimum expected width
        assert img.size[1] > 100  # Minimum expected height


def test_pdf2image_different_pages(sample_pdf):
    """Test PDF2Image with page selection options."""
    pdf_input = PDF2Image(sample_pdf)

    # Load only the first page
    images_page1 = pdf_input.load(first_page=1, last_page=1)
    assert isinstance(images_page1, list)
    assert len(images_page1) == 1
    assert isinstance(images_page1[0], Image.Image)

    # Load all pages
    images_all = pdf_input.load()
    assert len(images_all) >= len(
        images_page1
    )  # Should have at least as many pages


def test_pdf2image_integration_with_save(sample_pdf, tmp_path):
    """Test PDF2Image integration - loading and saving images."""
    # Test
    pdf_input = PDF2Image(sample_pdf)
    images = pdf_input.load()

    # Save images (test the example from the original commented code)
    for i, img in enumerate(images):
        output_path = tmp_path / f"page_{i + 1}.png"

        # Save the actual image
        img.save(str(output_path))

        # Verify the file was created and has content
        assert output_path.exists()
        assert output_path.stat().st_size > 0

        # Verify we can load the saved image
        from PIL import Image as PillowImage

        saved_img = PillowImage.open(output_path)
        assert saved_img.size == img.size
        saved_img.close()
