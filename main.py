import cv2

# haarcascade = suite de fichier d'entrainement
# CascadeClassifier = fonction pour récupéré le fichier d'entrainement pour l'utilisé
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")

# VidéoCapture = fonction pour récupéré la cam (ici 0 pour la cam principal)
cap = cv2.VideoCapture(0)

while True:
    # variable
    # cap.read() = récupéré les images de la cam
    ret, frame = cap.read()
    # gray = passe la vidéo on noir et blanc pour un travail plus simple
    # cvtColor = change la couleur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face = détecte le visage
    # scaleFactor = nombre de carré afficher
    # minNeighbors = plus il est élévé plus la détection et précise
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    # itération
    for x, y, w, h in face:
        # on récupére le rectangle du visage et on l'affiche
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

    # imshow = affiche la cam
    cv2.imshow('video', frame)

# refresh
cap.release()
cv2.destroyAllWindows()
