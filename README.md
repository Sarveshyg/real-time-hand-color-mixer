# Hand-Tracking Color Mixer

A real-time computer vision project that uses MediaPipe’s 21-point hand-landmark model to track finger positions through a webcam and convert fingertip distances into dynamic RGB color values.  

As you move or spread your fingers, the program measures three key distances—thumb–index, index–middle, and middle–ring—and maps them to the Red, Green, and Blue channels. The resulting mixed color is displayed live on screen along with smooth transitions to reduce jitter.  

This project demonstrates the basics of:
- Live webcam frame processing using OpenCV  
- Hand-landmark extraction using MediaPipe  
- Mapping geometric features (distances) to visual outputs  
- Drawing UI overlays and color swatches on video frames  
- Simple smoothing techniques for stable real-time visual feedback
