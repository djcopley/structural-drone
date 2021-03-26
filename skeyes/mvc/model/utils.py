import cv2


def image_crop(image, min_x, min_y, max_x, max_y):
    """
    Function crops a given image. Will break if min_x > max_x or min_y > max_y.
    """
    return image[min_y: max_y, min_x: max_x]


def image_annotate(image, min_x, min_y, max_x, max_y, text=None, color=(0, 255, 0), thickness=2):
    """
    Function draws a box on an image and adds text. Text is optional.
    """
    # COPY THE IMAGE!!! OpenCV modifies original!
    image = image.copy()
    cv2.rectangle(image, (min_x, min_y), (max_x, max_y), color, thickness)
    if text:
        text_y = min_y - 10
        if min_y - 10 < 20:
            text_y = max_y + 30
        cv2.putText(image, text, (min_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color)

    return image


def extract_class_names(filename: str) -> list:
    with open(filename, 'rt') as f:
        return f.read().rstrip('\n').split('\n')


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    image = image_annotate(frame, 0, 0, 200, 300, text="WINDOW")
    cv2.imshow("", image)
    cv2.waitKey(0)

    image = image_crop(frame, 0, 0, 200, 300)
    cv2.imshow("", image)
    cv2.waitKey(0)

    cv2.imshow("", frame)  # FRAME SHOULD BE ORIGINAL!
    cv2.waitKey(0)
