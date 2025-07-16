import cv2
import os
from lane_detector import detect_lanes
from utils.fps_counter import FPSCounter
from db_logger import log_lane_detection  # Optional logging

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return False

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_input = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps_input, (width, height))

    fps_counter = FPSCounter()
    fps_counter.start()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, lanes_detected = detect_lanes(frame)
        fps_counter.update()

        # Overlay lane status
        status_text = "Lanes Detected" if lanes_detected else "No Lane Found"
        color = (0, 255, 0) if lanes_detected else (0, 0, 255)
        cv2.putText(processed_frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Log to DB (optional)
        try:
            log_lane_detection(lanes_detected)
        except Exception as e:
            print("Logging Error:", e)

        out.write(processed_frame)
        cv2.imshow("Lane Detection Output", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    fps = fps_counter.stop()
    print(f"Processing Complete. FPS: {fps}")
    return True
