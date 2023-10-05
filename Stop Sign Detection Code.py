# import cv2
# from matplotlib import pyplot as plt

# # Provide the correct file path to your image
# image_path = "C:/Users/speed/Desktop/VS Code Stuff/Uni VS Code Stuff/Github Repositories/EXPO AI Learning/Learning_AI/Images for recognition/Stopsign 2.jpg"

# # Opening image
# img = cv2.imread(image_path)

# if img is None:
#     print("Image not found. Please provide a valid image path.")
# else:
#     # OpenCV opens images as BGR
#     # but we want it as RGB We'll
#     # also need a grayscale version
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # Provide the correct file path to your cascade classifier XML file
#     stop_data = cv2.CascadeClassifier('C:/Users/speed/Desktop/VS Code Stuff/Uni VS Code Stuff/Github Repositories/EXPO AI Learning/Learning_AI/Images for recognition/stop_data.xml')

#     found = stop_data.detectMultiScale(img_gray, minSize=(20, 20))

#     # Don't do anything if there's no sign
#     amount_found = len(found)

#     if amount_found != 0:
#         # There may be more than one
#         # sign in the image
#         for (x, y, width, height) in found:
#             # We draw a green rectangle around
#             # every recognized sign
#             cv2.rectangle(img_rgb, (x, y),
#                           (x + width, y + height),
#                           (0, 255, 0), 5)

#         # Creates the environment of
#         # the picture and shows it
#         plt.imshow(img_rgb)
#         plt.show()
