import cv2


img = cv2.imread("solar-system.jpg")

cv2.putText(img,
"Sun",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.7,
(255,255,255)
)

cv2.putText(img,
"Mercury",
(100,180),
cv2.FONT_HERSHEY_COMPLEX,
0.44,
(255,255,255)
)

cv2.putText(img,
"Venus",
(200,180),
cv2.FONT_HERSHEY_COMPLEX,
0.44,
(255,255,255)
)

cv2.putText(img,
"Earth",
(290,180),
cv2.FONT_HERSHEY_COMPLEX,
0.44,
(255,255,255)
)

cv2.putText(img,
"Mars",
(390,180),
cv2.FONT_HERSHEY_COMPLEX,
0.44,
(255,255,255)
)

cv2.putText(img,
"Jupiter",
(550,60),
cv2.FONT_HERSHEY_COMPLEX,
0.6,
(255,255,255)
)

cv2.putText(img,
"Saturn",
(780,140),
cv2.FONT_HERSHEY_COMPLEX,
0.55,
(255,255,255)
)

cv2.putText(img,
"Uranus",
(960,140),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255)
)

cv2.putText(img,
"Neptune",
(1100,140),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255)
)

cv2.imshow("solar_Sys",img)
cv2.waitKey(0)