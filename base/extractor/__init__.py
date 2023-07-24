from google.cloud import vision


def extract_text_from_image(image_path):
    # Instantiate a client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create an image instance
    image = vision.Image(content=content)

    # Configure the OCR feature
    ocr_feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)

    # Create a request object
    request = vision.AnnotateImageRequest(image=image, features=[ocr_feature])

    # Perform OCR request
    response = client.batch_annotate_images(requests=[request])

    # Extract the OCR'd text
    ocr_text = response.responses[0].full_text_annotation.text

    return ocr_text
