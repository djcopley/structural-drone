import cv2


def image_crop(image, min_x, min_y, max_x, max_y):
    """
    Function crops a given image. Will break if min_x > max_x or min_y > max_y.

    :param image:
    :param min_x:
    :param min_y:
    :param max_x:
    :param max_y:
    :return:
    """
    assert min_x < max_x, "min_x must be smaller than max_x."
    assert min_y < max_y, "min_y must be smaller than max_y."
    return image[min_y: max_y, min_x: max_x]


def image_annotate(image, min_x, min_y, max_x, max_y, text=None, damaged=False, thickness=2):
    """
    Function draws a box on an image and adds text. Text is optional.

    :param image:
    :param min_x:
    :param min_y:
    :param max_x:
    :param max_y:
    :param text:
    :param damaged:
    :param thickness:
    :return:
    """
    # Color selection
    green = (0, 255, 0)
    red = (0, 0, 255)
    color = red if damaged else green

    # COPY THE IMAGE!!! OpenCV modifies original!
    image = image.copy()

    # TODO: Change the text placement to inside the box with highlight
    cv2.rectangle(image, (min_x, min_y), (max_x, max_y), color, thickness)
    if text:
        text_y = min_y - 10
        if min_y - 10 < 20:
            text_y = max_y + 30
        cv2.putText(image, text, (min_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color)

    return image


def extract_class_names(filename: str) -> list:
    """

    :param filename:
    :return:
    """
    with open(filename, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')
    return classes


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    img = image_annotate(frame, 0, 0, 200, 300, text="WINDOW", damaged=True)
    cv2.imshow("", img)
    cv2.waitKey(0)

    img = image_crop(frame, 0, 0, 200, 300)
    cv2.imshow("", img)
    cv2.waitKey(0)

    cv2.imshow("", frame)  # FRAME SHOULD BE ORIGINAL!
    cv2.waitKey(0)
