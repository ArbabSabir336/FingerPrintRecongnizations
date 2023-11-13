import Funcations


image1 = Funcations.preprocessed_image('images/finger.jpg')
image2 = Funcations.preprocessed_image('images/finger.jpg')


featcher1 = Funcations.extra_features(image1)
featcher2 = Funcations.extra_features(image2)

if Funcations.match_funcations(featcher1,featcher2):
    print("Match")
else:
    print("Not Match")


