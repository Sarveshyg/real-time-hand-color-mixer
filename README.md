# Hand Tracking Color Mixer
![Hand-Tracking Color Mixer demo](assets/demo.gif)

This project transforms your hand into a color blender. By utilizing your webcam the app detects your fingers with MediaPipe’s 21-point hand landmark system. When you move or separate your fingers it measures three distances—thumb to index, index to middle and middle to ring. Each distance modifies one RGB color channel enabling color control through hand movements. The shown color changes immediately, with transitions and no flickering.

This is the process:

- OpenCV is used to capture video frames in time.
- MediaPipe detects your hand and pinpoints all landmarks.
- The space separating the fingertips is converted into RGB values.
- You observe both an overlay and a color sample, on the video display.
- Basic smoothing methods maintain a color while your hand shifts.

This is a straightforward and interactive demonstration of computer vision and real-time feedback.
