import cv2
import numpy as np

def region_of_interest(img):
    height, width = img.shape
    mask = np.zeros_like(img)

    # Define a polygon that roughly covers the road area
    polygon = np.array([[
        (int(0.1 * width), height),
        (int(0.45 * width), int(0.6 * height)),
        (int(0.55 * width), int(0.6 * height)),
        (int(0.9 * width), height)
    ]], dtype=np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def detect_lanes(frame):
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)
        cropped_edges = region_of_interest(edges)

        lines = cv2.HoughLinesP(
            cropped_edges,
            rho=1,
            theta=np.pi / 180,
            threshold=80,
            minLineLength=80,
            maxLineGap=20
        )

        line_image = np.zeros_like(frame)
        lanes_detected = False

        if lines is not None:
            for line in lines:
                for x1, y1, x2, y2 in line:
                    # Filter lines based on slope (angle)
                    if x2 - x1 == 0:
                        continue  # avoid division by zero
                    slope = (y2 - y1) / (x2 - x1)
                    angle = np.degrees(np.arctan(slope))

                    # Only consider lines within 20 to 70 degrees
                    if 20 < abs(angle) < 70:
                        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        lanes_detected = True

        final_frame = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
        return final_frame, lanes_detected

    except Exception as e:
        print("Lane Detection Error:", e)
        return frame, False
