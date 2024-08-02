import subprocess
import os

def run_detection(video_path):
    # Absolute path to detect.py
    detect_path = r"C:\Users\user\PycharmProjects\human_detection_v7\yolov7-object-tracking\detect.py"

    # Check if detect.py exists
    if not os.path.exists(detect_path):
        raise FileNotFoundError(f"File not found: {detect_path}")

    # Command to run the detect.py script
    command = [
        'python', detect_path,
        '--weights', 'yolov7.pt',
        '--source', video_path
    ]

    print("Running command:", " ".join(command))  # Debugging output

    try:
        # Execute the command
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command Output:\n", result.stdout)
        print("Command Error Output:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print(f"Error Output:\n{e.stderr}")

if __name__ == '__main__':
    # Hardcoded video path
    video_path = r"C:\Users\user\PycharmProjects\human_detection_v7\yolov7-object-tracking\hand_fire.mp4"

    run_detection(video_path)
